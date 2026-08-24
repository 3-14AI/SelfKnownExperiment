import re

with open('tests/test_engine.py', 'r') as f:
    text = f.read()

new_test = """
class TestIsDeepWaterGlider(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.entities = []
        self.universe.terrains = []
        self.universe.foods = []

    def test_stamina_cost_deep_water_glider_on_deep_water(self):
        e = Entity(name="e", x=0, y=0, max_stamina=100, stamina=100, is_deep_water_glider=True, is_aquatic=True)
        self.universe.entities.append(e)
        self.universe.add_terrain(Terrain(x=1, y=0, terrain_type='deep-water'))
        self.universe.move_entity(e, 1, 0)
        self.assertEqual(e.stamina, 100)

    def test_stamina_cost_deep_water_glider_off_deep_water(self):
        e = Entity(name="e", x=0, y=0, max_stamina=100, stamina=100, is_deep_water_glider=True, is_aquatic=True)
        self.universe.entities.append(e)
        self.universe.add_terrain(Terrain(x=1, y=0, terrain_type='water'))
        self.universe.move_entity(e, 1, 0)
        self.assertLess(e.stamina, 100)

    @mock.patch('random.random')
    def test_mutation_is_deep_water_glider(self, mock_random):
        mock_random.return_value = 0.01  # guarantee mutation

        parent = Entity(name="parent", x=2, y=2, energy=100, size=1, age=20, is_deep_water_glider=False)
        self.universe.entities = [parent]
        self.universe.reproduction_threshold = 10
        self.universe.reproduction_cost = 5
        self.universe.mutation_chance = 1.0

        self.universe.time = 0
        self.universe.tick()

        children = [e for e in self.universe.entities if e is not parent]
        if children:
            child = children[0]
            self.assertTrue(child.is_deep_water_glider)

"""

# Insert before if __name__ == '__main__':
if "if __name__ == '__main__':" in text:
    text = text.replace("if __name__ == '__main__':", new_test + "\nif __name__ == '__main__':", 1)
else:
    text += new_test

with open('tests/test_engine.py', 'w') as f:
    f.write(text)

print("Tests patched")
