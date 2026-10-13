import unittest
from src.universe.engine import Universe, Entity
import unittest.mock

class TestIsAmphibiousPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    def test_is_amphibious_predator_mutation(self):
        parent = Entity(name="Parent", x=1, y=1, energy=1000, age=5, size=20, is_amphibious_predator=False, lays_eggs=False, is_ageless=True, is_immune=True, is_pacifist=True, is_gluttonous=True, has_blubber=True)
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
        self.assertTrue(getattr(child, 'is_amphibious_predator', False))

    def test_is_amphibious_predator_combat(self):
        predator = Entity("Predator", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_amphibious_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey = Entity("Prey", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, is_amphibious=True, is_relentless=False, is_ageless=True, is_immune=True)
        prey_control = Entity("PreyControl", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, is_amphibious=False, is_relentless=False, is_ageless=True, is_immune=True)

        self.universe.add_entity(predator)
        self.universe.add_entity(prey)
        self.universe.add_entity(prey_control)

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            self.universe.tick()

        self.assertLess(prey.energy, prey_control.energy, "is_amphibious_predator should deal more damage to amphibious prey")
        self.assertGreater(prey.energy, 0, "Prey should still be alive")
        self.assertGreater(prey_control.energy, 0, "Control prey should still be alive")

if __name__ == '__main__':
    unittest.main()
