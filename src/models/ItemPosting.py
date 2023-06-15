from main import db

class ItemPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    tags = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=False)
    user =  db.Column(db.Integer, nullable=False)


    def __init__(self,image,description, tags, status, user):
        self.image = image
        self.description = description
        self.tags = tags
        self.status = status
        self.user = user