from app.models.models import Component


class ComponentDAO():
    def __init__(self, db=None):
        self.db = db

    def get_or_create_component(self, component_type_id, word):
        return self.get_component_by_type_id_and_word(component_type_id, word) \
               or self.create_component(component_type_id, word)

    def get_component_by_type_id_and_word(self, component_type_id, word):
        return self.db.session.query(Component) \
            .filter(Component.component_type_id == component_type_id) \
            .filter(Component.word == word).first()

    def create_component(self, component_type_id, word):
        new_component = Component(component_type_id=component_type_id, word=word)
        self.db.session.add(new_component)
        self.db.session.commit()
        return self.get_component_by_type_id_and_word(component_type_id, word)

    def get_all_components_by_type_id(self, component_type_id):
        return self.db.session.query(Component).filter(Component.component_type_id == component_type_id).all()
