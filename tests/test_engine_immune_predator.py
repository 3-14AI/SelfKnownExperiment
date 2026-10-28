import unittest
from unittest.mock import patch
from src.universe.engine import Entity, Universe

class TestIsImmunePredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.disease_chance = 0.0
        self.universe.localized_event_chance = 0.0

    @patch('random.random')
    def test_is_immune_predator_combat(self, mock_random):
        # We need a predator and a prey.
        # The predator should have is_immune_predator=True.
        # The prey should have is_immune=True.

        predator = Entity(name="predator", size=2, energy=20)
        predator.is_immune_predator = True
        predator.attack = 10
        predator.diet = 'carnivore'

        prey = Entity(name="prey", size=1, energy=10)
        prey.is_immune = True
        prey.defense = 10 # predator attack == prey defense -> control escape chance is 0.5

        # Test: With multiplier, effective_attack = 10 * 1.5 = 15.
        # Modified escape chance = defense / (effective_attack + defense) = 10 / 25 = 0.4.

        # Mock random to 0.45.
        # In control (no multiplier), 0.45 < 0.5 -> escapes.
        # In test (multiplier), 0.45 >= 0.4 -> fails to escape, eaten.

        mock_random.return_value = 0.45

        # We test both logic branches if possible, but actually Universe.tick() handles combat in multiple places.
        # The easiest is to just place them together and tick.
        predator.x, predator.y = 1, 1
        prey.x, prey.y = 1, 1

        self.universe.entities.append(predator)
        self.universe.entities.append(prey)

        self.universe.tick()

        self.assertFalse(prey.is_alive)
        self.assertNotIn(prey, self.universe.entities)

    @patch('random.random')
    def test_is_immune_predator_no_multiplier(self, mock_random):
        predator = Entity(name="predator", size=2, energy=20)
        predator.is_immune_predator = True
        predator.attack = 10
        predator.diet = 'carnivore'

        prey = Entity(name="prey", size=1, energy=10)
        prey.is_immune = False
        prey.defense = 10 # control escape chance is 0.5

        mock_random.return_value = 0.45

        predator.x, predator.y = 1, 1
        prey.x, prey.y = 1, 1

        self.universe.entities.append(predator)
        self.universe.entities.append(prey)

        self.universe.tick()

        # Prey should escape because no multiplier is applied.
        self.assertTrue(prey.is_alive)
        self.assertIn(prey, self.universe.entities)

    def test_is_immune_predator_mutation(self):
        parent = Entity(name="parent", size=5, energy=30, intelligence=10)
        parent.is_immune_predator = False
        self.universe.reproduction_threshold = 10
        self.universe.reproduction_cost = 5
        self.universe.entities.append(parent)

        # Force a child birth.
        with patch('random.random', return_value=0.0):
            parent.energy = 50
            self.universe.tick()

        children = [e for e in self.universe.entities if e is not parent]
        self.assertGreater(len(children), 0, 'A child should have been born')

        # We can test mutation by creating a child with forced mutation using patch
        with patch('random.random', return_value=0.0): # Force mutation (<0.05)
            parent.energy = 50
            self.universe.tick()

            children = [e for e in self.universe.entities if e is not parent]
            # one of the children should have the trait
            found_mutated = False
            for child in children:
                if getattr(child, 'is_immune_predator', False):
                    found_mutated = True
            self.assertTrue(found_mutated, "Mutation to is_immune_predator should occur")

if __name__ == '__main__':
    unittest.main()
