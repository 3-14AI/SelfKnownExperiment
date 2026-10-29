import unittest
from src.universe.engine import Universe, Entity
from unittest.mock import patch

class TestIsColdBloodedPredator(unittest.TestCase):
    def test_is_cold_blooded_predator_combat(self):
        universe = Universe(width=10, height=10)

        predator = Entity(name='test', x=5, y=5, energy=8, size=1, diet='carnivore', is_cold_blooded_predator=True)
        predator.reproduction_threshold = 99999
        predator.attack = 10

        prey = Entity(name='prey', x=5, y=5, energy=8, size=1, is_cold_blooded=True)
        prey.reproduction_threshold = 99999
        prey.defense = 0

        universe.entities.extend([predator, prey])

        with patch('src.universe.engine.random.random', return_value=0.5):
            universe.tick()

        # Base attack is 10, with a 1.5 multiplier -> 15 attack.
        # Defense is 0. Base damage is max(0, 15 - 0) = 15. Energy drain = 15 // 2 = 7
        # Prey should have 8 - 7 - 0.1 (tick loss) = ~0 or 1, and eventually die.
        # But actually 8 energy prey might die immediately if damage is enough.
        # 15 // 2 = 7 damage. 8 - 7 = 1 energy. Wait, base damage is 15. 15 // 2 = 7.
        self.assertEqual(prey.energy, 0, "Prey should take increased damage from cold blooded predator")

    def test_is_cold_blooded_predator_mutation(self):
        universe = Universe(width=10, height=10)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.localized_event_chance = 0.0

        parent = Entity(name='parent', x=5, y=5, energy=100, is_cold_blooded_predator=False)
        parent.reproduction_threshold = 80
        universe.entities.append(parent)

        with patch('src.universe.engine.random.random', return_value=0.0):
            universe.tick()

        children = [e for e in universe.entities if e is not parent]
        self.assertGreater(len(children), 0, "A child should have been born")
        child = children[0]

        self.assertTrue(getattr(child, 'is_cold_blooded_predator', False), "is_cold_blooded_predator trait should mutate to True")

if __name__ == '__main__':
    unittest.main()
