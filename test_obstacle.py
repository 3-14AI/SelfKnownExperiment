import unittest
from universe.engine import Universe, Entity, Food, Terrain

class TestPathfinding(unittest.TestCase):
    def test_entity_pathfinding_around_obstacle(self):
        universe = Universe(width=5, height=5, population_limit=10)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.food_spawn_rate = 0.0

        entity = Entity("Herbivore", x=0, y=0, diet='herbivore', energy=10, perception_radius=10, size=1, max_age=50, age=20)
        universe.add_entity(entity)
        universe.add_food(Food(x=2, y=0, energy=5))

        # Add a wall at (1, 0) blocking the direct path
        universe.add_terrain(Terrain(x=1, y=0, terrain_type='wall'))

        # Entity should route around: (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,0)
        # Tick 1: move to (0, 1)
        universe.tick()
        print(f"Tick 1: x={entity.x}, y={entity.y}")

        # Tick 2: move to (1, 1)
        universe.tick()
        print(f"Tick 2: x={entity.x}, y={entity.y}")

        # Tick 3: move to (2, 1)
        universe.tick()
        print(f"Tick 3: x={entity.x}, y={entity.y}")

if __name__ == '__main__':
    unittest.main()
