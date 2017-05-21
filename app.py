from flask import Flask, render_template, request, redirect, url_for, Response
import time
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
            # print(request.form['hostname'])
            return redirect(url_for('output'))
    return render_template('index.html', form=form, error=error)


@app.route("/output")
def output():
    def inner():
        for x in range(100):
            time.sleep(1)
            yield '%s<br/>\n' % x
    return Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately


if __name__ == "__main__":
    app.run()
