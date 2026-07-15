import random

class Food:
    def __init__(self, x=0, y=0, energy=5):
        self.x = x
        self.y = y
        self.energy = energy

class Entity:
    def __init__(self, name, x=0, y=0, energy=10, age=0, max_age=50, perception_radius=10, diet='herbivore', preferred_temperature=20, temperature_tolerance=40, is_infected=False, infection_time=0, species=None, symbiotic_with=None, attack=1, defense=1):
        if species is None:
            species = name
        if symbiotic_with is None:
            symbiotic_with = []
        self.species = species
        self.symbiotic_with = symbiotic_with
        self.attack = attack
        self.defense = defense
        self.name = name
        self.x = x
        self.y = y
        self.energy = energy
        self.age = age
        self.max_age = max_age
        self.perception_radius = perception_radius
        self.preferred_temperature = preferred_temperature
        self.temperature_tolerance = temperature_tolerance
        self.alerted_predator_pos = None
        self.is_infected = is_infected
        self.infection_time = infection_time
        self.memory = set()
        self.diet = diet
        self.preferred_temperature = preferred_temperature
        self.temperature_tolerance = temperature_tolerance

    @property
    def is_alive(self):
        return self.energy > 0 and self.age <= self.max_age


class LocalizedEvent:
    def __init__(self, event_type, x, y, radius, duration):
        self.event_type = event_type
        self.x = x
        self.y = y
        self.radius = radius
        self.duration = duration

class Terrain:
    def __init__(self, x=0, y=0, terrain_type='wall'):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type

class TemperatureZone:
    def __init__(self, x, y, radius, temperature_modifier):
        self.x = x
        self.y = y
        self.radius = radius
        self.temperature_modifier = temperature_modifier

class Universe:
    def __init__(self, width=100, height=100, food_spawn_rate=0.1, reproduction_threshold=20, reproduction_cost=10, population_limit=1000, season_length=50, day_length=20, disease_chance=0.01):
        self.time = 0
        self.entities = []
        self.foods = []
        self.terrains = []
        self.temperature_zones = []
        self.base_temperature = 20
        self.width = width
        self.height = height
        self.food_spawn_rate = food_spawn_rate
        self.reproduction_threshold = reproduction_threshold
        self.reproduction_cost = reproduction_cost
        self.population_limit = population_limit
        self.current_event = None
        self.event_remaining_time = 0
        self.event_chance = 0.05
        self.season_length = season_length
        self.day_length = day_length
        self.seasons = ['spring', 'summer', 'autumn', 'winter']
        self._last_season = 'spring'
        self.localized_events = []
        self.localized_event_chance = 0.02
        self.scent_trails = {}
        self.disease_chance = disease_chance

    @property
    def is_day(self):
        return (self.time % self.day_length) < (self.day_length // 2)

    @property
    def is_night(self):
        return not self.is_day

    @property
    def current_season(self):
        season_index = (self.time // self.season_length) % 4
        return self.seasons[season_index]

    def add_food(self, food, x=None, y=None):
        if x is not None:
            food.x = x
        if y is not None:
            food.y = y

        if not (0 <= food.x < self.width and 0 <= food.y < self.height):
            raise ValueError(f"Food out of bounds: ({food.x}, {food.y})")

        self.foods.append(food)

    def add_temperature_zone(self, zone):
        self.temperature_zones.append(zone)

    def get_temperature_at(self, x, y):
        temp = self.base_temperature
        for zone in self.temperature_zones:
            if (x - zone.x)**2 + (y - zone.y)**2 <= zone.radius**2:
                temp += zone.temperature_modifier
        return temp

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

    def get_preys_at(self, x, y):
        return [e for e in self.entities if e.x == x and e.y == y and e.diet == 'herbivore' and e.is_alive]

    def get_nearest_prey(self, x, y, max_distance=None):
        if not self.entities:
            return None

        nearest = None
        min_dist = float('inf')
        for e in self.entities:
            if e.diet != 'herbivore' or not e.is_alive:
                continue
            dist = abs(e.x - x) + abs(e.y - y)
            if max_distance is not None and dist > max_distance:
                continue
            if dist < min_dist:
                min_dist = dist
                nearest = e
        return nearest


    def get_nearest_predator(self, x, y, max_distance=None):
        if not self.entities:
            return None

        nearest = None
        min_dist = float('inf')
        for e in self.entities:
            if e.diet == 'carnivore' and e.is_alive:
                dist = abs(e.x - x) + abs(e.y - y)
                if max_distance is not None and dist > max_distance:
                    continue
                if dist < min_dist:
                    min_dist = dist
                    nearest = e
        return nearest


    def get_nearby_flockmates(self, entity, max_distance):
        flockmates = []
        for e in self.entities:
            if e != entity and e.is_alive and e.diet == entity.diet:
                dist = abs(e.x - entity.x) + abs(e.y - entity.y)
                if dist <= max_distance:
                    flockmates.append(e)
        return flockmates

    def tick(self):
        self.time += 1

        current_season = self.current_season

        # Decay scent trails
        new_scent_trails = {}
        for pos, intensity in self.scent_trails.items():
            if intensity > 1:
                new_scent_trails[pos] = intensity - 1
        self.scent_trails = new_scent_trails

        # Spontaneous disease outbreak
        if random.random() < self.disease_chance and self.entities:
            target = random.choice(self.entities)
            target.is_infected = True

        if current_season != self._last_season:
            self._last_season = current_season

        if current_season == 'spring':
            self.base_temperature = 20
        elif current_season == 'summer':
            self.base_temperature = 30
        elif current_season == 'autumn':
            self.base_temperature = 10
        elif current_season == 'winter':
            self.base_temperature = -5

        # Localized temperature-based terrain transitions
        terrains_to_remove = []
        for t in self.terrains:
            local_temp = self.get_temperature_at(t.x, t.y)
            if t.terrain_type == 'water' and local_temp <= 0:
                t.terrain_type = 'ice'
            elif t.terrain_type == 'ice' and local_temp > 0:
                t.terrain_type = 'water'
            elif t.terrain_type == 'mud' and local_temp >= 20 and random.random() < 0.05:
                terrains_to_remove.append(t)

        for t in terrains_to_remove:
            if t in self.terrains:
                self.terrains.remove(t)

        # Handle events
        if self.current_event:
            self.event_remaining_time -= 1
            if self.event_remaining_time <= 0:
                self.current_event = None
        elif random.random() < self.event_chance:
            self.current_event = random.choice(['storm', 'drought', 'earthquake', 'volcano'])
            self.event_remaining_time = random.randint(5, 15)

            if self.current_event == 'earthquake':
                for fx in range(self.width):
                    for fy in range(self.height):
                        if random.random() < 0.05:
                            terrains_here = self.get_terrains_at(fx, fy)
                            wall_terrains = [t for t in terrains_here if t.terrain_type == 'wall']
                            if wall_terrains:
                                for t in wall_terrains:
                                    self.terrains.remove(t)
                            else:
                                self.add_terrain(Terrain(x=fx, y=fy, terrain_type='wall'))
            elif self.current_event == 'volcano':
                for fx in range(self.width):
                    for fy in range(self.height):
                        if random.random() < 0.05:
                            terrains_here = self.get_terrains_at(fx, fy)
                            if terrains_here:
                                for t in terrains_here:
                                    if t.terrain_type not in ['water', 'ice', 'ash']:
                                        t.terrain_type = 'ash'
                            else:
                                self.add_terrain(Terrain(x=fx, y=fy, terrain_type='ash'))

        # Handle localized events
        if random.random() < self.localized_event_chance:
            event_type = random.choice(['rain', 'fire'])
            event_x = random.randint(0, self.width - 1)
            event_y = random.randint(0, self.height - 1)
            radius = random.randint(3, 8)
            duration = random.randint(10, 20)
            self.localized_events.append(LocalizedEvent(event_type, event_x, event_y, radius, duration))

        for event in self.localized_events[:]:
            event.duration -= 1
            if event.duration <= 0:
                self.localized_events.remove(event)
                continue

            if event.event_type == 'rain':
                if random.random() < 0.2:  # Chance to spawn food
                    fx = event.x + random.randint(-event.radius, event.radius)
                    fy = event.y + random.randint(-event.radius, event.radius)
                    if 0 <= fx < self.width and 0 <= fy < self.height:
                        if (fx - event.x)**2 + (fy - event.y)**2 <= event.radius**2:
                            self.add_food(Food(x=fx, y=fy))

                # Rain dynamic terrain (mud creation, washing away ash/sand)
                for _ in range(3): # Try a few spots per tick
                    rx = event.x + random.randint(-event.radius, event.radius)
                    ry = event.y + random.randint(-event.radius, event.radius)
                    if 0 <= rx < self.width and 0 <= ry < self.height:
                        if (rx - event.x)**2 + (ry - event.y)**2 <= event.radius**2:
                            terrains_here = self.get_terrains_at(rx, ry)
                            if terrains_here:
                                for t in terrains_here:
                                    if t.terrain_type in ['ash', 'sand']:
                                        self.terrains.remove(t)
                            elif random.random() < 0.1: # 10% chance to create mud if empty
                                self.add_terrain(Terrain(x=rx, y=ry, terrain_type='mud'))
            elif event.event_type == 'fire':
                for fx in range(max(0, event.x - event.radius), min(self.width, event.x + event.radius + 1)):
                    for fy in range(max(0, event.y - event.radius), min(self.height, event.y + event.radius + 1)):
                        if (fx - event.x)**2 + (fy - event.y)**2 <= event.radius**2:
                            # Kill entities
                            entities_here = self.get_entities_at(fx, fy)
                            for e in entities_here:
                                e.energy = 0
                                # Convert dead entity spot to ash terrain
                                self.add_terrain(Terrain(x=fx, y=fy, terrain_type='ash'))

                            # Destroy food
                            foods_here = self.get_foods_at(fx, fy)
                            for fd in foods_here:
                                self.foods.remove(fd)
                                # Convert destroyed food spot to ash terrain
                                self.add_terrain(Terrain(x=fx, y=fy, terrain_type='ash'))

                            # Convert existing non-water terrain to ash
                            terrains_here = self.get_terrains_at(fx, fy)
                            for t in terrains_here:
                                if t.terrain_type not in ['water', 'ice', 'ash']:
                                    t.terrain_type = 'ash'

        # High temperatures/drought create sand
        if self.current_event == 'drought' or (self.current_season == 'summer' and random.random() < 0.5):
            for _ in range(5):
                hx = random.randint(0, self.width - 1)
                hy = random.randint(0, self.height - 1)
                if self.get_temperature_at(hx, hy) >= 30:
                    if not self.get_terrains_at(hx, hy):
                        self.add_terrain(Terrain(x=hx, y=hy, terrain_type='sand'))

        # Spawn new food
        current_food_spawn_rate = self.food_spawn_rate
        if self.current_event == 'drought':
            current_food_spawn_rate = 0.0

        if current_food_spawn_rate > 0.0:
            if current_season == 'spring':
                current_food_spawn_rate *= 1.5
            elif current_season == 'summer':
                current_food_spawn_rate *= 1.0
            elif current_season == 'autumn':
                current_food_spawn_rate *= 0.8
            elif current_season == 'winter':
                current_food_spawn_rate *= 0.2

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

            if entity.is_infected:
                energy_loss += 1
                entity.infection_time += 1

                # Recovery
                if entity.infection_time > 10 and random.random() < 0.2:
                    entity.is_infected = False
                    entity.infection_time = 0

                # Spread
                if entity.is_infected:
                    for other in self.entities:
                        if other != entity and other.is_alive and not other.is_infected:
                            dist = abs(other.x - entity.x) + abs(other.y - entity.y)
                            if dist <= 2 and random.random() < 0.1:
                                other.is_infected = True

            # Temperature check
            current_temp = self.get_temperature_at(entity.x, entity.y)
            if not (entity.preferred_temperature - entity.temperature_tolerance <= current_temp <= entity.preferred_temperature + entity.temperature_tolerance):
                energy_loss += 1

            # Symbiosis check
            if entity.symbiotic_with:
                for other in self.entities:
                    if other != entity and other.is_alive and other.species in entity.symbiotic_with:
                        dist = abs(other.x - entity.x) + abs(other.y - entity.y)
                        if dist <= 2:
                            # Reduced energy loss due to symbiosis benefit
                            energy_loss = max(0, energy_loss - 1)
                            break

            entity.energy -= energy_loss
            # Age by 1 per tick
            entity.age += 1

            if entity.is_alive:
                # Reproduction
                if entity.energy >= self.reproduction_threshold and (len(self.entities) + len(new_entities) < self.population_limit):
                    entity.energy -= self.reproduction_cost

                    # Genetics and Mutations
                    # Base traits inherited from parent
                    child_max_age = entity.max_age
                    child_perception_radius = entity.perception_radius
                    child_preferred_temperature = entity.preferred_temperature
                    child_temperature_tolerance = entity.temperature_tolerance
                    child_attack = entity.attack
                    child_defense = entity.defense

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

                    if random.random() < mutation_chance:
                        child_preferred_temperature += random.randint(-5, 5)
                        child_preferred_temperature = max(-20, min(60, child_preferred_temperature))

                    if random.random() < mutation_chance:
                        child_temperature_tolerance += random.randint(-2, 2)
                        child_temperature_tolerance = max(1, child_temperature_tolerance)

                    if random.random() < mutation_chance:
                        child_attack += random.randint(-1, 1)
                        child_attack = max(0, child_attack)

                    if random.random() < mutation_chance:
                        child_defense += random.randint(-1, 1)
                        child_defense = max(0, child_defense)

                    child = Entity(name=f"{entity.name}_child", x=entity.x, y=entity.y,
                                   max_age=child_max_age, perception_radius=child_perception_radius, diet=entity.diet,
                                   preferred_temperature=child_preferred_temperature, temperature_tolerance=child_temperature_tolerance,
                                   species=entity.species, symbiotic_with=entity.symbiotic_with.copy(),
                                   attack=child_attack, defense=child_defense)
                    new_entities.append(child)

                effective_perception = entity.perception_radius if self.is_day else max(1, entity.perception_radius // 2)

                # Update entity memory with visible obstacles
                for t in self.terrains:
                    if t.terrain_type in ['wall', 'water'] and (abs(t.x - entity.x) + abs(t.y - entity.y)) <= effective_perception:
                        entity.memory.add((t.x, t.y))

                can_move = True
                if self.is_night and random.random() < 0.5:
                    can_move = False
                if entity.diet == 'herbivore':
                    if can_move:
                        # Communication & Flee behavior
                        nearest_predator = self.get_nearest_predator(entity.x, entity.y, max_distance=effective_perception)
                        if nearest_predator:
                            entity.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)
                            # Alert nearby flockmates (double perception radius for communication)
                            flockmates_to_alert = self.get_nearby_flockmates(entity, effective_perception * 2)
                            for f in flockmates_to_alert:
                                f.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)

                        if entity.alerted_predator_pos:
                            px, py = entity.alerted_predator_pos
                            # Try to move away from predator
                            best_pos = None
                            max_dist = -1
                            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                nx, ny = entity.x + dx, entity.y + dy
                                try:
                                    # Basic bounds/terrain check before moving
                                    if 0 <= nx < self.width and 0 <= ny < self.height:
                                        terrains_here = self.get_terrains_at(nx, ny)
                                        if not any(t.terrain_type in ['wall', 'water'] for t in terrains_here):
                                            dist_to_predator = abs(nx - px) + abs(ny - py)
                                            if dist_to_predator > max_dist:
                                                max_dist = dist_to_predator
                                                best_pos = (dx, dy)
                                except Exception:
                                    pass

                            if best_pos:
                                try:
                                    self.move_entity(entity, best_pos[0], best_pos[1])
                                except ValueError:
                                    pass
                            entity.alerted_predator_pos = None
                        else:
                            nearest_food = self.get_nearest_food(entity.x, entity.y, max_distance=effective_perception)
                            if nearest_food:
                                path = self.find_path(entity.x, entity.y, nearest_food.x, nearest_food.y, max_distance=effective_perception, memory=entity.memory)
                                if path and len(path) > 0:
                                    dx, dy = path[0]
                                    try:
                                        self.move_entity(entity, dx, dy)
                                    except ValueError:
                                        pass # Blocked
                            else:
                                # Flocking behavior: move towards center of mass of nearby flockmates
                                flockmates = self.get_nearby_flockmates(entity, effective_perception)
                                if flockmates:
                                    center_x = sum(e.x for e in flockmates) // len(flockmates)
                                    center_y = sum(e.y for e in flockmates) // len(flockmates)
                                    if center_x != entity.x or center_y != entity.y:
                                        path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory)
                                        if path and len(path) > 0:
                                            dx, dy = path[0]
                                            try:
                                                self.move_entity(entity, dx, dy)
                                            except ValueError:
                                                pass

                    # Check for food at entity location
                    foods_here = self.get_foods_at(entity.x, entity.y)
                    if foods_here:
                        food_to_eat = foods_here[0]
                        entity.energy += food_to_eat.energy
                        self.foods.remove(food_to_eat)
                elif entity.diet == 'carnivore':
                    if can_move:
                        nearest_prey = self.get_nearest_prey(entity.x, entity.y, max_distance=effective_perception)
                        if nearest_prey:
                            path = self.find_path(entity.x, entity.y, nearest_prey.x, nearest_prey.y, max_distance=effective_perception, memory=entity.memory)
                            if path and len(path) > 0:
                                dx, dy = path[0]
                                try:
                                    self.move_entity(entity, dx, dy)
                                except ValueError:
                                    pass # Blocked
                        else:
                            # Scent tracking behavior
                            best_scent = 0
                            best_pos = None
                            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                nx, ny = entity.x + dx, entity.y + dy
                                if (nx, ny) in self.scent_trails and self.scent_trails[(nx, ny)] > best_scent:
                                    terrains_here = self.get_terrains_at(nx, ny)
                                    if not any(t.terrain_type in ['wall', 'water'] for t in terrains_here):
                                        best_scent = self.scent_trails[(nx, ny)]
                                        best_pos = (dx, dy)
                            if best_pos:
                                try:
                                    self.move_entity(entity, best_pos[0], best_pos[1])
                                except ValueError:
                                    pass
                            else:
                                # Flocking behavior: move towards center of mass of nearby flockmates
                                flockmates = self.get_nearby_flockmates(entity, effective_perception)
                                if flockmates:
                                    center_x = sum(e.x for e in flockmates) // len(flockmates)
                                    center_y = sum(e.y for e in flockmates) // len(flockmates)
                                    if center_x != entity.x or center_y != entity.y:
                                        path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory)
                                        if path and len(path) > 0:
                                            dx, dy = path[0]
                                            try:
                                                self.move_entity(entity, dx, dy)
                                            except ValueError:
                                                pass


                    # Check for prey at entity location
                    preys_here = self.get_preys_at(entity.x, entity.y)
                    if preys_here:
                        prey_to_eat = preys_here[0]
                        total_stats = entity.attack + prey_to_eat.defense
                        escape_chance = prey_to_eat.defense / total_stats if total_stats > 0 else 0.5

                        if random.random() < escape_chance:
                            # Prey escapes
                            entity.energy -= 1
                            prey_to_eat.energy -= 1
                        else:
                            # Prey is eaten
                            entity.energy += prey_to_eat.energy
                            prey_to_eat.energy = 0 # Kill prey

            if entity.is_alive and entity.diet == 'herbivore':
                self.scent_trails[(entity.x, entity.y)] = 20


        self.entities = [e for e in self.entities if e.is_alive]
        for child in new_entities:
            self.add_entity(child)
