from app import db


class ComponentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrase.id'), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    components = db.relationship('Component', backref='component_type')

    def __init__(self, phrase_id, name):
        self.phrase_id = phrase_id
        self.name = name

    def __repr__(self):
        return '<ComponentType %r>' % (self.name)
