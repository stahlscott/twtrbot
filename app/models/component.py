from app import db


class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    component_type_id = db.Column(db.Integer, db.ForeignKey('component_type.id'), nullable=False)
    word = db.Column(db.String(140), nullable=False)

    def __init__(self, component_type_id, word):
        self.component_type_id = component_type_id
        self.word = word

    def __repr__(self):
        return '<Component %r>' % (self.word)
