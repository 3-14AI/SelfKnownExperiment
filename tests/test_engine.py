import unittest
from src.universe.engine import Universe, Entity

class TestUniverse(unittest.TestCase):
    def test_initial_state(self):
        universe = Universe()
        self.assertEqual(universe.time, 0)
        self.assertEqual(universe.entities, [])
        self.assertEqual(universe.width, 100)
        self.assertEqual(universe.height, 100)

    def test_add_entity(self):
        universe = Universe()
        entity = Entity("Adam")
        universe.add_entity(entity)
        self.assertEqual(len(universe.entities), 1)
        self.assertEqual(universe.entities[0], entity)
        self.assertEqual(entity.x, 0)
        self.assertEqual(entity.y, 0)

    def test_add_entity_custom_position(self):
        universe = Universe()
        entity = Entity("Eve")
        universe.add_entity(entity, x=10, y=20)
        self.assertEqual(entity.x, 10)
        self.assertEqual(entity.y, 20)

    def test_add_entity_out_of_bounds(self):
        universe = Universe()
        entity = Entity("Lilith")
        with self.assertRaises(ValueError):
            universe.add_entity(entity, x=100, y=10)
        with self.assertRaises(ValueError):
            universe.add_entity(entity, x=10, y=-1)

    def test_move_entity_valid(self):
        universe = Universe()
        entity = Entity("Adam")
        universe.add_entity(entity)
        universe.move_entity(entity, 5, 5)
        self.assertEqual(entity.x, 5)
        self.assertEqual(entity.y, 5)
        universe.move_entity(entity, -2, 3)
        self.assertEqual(entity.x, 3)
        self.assertEqual(entity.y, 8)

    def test_move_entity_invalid(self):
        universe = Universe(width=10, height=10)
        entity = Entity("Adam", x=5, y=5)
        universe.add_entity(entity)
        with self.assertRaises(ValueError):
            universe.move_entity(entity, 5, 0)  # new x = 10 (out of bounds)
        with self.assertRaises(ValueError):
            universe.move_entity(entity, 0, -6) # new y = -1 (out of bounds)
        # Verify position hasn't changed
        self.assertEqual(entity.x, 5)
        self.assertEqual(entity.y, 5)

    def test_get_entities_at(self):
        universe = Universe()
        e1 = Entity("E1", x=10, y=10)
        e2 = Entity("E2", x=10, y=10)
        e3 = Entity("E3", x=10, y=11)
        universe.add_entity(e1)
        universe.add_entity(e2)
        universe.add_entity(e3)

        at_10_10 = universe.get_entities_at(10, 10)
        self.assertEqual(len(at_10_10), 2)
        self.assertIn(e1, at_10_10)
        self.assertIn(e2, at_10_10)

        at_10_11 = universe.get_entities_at(10, 11)
        self.assertEqual(len(at_10_11), 1)
        self.assertEqual(at_10_11[0], e3)

        at_0_0 = universe.get_entities_at(0, 0)
        self.assertEqual(len(at_0_0), 0)

    def test_tick(self):
        universe = Universe()
        universe.tick()
        self.assertEqual(universe.time, 1)

    def test_entity_energy_default(self):
        entity = Entity("Adam")
        self.assertEqual(entity.energy, 10)

    def test_tick_consumes_energy(self):
        universe = Universe()
        entity = Entity("Adam", energy=10)
        universe.add_entity(entity)
        universe.tick()
        self.assertEqual(entity.energy, 9)
        self.assertEqual(len(universe.entities), 1)

    def test_entity_dies_on_zero_energy(self):
        universe = Universe()
        entity = Entity("Adam", energy=1)
        universe.add_entity(entity)
        universe.tick()
        self.assertEqual(entity.energy, 0)
        self.assertEqual(len(universe.entities), 0)

if __name__ == '__main__':
    unittest.main()
