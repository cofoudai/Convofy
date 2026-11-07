from flask import Flask, render template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"]):
def backend:
  if request.method == "POST":
        name = request.form.get("fname")
        email = request.form.get("email")
        return f"Thanks {name}! We received your email: {email}"
    return render_template("form.html")

