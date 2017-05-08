from app import db


class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Phrase %r>' % (self.name)


class ComponentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase_type_id = db.Column(db.Integer, db.ForeignKey('phrase.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, phrase_type_id, name):
        self.phrase_type_id = phrase_type_id
        self.name = name

    def __repr__(self):
        return '<ComponentType %r>' % (self.name)


class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    component_type_id = db.Column(db.Integer, db.ForeignKey('component_type.id'), nullable=False)
    word = db.Column(db.String(140), nullable=False)

    def __init__(self, component_type, word):
        self.component_type = component_type
        self.word = word

    def __repr__(self):
        return '<Component %r>' % (self.word)
