from flask import Flask, render_template
app = Flask(__name__)
@app.route('/index')
# def index():
#     return 'index'
@app.route('/')
def Home():
    return render_template('home.html')
@app.route('/product')
def pro():
    return render_template('product.html')
# app.run(port=5002)
app.run(port=5000, debug=True)
