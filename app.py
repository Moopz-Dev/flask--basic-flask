
from flask import Flask, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import flask_bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)


class MyForm(FlaskForm):
    name = StringField("Enter Your Name", validators=[DataRequired()])
    isAccept = BooleanField("Accept Terms and Conditions")
    gender = RadioField("Select your gender", choices=[
                        ('m', 'male'), ('f', 'female'), ('o', 'others')])
    skills = SelectField("Your skills", choices=[
                         ("English", "English"), ("Singing", "Singing"), ("Gaming", "Gaming")])
    address = TextAreaField("Your Address")
    submit = SubmitField("Save")


@app.route('/', methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash("Data saved successfully.")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skills'] = form.skills.data
        session['address'] = form.address.data
        # Clear Data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.address.data = ""
    data = {"name": "Moopz-Dev", "age": 30, "job": "Programmer"}
    return render_template("index.html", form=form, data=data)


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
