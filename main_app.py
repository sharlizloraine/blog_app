# This is a blog app that allows users to register and post blogs

from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '63b39e970e74a330324913b5db1b61e4'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///sitde.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(20), unique=True, nullable=False)
    email = db.Column(db.string(120), unique=True, nullable=False)
    image_file = db.Column(db.string(20), nullable=False, default='default.jpg')
    password = db.Column(db.string(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    

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


# Allows main app to run the web server
if __name__ == '__main__':
    app.run(debug=True)