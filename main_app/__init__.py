# This is a blog app that allows users to register and post blogs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '63b39e970e74a330324913b5db1b61e4'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from main_app import routes