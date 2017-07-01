################# 
#### imports #### 
#################

from flask import Flask, render_template, request, redirect, \
    url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import subprocess
import datetime
from functools import wraps
from time import sleep

from forms import AnsibleForm, LoginForm

################ 
#### config #### 
################

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from models import History, User

########################## 
#### helper functions #### 
##########################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

################ 
#### routes #### 
################

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('name', None)
    flash('Goodbye!')
    return redirect(url_for('login'))


@app.route("/login", methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['name']).first()
        if user and user.password == request.form['password']:
        # if user and bcrypt.check_password_hash(user.password,
        #             request.form['password']):
            session['logged_in'] = True
            session['user_id'] = user.id
            session['name'] = user.name
            flash('Welcome!')
            return redirect(url_for('main'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route("/", methods=['GET','POST'])
@login_required
def main():
    error = None
    form = AnsibleForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            session['hostname'] = form.hostname.data
            session['playbook'] = form.playbook.data
            session['output_level'] = form.output_level.data
            return redirect(url_for('output'))
    return render_template('main.html', form=form, error=error)


@app.route('/output')
@login_required
def output():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('output.html')


@app.route('/ansible_stream')
@login_required
def stream():
    hostname = session['hostname']
    playbook = session['playbook']
    output_level = session['output_level']
    username = session['user_id']

    def generate():
        ansible_command = "ansible-playbook {} -i ../ansible/hosts \
        ../ansible/{} --limit {}".format(output_level, playbook, hostname)
        proc = subprocess.Popen(
            [ansible_command],
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        output = ""
        for line in iter(proc.stdout.readline, ''):
            #sleep(0.1)
            output += str('<p>'+line+'</p>')
            yield '{}\n'.format(line.rstrip())
            
        with app.app_context():    
            new_record = History(
                datetime.datetime.utcnow(),
                hostname,
                playbook,
                output,
                username
            )
            db.session.add(new_record)
            db.session.commit()

    return app.response_class(generate(), mimetype='text/plain')


def histories():
    return db.session.query(History).order_by(History.date.asc())


def list_users():
    return db.session.query(User).order_by(User.name)


@app.route("/users")
@login_required
def users():
    return render_template('users.html', users=list_users())


@app.route("/history")
@login_required
def history():
    return render_template(
        'history.html',
        histories=histories()
    )


@app.route("/about")
@login_required
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
