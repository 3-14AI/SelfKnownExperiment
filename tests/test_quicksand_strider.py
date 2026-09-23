import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from universe.engine import Universe, Entity, Terrain, LocalizedEvent

class TestQuicksandStrider(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)

    def test_quicksand_strider_stamina_cost(self):
        # Create quicksand manually
        # In universe/engine.py, quicksands is a list of instances that just have x and y
        class QuicksandMock:
            def __init__(self, x, y):
                self.x = x
                self.y = y
        self.universe.quicksands = [QuicksandMock(6, 5)]

        # Entity without trait
        entity1 = Entity(name="Entity1", x=5, y=5, is_quicksand_strider=False, stamina=50, max_stamina=50)
        self.universe.entities.append(entity1)

        # Entity with trait
        entity2 = Entity(name="Entity2", x=5, y=5, is_quicksand_strider=True, stamina=50, max_stamina=50)
        self.universe.entities.append(entity2)

        # Move them inside quicksand (moving to 6, 5)
        self.universe.move_entity(entity1, 1, 0)
        self.universe.move_entity(entity2, 1, 0)

        self.assertLess(entity1.stamina, 50)
        self.assertEqual(entity2.stamina, 50)

    def test_quicksand_strider_mutation(self):
        parent = Entity(name="Parent", x=5, y=5, energy=1000, size=20, is_ageless=True, is_immune=True, is_pacifist=True, is_quicksand_strider=False, age=5, is_gluttonous=True, has_blubber=True)
        self.universe.entities.append(parent)
        self.universe.reproduction_threshold = 500
        self.universe.mutation_chance = 1.0 # Guarantee mutation

        self.universe.event_chance = 0.0
        self.universe.disease_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.foods = []

        for _ in range(100):
            if len(self.universe.entities) > 20:
                self.universe.entities = [parent]
            self.universe.tick()
            parent.energy = 1000

            for entity in self.universe.entities:
                if entity.is_quicksand_strider:
                    return # Mutation found

        self.fail("Mutation for is_quicksand_strider did not occur")

if __name__ == '__main__':
    unittest.main()
