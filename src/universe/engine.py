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
        base = self.size * 50
        return int(base * 1.5) if getattr(self, "has_blubber", False) else base

    def __init__(self, name, x=0, y=0, energy=10, age=0, max_age=50, perception_radius=10, diet='herbivore', preferred_temperature=20, temperature_tolerance=40, is_infected=False, infection_time=0, species=None, symbiotic_with=None, attack=1, defense=1, preferred_terrain=None, size=1, intelligence=1, inventory=None, target_species=None, target_plants=None, generation=0, mutations=0, hydration=50, max_hydration=50, is_sleeping=False, is_aquatic=False, is_flying=False, toxicity=0, poison_resistance=0, poisoned_time=0, camouflage=0.0, vision_type='normal', can_hibernate=False, lays_eggs=False, level=1, experience=0, can_hoard=False, max_stamina=50, stamina=50, is_nocturnal=False, can_burrow=False, has_spikes=False, can_spin_webs=False, is_venomous=False, can_photosynthesize=False, is_amphibious=False, has_shell=False, has_echolocation=False, is_aposematic=False, is_fruiting=False, is_immune=False, is_cold_blooded=False, is_electric=False, stunned_time=0, is_regenerative=False, has_claws=False, is_parasitic=False, has_scales=False, has_fur=False, can_climb=False, pack_hunter=False, has_bioluminescence=False, is_volcanic=False, is_forestal=False, is_desertic=False, is_social=False, is_carnivorous_plant=False, disease_vector=False, is_nocturnal_predator=False, is_scentless=False, can_sprint=False, is_vampiric=False, is_detritivore=False, can_sweat=False, has_blubber=False, is_mud_bather=False, is_filter_feeder=False, is_gluttonous=False, is_solitary=False, is_cannibalistic=False, is_ambush_predator=False, is_territorial=False, has_horns=False, is_migratory=False, is_cooperative=False, is_frugivore=False, is_agile=False, has_strong_stomach=False, is_opportunistic=False, has_thick_skin=False, has_sharp_teeth=False, is_hardy=False, is_fast_learner=False, is_playful=False, is_heavy_sleeper=False, is_patient=False, is_endurance_runner=False, is_evasive=False, is_prolific=False, is_adaptable=False, is_resourceful=False, is_vocal=False, is_nest_builder=False, is_nomadic=False, is_photosensitive=False, is_fearless=False, is_scavenger=False, is_scout=False, is_intimidating=False, is_cleaner=False, is_spiteful=False, is_sunbather=False, is_pack_mule=False, is_reckless=False, is_thief=False, is_absorbent=False, is_toxic=False, is_vibrant=False, is_arctic=False, is_fierce=False, is_lucky=False, is_telepathic=False, is_cautious=False, is_restless=False, is_vengeful=False, is_defensive=False, is_sturdy=False, is_slippery=False, can_leap=False, is_heavy=False, is_lightweight=False, is_stealthy=False, is_mimic=False, is_resilient=False, is_smelly=False, is_relentless=False, is_parasite_resistant=False, is_ruthless=False, is_protective=False, is_forager=False, is_tireless=False, is_vigilant=False, is_pacifist=False, is_farsighted=False, is_chameleon=False, is_bloodthirsty=False, is_unappetizing=False, is_introspective=False, is_frenzied=False, is_sun_tracker=False):
        self.has_blubber = has_blubber
        self.is_mud_bather = is_mud_bather
        self.is_filter_feeder = is_filter_feeder
        self.is_gluttonous = is_gluttonous
        self.is_solitary = is_solitary
        self.is_cannibalistic = is_cannibalistic
        self.is_ambush_predator = is_ambush_predator
        self.is_territorial = is_territorial
        self.has_horns = has_horns
        self.can_sprint = can_sprint
        self.is_migratory = is_migratory
        self.is_cooperative = is_cooperative
        self.is_frugivore = is_frugivore
        self.is_agile = is_agile
        self.has_strong_stomach = has_strong_stomach
        self.is_opportunistic = is_opportunistic
        self.has_thick_skin = has_thick_skin
        self.has_sharp_teeth = has_sharp_teeth
        self.is_hardy = is_hardy
        self.is_fast_learner = is_fast_learner
        self.is_playful = is_playful
        self.is_heavy_sleeper = is_heavy_sleeper
        self.is_patient = is_patient
        self.is_bloodthirsty = is_bloodthirsty
        self.is_unappetizing = is_unappetizing
        self.is_introspective = is_introspective
        self.is_frenzied = is_frenzied
        self.is_sun_tracker = is_sun_tracker
        self.is_endurance_runner = is_endurance_runner
        self.is_evasive = is_evasive
        self.is_prolific = is_prolific
        self.is_adaptable = is_adaptable
        self.is_resourceful = is_resourceful
        self.is_vocal = is_vocal
        self.is_nest_builder = is_nest_builder
        self.is_nomadic = is_nomadic
        self.is_photosensitive = is_photosensitive
        self.is_fearless = is_fearless
        self.is_scavenger = is_scavenger
        self.is_scout = is_scout
        self.is_intimidating = is_intimidating
        self.is_cleaner = is_cleaner
        self.is_spiteful = is_spiteful
        self.is_sunbather = is_sunbather
        self.is_vampiric = is_vampiric
        self.is_detritivore = is_detritivore
        self.can_sweat = can_sweat
        self.is_scentless = is_scentless
        self.is_nocturnal_predator = is_nocturnal_predator
        self.disease_vector = disease_vector
        self.is_carnivorous_plant = is_carnivorous_plant
        self.is_slippery = is_slippery
        self.can_leap = can_leap
        self.is_heavy = is_heavy
        self.is_lightweight = is_lightweight
        self.is_stealthy = is_stealthy
        self.is_mimic = is_mimic
        self.is_resilient = is_resilient
        self.is_smelly = is_smelly
        self.is_relentless = is_relentless
        self.is_parasite_resistant = is_parasite_resistant
        self.is_ruthless = is_ruthless
        self.is_protective = is_protective
        self.is_forager = is_forager
        self.is_tireless = is_tireless
        self.is_vigilant = is_vigilant
        self.is_pacifist = is_pacifist
        self.is_farsighted = is_farsighted
        self.is_chameleon = is_chameleon
        self.remained_stationary = True
        self.is_amphibious = is_amphibious
        self.is_volcanic = is_volcanic
        self.is_forestal = is_forestal
        self.is_desertic = is_desertic
        self.is_social = is_social
        self.is_aposematic = is_aposematic
        self.is_fruiting = is_fruiting
        self.is_immune = is_immune
        self.is_cold_blooded = is_cold_blooded
        self.is_electric = is_electric
        self.is_regenerative = is_regenerative
        self.has_claws = has_claws
        self.is_parasitic = is_parasitic
        self.has_scales = has_scales
        self.has_fur = has_fur
        self.can_climb = can_climb
        self.pack_hunter = pack_hunter
        self.has_bioluminescence = has_bioluminescence
        self.shared_target = None
        self.host = None
        self.attached_parasites = []
        self.stunned_time = stunned_time
        self.has_echolocation = has_echolocation
        self.has_shell = has_shell
        self.can_photosynthesize = can_photosynthesize
        self.is_venomous = is_venomous
        self.can_spin_webs = can_spin_webs
        self.max_stamina = max_stamina * 2 if getattr(self, 'is_endurance_runner', False) else max_stamina
        self.stamina = min(self.max_stamina, stamina * 2 if getattr(self, 'is_endurance_runner', False) else stamina)
        self.level = level
        self.experience = experience
        self.lays_eggs = lays_eggs
        self.is_nocturnal = is_nocturnal
        self.can_hoard = can_hoard
        self.is_pack_mule = is_pack_mule
        self.is_reckless = is_reckless
        self.is_thief = is_thief
        self.is_absorbent = is_absorbent
        self.is_toxic = is_toxic
        self.is_vibrant = is_vibrant
        self.is_arctic = is_arctic
        self.is_fierce = is_fierce
        self.is_lucky = is_lucky
        self.is_telepathic = is_telepathic
        self.is_cautious = is_cautious
        self.is_restless = is_restless
        self.is_vengeful = is_vengeful
        self.is_defensive = is_defensive
        self.is_sturdy = is_sturdy
        self.target_species = target_species
        self.target_plants = target_plants
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
        self.can_burrow = can_burrow
        self.has_spikes = has_spikes

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
        self.max_size = size
        self.size = max(1, size // 3) if age == 0 else size
        self.name = name
        self.x = x
        self.y = y
        self.energy = min(energy, self.size * 50)
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
        if getattr(self, 'is_fast_learner', False):
            amount *= 2
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
    def __init__(self, x=0, y=0, terrain_type='wall', elevation=0):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type
        self.elevation = elevation

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


    def get_elevation_at(self, x, y):
        terrains = self.get_terrains_at(x, y)
        if not terrains:
            return 0
        return max(getattr(t, 'elevation', 0) for t in terrains)

    def move_entity(self, entity, dx, dy):
        current_elevation = self.get_elevation_at(entity.x, entity.y)
        new_x = entity.x + dx
        new_y = entity.y + dy
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            raise ValueError(f"Movement out of bounds: ({new_x}, {new_y})")

        leaping = False
        if not self.is_passable(new_x, new_y, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)):
            if getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5:
                # Try leaping over
                leap_x, leap_y = new_x + dx, new_y + dy
                if 0 <= leap_x < self.width and 0 <= leap_y < self.height:
                    if self.is_passable(leap_x, leap_y, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)):
                        new_x, new_y = leap_x, leap_y
                        leaping = True
                    else:
                        raise ValueError(f"Movement blocked by terrain at ({new_x}, {new_y}) and leap target ({leap_x}, {leap_y}) is blocked")
                else:
                    raise ValueError(f"Movement blocked by terrain at ({new_x}, {new_y}) and leap target out of bounds")
            else:
                raise ValueError(f"Movement blocked by terrain at ({new_x}, {new_y})")

        target_elevation = self.get_elevation_at(new_x, new_y)
        elevation_diff = target_elevation - current_elevation

        entity.x = new_x
        entity.y = new_y

        terrains_here = self.get_terrains_at(new_x, new_y)

        if hasattr(entity, 'stamina'):
            stamina_cost = 1
            if getattr(entity, 'can_climb', False) and any(t.terrain_type == 'wall' for t in terrains_here):
                stamina_cost = 2

            if not getattr(entity, 'is_flying', False):
                if elevation_diff > 0:
                    if not getattr(entity, 'is_agile', False):
                        stamina_cost += elevation_diff
                elif elevation_diff < -1:
                    stamina_cost = max(0, stamina_cost - 1)
                    entity.energy = max(0, entity.energy - 1) # Fall damage risk

            if leaping:
                stamina_cost += 4 # Extra 4 cost for leaping (base 1 + 4 = 5)
            if getattr(entity, 'is_heavy', False):
                stamina_cost += 1
            if getattr(entity, 'is_lightweight', False):
                stamina_cost = max(0, stamina_cost - 1)
            if not getattr(entity, 'is_tireless', False):
                entity.stamina = max(0, entity.stamina - stamina_cost)

        if any(t.terrain_type == 'web' for t in terrains_here) and not getattr(entity, 'can_spin_webs', False):
            if hasattr(entity, 'stamina'):
                if getattr(entity, 'is_slippery', False) and random.random() < 0.5:
                    pass  # slipped away
                else:
                    entity.stamina = 0

    def get_terrains_at(self, x, y):
        return [t for t in self.terrains if t.x == x and t.y == y]

    def is_passable(self, x, y, is_aquatic=False, is_flying=False, is_amphibious=False, is_climbing=False):
        terrains_here = self.get_terrains_at(x, y)
        if not is_flying and not is_climbing and any(t.terrain_type == 'wall' for t in terrains_here):
            return False
        is_water = any(t.terrain_type in ['water', 'deep-water'] for t in terrains_here)
        if is_flying:
            return True
        if is_amphibious:
            is_deep_water = any(t.terrain_type == 'deep-water' for t in terrains_here)
            return not is_deep_water
        if is_aquatic:
            return is_water
        else:
            return not is_water

    def add_terrain(self, terrain):
        if terrain.x < 0 or terrain.x >= self.width or terrain.y < 0 or terrain.y >= self.height:
            return
        if not (0 <= terrain.x < self.width and 0 <= terrain.y < self.height):
            raise ValueError(f"Terrain out of bounds: ({terrain.x}, {terrain.y})")
        self.terrains.append(terrain)

    def find_path(self, start_x, start_y, target_x, target_y, max_distance=None, memory=None, is_aquatic=False, is_flying=False, is_amphibious=False, is_climbing=False, can_leap=False):
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
                            if self.is_passable(new_x, new_y, is_aquatic, is_flying, is_amphibious, is_climbing):
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y, path + [(dx, dy)]))
                            elif can_leap:
                                leap_x, leap_y = new_x + dx, new_y + dy
                                if (leap_x, leap_y) not in visited and 0 <= leap_x < self.width and 0 <= leap_y < self.height:
                                    if self.is_passable(leap_x, leap_y, is_aquatic, is_flying, is_amphibious, is_climbing):
                                        visited.add((leap_x, leap_y))
                                        # Only add the leap destination. If the path reaches target, it will return path
                                        # but the movement system currently processes 1 step dx, dy.
                                        # Actually, we need to return dx, dy. If we return (dx*2, dy*2) the move_entity function can handle it since it uses dx, dy directly.
                                        queue.append((leap_x, leap_y, path + [(dx * 2, dy * 2)]))

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
        is_cannibal_hungry = entity and getattr(entity, 'is_cannibalistic', False) and entity.energy < entity.max_energy * 0.3
        preys = [e for e in self.entities if e.x == x and e.y == y and e.is_alive and e != entity and (e.diet in ['herbivore', 'scavenger', 'omnivore'] or (is_cannibal_hungry and e.species == entity.species))]
        if entity and entity.target_species is not None:
            preys = [p for p in preys if p.species in entity.target_species]
        if entity and entity.energy >= entity.max_energy * 0.3:
            preys = [p for p in preys if not getattr(p, 'is_aposematic', False)]
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
                            if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) if entity else not any(ta.terrain_type in ['wall', 'water', 'deep-water'] for ta in self.get_terrains_at(nx, ny)):
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
            if not e.is_alive or e == entity:
                continue
            is_cannibal_target = entity and getattr(entity, 'is_cannibalistic', False) and entity.energy < entity.max_energy * 0.3 and e.species == entity.species
            if e.diet not in ['herbivore', 'scavenger', 'omnivore'] and not is_cannibal_target:
                continue
            if getattr(e, 'can_burrow', False) and e.is_sleeping:
                continue
            if entity and entity.target_species is not None and e.species not in entity.target_species:
                continue
            if getattr(e, 'is_aposematic', False) and entity and entity.energy >= entity.max_energy * 0.3:
                continue
            dist = abs(e.x - x) + abs(e.y - y)
            if max_distance is not None:
                camou = getattr(e, 'camouflage', 0.0)
                if getattr(e, 'is_chameleon', False) and getattr(e, 'remained_stationary', True):
                    camou = min(0.9, camou + 0.5)
                if getattr(e, 'is_vibrant', False):
                    camou = 0.0
                if entity and getattr(entity, 'has_echolocation', False):
                    camou = 0.0
                if getattr(e, 'has_bioluminescence', False):
                    camou = 0.0

                eff_max_distance = max_distance
                if entity and getattr(e, 'has_bioluminescence', False) and not self.is_day and getattr(entity, 'vision_type', 'normal') != 'night_vision' and not getattr(entity, 'has_echolocation', False) and not getattr(entity, 'is_nocturnal', False) and not getattr(entity, 'has_bioluminescence', False):
                    eff_max_distance = entity.perception_radius
                if getattr(e, 'is_stealthy', False):
                    eff_max_distance *= 0.5

                if dist > (eff_max_distance * (1.0 - camou)):
                    continue

            # Prefer smaller and weaker entities.
            # We calculate a score where lower is better.
            # Score incorporates distance, size, and defense.
            score = dist + (e.size * 2) + e.defense
            if score < best_score:
                best_score = score
                best_prey = e
        return best_prey


    def get_nearest_predator(self, x, y, max_distance=None, entity=None):
        if not self.entities:
            return None

        nearest = None
        min_dist = float('inf')
        for e in self.entities:
            if e.diet == 'carnivore' and e.is_alive:
                dist = abs(e.x - x) + abs(e.y - y)
                if max_distance is not None:
                    camou = getattr(e, 'camouflage', 0.0)
                    if getattr(e, 'is_chameleon', False) and getattr(e, 'remained_stationary', True):
                        camou = min(0.9, camou + 0.5)
                    if getattr(e, 'is_vibrant', False):
                        camou = 0.0
                    if entity and getattr(entity, 'has_echolocation', False):
                        camou = 0.0
                    eff_max_distance = max_distance
                    if getattr(e, 'is_stealthy', False):
                        eff_max_distance *= 0.5
                    if getattr(e, 'is_mimic', False):
                        eff_max_distance = min(2, eff_max_distance)
                    if dist > (eff_max_distance * (1.0 - camou)):
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
            if not getattr(target, 'is_immune', False):
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
            elif t.terrain_type == 'web' and random.random() < 0.05:
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
                                if getattr(e, 'is_volcanic', False):
                                    continue
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

        # Dynamic water levels
        if self.current_event == 'drought':
            for _ in range(10):
                hx = random.randint(0, self.width - 1)
                hy = random.randint(0, self.height - 1)
                terrains_here = self.get_terrains_at(hx, hy)
                for t in terrains_here:
                    if t.terrain_type == 'deep-water':
                        t.terrain_type = 'water'
                    elif t.terrain_type == 'water':
                        t.terrain_type = 'mud'
        elif self.current_event == 'storm':
            for _ in range(10):
                hx = random.randint(0, self.width - 1)
                hy = random.randint(0, self.height - 1)
                terrains_here = self.get_terrains_at(hx, hy)
                for t in terrains_here:
                    if t.terrain_type == 'mud':
                        t.terrain_type = 'water'
                    elif t.terrain_type == 'water':
                        t.terrain_type = 'deep-water'

                if any(t.terrain_type in ['water', 'deep-water'] for t in terrains_here):
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = hx + dx, hy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            adj_terrains = self.get_terrains_at(nx, ny)
                            if not adj_terrains:
                                if random.random() < 0.2:
                                    self.add_terrain(Terrain(x=nx, y=ny, terrain_type='mud'))
                            else:
                                for at in adj_terrains:
                                    if at.terrain_type in ['sand', 'ash']:
                                        at.terrain_type = 'mud'

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
            in_shelter = any(t.terrain_type == 'shelter' for t in terrains_here) or (getattr(entity, 'can_burrow', False) and entity.is_sleeping)

            if getattr(entity, 'is_sunbather', False) and self.is_day and self.get_temperature_at(entity.x, entity.y) > (entity.preferred_temperature + entity.temperature_tolerance / 2):
                entity.energy = min(entity.max_energy, entity.energy + 2)
                entity.stamina = min(getattr(entity, 'max_stamina', 50), getattr(entity, 'stamina', 50) + 2)
                entity.hydration = max(0, entity.hydration - 1)

            if getattr(entity, 'is_absorbent', False):
                terrains_here = self.get_terrains_at(entity.x, entity.y)
                if self.current_event == 'storm' or any(t.terrain_type in ['water', 'mud', 'deep-water'] for t in terrains_here):
                    entity.hydration = min(getattr(entity, 'max_hydration', 50), entity.hydration + 2)

            if getattr(entity, 'is_arctic', False):
                if any(t.terrain_type in ['snow', 'ice'] for t in terrains_here):
                    entity.energy = min(getattr(entity, 'max_energy', entity.size * 50), entity.energy + 1)

            if getattr(entity, 'is_cooperative', False) and entity.energy > entity.max_energy * 0.6:
                for e in self.entities:
                    if e != entity and e.is_alive and e.species == entity.species and e.energy < getattr(e, 'max_energy', e.size * 50) * 0.3:
                        dist = abs(e.x - entity.x) + abs(e.y - entity.y)
                        if dist <= 2:
                            transfer = min(5, entity.energy)
                            entity.energy -= transfer
                            e.energy += transfer
                            break

            if getattr(entity, 'is_thief', False) and getattr(entity, 'can_hoard', False) and entity.energy < entity.max_energy * 0.75:
                for e in self.entities:
                    if e != entity and e.is_alive and getattr(e, 'can_hoard', False) and getattr(e, 'inventory', []):
                        dist = abs(e.x - entity.x) + abs(e.y - entity.y)
                        if dist <= 1:
                            for idx, item in enumerate(e.inventory):
                                if isinstance(item, Food):
                                    stolen = e.inventory.pop(idx)
                                    entity.inventory.append(stolen)
                                    break
                            break


            start_pos_x, start_pos_y = entity.x, entity.y

            # Parasite drain logic
            if getattr(entity, 'is_parasitic', False):
                if getattr(entity, 'host', None) is not None:
                    host = entity.host
                    if not host.is_alive:
                        entity.host = None
                    else:
                        entity.x = host.x
                        entity.y = host.y
                        drain_amount = max(1, entity.size)
                        if host.energy > drain_amount:
                            host.energy -= drain_amount
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + drain_amount)
                        if host.hydration > drain_amount:
                            host.hydration -= drain_amount
                            entity.hydration = min(entity.max_hydration, entity.hydration + drain_amount)

            if current_season == 'winter' and getattr(entity, 'can_hibernate', False):
                entity.is_hibernating = True
                entity.is_sleeping = True
            else:
                entity.is_hibernating = False
                if getattr(entity, 'stamina', 50) <= 0:
                    entity.is_sleeping = True
                elif (self.is_night and not getattr(entity, 'is_nocturnal', False)) or (self.is_day and getattr(entity, 'is_nocturnal', False)):
                    if not entity.is_sleeping and random.random() < 0.2:
                        entity.is_sleeping = True
                else:
                    if getattr(entity, 'stamina', 50) >= getattr(entity, 'max_stamina', 50) * 0.5:
                        entity.is_sleeping = False

            if getattr(entity, 'is_restless', False):
                entity.is_sleeping = False



            # is_cleaner mechanic: remove parasites and cure diseases from nearby entities
            if getattr(entity, 'is_cleaner', False) and entity.is_alive:
                for other in self.entities:
                    if other != entity and other.is_alive:
                        dist = abs(other.x - entity.x) + abs(other.y - entity.y)
                        if dist <= 2:
                            cured_something = False
                            # Remove parasites
                            if hasattr(other, 'attached_parasites') and len(other.attached_parasites) > 0:
                                for parasite in list(other.attached_parasites):
                                    parasite.host = None
                                other.attached_parasites = []
                                cured_something = True
                                entity.energy += 5
                            # Cure disease
                            if getattr(other, 'is_infected', False):
                                other.is_infected = False
                                other.infection_time = 0
                                cured_something = True
                                entity.energy += 5

                            if cured_something:
                                cap = int(entity.max_energy * 1.5) if getattr(entity, 'is_gluttonous', False) else entity.max_energy
                                entity.energy = min(cap, entity.energy)

            # Consume energy per tick
            if getattr(entity, 'is_hibernating', False):
                if self.time % 10 == 0:
                    energy_loss = 1
                    entity.hydration -= 1
                else:
                    energy_loss = 0
            else:
                energy_loss = entity.size
                if getattr(entity, 'is_hardy', False) and entity.energy < entity.max_energy * 0.25:
                    if self.time % 2 != 0:
                        energy_loss = 0
                if getattr(entity, 'is_parasitic', False) and getattr(entity, 'host', None) is not None:
                    energy_loss = 0
                if self.current_event == 'storm':
                    energy_loss = 2 * entity.size if not in_shelter else entity.size
                elif self.current_event == 'blizzard':
                    if getattr(entity, 'is_arctic', False):
                        energy_loss = 0
                    else:
                        energy_loss = 3 * entity.size if not in_shelter else entity.size

                if entity.is_infected:
                    energy_loss += 1
                    entity.infection_time += 1

                    # Recovery
                    if entity.infection_time > 10 and random.random() < 0.2:
                        entity.is_infected = False
                        entity.infection_time = 0
                        entity.is_immune = True

                    # Spread
                    if entity.is_infected:
                        for other in self.entities:
                            if other != entity and other.is_alive and not other.is_infected and not getattr(other, 'is_immune', False):
                                dist = abs(other.x - entity.x) + abs(other.y - entity.y)
                                if dist <= 2 and random.random() < 0.1:
                                    other.is_infected = True

                # Shelter Building Mechanics
                if (entity.intelligence >= 5 or getattr(entity, 'is_nest_builder', False)) and entity.energy > 20 and not in_shelter:
                    build_chance = 0.05
                    if self.current_event in ['storm', 'blizzard']:
                        build_chance = 0.15
                    if random.random() < build_chance:
                        self.add_terrain(Terrain(x=entity.x, y=entity.y, terrain_type='shelter'))
                        entity.energy -= 10
                        in_shelter = True

                # Playful Trait Mechanics
                if getattr(entity, 'is_playful', False) and entity.is_alive:
                    has_playmate = False
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        adj_x, adj_y = entity.x + dx, entity.y + dy
                        for other in self.entities:
                            if other != entity and other.is_alive and other.x == adj_x and other.y == adj_y and other.species == entity.species:
                                has_playmate = True
                                break
                        if has_playmate:
                            break
                    if has_playmate:
                        entity.add_experience(1)

                # Web Spinning Mechanics
                if getattr(entity, 'can_spin_webs', False) and entity.energy > 15:
                    if random.random() < 0.1 and not any(t.terrain_type == 'web' for t in self.get_terrains_at(entity.x, entity.y)):
                        self.add_terrain(Terrain(x=entity.x, y=entity.y, terrain_type='web'))
                        entity.energy -= 2

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

                if getattr(entity, 'is_adaptable', False) and entity.hydration > 1 and abs(current_temp - entity.preferred_temperature) > 5:
                    if current_temp > entity.preferred_temperature:
                        entity.preferred_temperature += 1
                    else:
                        entity.preferred_temperature -= 1
                    entity.hydration -= 1

                if getattr(entity, 'is_cold_blooded', False):
                    if current_temp >= 25:
                        energy_loss = max(0, energy_loss - 1)
                    elif current_temp <= 5:
                        energy_loss += 1
                effective_tolerance = entity.temperature_tolerance
                if getattr(entity, 'has_fur', False):
                    effective_tolerance += 15
                    if current_temp >= 25:
                        energy_loss += 1
                if 'clothing' in entity.inventory:
                    effective_tolerance += 10
                if in_shelter:
                    effective_tolerance += 15
                if not (entity.preferred_temperature - effective_tolerance <= current_temp <= entity.preferred_temperature + effective_tolerance):
                    if current_temp < entity.preferred_temperature - effective_tolerance and getattr(entity, 'has_blubber', False):
                        pass # Blubber prevents cold penalty
                    elif current_temp > entity.preferred_temperature + effective_tolerance and getattr(entity, 'has_blubber', False):
                        energy_loss += 3 # Severe penalty in heat
                    elif current_temp > entity.preferred_temperature + effective_tolerance and getattr(entity, 'can_sweat', False) and entity.hydration > 5:
                        pass # Sweat prevents heat penalty, but drains hydration (already done in hydration block)
                    else:
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
                    if getattr(entity, 'is_resilient', False):
                        entity.poisoned_time = max(0, entity.poisoned_time - 1)

                # Hydration mechanics
                hydration_loss = 1
                if getattr(entity, 'has_scales', False) and self.time % 2 == 1:
                    hydration_loss = 0
                if getattr(entity, 'is_desertic', False) and current_temp > getattr(entity, 'preferred_temperature', 20) + getattr(entity, 'temperature_tolerance', 40) and self.time % 2 == 1:
                    hydration_loss = 0
                if getattr(entity, 'can_sweat', False) and entity.hydration > 5 and current_temp > getattr(entity, 'preferred_temperature', 20) + getattr(entity, 'temperature_tolerance', 40):
                    hydration_loss += 1
                if current_temp > getattr(entity, 'preferred_temperature', 20) + getattr(entity, 'temperature_tolerance', 40) and getattr(entity, 'is_photosensitive', False) and self.is_day:
                    hydration_loss += 1
                entity.hydration -= hydration_loss
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
                    energy_loss -= 6 if getattr(entity, 'is_heavy_sleeper', False) else 3

                if getattr(entity, 'is_social', False) and any(e for e in self.entities if e != entity and e.species == entity.species and e.is_alive and abs(e.x - entity.x) + abs(e.y - entity.y) <= 2):
                    energy_loss -= 1

                if getattr(entity, 'is_solitary', False):
                    if any(e for e in self.entities if e != entity and e.species == entity.species and e.is_alive and abs(e.x - entity.x) + abs(e.y - entity.y) <= 3):
                        energy_loss += 1
                    else:
                        energy_loss -= 1

                if getattr(entity, 'can_photosynthesize', False) and self.is_day:
                    energy_loss -= 2

                if getattr(entity, 'is_regenerative', False) and entity.energy < entity.max_energy and entity.hydration > 5:
                    energy_loss -= 2
                    entity.hydration -= 2

                if getattr(entity, 'is_volcanic', False) and any(t.terrain_type == 'ash' for t in self.get_terrains_at(entity.x, entity.y)):
                    energy_loss -= 3


                if getattr(entity, 'is_desertic', False) and any(t.terrain_type == 'sand' for t in self.get_terrains_at(entity.x, entity.y)):
                    energy_loss -= 1

                if getattr(entity, 'is_sun_tracker', False) and self.is_day and not any(t.terrain_type in ['shelter', 'ash'] for t in self.get_terrains_at(entity.x, entity.y)):
                    energy_loss -= 2

                if getattr(entity, 'is_filter_feeder', False) and getattr(entity, 'is_aquatic', False):
                    if any(t.terrain_type in ['water', 'deep-water'] for t in self.get_terrains_at(entity.x, entity.y)):
                        energy_loss -= 2

            if getattr(entity, "is_gluttonous", False):
                energy_loss += 1
            entity.energy = max(0, entity.energy - energy_loss)
            cap = int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy
            entity.energy = min(cap, entity.energy)
            # Age by 1 per tick
            entity.age += 1
            if entity.age % 10 == 0 and entity.size < getattr(entity, 'max_size', entity.size):
                entity.size += 1
            if self.time % self.day_length == 0:
                entity.add_experience(1)

            if entity.is_alive:
                # Reproduction
                reproduction_chance = min(1.0, 0.5 + (entity.intelligence * 0.05))
                eff_threshold = self.reproduction_threshold // 2 if getattr(entity, 'is_prolific', False) else self.reproduction_threshold
                eff_cost = self.reproduction_cost // 2 if getattr(entity, 'is_prolific', False) else self.reproduction_cost
                if getattr(entity, 'is_prolific', False):
                    reproduction_chance = min(1.0, reproduction_chance + 0.25)
                if getattr(entity, 'is_vibrant', False):
                    reproduction_chance = min(1.0, reproduction_chance + 0.25)

                if not entity.is_sleeping and entity.energy >= eff_threshold and (len(self.entities) + len(new_entities) < self.population_limit) and random.random() < reproduction_chance:
                    entity.energy -= eff_cost

                    # Genetics and Mutations
                    # Base traits inherited from parent
                    child_max_age = entity.max_age
                    child_perception_radius = entity.perception_radius
                    child_preferred_temperature = entity.preferred_temperature
                    child_temperature_tolerance = entity.temperature_tolerance
                    child_attack = entity.attack
                    child_defense = entity.defense
                    child_size = getattr(entity, 'max_size', entity.size)
                    child_intelligence = entity.intelligence
                    child_max_hydration = entity.max_hydration
                    child_toxicity = entity.toxicity
                    child_poison_resistance = entity.poison_resistance
                    child_camouflage = entity.camouflage
                    child_vision_type = getattr(entity, 'vision_type', 'normal')
                    child_can_hibernate = getattr(entity, 'can_hibernate', False)
                    child_lays_eggs = getattr(entity, 'lays_eggs', False)
                    child_can_hoard = getattr(entity, 'can_hoard', False)
                    child_is_nocturnal = getattr(entity, 'is_nocturnal', False)
                    child_can_burrow = getattr(entity, 'can_burrow', False)
                    child_has_spikes = getattr(entity, 'has_spikes', False)
                    child_can_spin_webs = getattr(entity, 'can_spin_webs', False)
                    child_is_venomous = getattr(entity, 'is_venomous', False)
                    child_is_amphibious = getattr(entity, 'is_amphibious', False)
                    child_has_shell = getattr(entity, 'has_shell', False)
                    child_is_aposematic = getattr(entity, 'is_aposematic', False)
                    child_is_fruiting = getattr(entity, 'is_fruiting', False)
                    child_is_immune = getattr(entity, 'is_immune', False)
                    child_is_cold_blooded = getattr(entity, 'is_cold_blooded', False)
                    child_is_electric = getattr(entity, "is_electric", False)
                    child_is_regenerative = getattr(entity, 'is_regenerative', False)
                    child_has_claws = getattr(entity, 'has_claws', False)
                    child_has_echolocation = getattr(entity, 'has_echolocation', False)
                    child_can_photosynthesize = getattr(entity, 'can_photosynthesize', False)
                    child_is_flying = getattr(entity, 'is_flying', False)
                    child_max_stamina = getattr(entity, 'max_stamina', 50)
                    if getattr(entity, 'is_endurance_runner', False):
                        child_max_stamina = child_max_stamina // 2
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
                        child_is_nocturnal = not child_is_nocturnal
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_burrow = not child_can_burrow
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_spikes = not child_has_spikes
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_spin_webs = not child_can_spin_webs
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_venomous = not child_is_venomous
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_photosynthesize = not child_can_photosynthesize
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_regenerative = not child_is_regenerative
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_max_stamina += random.randint(-5, 5)
                        child_max_stamina = max(10, child_max_stamina)
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

                    if random.random() < mutation_chance * 0.1:
                        child_is_amphibious = not child_is_amphibious
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_has_shell = not child_has_shell
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_has_echolocation = not child_has_echolocation
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_aposematic = not child_is_aposematic
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_fruiting = not child_is_fruiting
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_immune = True
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_cold_blooded = not child_is_cold_blooded
                        mutation_occurred = True
                    if random.random() < 0.05:
                        child_is_electric = not child_is_electric
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_claws = not child_has_claws

                    child_is_parasitic = getattr(entity, 'is_parasitic', False)
                    if random.random() < mutation_chance:
                        child_is_parasitic = not child_is_parasitic
                        mutation_occurred = True

                    child_has_scales = getattr(entity, 'has_scales', False)
                    if random.random() < mutation_chance:
                        child_has_scales = not child_has_scales
                        mutation_occurred = True

                    child_has_fur = getattr(entity, 'has_fur', False)
                    child_can_climb = getattr(entity, 'can_climb', False)
                    if random.random() < mutation_chance:
                        child_has_fur = not child_has_fur
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_can_climb = not child_can_climb
                        mutation_occurred = True

                    child_pack_hunter = getattr(entity, 'pack_hunter', False)
                    child_is_pack_mule = getattr(entity, 'is_pack_mule', False)
                    child_is_reckless = getattr(entity, 'is_reckless', False)
                    child_is_thief = getattr(entity, 'is_thief', False)
                    child_is_absorbent = getattr(entity, 'is_absorbent', False)
                    child_is_toxic = getattr(entity, 'is_toxic', False)
                    child_is_vibrant = getattr(entity, 'is_vibrant', False)
                    child_is_arctic = getattr(entity, 'is_arctic', False)
                    child_is_fierce = getattr(entity, 'is_fierce', False)
                    child_is_lucky = getattr(entity, 'is_lucky', False)
                    child_is_telepathic = getattr(entity, 'is_telepathic', False)
                    child_is_cautious = getattr(entity, 'is_cautious', False)
                    child_is_restless = getattr(entity, 'is_restless', False)
                    child_is_vengeful = getattr(entity, 'is_vengeful', False)
                    child_is_defensive = getattr(entity, 'is_defensive', False)
                    child_is_sturdy = getattr(entity, 'is_sturdy', False)
                    child_is_vocal = getattr(entity, 'is_vocal', False)
                    child_is_cleaner = getattr(entity, 'is_cleaner', False)
                    child_is_spiteful = getattr(entity, 'is_spiteful', False)
                    child_is_scout = getattr(entity, 'is_scout', False)
                    child_is_intimidating = getattr(entity, 'is_intimidating', False)
                    if random.random() < mutation_chance:
                        child_is_toxic = not child_is_toxic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_vibrant = not child_is_vibrant
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_arctic = not child_is_arctic
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_fierce = not child_is_fierce
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_lucky = not child_is_lucky
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_telepathic = not child_is_telepathic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_cautious = not child_is_cautious
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_restless = not child_is_restless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_vengeful = not child_is_vengeful
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_defensive = not child_is_defensive
                    if random.random() < mutation_chance:
                        child_is_sturdy = not child_is_sturdy
                        mutation_occurred = True
                    child_is_volcanic = getattr(entity, 'is_volcanic', False)
                    child_is_forestal = getattr(entity, 'is_forestal', False)
                    child_is_desertic = getattr(entity, 'is_desertic', False)
                    child_is_social = getattr(entity, 'is_social', False)
                    child_is_scout = getattr(entity, 'is_scout', False)
                    child_is_intimidating = getattr(entity, 'is_intimidating', False)
                    child_is_cleaner = getattr(entity, 'is_cleaner', False)
                    child_is_spiteful = getattr(entity, 'is_spiteful', False)
                    child_is_carnivorous_plant = getattr(entity, 'is_carnivorous_plant', False)
                    child_is_slippery = getattr(entity, 'is_slippery', False)
                    child_can_leap = getattr(entity, 'can_leap', False)
                    child_is_heavy = getattr(entity, 'is_heavy', False)
                    child_is_lightweight = getattr(entity, 'is_lightweight', False)
                    child_is_stealthy = getattr(entity, 'is_stealthy', False)
                    child_is_mimic = getattr(entity, 'is_mimic', False)
                    child_is_resilient = getattr(entity, 'is_resilient', False)
                    child_is_smelly = getattr(entity, 'is_smelly', False)
                    child_is_relentless = getattr(entity, 'is_relentless', False)
                    child_is_parasite_resistant = getattr(entity, 'is_parasite_resistant', False)
                    child_is_nocturnal_predator = getattr(entity, 'is_nocturnal_predator', False)
                    child_is_scentless = getattr(entity, 'is_scentless', False)
                    child_disease_vector = getattr(entity, 'disease_vector', False)
                    child_can_sprint = getattr(entity, 'can_sprint', False)
                    child_is_detritivore = getattr(entity, 'is_detritivore', False)
                    child_can_sweat = getattr(entity, 'can_sweat', False)
                    child_has_blubber = getattr(entity, 'has_blubber', False)
                    child_is_mud_bather = getattr(entity, 'is_mud_bather', False)
                    child_is_filter_feeder = getattr(entity, 'is_filter_feeder', False)
                    child_is_gluttonous = getattr(entity, 'is_gluttonous', False)
                    child_is_solitary = getattr(entity, 'is_solitary', False)
                    child_is_cannibalistic = getattr(entity, 'is_cannibalistic', False)
                    child_is_ambush_predator = getattr(entity, 'is_ambush_predator', False)
                    child_is_territorial = getattr(entity, 'is_territorial', False)
                    child_is_migratory = getattr(entity, 'is_migratory', False)
                    child_is_cooperative = getattr(entity, 'is_cooperative', False)
                    child_is_frugivore = getattr(entity, 'is_frugivore', False)
                    child_is_agile = getattr(entity, 'is_agile', False)
                    child_has_strong_stomach = getattr(entity, 'has_strong_stomach', False)
                    child_is_opportunistic = getattr(entity, 'is_opportunistic', False)
                    child_has_thick_skin = getattr(entity, 'has_thick_skin', False)
                    child_has_sharp_teeth = getattr(entity, 'has_sharp_teeth', False)
                    child_is_hardy = getattr(entity, 'is_hardy', False)
                    child_is_fast_learner = getattr(entity, 'is_fast_learner', False)
                    child_is_playful = getattr(entity, 'is_playful', False)
                    child_is_heavy_sleeper = getattr(entity, 'is_heavy_sleeper', False)
                    child_is_patient = getattr(entity, 'is_patient', False)
                    child_is_bloodthirsty = getattr(entity, 'is_bloodthirsty', False)
                    child_is_endurance_runner = getattr(entity, 'is_endurance_runner', False)
                    child_is_evasive = getattr(entity, 'is_evasive', False)
                    child_is_prolific = getattr(entity, 'is_prolific', False)
                    child_is_adaptable = getattr(entity, 'is_adaptable', False)
                    child_is_resourceful = getattr(entity, 'is_resourceful', False)
                    child_is_vocal = getattr(entity, 'is_vocal', False)
                    child_is_nest_builder = getattr(entity, 'is_nest_builder', False)
                    child_is_nomadic = getattr(entity, 'is_nomadic', False)
                    child_is_photosensitive = getattr(entity, 'is_photosensitive', False)
                    child_is_fearless = getattr(entity, 'is_fearless', False)
                    child_is_unappetizing = getattr(entity, 'is_unappetizing', False)
                    child_is_introspective = getattr(entity, 'is_introspective', False)
                    child_is_frenzied = getattr(entity, 'is_frenzied', False)
                    child_is_sun_tracker = getattr(entity, 'is_sun_tracker', False)
                    child_is_scavenger = getattr(entity, 'is_scavenger', False)
                    child_is_vampiric = getattr(entity, 'is_vampiric', False)
                    child_has_horns = getattr(entity, 'has_horns', False)
                    if random.random() < mutation_chance:
                        child_is_volcanic = not child_is_volcanic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_forestal = not child_is_forestal
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_desertic = not child_is_desertic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_social = not child_is_social
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_carnivorous_plant = not child_is_carnivorous_plant
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_slippery = not child_is_slippery
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_introspective = not child_is_introspective
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_frenzied = not child_is_frenzied
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_sun_tracker = not child_is_sun_tracker
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_leap = not child_can_leap
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_heavy = not child_is_heavy
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_lightweight = not child_is_lightweight
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_stealthy = not child_is_stealthy
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_mimic = not child_is_mimic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_resilient = not child_is_resilient
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_smelly = not child_is_smelly
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_relentless = not child_is_relentless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_parasite_resistant = not child_is_parasite_resistant
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_scentless = not child_is_scentless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_disease_vector = not child_disease_vector
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_nocturnal_predator = not child_is_nocturnal_predator
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_sprint = not child_can_sprint
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_detritivore = not child_is_detritivore
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_can_sweat = not child_can_sweat
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_blubber = not child_has_blubber
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_mud_bather = not child_is_mud_bather
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_filter_feeder = not child_is_filter_feeder
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_gluttonous = not child_is_gluttonous
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_solitary = not child_is_solitary
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_cannibalistic = not child_is_cannibalistic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_ambush_predator = not child_is_ambush_predator
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_territorial = not child_is_territorial
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_migratory = not child_is_migratory
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_cooperative = not child_is_cooperative
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_frugivore = not child_is_frugivore
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_agile = not child_is_agile
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_strong_stomach = not child_has_strong_stomach
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_opportunistic = not child_is_opportunistic
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_has_thick_skin = not child_has_thick_skin
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_sharp_teeth = not child_has_sharp_teeth
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_hardy = not child_is_hardy
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_fast_learner = not child_is_fast_learner
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_playful = not child_is_playful
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_heavy_sleeper = not child_is_heavy_sleeper
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_patient = not child_is_patient
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_bloodthirsty = not child_is_bloodthirsty
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_endurance_runner = not child_is_endurance_runner
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_evasive = not child_is_evasive
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_vampiric = not child_is_vampiric
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_has_horns = not child_has_horns
                        mutation_occurred = True

                    child_has_bioluminescence = getattr(entity, 'has_bioluminescence', False)
                    if random.random() < mutation_chance:
                        child_pack_hunter = not child_pack_hunter
                    if random.random() < mutation_chance:
                        child_has_bioluminescence = not child_has_bioluminescence
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_evasive = not child_is_evasive
                        mutation_occurred = True
                    child_is_prolific = getattr(entity, 'is_prolific', False)
                    if random.random() < mutation_chance:
                        child_is_prolific = not child_is_prolific
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_adaptable = not child_is_adaptable
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_resourceful = not child_is_resourceful
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_vocal = not child_is_vocal
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_nest_builder = not child_is_nest_builder
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_nomadic = not child_is_nomadic
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_photosensitive = not child_is_photosensitive
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_fearless = not child_is_fearless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_unappetizing = not child_is_unappetizing
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_scavenger = not child_is_scavenger
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_scout = not child_is_scout
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_intimidating = not child_is_intimidating
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_cleaner = not child_is_cleaner
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_spiteful = not child_is_spiteful
                        mutation_occurred = True

                    child_is_sunbather = getattr(entity, 'is_sunbather', False)
                    if random.random() < mutation_chance:
                        child_is_sunbather = not child_is_sunbather
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_pack_mule = not child_is_pack_mule
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_reckless = not child_is_reckless
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_thief = not child_is_thief
                        mutation_occurred = True

                    if random.random() < mutation_chance:
                        child_is_absorbent = not child_is_absorbent
                        mutation_occurred = True

                    child_is_ruthless = getattr(entity, 'is_ruthless', False)
                    child_is_protective = getattr(entity, 'is_protective', False)
                    child_is_forager = getattr(entity, 'is_forager', False)
                    child_is_tireless = getattr(entity, 'is_tireless', False)
                    child_is_vigilant = getattr(entity, 'is_vigilant', False)
                    child_is_pacifist = getattr(entity, 'is_pacifist', False)
                    child_is_farsighted = getattr(entity, 'is_farsighted', False)
                    child_is_chameleon = getattr(entity, 'is_chameleon', False)
                    if random.random() < mutation_chance:
                        child_is_ruthless = not child_is_ruthless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_protective = not child_is_protective
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_forager = not child_is_forager
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_tireless = not child_is_tireless
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_vigilant = not child_is_vigilant
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_pacifist = not child_is_pacifist
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_farsighted = not child_is_farsighted
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_chameleon = not child_is_chameleon
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

                    child_x = max(0, min(self.width - 1, entity.x))
                    child_y = max(0, min(self.height - 1, entity.y))
                    child = Entity(name=f"{entity.name}_child", x=child_x, y=child_y,
                                   max_age=child_max_age, perception_radius=child_perception_radius, diet=child_diet,
                                   preferred_temperature=child_preferred_temperature, temperature_tolerance=child_temperature_tolerance,
                                   species=child_species, symbiotic_with=entity.symbiotic_with.copy(),
                                   attack=child_attack, defense=child_defense, preferred_terrain=entity.preferred_terrain, size=child_size, is_pack_mule=child_is_pack_mule,
                                   intelligence=child_intelligence, target_species=child_target_species, target_plants=child_target_plants,
                                   generation=child_generation, mutations=child_mutations_count, max_hydration=child_max_hydration, hydration=child_max_hydration, is_sleeping=False, toxicity=child_toxicity, poison_resistance=child_poison_resistance, camouflage=child_camouflage, vision_type=child_vision_type, is_flying=child_is_flying, can_hibernate=child_can_hibernate, lays_eggs=child_lays_eggs, level=1, experience=0, can_hoard=child_can_hoard, max_stamina=child_max_stamina, stamina=child_max_stamina, is_nocturnal=child_is_nocturnal, can_burrow=child_can_burrow, has_spikes=child_has_spikes, can_spin_webs=child_can_spin_webs, is_venomous=child_is_venomous, can_photosynthesize=child_can_photosynthesize, is_amphibious=child_is_amphibious, has_shell=child_has_shell, has_echolocation=child_has_echolocation, is_aposematic=child_is_aposematic, is_fruiting=child_is_fruiting, is_immune=child_is_immune, is_cold_blooded=child_is_cold_blooded, is_electric=child_is_electric, is_regenerative=child_is_regenerative, has_claws=child_has_claws, is_parasitic=child_is_parasitic, has_scales=child_has_scales, has_fur=child_has_fur, can_climb=child_can_climb, pack_hunter=child_pack_hunter, has_bioluminescence=child_has_bioluminescence, is_volcanic=child_is_volcanic, is_forestal=child_is_forestal, is_desertic=child_is_desertic, is_social=child_is_social, is_carnivorous_plant=child_is_carnivorous_plant, disease_vector=child_disease_vector, is_nocturnal_predator=child_is_nocturnal_predator, is_scentless=child_is_scentless, can_sprint=child_can_sprint, is_vampiric=child_is_vampiric, is_detritivore=child_is_detritivore, can_sweat=child_can_sweat, has_blubber=child_has_blubber, is_mud_bather=child_is_mud_bather, is_filter_feeder=child_is_filter_feeder, is_gluttonous=child_is_gluttonous, is_solitary=child_is_solitary, is_cannibalistic=child_is_cannibalistic, is_ambush_predator=child_is_ambush_predator, is_territorial=child_is_territorial, has_horns=child_has_horns, is_migratory=child_is_migratory, is_cooperative=child_is_cooperative, is_frugivore=child_is_frugivore, is_agile=child_is_agile, has_strong_stomach=child_has_strong_stomach, is_opportunistic=child_is_opportunistic, has_thick_skin=child_has_thick_skin, has_sharp_teeth=child_has_sharp_teeth, is_hardy=child_is_hardy, is_fast_learner=child_is_fast_learner, is_playful=child_is_playful, is_heavy_sleeper=child_is_heavy_sleeper, is_patient=child_is_patient, is_endurance_runner=child_is_endurance_runner, is_evasive=child_is_evasive, is_prolific=child_is_prolific, is_adaptable=child_is_adaptable, is_resourceful=child_is_resourceful, is_vocal=child_is_vocal, is_nest_builder=child_is_nest_builder, is_nomadic=child_is_nomadic, is_photosensitive=child_is_photosensitive, is_fearless=child_is_fearless, is_scavenger=child_is_scavenger, is_scout=child_is_scout, is_intimidating=child_is_intimidating, is_cleaner=child_is_cleaner, is_spiteful=child_is_spiteful, is_sunbather=child_is_sunbather, is_reckless=child_is_reckless, is_thief=child_is_thief, is_absorbent=child_is_absorbent, is_toxic=child_is_toxic, is_vibrant=child_is_vibrant, is_arctic=child_is_arctic, is_fierce=child_is_fierce, is_lucky=child_is_lucky, is_telepathic=child_is_telepathic, is_cautious=child_is_cautious, is_restless=child_is_restless, is_vengeful=child_is_vengeful, is_defensive=child_is_defensive, is_sturdy=child_is_sturdy, is_slippery=child_is_slippery, can_leap=child_can_leap, is_heavy=child_is_heavy, is_lightweight=child_is_lightweight, is_stealthy=child_is_stealthy, is_mimic=child_is_mimic, is_resilient=child_is_resilient, is_smelly=child_is_smelly, is_relentless=child_is_relentless, is_parasite_resistant=child_is_parasite_resistant, is_ruthless=child_is_ruthless, is_protective=child_is_protective, is_forager=child_is_forager, is_tireless=child_is_tireless, is_vigilant=child_is_vigilant, is_pacifist=child_is_pacifist, is_farsighted=child_is_farsighted, is_chameleon=child_is_chameleon, is_bloodthirsty=child_is_bloodthirsty, is_unappetizing=child_is_unappetizing, is_introspective=child_is_introspective, is_frenzied=child_is_frenzied, is_sun_tracker=child_is_sun_tracker)
                    if getattr(entity, 'lays_eggs', False):
                        egg = Food(x=child_x, y=child_y, energy=5, plant_type='egg', max_age=20, hatch_entity=child)
                        self.add_food(egg)
                    else:
                        new_entities.append(child)

                effective_perception = 0 if (getattr(entity, 'is_heavy_sleeper', False) and getattr(entity, 'is_sleeping', False)) else (entity.perception_radius if (self.is_day != getattr(entity, 'is_nocturnal', False) or getattr(entity, 'vision_type', 'normal') == 'night_vision' or getattr(entity, 'has_echolocation', False) or getattr(entity, 'has_bioluminescence', False)) else max(1, entity.perception_radius // 2))
                if getattr(entity, 'is_farsighted', False) and effective_perception > 0:
                    effective_perception *= 2

                # Update entity memory with visible obstacles
                for t in self.terrains:
                    if not self.is_passable(t.x, t.y, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) and (abs(t.x - entity.x) + abs(t.y - entity.y)) <= effective_perception:
                        entity.memory.add((t.x, t.y))

                if getattr(entity, 'is_scout', False) and entity.memory:
                    flockmates = self.get_nearby_flockmates(entity, effective_perception * 2)
                    for flockmate in flockmates:
                        flockmate.memory.update(entity.memory)

                # Fruiting behavior: Drop food to bait prey or feed symbionts
                if getattr(entity, 'is_fruiting', False) and entity.energy > entity.max_energy * 0.6 and entity.is_alive:
                    if random.random() < 0.05:  # 5% chance per tick when well-fed
                        fruit = Food(x=entity.x, y=entity.y, energy=15, plant_type='fruit', max_age=30)
                        self.foods.append(fruit)
                        entity.energy = max(0, entity.energy - 10)

                # Eat from inventory if hungry and has hoarded food
                if getattr(entity, 'can_hoard', False) and entity.energy <= entity.max_energy * 0.5:
                    hoarded_foods = [item for item in entity.inventory if isinstance(item, Food)]
                    if hoarded_foods:
                        food_to_eat = hoarded_foods[0]
                        entity.inventory.remove(food_to_eat)
                        meat_multiplier = 2 if getattr(entity, "has_strong_stomach", False) and getattr(food_to_eat, "plant_type", "") == "meat" else 1
                        energy_gain = food_to_eat.energy * meat_multiplier * (2 if getattr(entity, "is_frugivore", False) and getattr(food_to_eat, "plant_type", "") == "fruit" else 1)
                        if getattr(entity, "is_forager", False) and getattr(food_to_eat, "plant_type", "") not in ["meat", "egg"]:
                            energy_gain += 5
                        if getattr(entity, 'is_scavenger', False) and getattr(food_to_eat, 'plant_type', '') == 'meat':
                            energy_gain += 5
                        entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + energy_gain)
                        if getattr(entity, 'is_resourceful', False):
                            entity.hydration = min(entity.max_hydration, entity.hydration + 10)
                        if not getattr(entity, 'has_strong_stomach', False) and getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                            entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                        if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                            entity.is_infected = False
                            entity.infection_time = 0
                            entity.poisoned_time = 0
                        if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                            entity.is_infected = False
                            entity.infection_time = 0
                            entity.poisoned_time = 0
                        if getattr(food_to_eat, 'plant_type', '') == 'meat' and getattr(entity, 'disease_vector', False) and not getattr(entity, 'is_immune', False):
                            if random.random() < 0.5:
                                entity.is_infected = True

                can_move = True

                # Detritivore eating terrain (ash/mud)
                if getattr(entity, 'is_detritivore', False):
                    terrains_here = self.get_terrains_at(entity.x, entity.y)
                    consumable_terrains = [t for t in terrains_here if t.terrain_type in ['ash', 'mud']]
                    if consumable_terrains:
                        t = consumable_terrains[0]
                        self.terrains.remove(t)
                        entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + 10)

                # Mud bather recovering hydration and stamina
                if getattr(entity, 'is_mud_bather', False):
                    terrains_here = self.get_terrains_at(entity.x, entity.y)
                    if any(t.terrain_type == 'mud' for t in terrains_here):
                        entity.hydration = min(entity.max_hydration, entity.hydration + 2)
                        entity.stamina = min(getattr(entity, 'max_stamina', 50), getattr(entity, 'stamina', 50) + 2)

                if getattr(entity, 'is_carnivorous_plant', False):
                    entities_here = self.get_entities_at(entity.x, entity.y)
                    for prey in entities_here:
                        if prey != entity and prey.is_alive and prey.size < entity.size:
                            if getattr(prey, 'is_slippery', False) and random.random() < 0.5:
                                continue
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + prey.energy)
                            entity.size += 1
                            entity.max_size = max(getattr(entity, 'max_size', entity.size), entity.size)
                            prey.energy = 0
                            prey.was_eaten = True
                            break

                if getattr(entity, "stunned_time", 0) > 0 and not getattr(entity, 'is_sturdy', False):
                    entity.stunned_time -= 1
                    if getattr(entity, 'is_resilient', False):
                        entity.stunned_time = max(0, entity.stunned_time - 1)
                    can_move = False
                if entity.is_sleeping:
                    can_move = False
                if self.time % entity.size != 0:
                    can_move = False
                if getattr(entity, 'is_cold_blooded', False) and current_temp <= 5:
                    if self.time % (entity.size * 2) != 0:
                        can_move = False
                if getattr(entity, 'is_heavy', False):
                    if self.time % (entity.size * 2) != 0:
                        can_move = False

                # sprinting lets entity move more frequently (e.g. bypass the size check partially)
                # but it requires a stamina cost if moving faster than size allows
                sprinting_now = False
                if can_move == False and getattr(entity, 'can_sprint', False) and entity.stamina >= 10 and (getattr(entity, "stunned_time", 0) <= 0 or getattr(entity, 'is_sturdy', False)) and not entity.is_sleeping:
                    can_move = True
                    sprinting_now = True
                if getattr(entity, 'has_fur', False) and current_temp >= 25:
                    if self.time % (entity.size * 2) != 0:
                        can_move = False

                # Parasite seeking logic (before standard movement)
                if sprinting_now:
                    entity.stamina = max(0, entity.stamina - 5)

                if getattr(entity, 'is_parasitic', False) and can_move:
                    if getattr(entity, 'host', None) is not None:
                        can_move = False # attached parasites just ride along
                    else:
                        # find host
                        best_host = None
                        best_dist = float('inf')
                        for other in self.entities:
                            if other != entity and other.is_alive and not getattr(other, 'is_parasitic', False) and not getattr(other, 'is_parasite_resistant', False):
                                dist = abs(other.x - entity.x) + abs(other.y - entity.y)
                                actual_perception = entity.perception_radius if (self.is_day != getattr(entity, 'is_nocturnal', False) or getattr(entity, 'vision_type', 'normal') == 'night_vision' or getattr(entity, 'has_echolocation', False) or getattr(entity, 'has_bioluminescence', False)) else max(1, entity.perception_radius // 2)
                                if dist <= actual_perception and dist < best_dist and other.size > entity.size:
                                    best_dist = dist
                                    best_host = other
                        if best_host:
                            if best_dist <= 1:
                                entity.host = best_host
                                if not hasattr(best_host, 'attached_parasites'):
                                    best_host.attached_parasites = []
                                best_host.attached_parasites.append(entity)
                                entity.x = best_host.x
                                entity.y = best_host.y
                                can_move = False
                            else:
                                path = self.find_path(entity.x, entity.y, best_host.x, best_host.y, max_distance=actual_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                if path:
                                    next_step = path[0]
                                    if self.is_passable(next_step[0], next_step[1], getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)):
                                        entity.x, entity.y = next_step
                                        entity.stamina = max(0, getattr(entity, 'stamina', 50) - 1)
                                can_move = False # we handled movement
                effective_diet = entity.diet
                if getattr(entity, 'is_opportunistic', False) and entity.energy < entity.max_energy * 0.25:
                    effective_diet = 'omnivore'

                if effective_diet in ['herbivore', 'scavenger']:
                    if can_move:
                        # Communication & Flee behavior
                        flee_dist = effective_perception * 2 if getattr(entity, 'is_cautious', False) else effective_perception
                        nearest_predator = self.get_nearest_predator(entity.x, entity.y, max_distance=flee_dist, entity=entity)
                        if nearest_predator and not getattr(entity, 'is_fearless', False):
                            entity.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)
                            # Alert nearby flockmates
                            if getattr(entity, 'is_telepathic', False):
                                flockmates_to_alert = [e for e in self.entities if getattr(e, 'species', None) == getattr(entity, 'species', None) and e != entity and e.is_alive]
                            else:
                                flockmates_to_alert = self.get_nearby_flockmates(entity, effective_perception * 4 if getattr(entity, 'is_vocal', False) else effective_perception * 2)
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
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + dx * 2, entity.y + dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
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
                                    path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                                    path = self.find_path(entity.x, entity.y, nearest_food.x, nearest_food.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                                            path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                            if path and len(path) > 0:
                                                dx, dy = path[0]
                                                try:
                                                    self.move_entity(entity, dx, dy)
                                                except ValueError:
                                                    pass
                                    elif getattr(entity, 'is_migratory', False):
                                        # Migration behavior
                                        target_y = self.height - 1 if self.current_season in ['autumn', 'winter'] else 0
                                        if entity.y != target_y:
                                            path = self.find_path(entity.x, entity.y, entity.x, target_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                        if getattr(entity, 'can_hoard', False) and entity.energy >= entity.max_energy - 20 and len([item for item in entity.inventory if isinstance(item, Food)]) < (entity.size * 4 if getattr(entity, 'is_pack_mule', False) else entity.size * 2):
                            entity.inventory.append(food_to_eat)
                            self.foods.remove(food_to_eat)
                        else:
                            meat_multiplier = 2 if getattr(entity, "has_strong_stomach", False) and getattr(food_to_eat, "plant_type", "") == "meat" else 1
                            energy_gain = food_to_eat.energy * meat_multiplier * (2 if getattr(entity, "is_frugivore", False) and getattr(food_to_eat, "plant_type", "") == "fruit" else 1)
                            if getattr(entity, "is_forager", False) and getattr(food_to_eat, "plant_type", "") not in ["meat", "egg"]:
                                energy_gain += 5
                            if getattr(entity, 'is_scavenger', False) and getattr(food_to_eat, 'plant_type', '') == 'meat':
                                energy_gain += 5
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + energy_gain)
                            if getattr(entity, 'is_resourceful', False):
                                entity.hydration = min(entity.max_hydration, entity.hydration + 10)
                            if not getattr(entity, 'has_strong_stomach', False) and getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            if getattr(food_to_eat, 'plant_type', '') == 'meat' and getattr(entity, 'disease_vector', False) and not getattr(entity, 'is_immune', False):
                                if random.random() < 0.5:
                                    entity.is_infected = True
                            self.foods.remove(food_to_eat)
                elif effective_diet == 'omnivore':
                    if can_move:
                        # Flee behavior
                        flee_dist = effective_perception * 2 if getattr(entity, 'is_cautious', False) else effective_perception
                        nearest_predator = self.get_nearest_predator(entity.x, entity.y, max_distance=flee_dist, entity=entity)
                        if nearest_predator and not getattr(entity, 'is_fearless', False):
                            entity.alerted_predator_pos = (nearest_predator.x, nearest_predator.y)
                            # Alert nearby flockmates
                            if getattr(entity, 'is_telepathic', False):
                                flockmates_to_alert = [e for e in self.entities if getattr(e, 'species', None) == getattr(entity, 'species', None) and e != entity and e.is_alive]
                            else:
                                flockmates_to_alert = self.get_nearby_flockmates(entity, effective_perception * 4 if getattr(entity, 'is_vocal', False) else effective_perception * 2)
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
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + dx * 2, entity.y + dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
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
                                    path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                    if path and len(path) > 0:
                                        dx, dy = path[0]
                                        try:
                                            self.move_entity(entity, dx, dy)
                                            moved_for_water = True
                                        except ValueError:
                                            pass

                            if not moved_for_water:
                                nearest_food = self.get_nearest_food(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                                nearest_prey = None if getattr(entity, 'is_pacifist', False) else self.get_nearest_prey(entity.x, entity.y, max_distance=effective_perception, entity=entity)

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

                                # Pack hunter targeting override
                                if getattr(entity, 'pack_hunter', False) and effective_diet in ['carnivore', 'omnivore']:
                                    if target_to_chase and hasattr(target_to_chase, 'species'):
                                        entity.shared_target = target_to_chase
                                        # Share with nearby pack members
                                        for e in self.entities:
                                            if e != entity and getattr(e, 'pack_hunter', False) and e.species == entity.species and e.is_alive and not e.is_sleeping:
                                                if abs(e.x - entity.x) + abs(e.y - entity.y) <= effective_perception * 2:
                                                    e.shared_target = target_to_chase
                                    elif getattr(entity, 'shared_target', None) and getattr(entity.shared_target, 'is_alive', False):
                                        target_to_chase = entity.shared_target

                                if target_to_chase:
                                    target_x, target_y = target_to_chase.x, target_to_chase.y
                                    if getattr(entity, 'pack_hunter', False) and hasattr(target_to_chase, 'species'):
                                        pack_mates = [e for e in self.entities if e != entity and getattr(e, 'pack_hunter', False) and e.species == entity.species and getattr(e, 'shared_target', None) == target_to_chase]
                                        if pack_mates:
                                            best_flank = None
                                            best_flank_dist = float('inf')
                                            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                                fx, fy = target_to_chase.x + dx, target_to_chase.y + dy
                                                if self.is_passable(fx, fy, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)):
                                                    if not any(e.x == fx and e.y == fy for e in pack_mates):
                                                        dist = abs(entity.x - fx) + abs(entity.y - fy)
                                                        if dist < best_flank_dist:
                                                            best_flank_dist = dist
                                                            best_flank = (fx, fy)
                                            if best_flank:
                                                target_x, target_y = best_flank

                                    path = self.find_path(entity.x, entity.y, target_x, target_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                                            if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + dx * 2, entity.y + dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
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
                                                path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                                if path and len(path) > 0:
                                                    dx, dy = path[0]
                                                    try:
                                                        self.move_entity(entity, dx, dy)
                                                    except ValueError:
                                                        pass
                                        elif getattr(entity, 'is_migratory', False):
                                            # Migration behavior
                                            target_y = self.height - 1 if self.current_season in ['autumn', 'winter'] else 0
                                            if entity.y != target_y:
                                                path = self.find_path(entity.x, entity.y, entity.x, target_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                        if getattr(entity, 'can_hoard', False) and entity.energy >= entity.max_energy - 20 and len([item for item in entity.inventory if isinstance(item, Food)]) < (entity.size * 4 if getattr(entity, 'is_pack_mule', False) else entity.size * 2):
                            entity.inventory.append(food_to_eat)
                            self.foods.remove(food_to_eat)
                        else:
                            meat_multiplier = 2 if getattr(entity, "has_strong_stomach", False) and getattr(food_to_eat, "plant_type", "") == "meat" else 1
                            energy_gain = food_to_eat.energy * meat_multiplier * (2 if getattr(entity, "is_frugivore", False) and getattr(food_to_eat, "plant_type", "") == "fruit" else 1)
                            if getattr(entity, "is_forager", False) and getattr(food_to_eat, "plant_type", "") not in ["meat", "egg"]:
                                energy_gain += 5
                            if getattr(entity, 'is_scavenger', False) and getattr(food_to_eat, 'plant_type', '') == 'meat':
                                energy_gain += 5
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + energy_gain)
                            if getattr(entity, 'is_resourceful', False):
                                entity.hydration = min(entity.max_hydration, entity.hydration + 10)
                            if not getattr(entity, 'has_strong_stomach', False) and getattr(food_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (food_to_eat.toxicity - entity.poison_resistance) * 5
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            if getattr(food_to_eat, 'plant_type', '') == 'medicinal':
                                entity.is_infected = False
                                entity.infection_time = 0
                                entity.poisoned_time = 0
                            if getattr(food_to_eat, 'plant_type', '') == 'meat' and getattr(entity, 'disease_vector', False) and not getattr(entity, 'is_immune', False):
                                if random.random() < 0.5:
                                    entity.is_infected = True
                            self.foods.remove(food_to_eat)
                    else:
                        preys_here = [] if getattr(entity, 'is_pacifist', False) else self.get_preys_at(entity.x, entity.y, entity=entity)
                        if preys_here:
                            prey_to_eat = preys_here[0]
                            prey_in_shelter = any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y))
                            effective_attack = entity.attack + (2 if 'weapon' in entity.inventory else 0)
                            if getattr(entity, 'is_farsighted', False):
                                effective_attack = max(0, effective_attack - 2)
                            if getattr(entity, 'is_territorial', False):
                                effective_attack += 2

                            if getattr(entity, 'has_claws', False):
                                effective_attack += 5
                            if getattr(entity, 'is_fierce', False):
                                effective_attack += 3
                            if getattr(entity, 'is_frenzied', False):
                                effective_attack += 5
                                entity.energy = max(0, entity.energy - 5)
                            if getattr(entity, 'has_horns', False):
                                effective_attack += 2
                            if getattr(entity, 'is_nocturnal_predator', False) and self.is_night:
                                effective_attack *= 1.5
                            if getattr(entity, 'is_ambush_predator', False) and getattr(entity, 'camouflage', 0.0) > 0.0 and not getattr(entity, 'is_vibrant', False) and not getattr(prey_to_eat, 'is_vigilant', False):
                                effective_attack *= 2.0
                                entity.stamina = max(0, entity.stamina - 10)
                            if getattr(entity, 'stamina', 50) <= 10:
                                effective_attack *= 0.5
                            effective_defense = prey_to_eat.defense + (2 if 'shield' in prey_to_eat.inventory else 0)
                            if getattr(prey_to_eat, 'is_defensive', False):
                                effective_defense += 3
                            if getattr(prey_to_eat, 'is_territorial', False):
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_forestal', False) and any(t.terrain_type == 'forest' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                                effective_defense += 3
                            if getattr(prey_to_eat, 'has_shell', False):
                                effective_defense += 5
                            if getattr(prey_to_eat, 'has_horns', False):
                                effective_defense += 1
                            if getattr(prey_to_eat, 'has_scales', False):
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_heavy', False):
                                effective_defense += 2
                            if getattr(entity, 'has_sharp_teeth', False):
                                if getattr(prey_to_eat, 'has_shell', False):
                                    effective_defense = max(0, effective_defense - 5)
                                if getattr(prey_to_eat, 'has_scales', False):
                                    effective_defense = max(0, effective_defense - 2)
                            if getattr(prey_to_eat, 'is_lightweight', False):
                                effective_defense = max(0, effective_defense - 2)
                            if getattr(prey_to_eat, 'has_thick_skin', False) and getattr(entity, 'has_claws', False):
                                effective_defense += 3
                            if getattr(prey_to_eat, 'stamina', 50) <= 10:
                                effective_defense *= 0.5
                            pack_members = [e for e in self.entities if e.species == entity.species and e != entity and e.is_alive and not e.is_sleeping and abs(e.x - entity.x) + abs(e.y - entity.y) <= 3]
                            herd_members = [e for e in self.entities if e.species == prey_to_eat.species and e != prey_to_eat and e.is_alive and not e.is_sleeping and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 3]
                            pack_bonus = sum(0.5 * e.attack for e in pack_members)

                            # Pack hunter bonus based on number of nearby pack members attacking same target
                            if getattr(entity, 'pack_hunter', False):
                                adjacent_pack_hunters = [e for e in pack_members if getattr(e, 'pack_hunter', False) and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 2]
                                pack_bonus += len(adjacent_pack_hunters) * 2

                            herd_bonus = sum(0.5 * e.defense for e in herd_members)
                            effective_attack += pack_bonus
                            effective_defense += herd_bonus


                            adjacent_protectors = [e for e in herd_members if getattr(e, 'is_protective', False) and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 2]


                            effective_defense += len(adjacent_protectors) * 2
                            if prey_in_shelter:
                                effective_defense += 3
                            if getattr(prey_to_eat, 'is_intimidating', False):
                                effective_attack = max(0, effective_attack - 2)
                            if getattr(prey_to_eat, 'is_smelly', False):
                                effective_attack = max(0, effective_attack - 2)
                            if getattr(entity, 'is_intimidating', False):
                                effective_defense = max(0, effective_defense - 2)

                            if getattr(entity, 'is_reckless', False):
                                effective_attack *= 2
                                effective_defense = 0

                            if getattr(entity, 'is_ruthless', False) and prey_to_eat.energy < (prey_to_eat.max_energy / 2):
                                effective_attack += 3

                            total_stats = effective_attack + effective_defense
                            escape_chance = effective_defense / total_stats if total_stats > 0 else 0.5
                            if getattr(prey_to_eat, 'is_evasive', False):
                                escape_chance = min(1.0, escape_chance + 0.2)
                            if getattr(prey_to_eat, 'is_lucky', False):
                                escape_chance = min(1.0, escape_chance + 0.1)

                            prey_to_eat.is_sleeping = False
                            if getattr(prey_to_eat, 'is_electric', False) and not getattr(entity, 'is_sturdy', False):
                                entity.stunned_time = 5
                            if getattr(prey_to_eat, 'has_spikes', False) and not getattr(entity, 'has_thick_skin', False):
                                entity.energy = max(0, entity.energy - 5)
                                entity.stamina = max(0, getattr(entity, 'stamina', 50) - 10)
                            if getattr(entity, 'is_venomous', False) and random.random() < 0.5:
                                prey_to_eat.poisoned_time += max(0, 10 - prey_to_eat.poison_resistance * 2)
                            if getattr(prey_to_eat, 'is_venomous', False) and random.random() < 0.5:
                                entity.poisoned_time += max(0, 10 - entity.poison_resistance * 2)
                            if getattr(entity, 'is_vampiric', False):
                                prey_to_eat.energy = max(0, prey_to_eat.energy - 5)
                                prey_to_eat.hydration = max(0, prey_to_eat.hydration - 5)
                                entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + 5)
                                entity.hydration = min(entity.max_hydration, entity.hydration + 5)
                            if random.random() < escape_chance:
                                # Prey escapes
                                entity.energy = max(0, entity.energy - 1)
                                prey_to_eat.energy = max(0, prey_to_eat.energy - 1)
                                if getattr(entity, 'is_relentless', False):
                                    prey_to_eat.energy = max(0, prey_to_eat.energy - int(effective_attack / 2))
                                prey_to_eat.defense += 0.5
                                prey_to_eat.attack += 0.1
                                entity.attack += 0.2
                                prey_to_eat.add_experience(2)
                                entity.stamina = max(0, getattr(entity, 'stamina', 50) - 5)
                                prey_to_eat.stamina = max(0, getattr(prey_to_eat, 'stamina', 50) - 5)
                            else:
                                # Prey is eaten
                                if getattr(prey_to_eat, 'is_spiteful', False):
                                    entity.energy = max(0, entity.energy - prey_to_eat.defense)
                                energy_gained = prey_to_eat.energy // 2 if getattr(prey_to_eat, "is_unappetizing", False) else prey_to_eat.energy
                                entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + energy_gained)
                                if getattr(entity, 'is_resourceful', False):
                                    entity.hydration = min(entity.max_hydration, entity.hydration + 10)
                                if getattr(prey_to_eat, 'is_toxic', False):
                                    entity.poisoned_time += 10
                                if not getattr(entity, 'has_strong_stomach', False) and getattr(prey_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                    entity.poisoned_time += (prey_to_eat.toxicity - entity.poison_resistance) * 5
                                entity.attack += 0.5
                                entity.defense += 0.5
                                entity.add_experience(5)
                                entity.stamina = max(0, getattr(entity, 'stamina', 50) - 2)
                                if getattr(entity, 'is_bloodthirsty', False):
                                    entity.stamina = min(getattr(entity, 'max_stamina', 50), getattr(entity, 'stamina', 50) + 20)
                                prey_to_eat.energy = 0
                                prey_to_eat.was_eaten = True

                elif effective_diet == 'carnivore' and not getattr(entity, 'is_parasitic', False):
                    if can_move:
                        moved_for_water = False
                        if entity.hydration <= entity.max_hydration / 2:
                            nearest_water = self.get_nearest_water(entity.x, entity.y, max_distance=effective_perception, entity=entity)
                            if nearest_water:
                                path = self.find_path(entity.x, entity.y, nearest_water.x, nearest_water.y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                if path and len(path) > 0:
                                    dx, dy = path[0]
                                    try:
                                        self.move_entity(entity, dx, dy)
                                        moved_for_water = True
                                    except ValueError:
                                        pass

                        if not moved_for_water:
                            nearest_prey = None if getattr(entity, 'is_pacifist', False) else self.get_nearest_prey(entity.x, entity.y, max_distance=effective_perception, entity=entity)

                            # Pack hunter targeting override for pure carnivores
                            if getattr(entity, 'pack_hunter', False) and effective_diet == 'carnivore':
                                if nearest_prey and hasattr(nearest_prey, 'species'):
                                    entity.shared_target = nearest_prey
                                    for e in self.entities:
                                        if e != entity and getattr(e, 'pack_hunter', False) and e.species == entity.species and e.is_alive and not e.is_sleeping:
                                            if abs(e.x - entity.x) + abs(e.y - entity.y) <= effective_perception * 2:
                                                e.shared_target = nearest_prey
                                elif getattr(entity, 'shared_target', None) and getattr(entity.shared_target, 'is_alive', False):
                                    nearest_prey = entity.shared_target

                            if nearest_prey:
                                target_x, target_y = nearest_prey.x, nearest_prey.y
                                if getattr(entity, 'pack_hunter', False) and hasattr(nearest_prey, 'species'):
                                    pack_mates = [e for e in self.entities if e != entity and getattr(e, 'pack_hunter', False) and e.species == entity.species and getattr(e, 'shared_target', None) == nearest_prey]
                                    if pack_mates:
                                        best_flank = None
                                        best_flank_dist = float('inf')
                                        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                            fx, fy = nearest_prey.x + dx, nearest_prey.y + dy
                                            if self.is_passable(fx, fy, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)):
                                                if not any(e.x == fx and e.y == fy for e in pack_mates):
                                                    dist = abs(entity.x - fx) + abs(entity.y - fy)
                                                    if dist < best_flank_dist:
                                                        best_flank_dist = dist
                                                        best_flank = (fx, fy)
                                        if best_flank:
                                            target_x, target_y = best_flank

                                path = self.find_path(entity.x, entity.y, target_x, target_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
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
                                        if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + dx * 2, entity.y + dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
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
                                            path = self.find_path(entity.x, entity.y, center_x, center_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                            if path and len(path) > 0:
                                                dx, dy = path[0]
                                                try:
                                                    self.move_entity(entity, dx, dy)
                                                except ValueError:
                                                    pass
                                    elif getattr(entity, 'is_migratory', False):
                                        # Migration behavior
                                        target_y = self.height - 1 if self.current_season in ['autumn', 'winter'] else 0
                                        if entity.y != target_y:
                                            path = self.find_path(entity.x, entity.y, entity.x, target_y, max_distance=effective_perception, memory=entity.memory, is_aquatic=getattr(entity, 'is_aquatic', False), is_flying=getattr(entity, 'is_flying', False), is_amphibious=getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))
                                            if path and len(path) > 0:
                                                dx, dy = path[0]
                                                try:
                                                    self.move_entity(entity, dx, dy)
                                                except ValueError:
                                                    pass


                    # Check for prey at entity location
                    preys_here = [] if getattr(entity, 'is_pacifist', False) else self.get_preys_at(entity.x, entity.y, entity=entity)
                    if preys_here:
                        prey_to_eat = preys_here[0]
                        prey_in_shelter = any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y))
                        effective_attack = entity.attack + (2 if 'weapon' in entity.inventory else 0)
                        if getattr(entity, 'is_farsighted', False):
                            effective_attack = max(0, effective_attack - 2)
                        if getattr(entity, 'is_territorial', False):
                            effective_attack += 2
                        if getattr(entity, 'has_claws', False):
                            effective_attack += 5
                        if getattr(entity, 'is_fierce', False):
                            effective_attack += 3
                        if getattr(entity, 'is_frenzied', False):
                            effective_attack += 5
                            entity.energy = max(0, entity.energy - 5)
                        if getattr(entity, 'has_horns', False):
                            effective_attack += 2
                        if getattr(entity, 'is_nocturnal_predator', False) and self.is_night:
                            effective_attack *= 1.5
                        if getattr(entity, 'is_ambush_predator', False) and getattr(entity, 'camouflage', 0.0) > 0.0 and not getattr(entity, 'is_vibrant', False) and not getattr(prey_to_eat, 'is_vigilant', False):
                            effective_attack *= 2.0
                            entity.stamina = max(0, entity.stamina - 10)
                        if getattr(entity, 'stamina', 50) <= 10:
                            effective_attack *= 0.5
                        effective_defense = prey_to_eat.defense + (2 if 'shield' in prey_to_eat.inventory else 0)
                        if getattr(prey_to_eat, 'is_defensive', False):
                            effective_defense += 3
                        if getattr(prey_to_eat, 'is_territorial', False):
                            effective_defense += 2
                        if getattr(prey_to_eat, 'has_shell', False):
                            effective_defense += 5
                        if getattr(prey_to_eat, 'has_horns', False):
                            effective_defense += 1
                        if getattr(prey_to_eat, 'has_scales', False):
                            effective_defense += 2
                        if getattr(prey_to_eat, 'is_heavy', False):
                            effective_defense += 2
                        if getattr(entity, 'has_sharp_teeth', False):
                            if getattr(prey_to_eat, 'has_shell', False):
                                effective_defense = max(0, effective_defense - 5)
                            if getattr(prey_to_eat, 'has_scales', False):
                                effective_defense = max(0, effective_defense - 2)
                        if getattr(prey_to_eat, 'is_lightweight', False):
                            effective_defense = max(0, effective_defense - 2)
                        if getattr(prey_to_eat, 'stamina', 50) <= 10:
                            effective_defense *= 0.5
                        pack_members = [e for e in self.entities if e.species == entity.species and e != entity and e.is_alive and not e.is_sleeping and abs(e.x - entity.x) + abs(e.y - entity.y) <= 3]
                        herd_members = [e for e in self.entities if e.species == prey_to_eat.species and e != prey_to_eat and e.is_alive and not e.is_sleeping and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 3]
                        pack_bonus = sum(0.5 * e.attack for e in pack_members)

                        if getattr(entity, 'pack_hunter', False):
                            adjacent_pack_hunters = [e for e in pack_members if getattr(e, 'pack_hunter', False) and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 2]
                            pack_bonus += len(adjacent_pack_hunters) * 2

                        herd_bonus = sum(0.5 * e.defense for e in herd_members)
                        effective_attack += pack_bonus
                        effective_defense += herd_bonus


                        adjacent_protectors = [e for e in herd_members if getattr(e, 'is_protective', False) and abs(e.x - prey_to_eat.x) + abs(e.y - prey_to_eat.y) <= 2]


                        effective_defense += len(adjacent_protectors) * 2
                        if prey_in_shelter:
                            effective_defense += 3
                        if getattr(prey_to_eat, 'is_intimidating', False):
                            effective_attack = max(0, effective_attack - 2)
                        if getattr(prey_to_eat, 'is_smelly', False):
                            effective_attack = max(0, effective_attack - 2)
                        if getattr(entity, 'is_intimidating', False):
                            effective_defense = max(0, effective_defense - 2)

                        if getattr(entity, 'is_reckless', False):
                            effective_attack *= 2
                            effective_defense = 0

                        if getattr(entity, 'is_ruthless', False) and prey_to_eat.energy < (prey_to_eat.max_energy / 2):
                            effective_attack += 3

                        total_stats = effective_attack + effective_defense
                        escape_chance = effective_defense / total_stats if total_stats > 0 else 0.5
                        if getattr(prey_to_eat, 'is_evasive', False):
                            escape_chance = min(1.0, escape_chance + 0.2)
                        if getattr(prey_to_eat, 'is_lucky', False):
                            escape_chance = min(1.0, escape_chance + 0.1)

                        prey_to_eat.is_sleeping = False
                        if getattr(prey_to_eat, 'is_electric', False) and not getattr(entity, 'is_sturdy', False):
                            entity.stunned_time = 5
                        if getattr(prey_to_eat, 'has_spikes', False) and not getattr(entity, 'has_thick_skin', False):
                            entity.energy = max(0, entity.energy - 5)
                            entity.stamina = max(0, getattr(entity, 'stamina', 50) - 10)
                        if getattr(entity, 'is_venomous', False) and random.random() < 0.5:
                            prey_to_eat.poisoned_time += max(0, 10 - prey_to_eat.poison_resistance * 2)
                        if getattr(prey_to_eat, 'is_venomous', False) and random.random() < 0.5:
                            entity.poisoned_time += max(0, 10 - entity.poison_resistance * 2)
                        if getattr(entity, 'is_vampiric', False):
                            prey_to_eat.energy = max(0, prey_to_eat.energy - 5)
                            prey_to_eat.hydration = max(0, prey_to_eat.hydration - 5)
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + 5)
                            entity.hydration = min(entity.max_hydration, entity.hydration + 5)
                        if random.random() < escape_chance:
                            # Prey escapes
                            entity.energy = max(0, entity.energy - 1)
                            prey_to_eat.energy = max(0, prey_to_eat.energy - 1)
                            if getattr(entity, 'is_relentless', False):
                                prey_to_eat.energy = max(0, prey_to_eat.energy - int(effective_attack / 2))

                            # Prey gains experience from surviving
                            prey_to_eat.defense += 0.5
                            if getattr(prey_to_eat, 'is_vengeful', False):
                                prey_to_eat.attack += 1
                            prey_to_eat.add_experience(2)
                            prey_to_eat.attack += 0.1

                            # Predator learns from failure
                            entity.attack += 0.2
                            entity.stamina = max(0, getattr(entity, 'stamina', 50) - 5)
                            prey_to_eat.stamina = max(0, getattr(prey_to_eat, 'stamina', 50) - 5)
                        else:
                            # Prey is eaten
                            if getattr(prey_to_eat, 'is_spiteful', False):
                                entity.energy = max(0, entity.energy - prey_to_eat.defense)
                            energy_gained = prey_to_eat.energy // 2 if getattr(prey_to_eat, "is_unappetizing", False) else prey_to_eat.energy
                            entity.energy = min(int(entity.max_energy * 1.5) if getattr(entity, "is_gluttonous", False) else entity.max_energy, entity.energy + energy_gained)
                            if getattr(entity, 'is_resourceful', False):
                                entity.hydration = min(entity.max_hydration, entity.hydration + 10)
                            if getattr(prey_to_eat, 'is_toxic', False):
                                entity.poisoned_time += 10
                            if not getattr(entity, 'has_strong_stomach', False) and getattr(prey_to_eat, 'toxicity', 0) > entity.poison_resistance:
                                entity.poisoned_time += (prey_to_eat.toxicity - entity.poison_resistance) * 5

                            # Gain experience/strength from eating prey
                            entity.attack += 0.5
                            entity.add_experience(5)
                            entity.defense += 0.5
                            entity.stamina = max(0, getattr(entity, 'stamina', 50) - 2)
                            if getattr(entity, 'is_bloodthirsty', False):
                                entity.stamina = min(getattr(entity, 'max_stamina', 50), getattr(entity, 'stamina', 50) + 20)

                            prey_to_eat.energy = 0 # Kill prey
                            prey_to_eat.was_eaten = True

            if entity.is_alive and entity.diet in ['herbivore', 'scavenger', 'omnivore'] and not getattr(entity, 'is_scentless', False):
                self.scent_trails[(entity.x, entity.y)] = 40 if getattr(entity, 'is_smelly', False) else 20

            if entity.is_alive:
                if getattr(entity, 'is_nomadic', False) and (entity.x != start_pos_x or entity.y != start_pos_y):
                    cap = int(entity.max_energy * 1.5) if getattr(entity, 'is_gluttonous', False) else entity.max_energy
                    entity.energy = min(cap, entity.energy + 2)

                entity.remained_stationary = (entity.x == start_pos_x and entity.y == start_pos_y)

                if entity.x == start_pos_x and entity.y == start_pos_y:
                    recovery = 5 if entity.is_sleeping else 2
                    if getattr(entity, 'is_patient', False):
                        recovery *= 2
                    if getattr(entity, 'is_endurance_runner', False):
                        recovery *= 2
                    if getattr(entity, 'is_photosensitive', False) and self.is_night:
                        recovery += 2
                    if getattr(entity, 'is_introspective', False):
                        entity.add_experience(2)
                    entity.stamina = min(getattr(entity, 'max_stamina', 50), getattr(entity, 'stamina', 50) + recovery)




        dead_entities = [e for e in self.entities if not e.is_alive]
        for dead in dead_entities:
            if hasattr(dead, 'attached_parasites'):
                for p in dead.attached_parasites:
                    p.host = None
                dead.attached_parasites = []
            if getattr(dead, 'host', None) is not None:
                if hasattr(dead.host, 'attached_parasites') and dead in dead.host.attached_parasites:
                    dead.host.attached_parasites.remove(dead)
                dead.host = None

            if not getattr(dead, 'was_eaten', False):
                meat_x = max(0, min(self.width - 1, dead.x))
                meat_y = max(0, min(self.height - 1, dead.y))
                self.add_food(Food(x=meat_x, y=meat_y, energy=dead.size * 5, plant_type='meat', toxicity=getattr(dead, 'toxicity', 0), max_age=60))

        self.entities = [e for e in self.entities if getattr(e, "is_alive", True)]
        for child in new_entities:
            self.add_entity(child)
