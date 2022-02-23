from flask import Flask, render_template, url_for
app = Flask(__name__)

# List of Post dictionaries 
posts = [
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 1',
        'content': 'First post content', 
        'date posted': 'February 2 2022'
    }, 
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 2',
        'content': 'Second post content', 
        'date posted': 'February 14 2022'
    },
    
    {
        'author': 'Sharliz Ang',
        'title': 'Blog Post 3',
        'content': 'Third post content', 
        'date posted': 'February 23 2022'
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

# Allows main app to run the web server
if __name__ == '__main__':
    app.run(debug=True)