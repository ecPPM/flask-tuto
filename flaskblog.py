from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1664cf7306ac7d859122b2ecfbc36788'

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

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)
