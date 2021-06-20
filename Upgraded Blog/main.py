from flask import Flask
from flask import template_rendered
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)