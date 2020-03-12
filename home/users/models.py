from app import db


class Guest(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(20))
    def __init__(self,  email=None):
        # self.name = name
        self.email = email
    # def __repr__(self):
    #     return super().__repr__()