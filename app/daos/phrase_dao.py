from app.models.models import Phrase


class PhraseDAO():
    def __init__(self, db=None):
        self.db = db

    def get_or_create_phrase(self, name, display_name):
        return self.get_phrase_by_name(name) or self.create_phrase(name, display_name)

    def get_phrase_by_name(self, name):
        return self.db.session.query(Phrase).filter(Phrase.name == name).first()

    def create_phrase(self, name, display_name):
        new_phrase = Phrase(name=name, display_name=display_name)
        self.db.session.add(new_phrase)
        self.db.session.commit()
        return self.get_phrase_by_name(name=name)
