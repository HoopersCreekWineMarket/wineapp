from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Josh"}
    posts = [
        {
            'author': {'username': 'John Wineman'},
            'body': 'Beautiful day in Wineland!'
        },
        {
            'author': {'username': 'Susan Grape'},
            'body': 'Wine is so cool!'
        }
    ]
    return render_template("index.html", title="Wineblog", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Username {} tried to login, {}'.format(
            form.username.data , form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)