import unittest
from src.universe.engine import Universe, Entity, Food
from src.universe.visualizer import CLIVisualizer

class TestCLIVisualizer(unittest.TestCase):
    def test_render_empty(self):
        universe = Universe(width=3, height=3)
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n...\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_food(self):
        universe = Universe(width=3, height=3)
        universe.add_food(Food(x=1, y=1))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.f.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=2, y=0))
        visualizer = CLIVisualizer(universe)
        expected_output = "..E\n...\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity_and_food(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=0, y=0))
        universe.add_food(Food(x=2, y=2))
        visualizer = CLIVisualizer(universe)
        expected_output = "E..\n...\n..f"
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity_on_food(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=1, y=1))
        universe.add_food(Food(x=1, y=1))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.E.\n..."
        self.assertEqual(visualizer.render(), expected_output)

if __name__ == '__main__':
    unittest.main()
