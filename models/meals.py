from database import db

class Meal(db.Model):
  #id, name, description, date, time, is_diet=False
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(60), nullable=False)
  description = db.Column(db.String(200), nullable=False)
  date = db.Column(db.Date, nullable=False)
  time = db.Column(db.Time, nullable=False)
  is_diet = db.Column(db.Boolean, default=False)
