from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import os


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = os.environ.get("INDI_PW")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
