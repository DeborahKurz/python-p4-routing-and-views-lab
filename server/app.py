#!/usr/bin/env python3

#5/27 redo:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    #Why do we not have any <h1>'s or something? Is it because it's just in the body?
    #How do I keep my development server running while I'm writing my code?
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ""
    for num in range(parameter):
        numbers += str(num) + "\n"
    return numbers

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    answer = None
    num1 = int(num1)
    num2 = int(num2)
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == 'div':
        answer = num1 / num2
    elif operation == '%':
        answer = num1 % num2
    return str(answer)

    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

























# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Python Operations with Flask Routing and Views</h1>'

# @app.route('/print/<parameter>')
# def print_string(parameter):
#     print(parameter)
#     return f'{parameter}'

# @app.route('/count/<parameter>')
# def count(parameter):
#     parameter = int(parameter)
#     numbers = ""
#     for num in range(parameter):
#         numbers += str(num)+"\n"
#     return numbers

# @app.route('/math/<num1>/<operation>/<num2>')
# def math(num1, operation, num2):
#     result = None
#     num1 = int(num1)
#     num2 = int(num2)
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == 'div':
#         result = num1 / num2
#     elif operation == '%':
#         result = num1 % num2
#     else:
#         pass
#     return str(result)




# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
