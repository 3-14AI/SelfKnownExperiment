import unittest
from src.universe.engine import Universe, Entity

class TestSturdySlipperyPredator(unittest.TestCase):
    def test_sturdy_predator_attack_multiplier(self):
        universe = Universe(width=10, height=10)
        # Prey with is_sturdy
        prey = Entity(name="prey", x=5, y=5, size=2, age=5, is_sturdy=True, defense=10)
        prey.energy = 5000
        # Predator with is_sturdy_predator and carnivore diet
        predator = Entity(name="pred", x=5, y=5, size=2, age=5, is_sturdy_predator=True, diet='carnivore', attack=9)
        predator.energy = 100

        universe.add_entity(prey)
        universe.add_entity(predator)

        initial_prey_energy = prey.energy
        universe.tick()

        # Effective attack should be 9 * 1.5 = 13.5
        # It deals damage since 13.5 > 10 (defense)
        self.assertLess(prey.energy, initial_prey_energy)

    def test_slippery_predator_attack_multiplier(self):
        universe = Universe(width=10, height=10)
        # Prey with is_slippery
        prey = Entity(name="prey", x=5, y=5, size=2, age=5, is_slippery=True, defense=10)
        prey.energy = 5000
        # Predator with is_slippery_predator and carnivore diet
        predator = Entity(name="pred", x=5, y=5, size=2, age=5, is_slippery_predator=True, diet='carnivore', attack=9)
        predator.energy = 100

        universe.add_entity(prey)
        universe.add_entity(predator)

        initial_prey_energy = prey.energy
        universe.tick()

        # Effective attack should be 9 * 1.5 = 13.5
        # It deals damage since 13.5 > 10 (defense)
        self.assertLess(prey.energy, initial_prey_energy)

class TestVisualizerSturdySlippery(unittest.TestCase):
    def test_visualizer_sturdy_predator(self):
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        entity = Entity(name="pred", x=5, y=5, size=1, age=5, is_sturdy_predator=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('☗', output)

    def test_visualizer_slippery_predator(self):
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        entity = Entity(name="pred", x=5, y=5, size=1, age=5, is_slippery_predator=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('∿', output)
