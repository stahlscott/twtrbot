from app.models.component_type import ComponentType


class ComponentTypeDAO():
    def __init__(self, db):
        self.db = db

    def get_or_create_component_type(self, name, phrase_id):
        return self.get_component_type_by_name(name) or self.create_component_type(name, phrase_id)

    def get_component_type_by_name(self, name):
        return self.db.session.query(ComponentType).filter(ComponentType.name == name).first()

    def create_component_type(self, name, phrase_id):
        new_component_type = ComponentType(name=name, phrase_id=phrase_id)
        self.db.session.add(new_component_type)
        self.db.session.commit()
        return self.get_component_type_by_name(name)
