import unittest
import random
from unittest.mock import patch
from src.universe.engine import Entity, Universe

class TestResilientPredator(unittest.TestCase):
    @patch('random.random')
    def test_is_resilient_predator_combat_modifier(self, mock_random):
        # Prevent escape: return 0.5 (which should be > escape_chance ~ 0.2)
        mock_random.return_value = 0.5

        universe = Universe(width=10, height=10)
        universe.reproduction_threshold = 10000

        predator = Entity(
            name="resilient_predator",
            x=5, y=5,
            energy=2000,
            size=50,
            age=5, max_age=100,
            diet="carnivore",
            is_resilient_predator=True,
            is_immune=True, is_ageless=True, lays_eggs=False, is_pacifist=False,
            is_gluttonous=True, has_blubber=True
        )
        predator.attack = 9 # Will be 12 against resilient prey

        prey_resilient = Entity(
            name="resilient_prey",
            x=5, y=5,
            energy=2000,
            size=50,
            age=5, max_age=100,
            is_resilient=True,
            is_immune=True, is_ageless=True, lays_eggs=False, is_pacifist=False,
            is_gluttonous=True, has_blubber=True
        )
        prey_resilient.defense = 10

        universe.entities = [predator, prey_resilient]
        print("Distance: ", abs(predator.x - prey_resilient.x) + abs(predator.y - prey_resilient.y))

        # Act
        universe.tick()

        # Resilient predator (8 * 1.5 = 12 attack) vs Resilient prey (10 defense)
        # Should win combat, predator energy increases, prey dies
        print([(e.name, e.energy, getattr(e, 'was_eaten', False)) for e in universe.entities])

        self.assertNotIn(prey_resilient, universe.entities)

        # Test normal prey
        universe2 = Universe(width=10, height=10)
        universe2.reproduction_threshold = 10000

        predator2 = Entity(
            name="resilient_predator2",
            x=5, y=5,
            energy=2000,
            size=50,
            age=5, max_age=100,
            diet="carnivore",
            is_resilient_predator=True,
            is_immune=True, is_ageless=True, lays_eggs=False, is_pacifist=False,
            is_gluttonous=True, has_blubber=True
        )
        predator2.attack = 9

        prey_normal = Entity(
            name="normal_prey",
            x=5, y=5,
            energy=2000,
            size=50,
            age=5, max_age=100,
            is_resilient=False,
            is_immune=True, is_ageless=True, lays_eggs=False, is_pacifist=False,
            is_gluttonous=True, has_blubber=True
        )
        prey_normal.defense = 10

        universe2.entities = [predator2, prey_normal]

        # Act
        universe2.tick()

        # Resilient predator (8 attack) vs Normal prey (10 defense)
        # Predator loses
        print([(e.name, e.energy, getattr(e, 'was_eaten', False)) for e in universe.entities])

        self.assertIn(prey_normal, universe2.entities)

if __name__ == '__main__':
    unittest.main()
