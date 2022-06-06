from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, id=post_id)
    # return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return render_template('./about.html')


@app.route("/blog")
def blog():
    return "<p>Some of people's thoughts!</p>"
