from app import db


class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(50), unique=True, nullable=False)
    component_types = db.relationship('ComponentType', backref='phrase')

    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name

    def __repr__(self):
        return '<Phrase %r>' % (self.name)
