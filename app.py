from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#set up database (flask_sqlalchemy library installed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

import routes