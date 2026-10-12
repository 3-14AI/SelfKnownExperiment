import unittest
from src.universe.engine import Universe, Entity, Food, Terrain, LocalizedEvent, Quicksand

class TestIsOmnivorePredator(unittest.TestCase):
    def test_is_omnivore_predator_mutation(self):
        import unittest.mock
        universe = Universe(width=10, height=10)
        parent = Entity(name="Parent", x=1, y=1, energy=1000, age=5, size=20, is_omnivore_predator=False, lays_eggs=False, is_ageless=True, is_immune=True, is_pacifist=True, is_gluttonous=True, has_blubber=True)
        universe.add_entity(parent)

        universe.mutation_chance = 1.0
        universe.reproduction_threshold = 100
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.localized_event_chance = 0.0

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            universe.tick()

        child = None
        for e in universe.entities:
            if e != parent:
                child = e
                break

        self.assertIsNotNone(child)
        self.assertTrue(getattr(child, 'is_omnivore_predator', False))

    def test_is_omnivore_predator_combat(self):
        import unittest.mock
        universe = Universe(width=10, height=10)

        # Predator with omnivore predator trait
        predator = Entity("Predator", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_omnivore_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        # Prey that is omnivore
        prey = Entity("Prey1", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='omnivore', is_relentless=False, is_ageless=True, is_immune=True)

        # Control Prey that is herbivore
        prey_control = Entity("Prey2", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='herbivore', is_relentless=False, is_ageless=True, is_immune=True)

        universe.add_entity(predator)
        universe.add_entity(prey)
        universe.add_entity(prey_control)

        # Base effective attack is 40. For prey, multiplier is 1.5, so attack 60. Defense 50.
        # Relentless deals damage even on escape. Wait, we mock escape to 0.0 so it fails to escape?
        # If random=0.0, escape succeeds because 0.0 < escape_chance. Damage is effective_attack / 2.
        # For prey (omnivore): 60 / 2 = 30 damage.
        # For prey_control (herbivore): 40 / 2 = 20 damage.

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            universe.tick()

        # Prey should have taken more damage than prey_control
        self.assertLess(prey.energy, prey_control.energy, "is_omnivore_predator should deal more damage to omnivore prey")

if __name__ == '__main__':
    unittest.main()
