import unittest
from unittest import mock
from src.universe.engine import Universe, Entity
from src.universe.visualizer import CLIVisualizer

class TestIsAshPredators(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10, population_limit=0)
        self.universe.entities = []
        self.universe.terrains = []
        self.universe.foods = []
        self.universe.localized_events = []
        self.universe.scent_trails = {}
        self.universe.event_chance = 0.0
        self.universe.disease_chance = 0.0
        self.universe.localized_event_chance = 0.0

    def test_is_ash_dancer_predator_combat_multiplier(self):
        predator = Entity(name="Predator", x=5, y=5, size=1, energy=50, is_ash_dancer_predator=True, attack=10, defense=10, diet='carnivore')
        prey = Entity(name="Prey", x=5, y=5, size=1, energy=50, is_ash_dancer=True, attack=10, defense=10)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        # Base escape chance: 10 / (10 + 10) = 0.50
        # Multiplied effective attack = 15
        # Multiplied escape chance = 10 / (15 + 10) = 0.40
        # Set random to 0.45. If multiplier is applied, 0.45 >= 0.40 -> prey is eaten
        # If multiplier is NOT applied, 0.45 < 0.50 -> prey escapes
        with mock.patch('src.universe.engine.random.random', return_value=0.45):
            self.universe.tick()

        self.assertNotIn(prey, self.universe.entities, "Prey should have been eaten due to the 1.5x attack multiplier")

    def test_is_ash_dweller_predator_combat_multiplier(self):
        predator = Entity(name="Predator", x=5, y=5, size=1, energy=50, is_ash_dweller_predator=True, attack=10, defense=10, diet='carnivore')
        prey = Entity(name="Prey", x=5, y=5, size=1, energy=50, is_ash_dweller=True, attack=10, defense=10)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        with mock.patch('src.universe.engine.random.random', return_value=0.45):
            self.universe.tick()
        self.assertNotIn(prey, self.universe.entities, "Prey should have been eaten due to the 1.5x attack multiplier")

    def test_is_ash_glider_predator_combat_multiplier(self):
        predator = Entity(name="Predator", x=5, y=5, size=1, energy=50, is_ash_glider_predator=True, attack=10, defense=10, diet='carnivore')
        prey = Entity(name="Prey", x=5, y=5, size=1, energy=50, is_ash_glider=True, attack=10, defense=10)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        with mock.patch('src.universe.engine.random.random', return_value=0.45):
            self.universe.tick()
        self.assertNotIn(prey, self.universe.entities, "Prey should have been eaten due to the 1.5x attack multiplier")

    def test_is_ash_strider_predator_combat_multiplier(self):
        predator = Entity(name="Predator", x=5, y=5, size=1, energy=50, is_ash_strider_predator=True, attack=10, defense=10, diet='carnivore')
        prey = Entity(name="Prey", x=5, y=5, size=1, energy=50, is_ash_strider=True, attack=10, defense=10)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        with mock.patch('src.universe.engine.random.random', return_value=0.45):
            self.universe.tick()
        self.assertNotIn(prey, self.universe.entities, "Prey should have been eaten due to the 1.5x attack multiplier")

    def test_is_ash_walker_predator_combat_multiplier(self):
        predator = Entity(name="Predator", x=5, y=5, size=1, energy=50, is_ash_walker_predator=True, attack=10, defense=10, diet='carnivore')
        prey = Entity(name="Prey", x=5, y=5, size=1, energy=50, is_ash_walker=True, attack=10, defense=10)
        self.universe.add_entity(predator)
        self.universe.add_entity(prey)

        with mock.patch('src.universe.engine.random.random', return_value=0.45):
            self.universe.tick()
        self.assertNotIn(prey, self.universe.entities, "Prey should have been eaten due to the 1.5x attack multiplier")

    @mock.patch('src.universe.engine.random.random', return_value=0.0)
    def test_is_ash_predators_mutation(self, mock_random):
        parent = Entity(name="Parent", x=5, y=5, size=1, energy=100, is_ash_dancer_predator=False, is_ash_dweller_predator=False, is_ash_glider_predator=False, is_ash_strider_predator=False, is_ash_walker_predator=False, lays_eggs=False)
        self.universe.add_entity(parent)
        self.universe.reproduction_threshold = 10
        self.universe.population_limit = 100
        self.universe.tick()
        children = [e for e in self.universe.entities if e is not parent]
        self.assertGreater(len(children), 0, "A child should have been born")

        child = children[0]
        self.assertTrue(getattr(child, 'is_ash_dancer_predator', False), "is_ash_dancer_predator should mutate")
        self.assertTrue(getattr(child, 'is_ash_dweller_predator', False), "is_ash_dweller_predator should mutate")
        self.assertTrue(getattr(child, 'is_ash_glider_predator', False), "is_ash_glider_predator should mutate")
        self.assertTrue(getattr(child, 'is_ash_strider_predator', False), "is_ash_strider_predator should mutate")
        self.assertTrue(getattr(child, 'is_ash_walker_predator', False), "is_ash_walker_predator should mutate")

    def test_is_ash_predators_visualizer(self):
        vis = CLIVisualizer(None)

        e1 = Entity(name="1", x=1, y=1, energy=50, is_ash_dancer_predator=True)
        self.universe.add_entity(e1)

        e2 = Entity(name="2", x=2, y=2, energy=50, is_ash_dweller_predator=True)
        self.universe.add_entity(e2)

        e3 = Entity(name="3", x=3, y=3, energy=50, is_ash_glider_predator=True)
        self.universe.add_entity(e3)

        e4 = Entity(name="4", x=4, y=4, energy=50, is_ash_strider_predator=True)
        self.universe.add_entity(e4)

        e5 = Entity(name="5", x=5, y=5, energy=50, is_ash_walker_predator=True)
        self.universe.add_entity(e5)

        vis = CLIVisualizer(self.universe)
        output = vis.render()

        self.assertIn('ǎ', output)
        self.assertIn('ā', output)
        self.assertIn('ä', output)
        self.assertIn('à', output)
        self.assertIn('á', output)
