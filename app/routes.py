from flask import Flask, render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm
@app.route('/home')
@app.route('/')
def home():
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
@app.route('/about_us all of us')
def about():
    return render_template('about.html')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for the user {}'.format(form.username.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In Here', form=form)
