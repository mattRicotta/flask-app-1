from flask import Flask, render_template
from resume import *
app = Flask(__name__)

@app.route('/')
def index():
  return render_template(
    "index.html", 
    links=links, 
    about=about, 
    work_experience=work_experience, 
    education=education, 
    certifications=certifications, 
    publications=publications, 
    skills=skills, 
    hobbies=hobbies
  )