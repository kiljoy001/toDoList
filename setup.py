"""
Sets up database
"""
from datetime import datetime
from model import db, User, Task

# create the database for model
db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

Task(name='Do the laundry').save()
Task(name='Do the dishes', performed=datetime.now()).save()
