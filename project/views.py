from flask import Flask, render_template, request, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import subprocess
import datetime
from time import sleep

from forms import AnsibleForm


app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from models import History

@app.route("/", methods=['GET','POST'])
def main():
    error = None
    form = AnsibleForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            session['hostname'] = form.hostname.data
            session['playbook'] = form.playbook.data

            return redirect(url_for('output'))
    return render_template('main.html', form=form, error=error)


@app.route('/output')
def output():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('output.html')


@app.route('/ansible_stream')
def stream():
    hostname = session['hostname']
    playbook = session['playbook']

    def generate():
        ansible_command = "ansible-playbook -vv -i ../ansible/hosts ../ansible/{} --limit {}".format(playbook, hostname)
        proc = subprocess.Popen(
            [ansible_command],
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        string = ""
        for line in iter(proc.stdout.readline, ''):
            # sleep(0.5)
            string+=str('<p>'+line+'</p>')
            yield '{}\n'.format(line.rstrip())
            
        with app.app_context():    
            new_record = History(
                datetime.datetime.utcnow(),
                'admin',
                hostname,
                playbook,
                string
            )
            db.session.add(new_record)
            db.session.commit()

    return app.response_class(generate(), mimetype='text/plain')


def histories():
    return db.session.query(History).order_by(History.date.asc())


@app.route("/history")
def history():
    return render_template(
        'history.html',
        histories=histories()
    )


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
