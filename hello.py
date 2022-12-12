from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
    return '<h1>hello {}</h1>. '.format(name)