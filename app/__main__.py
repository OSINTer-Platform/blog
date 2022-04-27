from flask import Flask, render_template

from app import app

@app.route("/")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
