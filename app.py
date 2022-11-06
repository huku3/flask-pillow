from flask import Flask
from flask import render_template
from flask import request
from PIL import Image


app = Flask(__name__)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files("uploadFile")
    img = Image.open(file)

    return render_template(show.html)


if __name__ == "__main__":
    app.run(debug=True)
