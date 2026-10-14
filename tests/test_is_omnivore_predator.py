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

        # Test 1: Normal attack against herbivore
        universe1 = Universe(width=10, height=10)
        universe1.event_chance = 0.0
        universe1.disease_chance = 0.0
        universe1.localized_event_chance = 0.0
        predator1 = Entity("Predator1", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_omnivore_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey_control = Entity("Prey2", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='herbivore', is_relentless=False, is_ageless=True, is_immune=True)
        universe1.add_entity(predator1)
        universe1.add_entity(prey_control)

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            universe1.tick()

        damage_control = 5000 - prey_control.energy

        # Test 2: Boosted attack against omnivore
        universe2 = Universe(width=10, height=10)
        universe2.event_chance = 0.0
        universe2.disease_chance = 0.0
        universe2.localized_event_chance = 0.0
        predator2 = Entity("Predator2", x=1, y=1, energy=5000, max_age=500, age=5, size=10, attack=40, defense=10, diet='carnivore', is_omnivore_predator=True, is_relentless=True, is_ageless=True, is_immune=True)
        prey = Entity("Prey1", x=1, y=1, energy=5000, max_age=500, age=5, size=100, attack=5, defense=50, diet='omnivore', is_relentless=False, is_ageless=True, is_immune=True)
        universe2.add_entity(predator2)
        universe2.add_entity(prey)

        with unittest.mock.patch('src.universe.engine.random.random', return_value=0.0):
            universe2.tick()

        damage_omni = 5000 - prey.energy

        self.assertGreater(damage_omni, damage_control, "is_omnivore_predator should deal more damage to omnivore prey")
