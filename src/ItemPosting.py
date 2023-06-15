from main import db

class ItemPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=False)
    tags = db.Column(db.String, nullable=False)