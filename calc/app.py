# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)



@app.route('/add')

def addition():
    '''Returns the sum of 2 numbers'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route('/sub')
    
def subtract():
    """Subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
    
def multiplication():
    """Multiplies a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
    
def division():
    """Divides a by b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

MATH = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
 @app.route('/math/<math_op>')
 def do_math(math_op):
    """Do math on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = MATH[math_op](a, b)
    return result