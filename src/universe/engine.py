import random

class Food:
    def __init__(self, x=0, y=0, energy=5):
        self.x = x
        self.y = y
        self.energy = energy

class Entity:
    def __init__(self, name, x=0, y=0, energy=10):
        self.name = name
        self.x = x
        self.y = y
        self.energy = energy

    @property
    def is_alive(self):
        return self.energy > 0

class Food:
    def __init__(self, x=0, y=0, energy=5):
        self.x = x
        self.y = y
        self.energy = energy

class Universe:
    def __init__(self, width=100, height=100, food_spawn_rate=0.1, reproduction_threshold=20, reproduction_cost=10):
        self.time = 0
        self.entities = []
        self.foods = []
        self.width = width
        self.height = height
        self.food_spawn_rate = food_spawn_rate
        self.reproduction_threshold = reproduction_threshold
        self.reproduction_cost = reproduction_cost

    def add_food(self, food, x=None, y=None):
        if x is not None:
            food.x = x
        if y is not None:
            food.y = y

        if not (0 <= food.x < self.width and 0 <= food.y < self.height):
            raise ValueError(f"Food out of bounds: ({food.x}, {food.y})")

        self.foods.append(food)

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

    def add_food(self, food, x=None, y=None):
        if x is not None:
            food.x = x
        if y is not None:
            food.y = y

        if not (0 <= food.x < self.width and 0 <= food.y < self.height):
            raise ValueError(f"Food out of bounds: ({food.x}, {food.y})")

        self.foods.append(food)

    def get_foods_at(self, x, y):
        return [f for f in self.foods if f.x == x and f.y == y]


    def get_nearest_food(self, x, y):
        if not self.foods:
            return None

        nearest = None
        min_dist = float('inf')
        for food in self.foods:
            dist = abs(food.x - x) + abs(food.y - y)
            if dist < min_dist:
                min_dist = dist
                nearest = food
        return nearest

    def tick(self):
        self.time += 1

        # Spawn new food
        if random.random() < self.food_spawn_rate:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.add_food(Food(x=x, y=y))

        new_entities = []

        for entity in self.entities:
            # Consume 1 energy per tick
            entity.energy -= 1

            if entity.is_alive:
                # Reproduction
                if entity.energy >= self.reproduction_threshold:
                    entity.energy -= self.reproduction_cost
                    child = Entity(name=f"{entity.name}_child", x=entity.x, y=entity.y)
                    new_entities.append(child)

                nearest_food = self.get_nearest_food(entity.x, entity.y)
                if nearest_food:
                    # Move towards food
                    dx = 0
                    dy = 0
                    if nearest_food.x > entity.x:
                        dx = 1
                    elif nearest_food.x < entity.x:
                        dx = -1

                    if nearest_food.y > entity.y:
                        dy = 1
                    elif nearest_food.y < entity.y:
                        dy = -1

                    if dx != 0 or dy != 0:
                        try:
                            self.move_entity(entity, dx, dy)
                        except ValueError:
                            pass # In case movement is out of bounds, shouldn't happen but safe

                # Check for food at entity location
                foods_here = self.get_foods_at(entity.x, entity.y)
                if foods_here:
                    food_to_eat = foods_here[0]
                    entity.energy += food_to_eat.energy
                    self.foods.remove(food_to_eat)

        self.entities = [e for e in self.entities if e.is_alive]
        for child in new_entities:
            self.add_entity(child)
