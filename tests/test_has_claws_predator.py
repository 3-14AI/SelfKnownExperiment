import unittest
from unittest.mock import patch
from src.universe.engine import Universe, Entity

class TestHasClawsPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.food_spawn_rate = 0.0
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    @patch('random.random')
    def test_has_claws_predator_combat_multiplier(self, mock_random):
        mock_random.return_value = 0.30

        predator1 = Entity(name="predator1", x=5, y=5, size=30, max_age=100)
        predator1.age = 100
        predator1.is_ageless = True
        predator1.energy = 50
        predator1.diet = 'carnivore'
        predator1.attack = 20

        prey1 = Entity(name="prey1", x=5, y=5, size=15, max_age=100)
        prey1.age = 100
        prey1.is_ageless = True
        prey1.energy = 50
        prey1.defense = 10
        prey1.has_claws = True

        self.universe.add_entity(predator1)
        self.universe.add_entity(prey1)

        self.universe.tick()

        # prey1 should survive as no predator trait
        self.assertTrue(prey1 in self.universe.entities)

        self.universe.entities = []

        predator2 = Entity(name="predator2", x=5, y=5, size=30, max_age=100, has_claws_predator=True)
        predator2.age = 100
        predator2.is_ageless = True
        predator2.energy = 50
        predator2.diet = 'carnivore'
        predator2.attack = 20

        prey2 = Entity(name="prey2", x=5, y=5, size=15, max_age=100)
        prey2.age = 100
        prey2.is_ageless = True
        prey2.energy = 50
        prey2.defense = 10
        prey2.has_claws = True

        self.universe.add_entity(predator2)
        self.universe.add_entity(prey2)

        self.universe.tick()

        # prey2 should be eaten due to predator trait giving higher attack
        self.assertFalse(prey2 in self.universe.entities)

    @patch('os.system')
    def test_has_claws_predator_visualizer(self, mock_system):
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(self.universe)
        entity = Entity(name="predator", x=2, y=2, has_claws_predator=True)
        entity.energy = 50
        self.universe.add_entity(entity)

        output = visualizer.render()
        self.assertIn('C', output)

if __name__ == '__main__':
    unittest.main()
