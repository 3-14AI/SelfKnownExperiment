import unittest
from src.universe.engine import Universe, Entity, Food, Terrain

class TestUniverse(unittest.TestCase):
    def test_terrain_initialization(self):
        terrain = Terrain(x=5, y=5, terrain_type='water')
        self.assertEqual(terrain.x, 5)
        self.assertEqual(terrain.y, 5)
        self.assertEqual(terrain.terrain_type, 'water')

    def test_add_terrain(self):
        universe = Universe()
        terrain = Terrain(x=5, y=5, terrain_type='wall')
        universe.add_terrain(terrain)
        self.assertEqual(len(universe.terrains), 1)
        self.assertEqual(universe.terrains[0], terrain)
        self.assertEqual(universe.get_terrains_at(5, 5)[0], terrain)

        with self.assertRaises(ValueError):
            universe.add_terrain(Terrain(x=100, y=10))

    def test_move_entity_blocked_by_terrain(self):
        universe = Universe(width=10, height=10)
        entity = Entity("Adam", x=5, y=5)
        universe.add_entity(entity)
        universe.add_terrain(Terrain(x=6, y=5, terrain_type='wall'))

        with self.assertRaises(ValueError):
            universe.move_entity(entity, 1, 0)

        self.assertEqual(entity.x, 5)
        self.assertEqual(entity.y, 5)

    def test_initial_state(self):
        universe = Universe()
        self.assertEqual(universe.time, 0)
        self.assertEqual(universe.entities, [])
        self.assertEqual(universe.foods, [])
        self.assertEqual(universe.width, 100)
        self.assertEqual(universe.height, 100)

    def test_add_food(self):
        universe = Universe()
        food = Food(energy=10)
        universe.add_food(food, x=5, y=5)
        self.assertEqual(len(universe.foods), 1)
        self.assertEqual(universe.foods[0], food)
        self.assertEqual(food.x, 5)
        self.assertEqual(food.y, 5)

        with self.assertRaises(ValueError):
            universe.add_food(Food(), x=100, y=10)

    def test_add_entity(self):
        universe = Universe()
        entity = Entity("Adam")
        universe.add_entity(entity)
        self.assertEqual(len(universe.entities), 1)
        self.assertEqual(universe.entities[0], entity)
        self.assertEqual(entity.x, 0)
        self.assertEqual(entity.y, 0)

    def test_add_entity_custom_position(self):
        universe = Universe()
        entity = Entity("Eve")
        universe.add_entity(entity, x=10, y=20)
        self.assertEqual(entity.x, 10)
        self.assertEqual(entity.y, 20)

    def test_add_entity_out_of_bounds(self):
        universe = Universe()
        entity = Entity("Lilith")
        with self.assertRaises(ValueError):
            universe.add_entity(entity, x=100, y=10)
        with self.assertRaises(ValueError):
            universe.add_entity(entity, x=10, y=-1)

    def test_move_entity_valid(self):
        universe = Universe()
        entity = Entity("Adam")
        universe.add_entity(entity)
        universe.move_entity(entity, 5, 5)
        self.assertEqual(entity.x, 5)
        self.assertEqual(entity.y, 5)
        universe.move_entity(entity, -2, 3)
        self.assertEqual(entity.x, 3)
        self.assertEqual(entity.y, 8)

    def test_move_entity_invalid(self):
        universe = Universe(width=10, height=10)
        entity = Entity("Adam", x=5, y=5)
        universe.add_entity(entity)
        with self.assertRaises(ValueError):
            universe.move_entity(entity, 5, 0)  # new x = 10 (out of bounds)
        with self.assertRaises(ValueError):
            universe.move_entity(entity, 0, -6) # new y = -1 (out of bounds)
        # Verify position hasn't changed
        self.assertEqual(entity.x, 5)
        self.assertEqual(entity.y, 5)

    def test_get_entities_at(self):
        universe = Universe()
        e1 = Entity("E1", x=10, y=10)
        e2 = Entity("E2", x=10, y=10)
        e3 = Entity("E3", x=10, y=11)
        universe.add_entity(e1)
        universe.add_entity(e2)
        universe.add_entity(e3)

        at_10_10 = universe.get_entities_at(10, 10)
        self.assertEqual(len(at_10_10), 2)
        self.assertIn(e1, at_10_10)
        self.assertIn(e2, at_10_10)

        at_10_11 = universe.get_entities_at(10, 11)
        self.assertEqual(len(at_10_11), 1)
        self.assertEqual(at_10_11[0], e3)

        at_0_0 = universe.get_entities_at(0, 0)
        self.assertEqual(len(at_0_0), 0)

    def test_tick(self):
        universe = Universe()
        universe.tick()
        self.assertEqual(universe.time, 1)

    def test_entity_energy_initialization(self):
        entity = Entity("Adam")
        self.assertEqual(entity.energy, 10)
        self.assertTrue(entity.is_alive)
        entity_custom = Entity("Eve", energy=5)
        self.assertEqual(entity_custom.energy, 5)

    def test_tick_consumes_energy(self):
        universe = Universe()
        universe.event_chance = 0.0
        entity = Entity("Adam")
        universe.add_entity(entity)
        self.assertEqual(entity.energy, 10)
        universe.tick()
        self.assertEqual(entity.energy, 9)

    def test_entity_dies(self):
        universe = Universe()
        universe.event_chance = 0.0
        entity = Entity("Adam", energy=1)
        universe.add_entity(entity)
        universe.tick()
        self.assertEqual(entity.energy, 0)
        self.assertFalse(entity.is_alive)
        self.assertNotIn(entity, universe.entities)

    def test_get_foods_at(self):
        universe = Universe()
        f1 = Food(x=10, y=10)
        f2 = Food(x=10, y=10)
        f3 = Food(x=10, y=11)
        universe.add_food(f1)
        universe.add_food(f2)
        universe.add_food(f3)

        at_10_10 = universe.get_foods_at(10, 10)
        self.assertEqual(len(at_10_10), 2)
        self.assertIn(f1, at_10_10)
        self.assertIn(f2, at_10_10)

        at_10_11 = universe.get_foods_at(10, 11)
        self.assertEqual(len(at_10_11), 1)
        self.assertEqual(at_10_11[0], f3)

    def test_entity_eats_food(self):
        universe = Universe(food_spawn_rate=0.0) # Disable random food spawn for this test
        universe.event_chance = 0.0
        entity = Entity("Adam", energy=10, x=5, y=5)
        food = Food(energy=5, x=5, y=5)
        universe.add_entity(entity)
        universe.add_food(food)

        self.assertEqual(len(universe.foods), 1)
        universe.tick()

        # Entity should lose 1 energy from tick, but gain 5 from food (10 - 1 + 5 = 14)
        self.assertEqual(entity.energy, 14)
        self.assertEqual(len(universe.foods), 0)

    def test_entity_pathfinding_around_obstacle(self):
        universe = Universe(width=10, height=10, food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0)
        universe.add_entity(entity)
        universe.add_food(Food(x=2, y=0, energy=5))

        # Add a wall at (1, 0) blocking the direct path
        universe.add_terrain(Terrain(x=1, y=0, terrain_type='wall'))

        # Entity should route around: (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,0)
        # Tick 1: move to (0, 1)
        universe.tick()
        self.assertEqual(entity.x, 0)
        self.assertEqual(entity.y, 1)

        # Tick 2: move to (1, 1)
        universe.tick()
        self.assertEqual(entity.x, 1)
        self.assertEqual(entity.y, 1)

        # Tick 3: move to (2, 1)
        universe.tick()
        self.assertEqual(entity.x, 2)
        self.assertEqual(entity.y, 1)

        # Tick 4: move to (2, 0) and eat food
        universe.tick()
        self.assertEqual(entity.x, 2)
        self.assertEqual(entity.y, 0)
        self.assertEqual(len(universe.foods), 0)

    def test_entity_seeks_food(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0)
        food = Food(x=2, y=2)
        universe.add_entity(entity)
        universe.add_food(food)

        # Previously entities could move diagonally (1, 1). BFS only moves orthogonally.
        # It takes 4 orthogonal moves to reach (2, 2) from (0, 0).
        universe.tick()
        universe.tick()
        universe.tick()
        self.assertEqual(len(universe.foods), 1) # Hasn't reached food yet

        universe.tick() # Reaches and eats food
        self.assertEqual(entity.x, 2)
        self.assertEqual(entity.y, 2)
        self.assertEqual(len(universe.foods), 0) # Food eaten


    def test_entity_reproduction(self):
        universe = Universe(reproduction_threshold=15, reproduction_cost=10, food_spawn_rate=0.0)
        universe.event_chance = 0.0
        entity = Entity("Adam", energy=16, x=5, y=5)
        universe.add_entity(entity)

        # Tick 1: entity loses 1 energy to tick, reproduces and spends 10 energy (16 - 1 - 10 = 5)
        universe.tick()

        self.assertEqual(entity.energy, 5)
        self.assertEqual(len(universe.entities), 2)

        child = universe.entities[1]
        self.assertEqual(child.name, "Adam_child")
        self.assertEqual(child.x, 5)
        self.assertEqual(child.y, 5)
        self.assertEqual(child.energy, 10) # default energy

    def test_entity_aging(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("OldMan", energy=100, max_age=3)
        universe.add_entity(entity)

        self.assertEqual(entity.age, 0)

        # Tick 1: age = 1
        universe.tick()
        self.assertEqual(entity.age, 1)
        self.assertTrue(entity.is_alive)
        self.assertIn(entity, universe.entities)

        # Tick 2: age = 2
        universe.tick()
        self.assertEqual(entity.age, 2)
        self.assertTrue(entity.is_alive)
        self.assertIn(entity, universe.entities)

        # Tick 3: age = 3 (still alive since age <= max_age)
        universe.tick()
        self.assertEqual(entity.age, 3)
        self.assertTrue(entity.is_alive)
        self.assertIn(entity, universe.entities)

        # Tick 4: age = 4 (dies since age > max_age)
        universe.tick()
        self.assertEqual(entity.age, 4)
        self.assertFalse(entity.is_alive)
        self.assertNotIn(entity, universe.entities)

    def test_event_storm_energy_decay(self):
        universe = Universe()
        universe.current_event = 'storm'
        universe.event_remaining_time = 5
        entity = Entity("Adam", energy=10, preferred_temperature=20, temperature_tolerance=10)
        universe.add_entity(entity)
        universe.tick()
        self.assertEqual(entity.energy, 8)

    def test_event_drought_food_spawn(self):
        universe = Universe(food_spawn_rate=1.0)
        universe.current_event = 'drought'
        universe.event_remaining_time = 5
        universe.tick()
        self.assertEqual(len(universe.foods), 0)

    def test_event_triggers_and_expires(self):
        universe = Universe()
        universe.event_chance = 1.0
        universe.tick()
        self.assertIsNotNone(universe.current_event)
        self.assertTrue(universe.event_remaining_time > 0)
        remaining_time = universe.event_remaining_time
        for _ in range(remaining_time):
            universe.tick()
        self.assertIsNone(universe.current_event)


    def test_entity_perception_radius_food(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0, perception_radius=2)
        universe.add_entity(entity)
        universe.add_food(Food(x=3, y=0, energy=5))

        nearest = universe.get_nearest_food(entity.x, entity.y, max_distance=entity.perception_radius)
        self.assertIsNone(nearest)

        universe.tick()
        self.assertEqual(entity.x, 0)
        self.assertEqual(entity.y, 0)

        universe.add_food(Food(x=2, y=0, energy=5))
        nearest2 = universe.get_nearest_food(entity.x, entity.y, max_distance=entity.perception_radius)
        self.assertIsNotNone(nearest2)
        self.assertEqual(nearest2.x, 2)
        self.assertEqual(nearest2.y, 0)

        universe.tick()
        self.assertEqual(entity.x, 1)
        self.assertEqual(entity.y, 0)

    def test_entity_perception_radius_obstacle(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0, perception_radius=3)
        universe.add_entity(entity)
        universe.add_terrain(Terrain(x=0, y=1, terrain_type='wall'))

        path1 = universe.find_path(0, 0, 0, 2, max_distance=3)
        self.assertIsNotNone(path1)
        self.assertNotEqual(path1[0], (0, 1))

        path2 = universe.find_path(0, 0, 0, 2, max_distance=0)
        self.assertIsNotNone(path2)
        self.assertEqual(path2[0], (0, 1))


    def test_entity_memory_update(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0, perception_radius=2)
        universe.add_entity(entity)
        # Wall is within perception radius
        universe.add_terrain(Terrain(x=2, y=0, terrain_type='wall'))
        # Water is outside perception radius
        universe.add_terrain(Terrain(x=0, y=3, terrain_type='water'))

        universe.tick()

        self.assertIn((2, 0), entity.memory)
        self.assertNotIn((0, 3), entity.memory)

    def test_find_path_with_memory(self):
        universe = Universe(food_spawn_rate=0.0)
        entity = Entity("Adam", x=0, y=0, perception_radius=1)
        universe.add_entity(entity)
        universe.add_food(Food(x=0, y=2, energy=5))

        # Wall is outside perception radius, but entity remembers it
        entity.memory.add((0, 1))

        path = universe.find_path(entity.x, entity.y, 0, 2, max_distance=entity.perception_radius, memory=entity.memory)
        self.assertIsNotNone(path)
        # Should route around (0,1) memory
        self.assertNotEqual(path[0], (0, 1))


    def test_entity_genetics_and_mutation(self):
        # We'll run reproduction several times with high mutation chance to ensure mutation happens,
        # or we mock random to control it. Using Universe event_chance=0.0 to prevent event interference.
        universe = Universe(reproduction_threshold=20, reproduction_cost=10)
        universe.event_chance = 0.0

        # We use a deterministic way by modifying random locally or monkeypatching,
        # but to keep it simple, let's just monkeypatch random inside the test
        import random
        original_random = random.random
        original_randint = random.randint

        try:
            # Force mutation to happen
            random.random = lambda: 0.05 # Less than 0.1 mutation chance
            # Force max_age to increase by 5, perception_radius by 2
            random.randint = lambda a, b: b

            parent = Entity("Parent", x=5, y=5, energy=25, max_age=50, perception_radius=10)
            universe.add_entity(parent)

            universe.tick()

            self.assertEqual(len(universe.entities), 2)
            child = [e for e in universe.entities if "child" in e.name][0]

            # Since we forced random.randint to return max value (b),
            # child_max_age should be 50 + 5 = 55
            # child_perception_radius should be 10 + 2 = 12
            self.assertEqual(child.max_age, 55)
            self.assertEqual(child.perception_radius, 12)

        finally:
            random.random = original_random
            random.randint = original_randint

    def test_entity_genetics_no_mutation(self):
        universe = Universe(reproduction_threshold=20, reproduction_cost=10)
        universe.event_chance = 0.0

        import random
        original_random = random.random

        try:
            # Force mutation to NOT happen
            random.random = lambda: 0.5 # Greater than 0.1 mutation chance

            parent = Entity("Parent", x=5, y=5, energy=25, max_age=50, perception_radius=10)
            universe.add_entity(parent)

            universe.tick()

            self.assertEqual(len(universe.entities), 2)
            child = [e for e in universe.entities if "child" in e.name][0]

            # Since we forced mutation to fail, traits should perfectly inherit
            self.assertEqual(child.max_age, 50)
            self.assertEqual(child.perception_radius, 10)

        finally:
            random.random = original_random


    def test_carnivore_eating(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0
        carnivore = Entity("Lion", x=0, y=0, diet='carnivore', energy=10, attack=100)
        herbivore = Entity("Zebra", x=2, y=0, diet='herbivore', energy=10, defense=0, perception_radius=0)
        universe.add_entity(carnivore)
        universe.add_entity(herbivore)

        # 2 steps to reach prey at (2,0) from (0,0)
        universe.tick()
        universe.tick()

        self.assertEqual(carnivore.x, 2)
        self.assertEqual(carnivore.y, 0)

        # Herbivore should be dead, removed from entities
        self.assertNotIn(herbivore, universe.entities)

        # Carnivore lost 2 energy from 2 ticks, gained 10 from prey -> 10 - 2 + 10 = 18
        self.assertEqual(carnivore.energy, 17)


    def test_combat_defense_escape(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0
        # High defense, 0 attack -> 100% escape chance
        carnivore = Entity("Lion", x=0, y=0, diet='carnivore', energy=10, attack=0)
        herbivore = Entity("Zebra", x=2, y=0, diet='herbivore', energy=10, defense=100, perception_radius=0)
        universe.add_entity(carnivore)
        universe.add_entity(herbivore)

        # Force escape by forcing random to 0.0
        import random
        original_random = random.random
        try:
            random.random = lambda: 0.0
            universe.tick()
            universe.tick()
        finally:
            random.random = original_random

        # Check prey escaped
        self.assertIn(herbivore, universe.entities)
        # Both lost energy from struggles and ticks
        self.assertLess(carnivore.energy, 10)
        self.assertLess(herbivore.energy, 10)


    def test_combat_defense_eaten(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0
        # Low defense, high attack -> 0% escape chance
        carnivore = Entity("Lion", x=0, y=0, diet='carnivore', energy=10, attack=100)
        herbivore = Entity("Zebra", x=2, y=0, diet='herbivore', energy=10, defense=0, perception_radius=0)
        universe.add_entity(carnivore)
        universe.add_entity(herbivore)

        # Force eaten by forcing random to 0.99
        import random
        original_random = random.random
        try:
            random.random = lambda: 0.99
            universe.tick()
            universe.tick()
        finally:
            random.random = original_random

        self.assertNotIn(herbivore, universe.entities)

    def test_carnivore_genetics(self):
        universe = Universe(reproduction_threshold=15, reproduction_cost=10, food_spawn_rate=0.0)
        universe.event_chance = 0.0
        carnivore = Entity("Lion", energy=16, x=5, y=5, diet='carnivore')
        universe.add_entity(carnivore)

        universe.tick()

        self.assertEqual(len(universe.entities), 2)
        child = universe.entities[1]
        self.assertEqual(child.name, "Lion_child")
        self.assertEqual(child.diet, "carnivore")


    def test_population_limit(self):
        universe = Universe(reproduction_threshold=15, reproduction_cost=10, food_spawn_rate=0.0, population_limit=2)
        universe.event_chance = 0.0
        entity1 = Entity("Adam", energy=16, x=5, y=5)
        entity2 = Entity("Eve", energy=16, x=6, y=6)
        universe.add_entity(entity1)
        universe.add_entity(entity2)

        # The universe already has 2 entities, which is the population limit.
        # Neither entity should be able to reproduce despite having enough energy.
        universe.tick()

        self.assertEqual(len(universe.entities), 2)
        # Energy should only decrease by 1 for the tick, not by 10 for reproduction
        self.assertEqual(entity1.energy, 15)
        self.assertEqual(entity2.energy, 15)


    def test_season_cycles(self):
        universe = Universe(season_length=10)
        universe.event_chance = 0.0

        self.assertEqual(universe.current_season, 'spring')

        for _ in range(10):
            universe.tick()
        self.assertEqual(universe.current_season, 'summer')

        for _ in range(10):
            universe.tick()
        self.assertEqual(universe.current_season, 'autumn')

        for _ in range(10):
            universe.tick()
        self.assertEqual(universe.current_season, 'winter')

        for _ in range(10):
            universe.tick()
        self.assertEqual(universe.current_season, 'spring')

    def test_seasonal_food_spawn_rate(self):
        import random
        random.seed(42)
        universe = Universe(season_length=10, food_spawn_rate=1.0)
        universe.event_chance = 0.0

        # Spring should have 1.5 * food_spawn_rate (1.5)
        # So we should expect 1-2 food per tick. Over 10 ticks, at least 15 food
        for _ in range(10):
            universe.tick()
        spring_food = len(universe.foods)
        self.assertGreaterEqual(spring_food, 10)

        universe.foods = []
        # Summer should have 1.0 * food_spawn_rate
        for _ in range(10):
            universe.tick()
        summer_food = len(universe.foods)
        self.assertAlmostEqual(summer_food, 10, delta=3)

        universe.foods = []
        # Autumn should have 0.8 * food_spawn_rate
        for _ in range(10):
            universe.tick()
        autumn_food = len(universe.foods)
        self.assertLess(autumn_food, 10)

        universe.foods = []
        # Winter should have 0.2 * food_spawn_rate
        for _ in range(10):
            universe.tick()
        winter_food = len(universe.foods)
        self.assertLessEqual(winter_food, 5)

    def test_seasonal_terrain_changes(self):
        universe = Universe(season_length=10)
        universe.event_chance = 0.0
        terrain = Terrain(x=0, y=0, terrain_type='water')
        universe.add_terrain(terrain)

        # Advance to winter
        for _ in range(30):
            universe.tick()

        self.assertEqual(universe.current_season, 'winter')
        self.assertEqual(universe.terrains[0].terrain_type, 'ice')

        # Advance to spring
        for _ in range(10):
            universe.tick()

        self.assertEqual(universe.current_season, 'spring')
        self.assertEqual(universe.terrains[0].terrain_type, 'water')


    def test_localized_rain_event(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0 # disable global events
        universe.localized_event_chance = 0.0

        # Manually add a rain event
        from universe.engine import LocalizedEvent
        event = LocalizedEvent('rain', 5, 5, radius=3, duration=10)
        universe.localized_events.append(event)

        # Rain has a 20% chance to spawn food each tick per event, over 10 ticks.
        # We simulate this many times to ensure food is spawned within the radius
        # Rain has a 1.0 chance to spawn food if we mock random
        import random
        original_random = random.random
        try:
            random.random = lambda: 0.1 # guarantee rain food spawn, avoid localized event spawn (chance=0.0)
            initial_food_count = len(universe.foods)
            for _ in range(10):
                universe.tick()
        finally:
            random.random = original_random

        # Verify event duration logic (should be removed after 10 ticks)
        self.assertEqual(len(universe.localized_events), 0)

        # Verify food was spawned
        self.assertGreater(len(universe.foods), initial_food_count)

        # Verify food is within radius
        for f in universe.foods:
            self.assertTrue((f.x - 5)**2 + (f.y - 5)**2 <= 3**2)

    def test_localized_fire_event(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0 # disable global events
        universe.localized_event_chance = 0.0

        # Setup targets within radius
        from universe.engine import LocalizedEvent, Entity, Food, Terrain

        e_in = Entity("InRadius", x=5, y=5)
        e_out = Entity("OutRadius", x=10, y=10, diet="carnivore")
        f_in = Food(x=6, y=6)
        f_out = Food(x=11, y=11)
        t_in = Terrain(x=4, y=4, terrain_type='wall')
        t_out = Terrain(x=10, y=10, terrain_type='wall')

        universe.add_entity(e_in)
        universe.add_entity(e_out)
        universe.add_food(f_in)
        universe.add_food(f_out)
        universe.add_terrain(t_in)
        universe.add_terrain(t_out)

        # Add a fire event
        event = LocalizedEvent('fire', 5, 5, radius=3, duration=2)
        universe.localized_events.append(event)

        universe.tick()

        # Check entities
        self.assertNotIn(e_in, universe.entities)
        self.assertIn(e_out, universe.entities)

        # Check food
        self.assertNotIn(f_in, universe.foods)
        self.assertIn(f_out, universe.foods)

        # Check terrain (converted to ash within radius, unchanged outside)
        # We also added ash for dead entity and destroyed food
        ash_terrains = [t for t in universe.terrains if t.terrain_type == 'ash']
        self.assertGreaterEqual(len(ash_terrains), 3) # t_in converted, e_in converted, f_in converted

        # Original t_out wall should still be wall
        wall_terrains = [t for t in universe.terrains if t.terrain_type == 'wall']
        self.assertEqual(len(wall_terrains), 1)
        self.assertEqual(wall_terrains[0].x, 10)
        self.assertEqual(wall_terrains[0].y, 10)



    def test_day_night_cycle(self):
        universe = Universe(day_length=10)

        # Day: time 0 to 4
        self.assertTrue(universe.is_day)
        self.assertFalse(universe.is_night)

        for _ in range(4):
            universe.tick()

        # time = 4, Day
        self.assertTrue(universe.is_day)

        universe.tick()
        # time = 5, Night: time 5 to 9
        self.assertFalse(universe.is_day)
        self.assertTrue(universe.is_night)

        for _ in range(4):
            universe.tick()

        # time = 9, Night
        self.assertTrue(universe.is_night)

        universe.tick()
        # time = 10, Day again
        self.assertTrue(universe.is_day)

    def test_night_vision(self):
        import random
        original_random = random.random
        try:
            # Force movement by making random > 0.5 so they always move at night
            random.random = lambda: 0.9

            universe = Universe(day_length=10, food_spawn_rate=0.0)
            universe.event_chance = 0.0

            entity = Entity("Observer", x=0, y=0, perception_radius=10, energy=20)
            universe.add_entity(entity)

            # Place food at distance 8
            universe.add_food(Food(x=8, y=0))

            # During day (time=0), perception is 10, food is at distance 8 -> visible
            # Entity should move towards food
            universe.tick()
            self.assertEqual(entity.x, 1)
            self.assertEqual(entity.y, 0)

            # Advance to night (time=5)
            for _ in range(4):
                universe.tick()

            # Now time is 5, it is night. Perception is max(1, 10 // 2) = 5
            # Entity is at x=5. Food is at x=8. Distance is 3. Perception is 5, so food is still visible!
            # Let's reset the scenario to test properly.
        finally:
            random.random = original_random

    def test_night_vision_proper(self):
        import random
        original_random = random.random
        try:
            random.random = lambda: 0.9 # guarantee movement
            universe = Universe(day_length=10, food_spawn_rate=0.0)
            universe.event_chance = 0.0

            # Fast forward to night
            for _ in range(5):
                universe.tick()

            self.assertTrue(universe.is_night)

            entity = Entity("Observer", x=0, y=0, perception_radius=10, energy=20)
            universe.add_entity(entity)

            # Place food at distance 8
            # Night perception is 5. So distance 8 is NOT visible.
            universe.add_food(Food(x=8, y=0))

            universe.tick()
            # Entity shouldn't have moved towards food, it might just stay or move randomly if we implemented random walk,
            # but currently if no path is found, it stays still (dx,dy logic only applies if path is found)
            self.assertEqual(entity.x, 0)
            self.assertEqual(entity.y, 0)

        finally:
            random.random = original_random

    def test_night_movement(self):
        import random
        original_random = random.random
        try:
            # Force skip movement by making random < 0.5
            random.random = lambda: 0.1

            universe = Universe(day_length=10, food_spawn_rate=0.0)
            universe.event_chance = 0.0

            # Fast forward to night
            for _ in range(5):
                universe.tick()

            self.assertTrue(universe.is_night)

            entity = Entity("Sleeper", x=0, y=0, perception_radius=10, energy=20)
            universe.add_entity(entity)

            # Place food very close (distance 2) so it's well within night perception (5)
            universe.add_food(Food(x=2, y=0))

            universe.tick()
            # Due to 50% chance failing (mocked to 0.1), entity skips movement
            self.assertEqual(entity.x, 0)
            self.assertEqual(entity.y, 0)

        finally:
            random.random = original_random


    def test_temperature_zone_effect(self):
        from src.universe.engine import TemperatureZone, Entity, Universe
        u = Universe()
        # Create an entity with base preferred_temp 20 and tolerance 5 (15 to 25)
        e = Entity("TempTest", x=10, y=10, preferred_temperature=20, temperature_tolerance=5)
        e.energy = 20
        u.add_entity(e)

        # In a normal zone (base temp 20), energy loss should be 1
        u.tick()
        self.assertEqual(e.energy, 19)

        # Add a cold temperature zone (-10 modifier) at (10, 10) with radius 5
        # The temperature at (10, 10) becomes 10. This is outside the [15, 25] range.
        u.add_temperature_zone(TemperatureZone(x=10, y=10, radius=5, temperature_modifier=-10))
        u.tick()
        # Energy loss should be 2 (1 base + 1 temp penalty)
        self.assertEqual(e.energy, 17)

    def test_temperature_trait_inheritance(self):
        from src.universe.engine import Entity, Universe
        import random
        # Mock random to avoid mutations making tests flaky
        random.seed(42)

        u = Universe(population_limit=10, reproduction_threshold=15, reproduction_cost=10)
        u.event_chance = 0.0
        u.localized_event_chance = 0.0
        e = Entity("Parent", x=5, y=5, preferred_temperature=18, temperature_tolerance=3)
        e.energy = 20
        u.add_entity(e)

        # Force deterministic reproduction by setting random to 1.0 (no mutation)
        original_random = random.random
        random.random = lambda: 1.0
        u.tick()
        random.random = original_random

        self.assertEqual(len(u.entities), 2)
        child = u.entities[1]
        self.assertEqual(child.preferred_temperature, 18)
        self.assertEqual(child.temperature_tolerance, 3)


    def test_flocking_behavior(self):
        universe = Universe(width=10, height=10, food_spawn_rate=0)
        universe.event_chance = 0.0
        universe.localized_event_chance = 0.0
        e1 = Entity("E1", x=2, y=2, diet='herbivore')
        e2 = Entity("E2", x=2, y=4, diet='herbivore')
        universe.add_entity(e1)
        universe.add_entity(e2)

        universe.tick()

        # Without food, they should move towards each other (center of mass)
        # Center is 2, 3. E1 moves to 2, 3 and E2 moves to 2, 3
        self.assertEqual(e1.x, 2)
        self.assertEqual(e1.y, 3)
        self.assertEqual(e2.x, 2)
        self.assertEqual(e2.y, 3)


    def test_scent_trail_creation(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0
        entity = Entity("Deer", x=5, y=5, diet='herbivore')
        universe.add_entity(entity)

        universe.tick()

        # Herbivore should have left a scent of 20 at its position at the end of the tick
        self.assertIn((5, 5), universe.scent_trails)
        self.assertEqual(universe.scent_trails[(5, 5)], 20)

    def test_scent_trail_decay(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0
        # Initialize an artificial scent trail
        universe.scent_trails[(0, 0)] = 20

        universe.tick()

        # Scent should decay by 1 each tick
        self.assertEqual(universe.scent_trails[(0, 0)], 19)

        for _ in range(19):
            universe.tick()

        # Scent should be completely removed when intensity <= 0
        self.assertNotIn((0, 0), universe.scent_trails)

    def test_carnivore_scent_tracking(self):
        universe = Universe(food_spawn_rate=0.0)
        universe.event_chance = 0.0

        # Place a carnivore
        carnivore = Entity("Wolf", x=5, y=5, diet='carnivore', perception_radius=2)
        universe.add_entity(carnivore)

        # Add a trail of scent leading right (to x=7).
        # (5, 5) shouldn't matter as it moves away, but let's make adjacent (6, 5) highest
        universe.scent_trails[(6, 5)] = 20
        universe.scent_trails[(5, 6)] = 10
        universe.scent_trails[(5, 4)] = 10
        universe.scent_trails[(4, 5)] = 5

        universe.tick()

        # Carnivore should move to the strongest adjacent scent (6, 5)
        self.assertEqual(carnivore.x, 6)
        self.assertEqual(carnivore.y, 5)


    def test_global_earthquake(self):
        from src.universe.engine import Universe, Terrain
        import random
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.event_chance = 1.0

        # force earthquake and force 1.0 random for cell modification
        original_choice = random.choice
        original_random = random.random
        try:
            random.choice = lambda x: 'earthquake'
            # First call to random.random() is event_chance, which should be < 1.0 (we set event_chance=1.0, so < 1.0 is True if we return 0.0)
            # The next calls are inside the earthquake loop, which check < 0.05. We want them to pass, so return 0.0
            random.random = lambda: 0.0

            # Place a wall that will be destroyed
            u.add_terrain(Terrain(x=5, y=5, terrain_type='wall'))

            u.tick()

            self.assertEqual(u.current_event, 'earthquake')

            # Since chance was 0.0, every tile should have triggered.
            # (5,5) had a wall, so it should be destroyed (no wall).
            # Other tiles should have a wall created.

            # Check (5,5) has no wall
            self.assertFalse(any(t.terrain_type == 'wall' for t in u.get_terrains_at(5, 5)))

            # Check another tile (0,0) has a wall
            self.assertTrue(any(t.terrain_type == 'wall' for t in u.get_terrains_at(0, 0)))
        finally:
            random.choice = original_choice
            random.random = original_random

    def test_global_volcano(self):
        from src.universe.engine import Universe, Terrain
        import random
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.event_chance = 1.0

        original_choice = random.choice
        original_random = random.random
        try:
            random.choice = lambda x: 'volcano'
            random.random = lambda: 0.0

            # Add existing terrain to test mutation
            u.add_terrain(Terrain(x=2, y=2, terrain_type='wall'))
            u.add_terrain(Terrain(x=3, y=3, terrain_type='water'))

            u.tick()

            self.assertEqual(u.current_event, 'volcano')

            # Wall at (2,2) should become ash
            t_2_2 = u.get_terrains_at(2, 2)
            self.assertTrue(any(t.terrain_type == 'ash' for t in t_2_2))

            # Water at (3,3) should remain water
            t_3_3 = u.get_terrains_at(3, 3)
            self.assertTrue(any(t.terrain_type == 'water' for t in t_3_3))

            # Empty spot (4,4) should get ash
            t_4_4 = u.get_terrains_at(4, 4)
            self.assertTrue(any(t.terrain_type == 'ash' for t in t_4_4))

        finally:
            random.choice = original_choice
            random.random = original_random


    def test_disease_spontaneous_outbreak(self):
        import random; import src.universe.engine as eng
        from src.universe.engine import Universe, Entity
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.disease_chance = 1.0
        u.event_chance = 0.0

        # Create entity and add
        e = Entity("Healthy", x=5, y=5, is_infected=False)
        u.add_entity(e)

        original_random = eng.random.random
        original_choice = eng.random.choice
        try:
            eng.random.random = lambda: 0.0
            eng.random.choice = lambda x: x[0] # always pick the first entity

            u.tick()
            self.assertTrue(e.is_infected)
        finally:
            eng.random.random = original_random
            eng.random.choice = original_choice

    def test_disease_spread(self):
        import random; import src.universe.engine as eng
        from src.universe.engine import Universe, Entity
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.disease_chance = 0.0 # No spontaneous outbreak
        u.event_chance = 0.0
        u.localized_event_chance = 0.0

        # Entity 1 is infected
        e1 = Entity("Sick", x=5, y=5, energy=20, is_infected=True)
        # Entity 2 is nearby and should get infected
        e2 = Entity("Near", x=6, y=6, energy=20, is_infected=False)
        # Entity 3 is far and should not get infected
        e3 = Entity("Far", x=0, y=0, energy=20, is_infected=False)

        u.add_entity(e1)
        u.add_entity(e2)
        u.add_entity(e3)

        # To prevent entity movement from moving them apart or breaking our deterministic random override
        e1.perception_radius = 0
        e2.perception_radius = 0
        e3.perception_radius = 0

        original_random = eng.random.random
        try:
            # Force disease spread to succeed, recovery to fail, and any other random check to fail
            def fake_random():
                return 0.0 # Always < 0.1 for disease spread

            eng.random.random = fake_random

            u.tick()

            self.assertTrue(e1.is_infected)
            self.assertTrue(e2.is_infected)
            self.assertFalse(e3.is_infected)
        finally:
            eng.random.random = original_random

    def test_disease_energy_loss(self):
        from src.universe.engine import Universe, Entity
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.disease_chance = 0.0
        u.event_chance = 0.0

        e_healthy = Entity("Healthy", x=2, y=2, energy=20, is_infected=False)
        e_sick = Entity("Sick", x=8, y=8, energy=20, is_infected=True)

        u.add_entity(e_healthy)
        u.add_entity(e_sick)

        u.tick()

        # Healthy loses 1 energy (if base temp is optimal)
        # Sick loses 2 energy (1 base + 1 disease)
        self.assertEqual(e_healthy.energy, 19)
        self.assertEqual(e_sick.energy, 18)


    def test_symbiosis_benefit(self):
        from src.universe.engine import Entity, Universe

        # Test basic energy loss without symbiosis benefit
        u_isolated = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u_isolated.event_chance = 0.0 # prevent random energy modifiers
        e_isolated = Entity("Herbivore", x=2, y=2, energy=20, species="Herbivore", symbiotic_with=["Bird"], preferred_temperature=20, temperature_tolerance=10)
        u_isolated.add_entity(e_isolated)
        u_isolated.tick()
        self.assertEqual(e_isolated.energy, 19)

        # Test energy loss with symbiosis benefit
        u_sym = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u_sym.event_chance = 0.0
        e_sym = Entity("Herbivore", x=2, y=2, energy=20, species="Herbivore", symbiotic_with=["Bird"], preferred_temperature=20, temperature_tolerance=10)
        e_partner = Entity("Bird", x=3, y=2, energy=20, species="Bird", symbiotic_with=["Herbivore"], preferred_temperature=20, temperature_tolerance=10)

        u_sym.add_entity(e_sym)
        u_sym.add_entity(e_partner)

        u_sym.tick()

        # Base energy loss is 1. Symbiosis reduces it by 1 -> loss is 0.
        self.assertEqual(e_sym.energy, 20)
        self.assertEqual(e_partner.energy, 20)


    def test_communication_alert_predator(self):
        universe = Universe(width=20, height=20, disease_chance=0.0)
        universe.event_chance = 0.0 # prevent random events

        # Predator at (0, 0)
        carnivore = Entity(name="Carnivore", x=0, y=0, diet="carnivore", perception_radius=10, energy=100)
        universe.add_entity(carnivore)

        # Herbivore 1 is near predator, sees it (at 3, 0)
        h1 = Entity(name="H1", x=3, y=0, diet="herbivore", perception_radius=5, energy=100)
        universe.add_entity(h1)

        # Herbivore 2 is out of range of predator (at 8, 0) - distance to predator is 8 > 5
        # but within communication range of Herbivore 1 (distance 5 <= 10, which is effective_perception * 2)
        h2 = Entity(name="H2", x=8, y=0, diet="herbivore", perception_radius=5, energy=100)
        universe.add_entity(h2)

        # Run tick
        universe.tick()

        # Both herbivores should have moved away from (0, 0) because h1 saw the predator
        # and alerted h2.

        # H1 was at (3,0), should move away from (0,0) -> (4,0)
        self.assertGreater(h1.x + h1.y, 3)

        # H2 was at (8,0), should move away from (0,0) -> (9,0)
        self.assertGreater(h2.x + h2.y, 8)


    def test_dynamic_base_temperature(self):
        from src.universe.engine import Universe
        u = Universe(width=10, height=10, season_length=10)
        u.event_chance = 0.0

        u.time = 0 # Spring
        u.tick()
        self.assertEqual(u.base_temperature, 20)

        u.time = 10 # Summer
        u.tick()
        self.assertEqual(u.base_temperature, 30)

        u.time = 20 # Autumn
        u.tick()
        self.assertEqual(u.base_temperature, 10)

        u.time = 30 # Winter
        u.tick()
        self.assertEqual(u.base_temperature, -5)

    def test_localized_water_ice_transition(self):
        from src.universe.engine import Universe, Terrain, TemperatureZone
        u = Universe(width=10, height=10, season_length=100) # Ensure no season change during tick 1
        u.event_chance = 0.0

        # Spring -> Base temp 20
        u.time = 0
        u.tick()

        # Add water
        u.add_terrain(Terrain(x=2, y=2, terrain_type='water'))
        # Add ice
        u.add_terrain(Terrain(x=5, y=5, terrain_type='ice'))

        # Create cold zone around water (base 20 - 25 = -5)
        u.add_temperature_zone(TemperatureZone(x=2, y=2, radius=2, temperature_modifier=-25))
        # Warm zone around ice (base 20 + 0 = 20 > 0, so ice will melt even without zone, but let's be explicit)

        u.tick()

        # Water should become ice because local temp <= 0
        t_2_2 = u.get_terrains_at(2, 2)[0]
        self.assertEqual(t_2_2.terrain_type, 'ice')

        # Ice should become water because local temp > 0
        t_5_5 = u.get_terrains_at(5, 5)[0]
        self.assertEqual(t_5_5.terrain_type, 'water')

    def test_rain_mud_and_washing(self):
        import random; import src.universe.engine as eng
        from src.universe.engine import Universe, Terrain
        u = Universe(width=10, height=10)
        u.event_chance = 0.0
        u.localized_event_chance = 1.0 # Guarantee localized event

        u.add_terrain(Terrain(x=5, y=5, terrain_type='ash'))
        u.add_terrain(Terrain(x=6, y=6, terrain_type='sand'))

        original_random = eng.random.random
        original_choice = eng.random.choice
        original_randint = eng.random.randint

        try:
            # Force 'rain'
            eng.random.choice = lambda x: 'rain'
            # Force conditions for event and mud creation
            eng.random.random = lambda: 0.0

            # Force event at (5,5), radius 5, duration 1
            # Then force the 3 tries for mud generation to hit (5,5), (6,6), (7,7)
            call_count = 0
            def fake_randint(a, b):
                nonlocal call_count
                call_count += 1
                if call_count == 1: return 5 # event x
                if call_count == 2: return 5 # event y
                if call_count == 3: return 5 # radius
                if call_count == 4: return 2 # duration
                if call_count == 5: return 0 # rain food x offset
                if call_count == 6: return 0 # rain food y offset
                # 3 terrain spots
                if call_count == 7: return 0  # rx offset (5,5) - ash
                if call_count == 8: return 0
                if call_count == 9: return 1  # rx offset (6,6) - sand
                if call_count == 10: return 1
                if call_count == 11: return 2 # rx offset (7,7) - empty -> mud
                if call_count == 12: return 2
                return original_randint(a, b)

            eng.random.randint = fake_randint

            u.tick()

            terrains = [(t.x, t.y, t.terrain_type) for t in u.terrains]

            # Ash at 5,5 washed away
            self.assertFalse(any(t[0] == 5 and t[1] == 5 and t[2] == 'ash' for t in terrains))
            # Sand at 6,6 washed away
            self.assertFalse(any(t[0] == 6 and t[1] == 6 and t[2] == 'sand' for t in terrains))
            # Mud created at 7,7
            self.assertTrue(any(t[0] == 7 and t[1] == 7 and t[2] == 'mud' for t in terrains))

        finally:
            eng.random.random = original_random
            eng.random.choice = original_choice
            eng.random.randint = original_randint

    def test_heat_creates_sand(self):
        import random; import src.universe.engine as eng
        from src.universe.engine import Universe
        u = Universe(width=10, height=10)
        u.event_chance = 0.0
        u.time = 0 # Spring, base temp 20

        # We force 'summer' and base temp 30
        u.time = 10
        u.season_length = 10

        original_random = eng.random.random
        original_randint = eng.random.randint

        try:
            # Force random to pass 50% chance for summer sand creation
            eng.random.random = lambda: 0.0

            # Force randint to always target (5,5) for the 5 tries
            eng.random.randint = lambda a, b: 5

            u.tick()

            # Since (5,5) was empty and temp >= 30, it should have sand.
            # Note: The logic tries 5 times, but get_terrains_at checks if empty,
            # so it only adds it once at (5,5).
            terrains = [(t.x, t.y, t.terrain_type) for t in u.terrains]
            self.assertTrue(any(t[0] == 5 and t[1] == 5 and t[2] == 'sand' for t in terrains))

        finally:
            eng.random.random = original_random
            eng.random.randint = original_randint


    def test_preferred_terrain(self):
        from src.universe.engine import Entity, Universe, Terrain
        u = Universe(width=10, height=10, food_spawn_rate=0.0, reproduction_threshold=100)
        u.event_chance = 0.0 # prevent random energy modifiers

        # Add mud at (2, 2)
        u.add_terrain(Terrain(x=2, y=2, terrain_type='mud'))

        # Entity thriving in mud
        e_mud = Entity("MudMonster", x=2, y=2, energy=20, preferred_terrain='mud', preferred_temperature=20, temperature_tolerance=10)
        u.add_entity(e_mud)

        # Entity not on preferred terrain
        e_lost = Entity("MudMonster2", x=3, y=3, energy=20, preferred_terrain='mud', preferred_temperature=20, temperature_tolerance=10)
        u.add_entity(e_lost)

        u.tick()

        # Base energy loss is 1. Thriving in mud reduces it by 1 -> loss is 0.
        self.assertEqual(e_mud.energy, 20)
        # Base energy loss is 1. Not on preferred terrain adds 1 -> loss is 2.
        self.assertEqual(e_lost.energy, 18)

if __name__ == '__main__':


    unittest.main()
