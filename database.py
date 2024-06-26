from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, JSON, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Boolean

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
notes = db.Column(String(100))
priority = db.Column(Integer, default=0)
completed = db.Column(Boolean, default=False)
due_date = db.Column(String(50))

class Todo(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    recommendations = []  # non-persistent field
    recommendations_json = db.Column(db.JSON)

    def __str__(self):
        return self.name
    
    def priority_str(self):
        """
        Returns the priority as a string.
        """
        str = "Not Set"
        if self.priority == 1:
            str = "High"
        elif self.priority == 2:
            str = "Medium"
        elif self.priority == 3:
            str = "Low"

        return str

def completed_str(self):
    """
    Returns the completed status as a string.
    """
    if self.completed:
        return "Yes"
    else:    
        return "No"
    
    
    