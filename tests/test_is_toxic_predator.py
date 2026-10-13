import unittest
from src.universe.engine import Universe, Entity, Food, Terrain, LocalizedEvent, Quicksand
import unittest.mock

class TestIsToxicPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    def test_is_toxic_predator_mutation(self):
        parent = Entity(name="Parent", x=1, y=1, energy=1000, age=5, size=20, is_toxic_predator=False, lays_eggs=False, is_ageless=True, is_immune=True, is_pacifist=True, is_gluttonous=True, has_blubber=True)
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
        self.assertTrue(getattr(child, 'is_toxic_predator', False))

    def test_is_toxic_predator_combat(self):
        predator = Entity("Predator", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_toxic_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey = Entity("Prey", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, is_toxic=True, is_relentless=False, is_ageless=True, is_immune=True)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        # Base effective attack is 40. Multiplier is 1.5. So 60.
        # Relentless deals damage even on escape. Escape chance is 0.0 mock so escape succeeds (0.0 < escape_chance).
        # Damage is 60 / 2 = 30.

        # Test without is_toxic
        prey_control = Entity("PreyControl", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, is_toxic=False, is_relentless=False, is_ageless=True, is_immune=True)
        self.universe.add_entity(prey_control)

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            self.universe.tick()

        # Predator attacks both.
        # Prey should have taken more damage than prey_control
        self.assertLess(prey.energy, prey_control.energy, "is_toxic_predator should deal more damage to toxic prey")

if __name__ == '__main__':
    unittest.main()
