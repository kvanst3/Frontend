from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = os.environ.get("INDI_PW")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return render_template('success.html')
        return render_template('login.html', form=form)
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
