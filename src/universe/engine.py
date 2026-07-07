class Entity:
    def __init__(self, name, x=0, y=0, energy=10):
        self.name = name
        self.x = x
        self.y = y
        self.energy = energy

    @property
    def is_alive(self):
        return self.energy > 0

class Universe:
    def __init__(self, width=100, height=100):
        self.time = 0
        self.entities = []
        self.width = width
        self.height = height

    def add_entity(self, entity, x=None, y=None):
        if x is not None:
            entity.x = x
        if y is not None:
            entity.y = y

        if not (0 <= entity.x < self.width and 0 <= entity.y < self.height):
            raise ValueError(f"Entity out of bounds: ({entity.x}, {entity.y})")

        self.entities.append(entity)

    def move_entity(self, entity, dx, dy):
        new_x = entity.x + dx
        new_y = entity.y + dy
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            raise ValueError(f"Movement out of bounds: ({new_x}, {new_y})")
        entity.x = new_x
        entity.y = new_y

    def get_entities_at(self, x, y):
        return [e for e in self.entities if e.x == x and e.y == y]

    def tick(self):
        self.time += 1
        for entity in self.entities:
            entity.energy -= 1
        self.entities = [e for e in self.entities if e.is_alive]
