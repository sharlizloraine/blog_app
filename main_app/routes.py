from flask import render_template, url_for, flash, redirect 
from main_app import app
from main_app.forms import RegistrationForm, LoginForm
from main_app.models import User, Post

# List of Post dictionaries 
posts = [
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 2 2022'
    }, 
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 2',
        'content': 'Second post content', 
        'date_posted': 'February 14 2022'
    },
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 3',
        'content': 'Third post content', 
        'date_posted': 'February 23 2022'
    }
]

# Routes 

# Route for homepage
@app.route("/") # Route for main page 
@app.route("/home") # Route to home page 
def home():
    return render_template('home.html', posts=posts) # Call to render the home page template 

# Route for about page 
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Route for registration page 
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): 
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# Route for login page 
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Login Unsuccessful! Please check your username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)