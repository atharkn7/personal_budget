from flask import Flask, render_template, request, redirect, flash
from flask_session import Session

# Importing all form classes
from form_config.forms import *

#Initialize App
app = Flask(__name__)

""" APP Configuration """
# File System Config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configuring Secret Key
app.config["SECRET_KEY"] = "mysecretkey"


# Home Directory asking to Login
@app.route("/")
def index():
    form = LoginForm()
    return render_template("login.html", form=form)


# Registering new user
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash("Form Submitted!")
        return redirect("/register")
    
    return render_template("register.html", form=form)    
    

if __name__ == "__main__":
    app.run(debug=True)