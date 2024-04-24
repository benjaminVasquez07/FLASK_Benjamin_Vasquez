from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.router ("benja")
def benja():
    return 'hala madrid!'