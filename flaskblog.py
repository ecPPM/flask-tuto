from flask import Flask, render_template

posts = [
    {
        'author' : 'Alex',
        'date_posted' : '8/6/22',
        'title' : 'Blog post 1',
        'content' : 'First post content'
    },
    {
        'author' : 'Bob',
        'date_posted' : '9/6/22',
        'title' : 'Blog post 2',
        'content' : 'Second post content'
    }
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")