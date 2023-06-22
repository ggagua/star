from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import random
from swapi import character
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from sqlalchemy.orm import relationship
from chatapi import chat_with_gpt
import sqlite3
from flask import jsonify
import os
from dotenv import load_dotenv
from redis import Redis




app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SECRET_KEY'] = 'highlysecuredhashkey'
db = SQLAlchemy(app)


#აკავშირების ფლასკს და ჩვენს ლოგინ სისტემას
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
load_dotenv()

redis = Redis(host='localhost', port=6379)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    message = db.relationship('Message', backref='logusr', uselist=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    user_input = db.Column(db.String(150))
    chatgpt_response = db.Column(db.String(350))

    def __str__(self):
        return f'{self.logged_user.username}: {self.user_input}'






with app.app_context():
    db.create_all()





class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
        Length(min=4, max=16)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(),
         Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            flash('Username already exists. Please choose a different one.', 'error')
            raise ValidationError(
                'Username already exists. Please choose a different one.')
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
        Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(),
         Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

limiter = Limiter(get_remote_address, app=app, storage_uri='redis://localhost:6379')

@app.route('/')
def home():
    return render_template('index.html')

    
    
@app.route('/next',)
def nextpage():
        return render_template('next-page.html')


@app.route('/login', methods = ['GET', 'POST'])
@limiter.limit("5/minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard', index=0))
        else:
            flash('Wrong credentials.', 'error')

    return render_template('login.html', form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.validate_username(form.username):
            pass
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/dashboard/', defaults={'index': 0})
@app.route('/dashboard/<int:index>')
@login_required
def dashboard(index):
    character_data = character
    main_title = list(character_data.keys())[index]
    main_description = character_data[main_title]['description']
    main_image = character_data[main_title]['image_url']
    return render_template('dashboard.html', main_image=main_image, main_description = main_description, main_title = main_title, index=index, character_data=character_data)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/about')
@login_required
def about():
    return render_template('about.html')


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    user_id = current_user.id
    chats = Message.query.filter_by(user_id=user_id).all()
    if request.method == 'POST':
        message = request.form.get('message')
        response = chat_with_gpt(message)
        data = {'message': message,
                'response': response}
        chat = Message(user_id=user_id, user_input=message, chatgpt_response=response)
        db.session.add(chat)
        db.session.commit()
        return jsonify(data)
    return render_template('chat.html', chats=chats)

@app.route('/creators')
def creators():
    return render_template('creators.html')



@app.errorhandler(404)
def page_not_found(e):
    names = ['not-found.html', 'not-found2.html']
    return render_template(random.choice(names))

@app.errorhandler(429)
def rate_reached(e):
    flash('Too many requests, you have sent. Try again in 1 minute, you should.')
    return render_template('limit.html')

@app.errorhandler(IndexError)
def handle_index_error(error):
    return redirect(url_for('dashboard', index = 0))




if __name__ == '__main__':
    app.run(debug=True)

