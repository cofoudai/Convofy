from flask import Flask, render template, request

app = Flask(__name__)

@app.route("/"):
def backend:
   return render_template("index.html")

