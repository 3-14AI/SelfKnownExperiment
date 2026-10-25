import unittest
from src.universe.engine import Entity, Universe
from src.universe.visualizer import CLIVisualizer
import random
from unittest.mock import patch

class TestHasBioluminescencePredator(unittest.TestCase):
    def test_has_bioluminescence_predator(self):
        universe = Universe(width=10, height=10)
        universe.reproduction_threshold = 100000

        predator = Entity(name="predator", x=0, y=0, energy=50, diet="carnivore", has_bioluminescence_predator=True, max_age=100)
        predator.age = 100
        predator.is_ageless = True
        predator.attack = 20
        universe.add_entity(predator)

        prey = Entity(name="prey", x=1, y=0, energy=50, has_bioluminescence=True, max_age=100)
        prey.age = 100
        prey.is_ageless = True
        prey.defense = 20
        universe.add_entity(prey)

        # Baseline: defense = 20, attack = 20. Escape chance without multiplier = 0.5.
        # With multiplier: effective_attack = 30. Escape chance = min(0.9, max(0.1, 20 / (20 + 30))) = 0.4.

        # Test 1: Random value between 0.4 and 0.5. Prey survives if no multiplier, eaten if multiplier.
        # Since multiplier is applied, escape chance is 0.4. If rand is 0.45, rand < escape_chance is False -> Prey eaten.
        with patch('random.random', return_value=0.45):
            universe.tick()

        self.assertFalse(prey.is_alive)
        self.assertTrue(predator.energy >= 50)

    def test_has_bioluminescence_predator_visualizer(self):
        universe = Universe(10, 10)
        entity = Entity("L-predator", x=0, y=0, energy=100)
        entity.has_bioluminescence_predator = True
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('L', output)

if __name__ == "__main__":
    unittest.main()
