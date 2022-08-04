from flask import Flask, render_template, request
from workers import run_work, size_reducer
from werkzeug.utils import secure_filename

import os
from PIL import Image



app = Flask(__name__)

# app.config()

@app.route("/")
@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/upload", methods=["POST"])
def upload():
    image = request.files['image']
    file = secure_filename(image.filename)
    image.save(file)    
    size_reducer(file)

    return "Done"
if __name__ == "__main__":
    app.run(debug=True)   