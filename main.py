# Write a program for a web app using flask, to compress PDF, PNG and JPG files, with the file quality retained. Add an upload button to select a file and compress it, and save the compressed file to the same directory.

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sys
import time
import subprocess
import PyPDF2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(secure_filename(file.filename))
    if file.filename.endswith(".pdf"):
        compress_pdf(file.filename)
    elif file.filename.endswith(".png"):
        compress_png(file.filename)
    elif file.filename.endswith(".jpg"):
        compress_jpg(file.filename)
    else:
        return "File type not supported"
    return redirect(url_for("index"))

def compress_pdf(file):
    file_name = os.path.basename(file)
    file_name = file_name[:-4]
    file_name = file_name + "_compressed.pdf"
    file_path = os.path.dirname(file)
    file_path = file_path + "/"
    file_path = file_path + file_name
    pdf = PyPDF2.PdfFileReader(file)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    with open(file_path, "wb") as out:
        pdf_writer.write(out)

def compress_png(file):
    file_name = os.path.basename(file)
    file_name = file_name[:-4]
    file_name = file_name + "_compressed.png"
    file_path = os.path.dirname(file)
    file_path = file_path + "/"
    file_path = file_path + file_name
    image = Image.open(file)
    image.save(file_path, optimize=True, quality=85)

def compress_jpg(file):
    file_name = os.path.basename(file)
    file_name = file_name[:-4]
    file_name = file_name + "_compressed.jpg"
    file_path = os.path.dirname(file)
    file_path = file_path + "/"
    file_path = file_path + file_name
    image = Image.open(file)
    image.save(file_path, optimize=True, quality=85)

if __name__ == "__main__":
    app.run(debug=True)


