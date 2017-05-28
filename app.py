from flask import Flask, render_template, request, redirect, url_for, session
import time
import subprocess
from math import sqrt
from time import sleep


from forms import AnsibleForm


app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'


@app.route("/", methods=['GET','POST'])
def main():
    error = None
    form = AnsibleForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            session['host'] = request.form['hostname']
            return redirect(url_for('index'))
    return render_template('index.html', form=form, error=error)


@app.route('/output')
def index():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('output.html')


@app.route('/stream_sqrt')
def stream():
    host = session['host']
    def generate():
        ansible_command="ansible-playbook -vv -i ansible/hosts ansible/user.yml --limit {}".format(host)
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
