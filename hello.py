from flask import Flask
app = Flask(__name__)


# Different routes using the decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1> ' \
           '<p> This is a paragraph </h1>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


# Different decorators
def make_bold(function):
    def wrapper_function():
        return f'<b> {function()} <b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f' <em> {function()} </em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f' <u> {function()} </u>'
    return wrapper_function


# Chaining of different "style" decorators
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye !'


# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Greetings there {name}, your id is {number}'


if __name__ == "__main__":
    app.run(debug=True)
