class Entity:
    def __init__(self, name):
        self.name = name

class Universe:
    def __init__(self):
        self.time = 0
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def tick(self):
        self.time += 1
