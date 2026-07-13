import random

class Food:
    def __init__(self, x=0, y=0, energy=5):
        self.x = x
        self.y = y
        self.energy = energy

class Entity:
    def __init__(self, name, x=0, y=0, energy=10, age=0, max_age=50, perception_radius=10):
        self.name = name
        self.x = x
        self.y = y
        self.energy = energy
        self.age = age
        self.max_age = max_age
        self.perception_radius = perception_radius
        self.memory = set()

    @property
    def is_alive(self):
        return self.energy > 0 and self.age <= self.max_age

class Terrain:
    def __init__(self, x=0, y=0, terrain_type='wall'):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type

class Universe:
    def __init__(self, width=100, height=100, food_spawn_rate=0.1, reproduction_threshold=20, reproduction_cost=10):
        self.time = 0
        self.entities = []
        self.foods = []
        self.terrains = []
        self.width = width
        self.height = height
        self.food_spawn_rate = food_spawn_rate
        self.reproduction_threshold = reproduction_threshold
        self.reproduction_cost = reproduction_cost
        self.current_event = None
        self.event_remaining_time = 0
        self.event_chance = 0.05

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

        terrains_here = self.get_terrains_at(new_x, new_y)
        if any(t.terrain_type in ['wall', 'water'] for t in terrains_here):
            raise ValueError(f"Movement blocked by terrain at ({new_x}, {new_y})")

        entity.x = new_x
        entity.y = new_y

    def get_terrains_at(self, x, y):
        return [t for t in self.terrains if t.x == x and t.y == y]

    def add_terrain(self, terrain):
        if not (0 <= terrain.x < self.width and 0 <= terrain.y < self.height):
            raise ValueError(f"Terrain out of bounds: ({terrain.x}, {terrain.y})")
        self.terrains.append(terrain)

    def find_path(self, start_x, start_y, target_x, target_y, max_distance=None, memory=None):
        from collections import deque
        queue = deque([(start_x, start_y, [])])
        visited = {(start_x, start_y)}

        # Directions: up, down, left, right
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while queue:
            current_x, current_y, path = queue.popleft()

            if current_x == target_x and current_y == target_y:
                return path

            for dx, dy in directions:
                new_x = current_x + dx
                new_y = current_y + dy

                if (new_x, new_y) not in visited:
                    if 0 <= new_x < self.width and 0 <= new_y < self.height:
                        # Ignore if in memory
                        if memory is not None and (new_x, new_y) in memory:
                            visited.add((new_x, new_y))
                        # Ignore obstacles beyond perception radius
                        elif max_distance is not None and (abs(new_x - start_x) + abs(new_y - start_y)) > max_distance:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y, path + [(dx, dy)]))
                        else:
                            terrains_here = self.get_terrains_at(new_x, new_y)
                            if not any(t.terrain_type in ['wall', 'water'] for t in terrains_here):
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y, path + [(dx, dy)]))

        return None  # No path found

    def get_entities_at(self, x, y):
        return [e for e in self.entities if e.x == x and e.y == y]

    def get_foods_at(self, x, y):
        return [f for f in self.foods if f.x == x and f.y == y]

    def get_nearest_food(self, x, y, max_distance=None):
        if not self.foods:
            return None

        nearest = None
        min_dist = float('inf')
        for food in self.foods:
            dist = abs(food.x - x) + abs(food.y - y)
            if max_distance is not None and dist > max_distance:
                continue
            if dist < min_dist:
                min_dist = dist
                nearest = food
        return nearest

    def tick(self):
        self.time += 1

        # Handle events
        if self.current_event:
            self.event_remaining_time -= 1
            if self.event_remaining_time <= 0:
                self.current_event = None
        elif random.random() < self.event_chance:
            self.current_event = random.choice(['storm', 'drought'])
            self.event_remaining_time = random.randint(5, 15)

        # Spawn new food
        current_food_spawn_rate = self.food_spawn_rate
        if self.current_event == 'drought':
            current_food_spawn_rate = 0.0

        if random.random() < current_food_spawn_rate:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.add_food(Food(x=x, y=y))

        new_entities = []

        for entity in self.entities:
            # Consume energy per tick
            energy_loss = 1
            if self.current_event == 'storm':
                energy_loss = 2
            entity.energy -= energy_loss
            # Age by 1 per tick
            entity.age += 1

            if entity.is_alive:
                # Reproduction
                if entity.energy >= self.reproduction_threshold:
                    entity.energy -= self.reproduction_cost

                    # Genetics and Mutations
                    # Base traits inherited from parent
                    child_max_age = entity.max_age
                    child_perception_radius = entity.perception_radius

                    # Mutation chance
                    mutation_chance = 0.1
                    if random.random() < mutation_chance:
                        # Mutate max_age by up to +/- 5
                        child_max_age += random.randint(-5, 5)
                        child_max_age = max(10, child_max_age) # Ensure it doesn't go too low

                    if random.random() < mutation_chance:
                        # Mutate perception_radius by up to +/- 2
                        child_perception_radius += random.randint(-2, 2)
                        child_perception_radius = max(1, child_perception_radius) # Minimum perception of 1

                    child = Entity(name=f"{entity.name}_child", x=entity.x, y=entity.y,
                                   max_age=child_max_age, perception_radius=child_perception_radius)
                    new_entities.append(child)

                # Update entity memory with visible obstacles
                for t in self.terrains:
                    if t.terrain_type in ['wall', 'water'] and (abs(t.x - entity.x) + abs(t.y - entity.y)) <= entity.perception_radius:
                        entity.memory.add((t.x, t.y))

                nearest_food = self.get_nearest_food(entity.x, entity.y, max_distance=entity.perception_radius)
                if nearest_food:
                    path = self.find_path(entity.x, entity.y, nearest_food.x, nearest_food.y, max_distance=entity.perception_radius, memory=entity.memory)
                    if path and len(path) > 0:
                        dx, dy = path[0]
                        try:
                            self.move_entity(entity, dx, dy)
                        except ValueError:
                            pass # Blocked

                # Check for food at entity location
                foods_here = self.get_foods_at(entity.x, entity.y)
                if foods_here:
                    food_to_eat = foods_here[0]
                    entity.energy += food_to_eat.energy
                    self.foods.remove(food_to_eat)

        self.entities = [e for e in self.entities if e.is_alive]
        for child in new_entities:
            self.add_entity(child)
