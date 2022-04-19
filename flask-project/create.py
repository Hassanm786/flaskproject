from application import db
from application.models import Fighter, Roster

db.drop_all()
db.create_all()