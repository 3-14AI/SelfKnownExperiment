import unittest
from unittest.mock import patch
from src.universe.engine import Universe, Entity, Terrain

class TestIsDeserticPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    @patch('src.universe.engine.random.random')
    def test_is_desertic_predator_mutation(self, mock_random):
        mock_random.return_value = 0.0
        parent1 = Entity(name="test", x=1, y=1, energy=8, size=1, is_desertic_predator=False)
        parent1.reproduction_threshold = 999999
        self.universe.entities.append(parent1)

        parent1.universe = self.universe
        self.universe.mutation_chance = 1.0
        parent1.mutation_chance = 1.0
        children = []
        for _ in range(2000):
            parent1.energy = 50
            parent1.age = 10
            parent1.hydration = 50
            parent1.reproduction_threshold = 40
            parent1.reproduction_hydration_threshold = 40
            self.universe.tick()
            children = [e for e in self.universe.entities if e is not parent1]
            if children:
                 break

        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(c, 'is_desertic_predator', False) for c in children))

    @patch('src.universe.engine.random.random')
    def test_is_desertic_predator_combat(self, mock_random):
        uni = Universe(width=10, height=10)
        uni.event_chance = 0.0

        predator = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_desertic_predator=True)
        predator.attack = 10
        uni.entities.append(predator)

        prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_desertic=True)
        prey.defense = 5
        uni.entities.append(prey)

        mock_random.side_effect = lambda: 0.30

        uni.tick()

        self.assertNotIn(prey, uni.entities)

        # Control
        uni2 = Universe(width=10, height=10)
        uni2.event_chance = 0.0

        c_pred = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_desertic_predator=False)
        c_pred.attack = 10
        uni2.entities.append(c_pred)

        c_prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_desertic=True)
        c_prey.defense = 5
        uni2.entities.append(c_prey)

        mock_random.side_effect = lambda: 0.30
        uni2.tick()

        self.assertIn(c_prey, uni2.entities)

class TestIsForestalPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    @patch('src.universe.engine.random.random')
    def test_is_forestal_predator_mutation(self, mock_random):
        mock_random.return_value = 0.0
        parent1 = Entity(name="test", x=1, y=1, energy=8, size=1, is_forestal_predator=False)
        parent1.reproduction_threshold = 999999
        self.universe.entities.append(parent1)

        parent1.universe = self.universe
        self.universe.mutation_chance = 1.0
        parent1.mutation_chance = 1.0
        children = []
        for _ in range(2000):
            parent1.energy = 50
            parent1.age = 10
            parent1.hydration = 50
            parent1.reproduction_threshold = 40
            parent1.reproduction_hydration_threshold = 40
            self.universe.tick()
            children = [e for e in self.universe.entities if e is not parent1]
            if children:
                 break

        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(c, 'is_forestal_predator', False) for c in children))

    @patch('src.universe.engine.random.random')
    def test_is_forestal_predator_combat(self, mock_random):
        uni = Universe(width=10, height=10)
        uni.event_chance = 0.0

        predator = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_forestal_predator=True)
        predator.attack = 10
        uni.entities.append(predator)

        prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_forestal=True)
        prey.defense = 5
        uni.entities.append(prey)

        mock_random.side_effect = lambda: 0.30
        uni.tick()
        self.assertNotIn(prey, uni.entities)

        uni2 = Universe(width=10, height=10)
        uni2.event_chance = 0.0
        c_pred = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_forestal_predator=False)
        c_pred.attack = 10
        uni2.entities.append(c_pred)

        c_prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_forestal=True)
        c_prey.defense = 5
        uni2.entities.append(c_prey)

        mock_random.side_effect = lambda: 0.30
        uni2.tick()
        self.assertIn(c_prey, uni2.entities)

class TestIsVolcanicPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    @patch('src.universe.engine.random.random')
    def test_is_volcanic_predator_mutation(self, mock_random):
        mock_random.return_value = 0.0
        parent1 = Entity(name="test", x=1, y=1, energy=8, size=1, is_volcanic_predator=False)
        parent1.reproduction_threshold = 999999
        self.universe.entities.append(parent1)

        parent1.universe = self.universe
        self.universe.mutation_chance = 1.0
        parent1.mutation_chance = 1.0
        children = []
        for _ in range(2000):
            parent1.energy = 50
            parent1.age = 10
            parent1.hydration = 50
            parent1.reproduction_threshold = 40
            parent1.reproduction_hydration_threshold = 40
            self.universe.tick()
            children = [e for e in self.universe.entities if e is not parent1]
            if children:
                 break

        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(c, 'is_volcanic_predator', False) for c in children))

    @patch('src.universe.engine.random.random')
    def test_is_volcanic_predator_combat(self, mock_random):
        uni = Universe(width=10, height=10)
        uni.event_chance = 0.0

        predator = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_volcanic_predator=True)
        predator.attack = 10
        uni.entities.append(predator)

        prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_volcanic=True)
        prey.defense = 5
        uni.entities.append(prey)

        mock_random.side_effect = lambda: 0.30
        uni.tick()
        self.assertNotIn(prey, uni.entities)

        uni2 = Universe(width=10, height=10)
        uni2.event_chance = 0.0
        c_pred = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_volcanic_predator=False)
        c_pred.attack = 10
        uni2.entities.append(c_pred)

        c_prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_volcanic=True)
        c_prey.defense = 5
        uni2.entities.append(c_prey)

        mock_random.side_effect = lambda: 0.30
        uni2.tick()
        self.assertIn(c_prey, uni2.entities)

class TestIsArcticPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.localized_event_chance = 0.0
        self.universe.disease_chance = 0.0

    @patch('src.universe.engine.random.random')
    def test_is_arctic_predator_mutation(self, mock_random):
        mock_random.return_value = 0.0
        parent1 = Entity(name="test", x=1, y=1, energy=8, size=1, is_arctic_predator=False)
        parent1.reproduction_threshold = 999999
        self.universe.entities.append(parent1)

        parent1.universe = self.universe
        self.universe.mutation_chance = 1.0
        parent1.mutation_chance = 1.0
        children = []
        for _ in range(2000):
            parent1.energy = 50
            parent1.age = 10
            parent1.hydration = 50
            parent1.reproduction_threshold = 40
            parent1.reproduction_hydration_threshold = 40
            self.universe.tick()
            children = [e for e in self.universe.entities if e is not parent1]
            if children:
                 break

        self.assertGreater(len(children), 0, 'A child should have been born')
        self.assertTrue(any(getattr(c, 'is_arctic_predator', False) for c in children))

    @patch('src.universe.engine.random.random')
    def test_is_arctic_predator_combat(self, mock_random):
        uni = Universe(width=10, height=10)
        uni.event_chance = 0.0

        predator = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_arctic_predator=True)
        predator.attack = 10
        uni.entities.append(predator)

        prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_arctic=True)
        prey.defense = 5
        uni.entities.append(prey)

        mock_random.side_effect = lambda: 0.30
        uni.tick()
        self.assertNotIn(prey, uni.entities)

        uni2 = Universe(width=10, height=10)
        uni2.event_chance = 0.0
        c_pred = Entity(name="pred", x=1, y=1, energy=8, size=1, diet='carnivore', is_arctic_predator=False)
        c_pred.attack = 10
        uni2.entities.append(c_pred)

        c_prey = Entity(name="prey", x=1, y=1, energy=8, size=1, is_arctic=True)
        c_prey.defense = 5
        uni2.entities.append(c_prey)

        mock_random.side_effect = lambda: 0.30
        uni2.tick()
        self.assertIn(c_prey, uni2.entities)
