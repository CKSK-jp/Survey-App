from flask import Flask, render_template, request

from surveys import Question

app = Flask(__name__)


# default landing page for user
@app.route("/")
def story_selection():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
