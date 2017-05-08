from flask import Flask, render_template, request
from forms import AnsibleForm


app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'

# WTF_CSRF_ENABLED = False
# SECRET_KEY = 'my_precious'

@app.route("/")
def main():
    form = AnsibleForm(request.form)
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()