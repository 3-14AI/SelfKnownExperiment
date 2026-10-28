import unittest
from unittest.mock import patch
from src.universe.engine import Entity, Universe
from src.universe.visualizer import CLIVisualizer

class TestIsEmpathicPredator(unittest.TestCase):
    def test_combat_multiplier(self):
        universe = Universe(width=10, height=10)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.localized_event_chance = 0.0

        predator = Entity(name='Pred', x=0, y=0, size=2, energy=20, is_empathic_predator=True)
        predator.diet = 'carnivore'
        predator.attack = 20
        prey = Entity(name='Prey', x=0, y=0, size=1, energy=10, is_empathic=True)
        prey.defense = 20

        universe.add_entity(predator)
        universe.add_entity(prey)

        with patch('random.random', return_value=0.45):
            universe.tick()

        self.assertFalse(prey.is_alive)

    def test_mutation(self):
        universe = Universe(width=10, height=10)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.localized_event_chance = 0.0

        parent = Entity(name='Parent', x=0, y=0, size=2, energy=100, is_empathic_predator=False, lays_eggs=False, is_parasitic=False, is_vampiric=False)
        parent.reproduction_threshold = 10
        universe.add_entity(parent)
        universe.mutation_chance = 1.0

        with patch('random.random', return_value=0.0): # force mutation
            universe.tick()

        children = [e for e in universe.entities if e is not parent]
        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(child, 'is_empathic_predator', False) for child in children))

    @patch('os.system')
    def test_visualizer(self, mock_os):
        universe = Universe(width=10, height=10)
        entity = Entity(name='Pred', x=0, y=0, size=2, energy=20, is_empathic_predator=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('ē', output)

if __name__ == '__main__':
    unittest.main()
