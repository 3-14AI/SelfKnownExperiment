import unittest
from src.universe.engine import Universe, Entity

class TestTerritorialPredator(unittest.TestCase):
    def test_is_territorial_predator(self):
        universe = Universe(width=10, height=10)
        universe.mutation_chance = 0.0

        predator = Entity(name="pred", x=5, y=5, size=2, energy=100, max_age=50, age=5, diet='carnivore', attack=9, defense=5, is_territorial_predator=True)
        prey = Entity(name="prey", x=5, y=5, size=2, energy=2, max_age=50, age=5, diet='herbivore', attack=2, defense=10, is_territorial=True)

        universe.add_entity(predator)
        universe.add_entity(prey)

        import unittest.mock
        with unittest.mock.patch('random.random', return_value=0.5):
            universe.tick()

        self.assertNotIn(prey, universe.entities)

    def test_is_territorial_predator_mutation(self):
        universe = Universe(width=10, height=10)
        # Using self.mutation_chance is ignored by the reproduction logic, it uses 0.1.
        universe.event_chance = 0.0
        universe.localized_event_chance = 0.0
        universe.disease_chance = 0.0
        universe.reproduction_threshold = 100

        parent = Entity(name="parent", x=5, y=5, size=5, energy=5000, max_age=100, age=5, lays_eggs=False, is_ageless=True, is_immune=True, is_pacifist=True, is_gluttonous=True, has_blubber=True, is_territorial_predator=False)
        universe.add_entity(parent)

        import unittest.mock
        with unittest.mock.patch('random.random', return_value=0.05): # Less than 0.1
            universe.tick()

        children = [e for e in universe.entities if e is not parent]
        self.assertGreater(len(children), 0)
        self.assertTrue(getattr(children[0], 'is_territorial_predator', False))

if __name__ == '__main__':
    unittest.main()
