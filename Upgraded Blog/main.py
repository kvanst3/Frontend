from flask import Flask
from flask import template_rendered
from flask.templating import render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/752bea529869fdd9037a").json()

@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", post=posts[id -1])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)