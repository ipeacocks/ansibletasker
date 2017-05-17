from flask import Flask, render_template, request
from forms import AnsibleForm


app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'


@app.route("/", methods=['GET','POST'])
def main():
    form = AnsibleForm(request.form)
    if request.method == 'POST':
       print request.form['hostname']
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()