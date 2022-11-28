# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<operation>')
def calculate(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    if(operation == 'add'):
        return f'''{a} + {b} = {add(a,b)}'''
    elif(operation == 'sub'):
        return f'''{a} - {b} = {sub(a,b)}'''
    elif(operation == 'mult'):
        return f'''{a} * {b} = {mult(a,b)}'''
    elif(operation == 'div'):
        return f'''{a} - {b} = {div(a,b)}'''

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    if(operation == 'add'):
        return f'''{a} + {b} = {add(a,b)}'''
    elif(operation == 'sub'):
        return f'''{a} - {b} = {sub(a,b)}'''
    elif(operation == 'mult'):
        return f'''{a} * {b} = {mult(a,b)}'''
    elif(operation == 'div'):
        return f'''{a} - {b} = {div(a,b)}'''