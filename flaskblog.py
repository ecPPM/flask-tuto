from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "Home Page for flaskblog"

@app.route("/about")
def about():
    return "About Page for flaskblog"