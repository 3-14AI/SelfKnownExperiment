import unittest
from src.universe.engine import Universe, Entity, Food, Terrain
from src.universe.visualizer import CLIVisualizer

class TestCLIVisualizer(unittest.TestCase):
    def test_render_terrain(self):
        universe = Universe(width=3, height=3)
        universe.add_terrain(Terrain(x=0, y=0, terrain_type='wall'))
        universe.add_terrain(Terrain(x=2, y=2, terrain_type='water'))
        visualizer = CLIVisualizer(universe)
        expected_output = "#..\n...\n..~"
        self.assertEqual(visualizer.render(), expected_output)

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


    def test_render_carnivore(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestCarnivore", x=1, y=1, diet='carnivore'))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.C.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_infected(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestInfected", x=1, y=1, is_infected=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.S.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_aposematic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestApos", x=1, y=1, is_aposematic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.A.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_photosynthesize(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestPhoto", x=1, y=1, can_photosynthesize=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.P.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_hibernating(self):
        universe = Universe(width=3, height=3)
        entity = Entity("TestHiber", x=1, y=1, diet='carnivore', can_hibernate=True)
        entity.is_hibernating = True
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.c.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_level(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestLevel", x=1, y=1, diet='omnivore', level=3))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.O.\n..."
        self.assertEqual(visualizer.render(), expected_output)

if __name__ == '__main__':
    unittest.main()
