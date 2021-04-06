from app import db
from models import *
from datetime import datetime

db.create_all()


# create a record for test user
test_user = User(
  username='TestUser123',
  name_first='Test',
  name_last='User', 
  email='TestUser123@example.email.com',
  street='123 Fake St',
  city='Springfield',
  state='OR'
)

# add user and flush to obtain autonumber PK
db.session.add(test_user)
db.session.flush()

# create a job record for the test user
j1 = Job(
  user_id=test_user.id,
  title='VP of Sales',
  org='ABC Company',
  city='Springfield',
  state='OR',
  started_on=datetime(2015, 1, 1)
)

# add job and flush to obtain autonumber PK
db.session.add(j1)
db.session.flush()

# create highlights for Job j1
jh_lst = [
  'Increased sales yearly by 60% from 2018-2020',
  'Led a sales department of 50 people selling over $1M per year',
  'Bought everybody lunch on Fridays because I\'m just that awesome!'
]

for item in jh_lst:
  db.session.add(JobHighlight(job_id=j1.id, description=item))

# create education for Test User
e1 = Education(
  user_id=test_user.id,
  level='Bachelor of Science',
  major='Rocket Science',
  org='Some University',
  city='Springfield',
  state='OR',
  started_on=datetime(2000,9,1),
  ended_on=datetime(2004, 5, 1)
)

e2 = Education(
  user_id=test_user.id,
  level='MBA',
  major='Business',
  org='An Even Better University',
  city='Shelbyville',
  state='OR',
  started_on=datetime(2004, 9, 1),
  ended_on=datetime(2006, 6, 1)
)

db.session.add(e1)
db.session.add(e2)

# create skills
skills_lst = [
  'Making People Awesome',
  'Holding it down',
  'Bringing it up',
  'Making things happen'
]

for item in skills_lst:
  db.session.add(Skill(user_id=test_user.id, skill=item))

# create hobbies
hby_lst = [
  'Making Sculptures',
  'Whittling',
  'Shower Singing',
  'Whistling'
]

for item in hby_lst:
  db.session.add(Hobby(user_id=test_user.id, hobby=item))

# Commit Changes to Database
db.session.commit()