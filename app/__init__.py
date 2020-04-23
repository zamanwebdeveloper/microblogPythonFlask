from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_string_here'
from app import routes
# app.run(port=5002)
