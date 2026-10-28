import unittest
from unittest.mock import patch
from src.universe.engine import Universe, Entity

class TestIsTrackerPredator(unittest.TestCase):
    def test_combat_multiplier(self):
        universe = Universe(width=10, height=10)
        predator = Entity(name='Pred', x=0, y=0, size=2, energy=20, is_tracker_predator=True)
        predator.diet = 'carnivore'
        prey = Entity(name='Prey', x=0, y=0, size=1, energy=10, defense=5, is_tracker=True)
        universe.add_entity(predator)
        universe.add_entity(prey)

        # effective_defense = 5
        # without multiplier: effective_attack = 5
        # total = 10, escape = 5/10 = 0.5
        # with multiplier (1.5x): effective_attack = 7.5
        # total = 12.5, escape = 5/12.5 = 0.4
        predator.attack = 5

        # Mock random so that 0.45 causes escape without multiplier (0.45 < 0.5), but catch with multiplier (0.45 >= 0.4)
        with patch('random.random', return_value=0.45):
            universe.tick()

        self.assertFalse(prey.is_alive)

    def test_mutation(self):
        universe = Universe(width=10, height=10)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.localized_event_chance = 0.0

        parent = Entity(name='Parent', x=0, y=0, size=2, energy=100, is_tracker_predator=False, lays_eggs=False, is_parasitic=False, is_vampiric=False)
        parent.reproduction_threshold = 50
        parent.reproduction_cost = 20
        universe.add_entity(parent)

        with patch('random.random', return_value=0.01):
            universe.tick()

        children = [e for e in universe.entities if e is not parent]
        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(child, 'is_tracker_predator', False) for child in children))

if __name__ == '__main__':
    unittest.main()
