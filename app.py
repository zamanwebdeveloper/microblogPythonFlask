from flask import Flask
app = Flask(__name__)
@app.route('/index')
# def index():
#     return 'index'
@app.route('/')
def Home():
    return 'Welcome to Home Page'
@app.route('/product')
def pro():
    return 'This is the product page'
# app.run(port=5002)
app.run(port=5000, debug=True)
