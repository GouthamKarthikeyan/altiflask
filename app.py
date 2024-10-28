from flask import Flask
app = Flask(__name__)

@app.route('/')
def appMVP():
    return "Hello World , From Goutham KK !"
