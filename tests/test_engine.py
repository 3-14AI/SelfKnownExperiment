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
        entity = Entity("Adam", energy=10)
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
        carnivore = Entity("Lion", x=0, y=0, diet='carnivore', energy=10)
        herbivore = Entity("Zebra", x=2, y=0, diet='herbivore', energy=10)
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

if __name__ == '__main__':
    unittest.main()
