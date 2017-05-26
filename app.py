from flask import Flask, render_template, request, redirect, url_for, Response
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
            my_host = request.form['hostname']
            # return redirect(url_for('output', host=my_host))
            return redirect(url_for('index'))
    return render_template('index.html', form=form, error=error)


# @app.route('/output')
# def output():
#     host = request.args['host']
#     def inner():
#         ansible_command="ansible-playbook -i ansible/hosts ansible/user.yml --limit {}".format(host)
#         proc = subprocess.Popen(
#             [ansible_command],
#             shell=True,
#             stdout=subprocess.PIPE,
#             universal_newlines=True
#         )

#         for line in iter(proc.stdout.readline, ''):
#             time.sleep(1)
#             yield line.rstrip()+'<br/>\n'

#     return Response(inner(), mimetype='text/html')


@app.route('/output')
def index():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('output.html')


@app.route('/stream_sqrt')
def stream():
    def generate():
        for i in range(500):
            yield '{}\n'.format(sqrt(i))
            sleep(1)

    return app.response_class(generate(), mimetype='text/plain')


if __name__ == "__main__":
    app.run()
