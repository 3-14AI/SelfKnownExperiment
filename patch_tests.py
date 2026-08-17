import re

test_code = """
class TestIsTracker(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)

    def test_is_tracker_scent_detection(self):
        # Create an entity with is_tracker=True, stamina=50 to allow movement
        entity = Entity(name="tracker", x=5, y=5, is_tracker=True, stamina=50, max_stamina=50, energy=100)
        self.universe.entities.append(entity)

        # Place a strong scent trail at distance 2 (7, 5)
        self.universe.scent_trails[(7, 5)] = 20

        # Also put a weak scent at distance 1 to ensure it prefers the strong one
        self.universe.scent_trails[(6, 5)] = 5

        # It should move towards (7, 5) which means taking a step in (1, 0) direction
        self.universe.tick()

        self.assertEqual(entity.x, 6)
        self.assertEqual(entity.y, 5)

    def test_is_tracker_mutation(self):
        parent = Entity(name="parent", x=1, y=1, energy=100, max_energy=100, size=2, age=5, max_age=10)
        # Ensure it has enough energy to reproduce
        self.universe.entities.append(parent)

        original_random = random.random
        try:
            # Force mutation chance to succeed
            random.random = lambda: 0.0

            # Since random is 0.0, it will mutate the boolean trait from False to True.
            self.universe.tick()

            children = [e for e in self.universe.entities if e != parent]
            if children:
                child = children[0]
                self.assertTrue(getattr(child, 'is_tracker', False))
        finally:
            random.random = original_random
"""

with open('tests/test_engine.py', 'r') as f:
    content = f.read()

# Insert before if __name__ == '__main__':
content = content.replace("if __name__ == '__main__':", test_code + "\nif __name__ == '__main__':")

with open('tests/test_engine.py', 'w') as f:
    f.write(content)
