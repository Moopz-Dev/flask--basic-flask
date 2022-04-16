
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


class MyForm(FlaskForm):
    name = StringField("Enter Your Name")
    submit = SubmitField("Save")


@app.route('/', methods=["GET", "POST"])
def index():
    form = MyForm()
    name = False
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    data = {"name": "Moopz-Dev", "age": 30, "job": "Programmer"}
    return render_template("index.html", data=data, form=form, name=name)


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
