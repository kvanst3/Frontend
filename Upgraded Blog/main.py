from flask import Flask
from flask import template_rendered
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)