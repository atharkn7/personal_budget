from flask import Flask, render_template, request, redirect
from flask_session import Session

#Configure app
app = Flask(__name__)

#Configuring session to use file system
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Home Directory asking to Login
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # Post
        return render_template("login.html")

# Registering new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    else: 
        return redirect("/")