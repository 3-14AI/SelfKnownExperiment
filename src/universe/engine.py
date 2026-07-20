import random

class Food:
    def __init__(self, x=0, y=0, energy=5, plant_type='generic', toxicity=0, age=0, max_age=100, hatch_entity=None):
        self.hatch_entity = hatch_entity
        self.age = age
        self.max_age = max_age
        self.x = x
        self.y = y
        self.energy = energy
        self.plant_type = plant_type
        self.toxicity = toxicity

class Entity:
    @property
    def max_energy(self):
        return self.size * 50

    def __init__(self, name, x=0, y=0, energy=10, age=0, max_age=50, perception_radius=10, diet='herbivore', preferred_temperature=20, temperature_tolerance=40, is_infected=False, infection_time=0, species=None, symbiotic_with=None, attack=1, defense=1, preferred_terrain=None, size=1, intelligence=1, inventory=None, target_species=None, target_plants=None, generation=0, mutations=0, hydration=50, max_hydration=50, is_sleeping=False, is_aquatic=False, is_flying=False, toxicity=0, poison_resistance=0, poisoned_time=0, camouflage=0.0, vision_type='normal', can_hibernate=False, lays_eggs=False, level=1, experience=0, can_hoard=False):
        self.level = level
        self.experience = experience
        self.lays_eggs = lays_eggs
        self.can_hoard = can_hoard
        self.target_species = target_species
        self.is_sleeping = is_sleeping
        self.is_aquatic = is_aquatic
        self.is_flying = is_flying
        self.toxicity = toxicity
        self.poison_resistance = poison_resistance
        self.poisoned_time = poisoned_time
        self.camouflage = camouflage
        self.vision_type = vision_type
        self.can_hibernate = can_hibernate
        self.is_hibernating = False

        if diet == 'herbivore' and target_plants is None:
            target_plants = ['generic', 'berry', 'leaf', 'flower', 'toxic_plant', 'medicinal']
        elif diet == 'scavenger' and target_plants is None:
            target_plants = ['meat']
        elif diet == 'omnivore' and target_plants is None:
            target_plants = ['generic', 'berry', 'leaf', 'flower', 'meat', 'toxic_plant', 'medicinal']
        self.target_plants = target_plants
        self.generation = generation
        self.mutations = mutations
        if species is None:
            species = name
        if symbiotic_with is None:
            symbiotic_with = []
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.intelligence = intelligence
        self.species = species
        self.symbiotic_with = symbiotic_with
        self.attack = attack
        self.defense = defense
        self.preferred_terrain = preferred_terrain
        self.size = size
        self.name = name
        self.x = x
        self.y = y
        self.energy = min(energy, size * 50)
        self.age = age
        self.max_age = max_age
        self.perception_radius = perception_radius
        self.preferred_temperature = preferred_temperature
        self.temperature_tolerance = temperature_tolerance
        self.alerted_predator_pos = None
        self.is_infected = is_infected
        self.infection_time = infection_time
        self.was_eaten = False
        self.memory = set()
        self.diet = diet
        self.preferred_temperature = preferred_temperature
        self.temperature_tolerance = temperature_tolerance
        self.hydration = hydration
        self.max_hydration = max_hydration

    @property
    def experience_to_next_level(self):
        return self.level * 10

    def add_experience(self, amount):
        self.experience += amount
        while self.experience >= self.experience_to_next_level:
            self.experience -= self.experience_to_next_level
            self.level += 1
            self.attack += 1
            self.defense += 1
            self.energy = self.max_energy

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

        if not self.is_passable(new_x, new_y, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)):
            raise ValueError(f"Movement blocked by terrain at ({new_x}, {new_y})")

        entity.x = new_x
        entity.y = new_y

    def get_terrains_at(self, x, y):
        return [t for t in self.terrains if t.x == x and t.y == y]

    def is_passable(self, x, y, is_aquatic=False, is_flying=False):
        terrains_here = self.get_terrains_at(x, y)
        if not is_flying and any(t.terrain_type == 'wall' for t in terrains_here):
            return False
        is_water = any(t.terrain_type in ['water', 'deep-water'] for t in terrains_here)
        if is_flying:
            return True
        if is_aquatic:
            return is_water
        else:
            return not is_water

    def add_terrain(self, terrain):
        if not (0 <= terrain.x < self.width and 0 <= terrain.y < self.height):
            raise ValueError(f"Terrain out of bounds: ({terrain.x}, {terrain.y})")
        self.terrains.append(terrain)

    def find_path(self, start_x, start_y, target_x, target_y, max_distance=None, memory=None, is_aquatic=False, is_flying=False):
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
                            if self.is_passable(new_x, new_y, is_aquatic, is_flying):
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y, path + [(dx, dy)]))

        return None  # No path found

    def get_entities_at(self, x, y):
        return [e for e in self.entities if e.x == x and e.y == y]

    def get_foods_at(self, x, y, entity=None):
        foods = [f for f in self.foods if f.x == x and f.y == y]
        if entity and entity.target_plants is not None:
            foods = [f for f in foods if f.plant_type in entity.target_plants]
        return foods

    def get_nearest_food(self, x, y, max_distance=None, entity=None):
        if not self.foods:
            return None

        nearest = None
        min_dist = float('inf')
        needs_medicine = entity is not None and (getattr(entity, 'is_infected', False) or getattr(entity, 'poisoned_time', 0) > 0) and (entity.target_plants is None or 'medicinal' in entity.target_plants)
        has_medicinal = any(f.plant_type == 'medicinal' for f in self.foods) if needs_medicine else False

        for food in self.foods:
            if entity and entity.target_plants is not None and food.plant_type not in entity.target_plants:
                continue
            if needs_medicine and has_medicinal and food.plant_type != 'medicinal':
                continue
            dist = abs(food.x - x) + abs(food.y - y)
            if max_distance is not None and dist > max_distance:
                continue
            if dist < min_dist:
                min_dist = dist
                nearest = food
        return nearest

    def get_preys_at(self, x, y, entity=None):
        preys = [e for e in self.entities if e.x == x and e.y == y and e.diet in ['herbivore', 'scavenger', 'omnivore'] and e.is_alive and e != entity]
        if entity and entity.target_species is not None:
            preys = [p for p in preys if p.species in entity.target_species]
        return preys


    def get_nearest_water(self, x, y, max_distance=None, entity=None):
        class Target:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        nearest = None
        min_dist = float('inf')
        for t in self.terrains:
            if t.terrain_type == 'water':
                # Can be adjacent directly
                if abs(t.x - x) + abs(t.y - y) <= 1:
                    return Target(x, y) # already here

                dist = abs(t.x - x) + abs(t.y - y)
                if max_distance is None or dist <= max_distance:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = t.x + dx, t.y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)) if entity else not any(ta.terrain_type in ['wall', 'water', 'deep-water'] for ta in self.get_terrains_at(nx, ny)):
                                dist_to_adj = abs(nx - x) + abs(ny - y)
                                if dist_to_adj < min_dist:
                                    min_dist = dist_to_adj
                                    nearest = Target(nx, ny)
        return nearest
    def get_nearest_prey(self, x, y, max_distance=None, entity=None):
        if not self.entities:
            return None

        best_prey = None
        best_score = float('inf')
        for e in self.entities:
            if e.diet not in ['herbivore', 'scavenger', 'omnivore'] or not e.is_alive:
                continue
            if e == entity:
                continue
            if entity and entity.target_species is not None and e.species not in entity.target_species:
                continue
            dist = abs(e.x - x) + abs(e.y - y)
            if max_distance is not None and dist > (max_distance * (1.0 - getattr(e, 'camouflage', 0.0))):
                continue

            # Prefer smaller and weaker entities.
            # We calculate a score where lower is better.
            # Score incorporates distance, size, and defense.
            score = dist + (e.size * 2) + e.defense
            if score < best_score:
                best_score = score
                best_prey = e
        return best_prey


    def get_nearest_predator(self, x, y, max_distance=None):
        if not self.entities:
            return None

        nearest = None
        min_dist = float('inf')
        for e in self.entities:
            if e.diet == 'carnivore' and e.is_alive:
                dist = abs(e.x - x) + abs(e.y - y)
                if max_distance is not None and dist > (max_distance * (1.0 - getattr(e, 'camouflage', 0.0))):
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

        if self.current_event == 'blizzard':
            self.base_temperature -= 20

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
            if current_season == 'spring' or current_season == 'autumn':
                event_choices = ['storm', 'earthquake', 'volcano']
            elif current_season == 'summer':
                event_choices = ['storm', 'drought', 'earthquake', 'volcano']
            else: # winter
                event_choices = ['blizzard', 'earthquake', 'volcano']
            self.current_event = random.choice(event_choices)
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
            if current_season == 'spring':
                event_type = random.choice(['rain', 'rain', 'fire'])
            elif current_season == 'summer':
                event_type = random.choice(['rain', 'fire', 'fire'])
            elif current_season == 'autumn':
                event_type = random.choice(['rain', 'fire'])
            else: # winter
                event_type = 'snow'

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
                            ptype = random.choice(['generic', 'berry', 'leaf', 'flower'])
                            self.add_food(Food(x=fx, y=fy, plant_type=ptype))

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
            elif event.event_type == 'snow':
                # Convert water to ice and other terrain to snow randomly
                for _ in range(3):
                    rx = event.x + random.randint(-event.radius, event.radius)
                    ry = event.y + random.randint(-event.radius, event.radius)
                    if 0 <= rx < self.width and 0 <= ry < self.height:
                        if (rx - event.x)**2 + (ry - event.y)**2 <= event.radius**2:
                            terrains_here = self.get_terrains_at(rx, ry)
                            if terrains_here:
                                for t in terrains_here:
                                    if t.terrain_type == 'water':
                                        t.terrain_type = 'ice'
                                    elif t.terrain_type not in ['wall', 'ice'] and random.random() < 0.5:
                                        t.terrain_type = 'snow'
                            elif random.random() < 0.3:
                                self.add_terrain(Terrain(x=rx, y=ry, terrain_type='snow'))

        # High temperatures/drought create sand
        if self.current_event == 'drought' or (self.current_season == 'summer' and random.random() < 0.5):
            for _ in range(5):
                hx = random.randint(0, self.width - 1)
                hy = random.randint(0, self.height - 1)
                if self.get_temperature_at(hx, hy) >= 30:
                    if not self.get_terrains_at(hx, hy):
                        self.add_terrain(Terrain(x=hx, y=hy, terrain_type='sand'))


        # Food spoilage and organic spreading logic
        active_foods = []
        for food in self.foods:
            temp = self.get_temperature_at(food.x, food.y)
            if temp > 25:
                food.age += 2
            elif temp <= 0:
                food.age += 0
            else:
                food.age += 1
            if food.age < food.max_age:
                active_foods.append(food)
            elif getattr(food, 'hatch_entity', None) is not None:
                self.entities.append(food.hatch_entity)

            # Organic spreading
            if food.age > 10 and random.random() < 0.005 and getattr(food, 'plant_type', 'generic') != 'meat':
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                if dx != 0 or dy != 0:
                    nx, ny = food.x + dx, food.y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.get_foods_at(nx, ny) and not any(f.x == nx and f.y == ny for f in active_foods) and not any(t.terrain_type in ['water', 'wall', 'ice'] for t in self.get_terrains_at(nx, ny)):
                            active_foods.append(Food(x=nx, y=ny, energy=food.energy, plant_type=food.plant_type, toxicity=food.toxicity))

        self.foods = active_foods


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

        spawn_count = int(current_food_spawn_rate)
        fractional_chance = current_food_spawn_rate - spawn_count
        total_to_spawn = spawn_count + (1 if random.random() < fractional_chance else 0)

        for _ in range(total_to_spawn):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if current_season == 'spring':
                choices = ['generic', 'berry', 'leaf', 'flower', 'flower', 'flower']
            elif current_season == 'summer':
                choices = ['generic', 'berry', 'berry', 'berry', 'leaf', 'flower']
            elif current_season == 'autumn':
                choices = ['generic', 'berry', 'leaf', 'leaf', 'leaf', 'flower']
            else: # winter
                choices = ['generic', 'generic', 'generic', 'generic', 'berry', 'leaf']

            ptype = random.choice(choices)
            toxicity = 0
            rand_val = random.random()
            if rand_val < 0.1:
                ptype = 'toxic_plant'
                toxicity = random.randint(1, 3)
            elif rand_val < 0.15:
                ptype = 'medicinal'
            self.add_food(Food(x=x, y=y, plant_type=ptype, toxicity=toxicity))

        new_entities = []

        for entity in self.entities:
            terrains_here = self.get_terrains_at(entity.x, entity.y)
            in_shelter = any(t.terrain_type == 'shelter' for t in terrains_here)


            if current_season == 'winter' and getattr(entity, 'can_hibernate', False):
                entity.is_hibernating = True
                entity.is_sleeping = True
            else:
                entity.is_hibernating = False
                if self.is_night:
                    if not entity.is_sleeping and random.random() < 0.2:
                        entity.is_sleeping = True
                else:
                    entity.is_sleeping = False



            # Consume energy per tick
            if getattr(entity, 'is_hibernating', False):
                if self.time % 10 == 0:
                    energy_loss = 1
                    entity.hydration -= 1
                else:
                    energy_loss = 0
            else:
                energy_loss = entity.size
                if self.current_event == 'storm':
                    energy_loss = 2 * entity.size if not in_shelter else entity.size
                elif self.current_event == 'blizzard':
                    energy_loss = 3 * entity.size if not in_shelter else entity.size

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

                # Shelter Building Mechanics
                if entity.intelligence >= 5 and entity.energy > 20 and not in_shelter:
                    build_chance = 0.05
                    if self.current_event in ['storm', 'blizzard']:
                        build_chance = 0.15
                    if random.random() < build_chance:
                        self.add_terrain(Terrain(x=entity.x, y=entity.y, terrain_type='shelter'))
                        entity.energy -= 10
                        in_shelter = True

                # Crafting Mechanics
                if entity.intelligence >= 5 and entity.energy > 15:
                    if random.random() < 0.1: # 10% chance per tick to craft something
                        needed_tools = [t for t in ['weapon', 'shield', 'clothing'] if t not in entity.inventory]
                        if needed_tools:
                            crafted_tool = random.choice(needed_tools)
                            entity.inventory.append(crafted_tool)
                            entity.energy -= 5

                # Temperature check
                current_temp = self.get_temperature_at(entity.x, entity.y)
                effective_tolerance = entity.temperature_tolerance
                if 'clothing' in entity.inventory:
                    effective_tolerance += 10
                if in_shelter:
                    effective_tolerance += 15
                if not (entity.preferred_temperature - effective_tolerance <= current_temp <= entity.preferred_temperature + effective_tolerance):
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

                # Terrain check
                if entity.preferred_terrain:
                    terrains_here = self.get_terrains_at(entity.x, entity.y)
                    terrain_types = [t.terrain_type for t in terrains_here]
                    if entity.preferred_terrain in terrain_types:
                        energy_loss = max(0, energy_loss - 1)
                    else:
                        energy_loss += 1

                if getattr(entity, 'poisoned_time', 0) > 0:
                    energy_loss += 1
                    entity.poisoned_time -= 1

                # Hydration mechanics
                entity.hydration -= 1
                if entity.hydration <= 0:
                    energy_loss += 1

                # Check if adjacent to water to drink
                water_adjacent = False
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                    terrains_here = self.get_terrains_at(entity.x + dx, entity.y + dy)
                    if any(t.terrain_type == 'water' for t in terrains_here):
                        water_adjacent = True
                        break
                if water_adjacent:
                    entity.hydration = entity.max_hydration

                # Shelter healing/recovery
                if in_shelter:
                    energy_loss -= 2

                if entity.is_sleeping:
                    energy_loss -= 3

            entity.energy -= energy_loss
            # Age by 1 per tick
            entity.age += 1
            if self.time % self.day_length == 0:
                entity.add_experience(1)

            if entity.is_alive:
                # Reproduction
                reproduction_chance = min(1.0, 0.5 + (entity.intelligence * 0.05))
                if not entity.is_sleeping and entity.energy >= self.reproduction_threshold and (len(self.entities) + len(new_entities) < self.population_limit) and random.random() < reproduction_chance:
                    entity.energy -= self.reproduction_cost

                    # Genetics and Mutations
                    # Base traits inherited from parent
                    child_max_age = entity.max_age
                    child_perception_radius = entity.perception_radius
                    child_preferred_temperature = entity.preferred_temperature
                    child_temperature_tolerance = entity.temperature_tolerance
                    child_attack = entity.attack
                    child_defense = entity.defense
                    child_size = entity.size
                    child_intelligence = entity.intelligence
                    child_max_hydration = entity.max_hydration
                    child_toxicity = entity.toxicity
                    child_poison_resistance = entity.poison_resistance
                    child_camouflage = entity.camouflage
                    child_vision_type = getattr(entity, 'vision_type', 'normal')
                    child_can_hibernate = getattr(entity, 'can_hibernate', False)
                    child_lays_eggs = getattr(entity, 'lays_eggs', False)
                    child_can_hoard = getattr(entity, 'can_hoard', False)
                    child_is_flying = getattr(entity, 'is_flying', False)
                    child_target_species = entity.target_species.copy() if entity.target_species else None
                    child_target_plants = entity.target_plants.copy() if entity.target_plants else None
                    child_generation = entity.generation + 1
                    child_mutations_count = entity.mutations
                    child_species = entity.species

                    # Mutation chance
                    mutation_chance = 0.1
                    mutation_occurred = False
                    if random.random() < mutation_chance:
                        # Mutate max_age by up to +/- 5
                        child_max_age += random.randint(-5, 5)
                        child_max_age = max(10, child_max_age) # Ensure it doesn't go too low
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        # Mutate perception_radius by up to +/- 2
                        child_perception_radius += random.randint(-2, 2)
                        child_perception_radius = max(1, child_perception_radius) # Minimum perception of 1
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_preferred_temperature += random.randint(-5, 5)
                        child_preferred_temperature = max(-20, min(60, child_preferred_temperature))
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_temperature_tolerance += random.randint(-2, 2)
                        child_temperature_tolerance = max(1, child_temperature_tolerance)
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_attack += random.randint(-1, 1)
                        child_attack = max(0, child_attack)
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_defense += random.randint(-1, 1)
                        child_defense = max(0, child_defense)
                        mutation_occurred = True

                    child_diet = entity.diet
                    if random.random() < mutation_chance:
                        child_diet = random.choice(['herbivore', 'carnivore', 'scavenger', 'omnivore'])
                        mutation_occurred = True
                        # Reset target preferences on diet change
                        child_target_plants = None
                        child_target_species = None

                    if random.random() < mutation_chance:
                        child_size += random.randint(-1, 1)
                        child_size = max(1, child_size)
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_toxicity = max(0, child_toxicity + random.choice([-1, 1]))
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_poison_resistance = max(0, child_poison_resistance + random.choice([-1, 1]))
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_can_hibernate = not child_can_hibernate
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_lays_eggs = not child_lays_eggs
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_hoard = not child_can_hoard
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_max_hydration += random.randint(-5, 5)
                        child_max_hydration = max(10, child_max_hydration)
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_intelligence += random.randint(-1, 1)
                        child_intelligence = max(1, child_intelligence)
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_camouflage = min(0.8, max(0.0, child_camouflage + random.uniform(-0.1, 0.1)))
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_vision_type = 'night_vision' if child_vision_type == 'normal' else 'normal'
                        mutation_occurred = True

                    if random.random() < mutation_chance * 0.1:
                        child_is_flying = not child_is_flying
                        mutation_occurred = True

                    if mutation_occurred:
                        child_mutations_count += 1
                        if child_mutations_count >= 5:
                            child_species = child_species + "_evo"
                            child_mutations_count = 0

                        # Predator adaptation
                        if child_diet == 'carnivore' and child_target_species is not None:
                            # 20% chance to adapt diet if mutates
                            if random.random() < 0.20:
                                all_species = list(set([e.species for e in self.entities]))
                                if all_species:
                                    new_target = random.choice(all_species)
                                    if new_target not in child_target_species:
                                        child_target_species.append(new_target)

                    child = Entity(name=f"{entity.name}_child", x=entity.x, y=entity.y,
                                   max_age=child_max_age, perception_radius=child_perception_radius, diet=child_diet,
                                   preferred_temperature=child_preferred_temperature, temperature_tolerance=child_temperature_tolerance,
                                   species=child_species, symbiotic_with=entity.symbiotic_with.copy(),
                                   attack=child_attack, defense=child_defense, preferred_terrain=entity.preferred_terrain, size=child_size,
                                   intelligence=child_intelligence, target_species=child_target_species, target_plants=child_target_plants,
                                   generation=child_generation, mutations=child_mutations_count, max_hydration=child_max_hydration, hydration=child_max_hydration, is_sleeping=False, toxicity=child_toxicity, poison_resistance=child_poison_resistance, camouflage=child_camouflage, vision_type=child_vision_type, is_flying=child_is_flying, can_hibernate=child_can_hibernate, lays_eggs=child_lays_eggs, level=1, experience=0, can_hoard=child_can_hoard)
                    if getattr(entity, 'lays_eggs', False):
                        egg = Food(x=entity.x, y=entity.y, energy=5, plant_type='egg', max_age=20, hatch_entity=child)
                        self.add_food(egg)
                    else:
                        new_entities.append(child)

                effective_perception = entity.perception_radius if (self.is_day or getattr(entity, 'vision_type', 'normal') == 'night_vision') else max(1, entity.perception_radius // 2)

                # Update entity memory with visible obstacles
                for t in self.terrains:
                    if not self.is_passable(t.x, t.y, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)) and (abs(t.x - entity.x) + abs(t.y - entity.y)) <= effective_perception:
                        entity.memory.add((t.x, t.y))

                # Eat from inventory if hungry and has hoarded food
                if getattr(entity, 'can_hoard', False) and entity.energy <= entity.max_energy * 0.5:
                    hoarded_foods = [item for item in entity.inventory if isinstance(item, Food)]
                    if hoarded_foods:
                        food_to_eat = hoarded_foods[0]
                        entity.inventory.remove(food_to_eat)
                        entity.energy = min(entity.max_energy, entity.energy + food_to_eat.energy)
                        if getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                            entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                        if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                            entity.is_infected = False
                            entity.infection_time = 0
                            entity.poisoned_time = 0
                        if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                            entity.is_infected = False
                            entity.infection_time = 0
                            entity.poisoned_time = 0

                can_move = True
                if entity.is_sleeping:
                    can_move = False
                if self.time % entity.size != 0:
                    can_move = False
                if entity.diet in ['herbivore', 'scavenger']:
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
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)):
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
                            moved_for_water = False
                            if entity.hydration <= entity.max_hydration / 2:
                                nearest_water = self.get_nearest_water(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                                if nearest_water:
                                    path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                    if path and len(path) > 0:
                                        dx, dy = path[0]
                                        try:
                                            self.move_entity(entity, dx, dy)
                                            moved_for_water = True
                                        except ValueError:
                                            pass

                            if not moved_for_water:
                                nearest_food = self.get_nearest_food(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                                if nearest_food:
                                    path = self.find_path(entity.x, entity.y, nearest_food.x, nearest_food.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
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
                                            path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                            if path and len(path) > 0:
                                                dx, dy = path[0]
                                                try:
                                                    self.move_entity(entity, dx, dy)
                                                except ValueError:
                                                    pass

                    # Check for food at entity location
                    foods_here = self.get_foods_at(entity.x, entity.y, entity=entity)
                    if foods_here:
                        food_to_eat = foods_here[0]
                        if getattr(entity, 'can_hoard', False) and entity.energy >= entity.max_energy - 20 and len([item for item in entity.inventory if isinstance(item, Food)]) < entity.size * 2:
                            entity.inventory.append(food_to_eat)
                            self.foods.remove(food_to_eat)
                        else:
                            entity.energy = min(entity.max_energy, entity.energy + food_to_eat.energy)
                            if getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            self.foods.remove(food_to_eat)
                elif entity.diet == 'omnivore':
                    if can_move:
                        # Flee behavior
                        nearest_predator = self.get_nearest_predator(entity.x, entity.y, max_distance=effective_perception)
                        if nearest_predator:
                            entity.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)
                            # Alert nearby flockmates
                            flockmates_to_alert = self.get_nearby_flockmates(entity, effective_perception * 2)
                            for f in flockmates_to_alert:
                                f.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)

                        if entity.alerted_predator_pos:
                            px, py = entity.alerted_predator_pos
                            best_pos = None
                            max_dist = -1
                            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                nx, ny = entity.x + dx, entity.y + dy
                                try:
                                    if 0 <= nx < self.width and 0 <= ny < self.height:
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)):
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
                            moved_for_water = False
                            if entity.hydration <= entity.max_hydration / 2:
                                nearest_water = self.get_nearest_water(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                                if nearest_water:
                                    path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                    if path and len(path) > 0:
                                        dx, dy = path[0]
                                        try:
                                            self.move_entity(entity, dx, dy)
                                            moved_for_water = True
                                        except ValueError:
                                            pass

                            if not moved_for_water:
                                nearest_food = self.get_nearest_food(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                                nearest_prey = self.get_nearest_prey(entity.x, entity.y, max_distance=effective_perception, entity=entity)

                                target_to_chase = None
                                dist_food = float('inf')
                                dist_prey = float('inf')

                                if nearest_food:
                                    dist_food = abs(nearest_food.x - entity.x) + abs(nearest_food.y - entity.y)
                                if nearest_prey:
                                    dist_prey = abs(nearest_prey.x - entity.x) + abs(nearest_prey.y - entity.y)

                                if nearest_food and nearest_prey:
                                    if dist_food <= dist_prey:
                                        target_to_chase = nearest_food
                                    else:
                                        target_to_chase = nearest_prey
                                elif nearest_food:
                                    target_to_chase = nearest_food
                                elif nearest_prey:
                                    target_to_chase = nearest_prey

                                if target_to_chase:
                                    path = self.find_path(entity.x, entity.y, target_to_chase.x, target_to_chase.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                    if path and len(path) > 0:
                                        dx, dy = path[0]
                                        try:
                                            self.move_entity(entity, dx, dy)
                                        except ValueError:
                                            pass
                                else:
                                    # Scent tracking behavior
                                    best_scent = 0
                                    best_pos = None
                                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                        nx, ny = entity.x + dx, entity.y + dy
                                        if (nx, ny) in self.scent_trails and self.scent_trails[(nx, ny)] > best_scent:
                                            if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)):
                                                best_scent = self.scent_trails[(nx, ny)]
                                                best_pos = (dx, dy)
                                    if best_pos:
                                        try:
                                            self.move_entity(entity, best_pos[0], best_pos[1])
                                        except ValueError:
                                            pass
                                    else:
                                        # Flocking behavior
                                        flockmates = self.get_nearby_flockmates(entity, effective_perception)
                                        if flockmates:
                                            center_x = sum(e.x for e in flockmates) // len(flockmates)
                                            center_y = sum(e.y for e in flockmates) // len(flockmates)
                                            if center_x != entity.x or center_y != entity.y:
                                                path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                                if path and len(path) > 0:
                                                    dx, dy = path[0]
                                                    try:
                                                        self.move_entity(entity, dx, dy)
                                                    except ValueError:
                                                        pass

                    # Eat food if present, else eat prey
                    foods_here = self.get_foods_at(entity.x, entity.y, entity=entity)
                    if foods_here:
                        food_to_eat = foods_here[0]
                        if getattr(entity, 'can_hoard', False) and entity.energy >= entity.max_energy - 20 and len([item for item in entity.inventory if isinstance(item, Food)]) < entity.size * 2:
                            entity.inventory.append(food_to_eat)
                            self.foods.remove(food_to_eat)
                        else:
                            entity.energy = min(entity.max_energy, entity.energy + food_to_eat.energy)
                            if getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            self.foods.remove(food_to_eat)
                    else:
                        preys_here = self.get_preys_at(entity.x, entity.y, entity=entity)
                        if preys_here:
                            prey_to_eat = preys_here[0]
                            prey_in_shelter = any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y))
                            effective_attack = entity.attack + (2 if 'weapon' in entity.inventory else 0)
                            effective_defense = prey_to_eat.defense + (2 if 'shield' in prey_to_eat.inventory else 0)
                            pack_members = [e for e in self.entities if e.species == entity.species and e != entity and e.is_alive and not e.is_sleeping and abs(e.x - entity.x) + abs(e.y - entity.y) <= 3]
                            herd_members = [e for e in self.entities if e.species == prey_to_eat.species and e != prey_to_eat and e.is_alive and not e.is_sleeping and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 3]
                            pack_bonus = sum(0.5 * e.attack for e in pack_members)
                            herd_bonus = sum(0.5 * e.defense for e in herd_members)
                            effective_attack += pack_bonus
                            effective_defense += herd_bonus
                            if prey_in_shelter:
                                effective_defense += 3
                            total_stats = effective_attack + effective_defense
                            escape_chance = effective_defense / total_stats if total_stats > 0 else 0.5

                            prey_to_eat.is_sleeping = False
                            if random.random() < escape_chance:
                                # Prey escapes
                                entity.energy -= 1
                                prey_to_eat.energy -= 1
                                prey_to_eat.defense += 0.5
                                prey_to_eat.attack += 0.1
                                entity.attack += 0.2
                                prey_to_eat.add_experience(2)
                            else:
                                # Prey is eaten
                                entity.energy = min(entity.max_energy, entity.energy + prey_to_eat.energy)
                                if getattr(prey_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                    entity.poisoned_time += (prey_to_eat.toxicity - entity.poison_resistance) * 5
                                entity.attack += 0.5
                                entity.defense += 0.5
                                entity.add_experience(5)
                                prey_to_eat.energy = 0
                                prey_to_eat.was_eaten = True

                elif entity.diet == 'carnivore':
                    if can_move:
                        moved_for_water = False
                        if entity.hydration <= entity.max_hydration / 2:
                            nearest_water = self.get_nearest_water(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                            if nearest_water:
                                path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                if path and len(path) > 0:
                                    dx, dy = path[0]
                                    try:
                                        self.move_entity(entity, dx, dy)
                                        moved_for_water = True
                                    except ValueError:
                                        pass

                        if not moved_for_water:
                            nearest_prey = self.get_nearest_prey(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                            if nearest_prey:
                                path = self.find_path(entity.x, entity.y, nearest_prey.x, nearest_prey.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
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
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False)):
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
                                            path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False))
                                            if path and len(path) > 0:
                                                dx, dy = path[0]
                                                try:
                                                    self.move_entity(entity, dx, dy)
                                                except ValueError:
                                                    pass


                    # Check for prey at entity location
                    preys_here = self.get_preys_at(entity.x, entity.y, entity=entity)
                    if preys_here:
                        prey_to_eat = preys_here[0]
                        prey_in_shelter = any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y))
                        effective_attack = entity.attack + (2 if 'weapon' in entity.inventory else 0)
                        effective_defense = prey_to_eat.defense + (2 if 'shield' in prey_to_eat.inventory else 0)
                        pack_members = [e for e in self.entities if e.species == entity.species and e != entity and e.is_alive and not e.is_sleeping and abs(e.x - entity.x) + abs(e.y - entity.y) <= 3]
                        herd_members = [e for e in self.entities if e.species == prey_to_eat.species and e != prey_to_eat and e.is_alive and not e.is_sleeping and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 3]
                        pack_bonus = sum(0.5 * e.attack for e in pack_members)
                        herd_bonus = sum(0.5 * e.defense for e in herd_members)
                        effective_attack += pack_bonus
                        effective_defense += herd_bonus
                        if prey_in_shelter:
                            effective_defense += 3
                        total_stats = effective_attack + effective_defense
                        escape_chance = effective_defense / total_stats if total_stats > 0 else 0.5

                        prey_to_eat.is_sleeping = False
                        if random.random() < escape_chance:
                            # Prey escapes
                            entity.energy -= 1
                            prey_to_eat.energy -= 1

                            # Prey gains experience from surviving
                            prey_to_eat.defense += 0.5
                            prey_to_eat.add_experience(2)
                            prey_to_eat.attack += 0.1

                            # Predator learns from failure
                            entity.attack += 0.2
                        else:
                            # Prey is eaten
                            entity.energy = min(entity.max_energy, entity.energy + prey_to_eat.energy)
                            if getattr(prey_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (prey_to_eat.toxicity - entity.poison_resistance) * 5

                            # Gain experience/strength from eating prey
                            entity.attack += 0.5
                            entity.add_experience(5)
                            entity.defense += 0.5

                            prey_to_eat.energy = 0 # Kill prey
                            prey_to_eat.was_eaten = True

            if entity.is_alive and entity.diet in ['herbivore', 'scavenger', 'omnivore']:
                self.scent_trails[(entity.x, entity.y)] = 20



        dead_entities = [e for e in self.entities if not e.is_alive]
        for dead in dead_entities:
            if not getattr(dead, 'was_eaten', False):
                self.add_food(Food(x=dead.x, y=dead.y, energy=dead.size * 5, plant_type='meat', toxicity=getattr(dead, 'toxicity', 0), max_age=60))

        self.entities = [e for e in self.entities if getattr(e, "is_alive", True)]
        for child in new_entities:
            self.add_entity(child)
