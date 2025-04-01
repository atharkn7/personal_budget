from flask import Flask, render_template, request, redirect
from flask_session import Session

#Configuring session


app = Flask(__name__)

# Home Directory asking to Login
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")

# Registering new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    else: 
        return redirect("/")