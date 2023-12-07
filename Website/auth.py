from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import random
import json
auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            email = request.form.get("email")
            username = request.form.get("username")
            psw = request.form.get("password")
            cpsw = request.form.get("cpassword")
            if Users.query.filter_by(email=email).first():
                raise ValueError("Email is already used")
            elif len(email) < 4:
                raise ValueError("Email must be greater than 4 characters")
            elif len(username) < 2:
                raise ValueError("User name must be greater than 2 characters")
            elif psw != cpsw:
                raise ValueError("The passwords don't match")
            elif len(psw) < 7:
                raise ValueError("Password must be at least 7 characters")
            new_user = Users(
                email=email,
                username=username,
                password=generate_password_hash(psw, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            print(request.form)
            return redirect(url_for("auth.login"))
            

        except ValueError as e:
            return render_template("error.html",message=str(e))

    return render_template("register2.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form.get("username")
            psw = request.form.get("password")
            user = Users.query.filter_by(email=username).first()

            if user:
                if check_password_hash(user.password, psw):
                
                  
                    return render_template("index.html")
                else:
                    raise ValueError("Incorrect password")
                
                    
            else:
                raise ValueError("User does not exist")
                
        except ValueError as e:
            return render_template("error.html",message=str(e))

    return render_template("login.html")




