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
            session['subsystem'] = form.subsystem.data
            ansible_command = "ansible-playbook -vvv -i ansible/hosts ansible/{}.yml --limit {}".format(form.subsystem.data, form.hostname.data)
            new_record = History(
                'admin',
                ansible_command,
                datetime.datetime.utcnow()
            )
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for('output'))
    return render_template('main.html', form=form, error=error)


@app.route('/output')
def output():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('output.html')


@app.route('/ansible_stream')
def stream():
    hostname = session['hostname']
    subsystem = session['subsystem']

    def generate():
        ansible_command = "ansible-playbook -vvv -i ansible/hosts ansible/{}.yml --limit {}".format(subsystem, hostname)
        proc = subprocess.Popen(
            [ansible_command],
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for line in iter(proc.stdout.readline, ''):
            sleep(0.5)
            yield '{}\n'.format(line.rstrip())
            
    return app.response_class(generate(), mimetype='text/plain')


if __name__ == "__main__":
    app.run()
