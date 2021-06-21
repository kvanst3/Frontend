from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = os.environ.get("INDI_PW")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    # if request.method == "POST":
    #     if form.validate_on_submit():
    #         return redirect('success.html')
    #     return render_template('denied.html')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
