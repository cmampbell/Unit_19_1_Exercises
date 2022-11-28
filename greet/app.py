from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome/<word>')
def welcome_message(word=''):
    if(word == "home"):
        return """welcome home"""
    elif(word == "back"):
        return """welcome back"""
    
@app.route('/welcome')
def welcome():
    return """welcome"""