from flask import Flask, render_template
from app import app
from app.forms import LoginForm
@app.route('/home')
@app.route('/')
def Home():
    user = {'username': 'Syed Zaman Mostafiz'}
    posts = [
        {
            'author':{'username': 'Jhon'},
            'body':'This is a beautiful day'
        },
        {
            'author': {'username': 'Jhon'},
            'body': "I'm Good Today"
        },
        {
            'author': {'username': 'Alice'},
            'body': "Got a new jog today"
        },
    ]
    return render_template('home.html',title='Home',user=user, posts=posts)
@app.route('/product')
def product():
    return render_template('product.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In Here', form=form)
