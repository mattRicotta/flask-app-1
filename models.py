from datetime import datetime
from app import app, db

# User Class - name and contact info
class User(db.Model):
  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  username = db.Column(db.String(50), index = True, unique = True)
  name_first = db.Column(db.String(50), index = True, nullable = False)
  name_last = db.Column(db.String(50), index = True, nullable = False)
  email = db.Column(db.String(50), index = True, unique = True)
  street = db.Column(db.String(50))
  city = db.Column(db.String(50))
  state = db.Column(db.String(2))
  db.UniqueConstraint(username, email)
  
  # User child relationships
  resumes = db.relationship('Resume', backref='user', lazy='dynamic')
  jobs = db.relationship('Job', backref='user', lazy='dynamic')
  education = db.relationship('Education', backref='user', lazy='dynamic')
  certifications = db.relationship('Certification', backref='user', lazy='dynamic')
  skills = db.relationship('Skill', backref='user', lazy='dynamic')
  hobbies = db.relationship('Hobby', backref='user', lazy='dynamic')

  def __repr__(self):
    return self.username

# Job Class
class Job(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent user
  title = db.Column(db.String(50), index = True, nullable = False)
  org = db.Column(db.String(50), index = True, nullable = False)
  started_on = db.Column(db.DateTime, index = True, nullable = False)
  ended_on = db.Column(db.DateTime, index = True)
  city = db.Column(db.String(50))
  state = db.Column(db.String(50))
  highlights = db.relationship('JobHighlight', backref='job', lazy='dynamic')

  def __repr__(self):
    return "{} at {}".format(self.title, self.org)

# JobHighlight Class
class JobHighlight(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  job_id = db.Column(db.Integer, db.ForeignKey('job.id')) # parent job
  description = db.Column(db.String(150))
  
  def __repr__(self):
    return "{}: {}".format(self.job_id, self.description)

# Education Class
class Education(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent User
  level = db.Column(db.String(50), nullable = False)
  major = db.Column(db.String(50), nullable = False)
  org = db.Column(db.String(50), index=True, nullable = False)
  started_on = db.Column(db.DateTime, index=True, nullable = False)
  ended_on = db.Column(db.DateTime, index=True)
  city = db.Column(db.String(50), nullable = False)
  state = db.Column(db.String(20), nullable = False)
  
  def __repr__(self):
    return "{} from {}".format(self.level, self.org)

# Certification Class
class Certification(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent User
  cert_name = db.Column(db.String(50), nullable = False)
  org = db.Column(db.String(50), nullable = False)
  awarded_on = db.Column(db.DateTime, nullable = False)
  
  def __repr__(self):
    return f"{self.user}: {self.cert_name}"

# Skill Class
class Skill(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent User
  skill = db.Column(db.String(50), index = True, nullable = False)

  def __repr__(self):
    return f"{self.user}: {self.skill}"

class Hobby(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent User
  hobby = db.Column(db.String(50), index = True, nullable = False)

  def __repr__(self):
    return f"{self.user}: {self.hobby}"

class Resume(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # parent User
  name = db.Column(db.String(50), index=True, unique=True)

  def __repr__(self):
    return f"{self.user}: {self.name}"
