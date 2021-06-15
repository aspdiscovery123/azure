
from flask import Flask 
app=Flask(__name__)
@app.route('/')

def hello():
    return " hello from Azure web app sevrice"
app.run(host='0.0.0.0')
