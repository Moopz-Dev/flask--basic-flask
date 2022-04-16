from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/user/<name>/<age>')
def user(name, age):
    return "<h1>Hello {}, Age: {} </h1>".format(name, age)


if __name__ == "__main__":
    app.run(debug=True)
