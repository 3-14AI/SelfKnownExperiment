import unittest
from src.universe.engine import Universe, Entity, Food, Terrain, LocalizedEvent, Quicksand
import unittest.mock

class TestIsScavengerPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    def test_is_scavenger_predator_mutation(self):
        parent = Entity(name="Parent", x=1, y=1, energy=1000, age=5, size=20, is_scavenger_predator=False, lays_eggs=False, is_ageless=True, is_immune=True, is_pacifist=True, is_gluttonous=True, has_blubber=True)
        self.universe.add_entity(parent)

        self.universe.mutation_chance = 1.0
        self.universe.reproduction_threshold = 100
        parent.energy = 1000
        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            self.universe.tick()
        child = None
        for e in self.universe.entities:
            if e != parent:
                child = e
                break
        self.assertIsNotNone(child)
        self.assertTrue(getattr(child, 'is_scavenger_predator', False))

    def test_is_scavenger_predator_combat_with_diet(self):
        predator = Entity("Predator", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_scavenger_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey = Entity("Prey", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='scavenger', is_relentless=False, is_ageless=True, is_immune=True)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        # Base effective attack is 40. Multiplier is 1.5. So 60.
        # Defense is 50. Wait, diet='scavenger' doesn't exist, wait, diet can be anything if custom or 'herbivore'/'carnivore'/'omnivore'.
        # We can also test the trait: is_scavenger=True

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            self.universe.tick()

        self.assertLess(prey.energy, 4980)

    def test_is_scavenger_predator_combat_with_trait(self):
        predator = Entity("Predator", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_scavenger_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey = Entity("Prey", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='herbivore', is_scavenger=True, is_relentless=False, is_ageless=True, is_immune=True)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            self.universe.tick()

        self.assertLess(prey.energy, 4980)
