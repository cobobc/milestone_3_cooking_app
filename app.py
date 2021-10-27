import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_heading="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_heading="Contact")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", page_heading="Recipes")


@app.route("/login")
def login():
    return render_template("login.html", page_heading="Sign up or Login")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)