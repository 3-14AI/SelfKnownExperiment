import unittest
from src.universe.engine import Universe, Entity

class TestUniverse(unittest.TestCase):
    def test_initial_state(self):
        universe = Universe()
        self.assertEqual(universe.time, 0)
        self.assertEqual(universe.entities, [])

    def test_add_entity(self):
        universe = Universe()
        entity = Entity("Adam")
        universe.add_entity(entity)
        self.assertEqual(len(universe.entities), 1)
        self.assertEqual(universe.entities[0], entity)

    def test_tick(self):
        universe = Universe()
        universe.tick()
        self.assertEqual(universe.time, 1)

if __name__ == '__main__':
    unittest.main()
