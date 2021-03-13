from flask import Flask, render_template
from resume_data import about, work_experience, education, certifications, publications, skills, hobbies

app = Flask(__name__)

@app.route('/')
def index():
  return render_template(
    "index.html", 
    about=about, 
    work_experience=work_experience, 
    education=education, 
    certifications=certifications, 
    publications=publications, 
    skills=skills, 
    hobbies=hobbies
  )