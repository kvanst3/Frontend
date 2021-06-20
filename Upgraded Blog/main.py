from flask import Flask, template_rendered, request
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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True)