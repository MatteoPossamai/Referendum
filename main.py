from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__,static_url_path='/static')
app.secret_key = "referendumKey"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)