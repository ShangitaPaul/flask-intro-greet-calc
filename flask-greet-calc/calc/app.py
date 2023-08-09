# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))  # Avoid division by zero
    result = div(a, b)
    return str(result)

# Add a route /math/<operation> that allows the user to enter in a URL like:
# http://localhost:5000/math/add?a=10&b=30
# And get back a JSON response like:
# { "operation": "add", "value": 40 }
# The result of the operation should be returned as a string.
# The valid operations are add, sub, mult, and div.
# If an invalid operation is performed, the response should be
# { "error": "operation not supported" }
operations = {"add": add, "sub": sub, "mult": mult, "div": div}

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if operation == 'add':
        result = add(a, b)
    elif operation == 'sub':
        result = sub(a, b)
    elif operation == 'mult':
        result = mult(a, b)
    elif operation == 'div':
        result = div(a, b)
    else:
        return 'Invalid operation'
    return {'operation': operation, 'value': result}
