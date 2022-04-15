from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Flask Framework</h1>"


@app.route('/about')
def about():
    return "<h1>About Me</h1>"


@app.route('/admin')
def admin():
    return "<h1>Hello Admin</h1>"


@app.route('/user/<name>/<age>')
def user(name, age):
    return "<h1>Hello {}, Age: {} </h1>".format(name, age)


if __name__ == "__main__":
    app.run(debug=True)
