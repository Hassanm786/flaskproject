from wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_wtf import FlaskForm
from application import db



class Fighter(db.Model):
    __tablename__ = "Fighter"
    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
    name = db.Column(db.String(65), nullable=False, unique = True)
    country = db.Column(db.String(35), nullable=False)
    roster = db.relationship('Roster', backref="rosterbr")
   

class Roster(db.Model):
    __tablename__ = "Roster"
    id = db.Column(db.Integer, primary_key=True)
    weight_class = (db.Column(db.String(25), nullable=False))
    rank = db.Column(db.Integer, nullable=False)
    fighter_name = db.Column(db.String(65), db.ForeignKey("Fighter.name"))

class AddFighter(FlaskForm):
    name = StringField("Enter the full name of the fighter")
    country = StringField("Enter the country the fighter is representing")
    submit = SubmitField("Submit")
    
class AddRoster(FlaskForm):
    weight_class = StringField("Please enter the weight class")
    rank = IntegerField("Enter the fighters rank")
    fighter_name = StringField("Add the fighter name")
    submit = SubmitField("Submit")