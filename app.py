from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from resume_helper import * 
from index_helper import *

app = Flask(__name__)
#set up database (flask_sqlalchemy library installed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

# home page
@app.route('/')
def index():
  return render_template("index.html", index_links=index_links)

# projects page
@app.route('/projects')
def projects():
  return render_template("projects.html")
# resume page
@app.route('/resume')
def resume():
  def list_chunk(lst, chunk_length):

    return [lst[i:i + chunk_length] for i in range(0, len(lst), chunk_length)]

  return render_template("resume.html",
    contact_info=contact_info, 
    links=links, 
    about=about, 
    work_experience=work_experience, 
    education=education, 
    certifications=certifications, 
    publications=publications, 
    skills=list_chunk(skills, 4), 
    hobbies=list_chunk(hobbies, 4)
  )
