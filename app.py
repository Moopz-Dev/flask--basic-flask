from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    data = {"name": "Moopz-Dev", "age": 30, "job": "Programmer"}
    return render_template("index.html", data=data)


@app.route('/about')
def about():
    products = ["Attires", "Elctronics", "Toiletries"]
    return render_template("about.html", products=products)


@app.route('/admin')
def admin():
    username = "Moopz"
    return render_template("admin.html", username=username)


@app.route('/user/<name>/<age>')
def user(name, age):
    return "<h1>Hello {}, Age: {} </h1>".format(name, age)


@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    details = request.args.get('details')
    return render_template("thankyou.html", data={"fname": fname, "details": details})


if __name__ == "__main__":
    app.run(debug=True)
