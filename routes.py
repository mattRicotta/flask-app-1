# env
from flask import render_template, request, url_for
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# local
from app import app, db
from models import *

# resume-app page
@app.route('/')
def index():
  users = User.query.all()
  return render_template("index.html", users=users)

@app.route('/newuser')
def newuser():
  return render_template("new_user.html")

@app.route('/profile/<int:user_id>')
def profile(user_id):
  user = User.query.get(user_id)
  return render_template("profile.html", user=user)

# resume page
'''
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
'''
