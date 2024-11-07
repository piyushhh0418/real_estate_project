from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import db from __init__.py
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Logged in successfully!", category='success')
            return redirect(url_for('views.home'))
        else:
            flash("Incorrect email or password. Please try again.", category='error')
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone = request.form.get('phone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        print(f"Password1: {password1}, Password2: {password2}")  # Debugging

        # Ensure password fields are not None or empty
        if not password1 or not password2:
            flash("Password fields cannot be empty", category="error")
            return redirect(url_for('auth.sign_up'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category='error')
        elif len(name) < 3:
            flash('Name must be greater than 2 characters.', category='error')
        elif len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(phone) != 10:
            flash('Phone number cannot be greater than 10 digits.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        else:
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
            new_user = User(email=email, first_name=name, phone=phone, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created Successfully!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", show_chatbot=False)

