import unittest
import random
from unittest.mock import patch
from src.universe.engine import Universe, Entity

class TestIsTirelessPredator(unittest.TestCase):
    @patch('random.random', return_value=0.5)
    def test_is_tireless_predator_attack_multiplier(self, mock_random):
        universe = Universe(width=10, height=10)

        predator = Entity(
            name="predator",
            x=5, y=5,
            age=5,
            size=5,
            energy=1000,
            attack=40,
            diet="carnivore",
            is_tireless_predator=True
        )

        prey_tireless = Entity(
            name="prey_tireless",
            x=5, y=5,
            age=5,
            size=5,
            energy=100,
            defense=50,
            is_tireless=True,
            diet="herbivore"
        )

        universe.entities = [predator, prey_tireless]

        universe.tick()
        universe.tick()
        universe.tick()

        self.assertNotIn(prey_tireless, universe.entities, "The tireless predator should have killed the tireless prey due to the attack multiplier.")

        universe2 = Universe(width=10, height=10)
        predator2 = Entity(
            name="predator",
            x=5, y=5,
            age=5,
            size=5,
            energy=1000,
            attack=40,
            diet="carnivore",
            is_tireless_predator=True
        )

        prey_normal = Entity(
            name="prey_normal",
            x=5, y=5,
            age=5,
            size=5,
            energy=100,
            defense=50,
            is_tireless=False,
            diet="herbivore"
        )

        universe2.entities = [predator2, prey_normal]

        universe2.tick()
        universe2.tick()
        universe2.tick()

        self.assertIn(prey_normal, universe2.entities, "The tireless predator should NOT have killed the normal prey because the attack was lower than defense.")

if __name__ == '__main__':
    unittest.main()
