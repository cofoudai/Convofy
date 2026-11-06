from flask import Flask, render template

app = Flask(__name__)

@app.route("/"):
def backend:
  return render_template("index.html")

if name = "__main__":
  app.run(debug=True)

