import unittest
from unittest.mock import patch
from src.universe.engine import Entity, Universe
from src.universe.visualizer import CLIVisualizer

class TestIsCarnivorousPlantPredator(unittest.TestCase):
    def setUp(self):
        self.universe = Universe(width=10, height=10)
        self.universe.event_chance = 0.0
        self.universe.disease_chance = 0.0
        self.universe.localized_event_chance = 0.0

    @patch('src.universe.engine.random.random')
    def test_is_carnivorous_plant_predator_combat_multiplier(self, mock_random):
        mock_random.return_value = 0.4

        # Test 1: with multiplier, prey is eaten
        predator = Entity(name='TestEntity', x=5, y=5, energy=50, age=5, size=1, perception_radius=5, diet='carnivore', species='carnivore')
        predator.is_aerial_predator = False
        predator.is_omnivore = False
        predator.is_herbivore_predator = False
        predator.is_omnivore_predator = False
        predator.is_scavenger_predator = False
        predator.is_amphibious_predator = False
        predator.is_aquatic_predator = False
        predator.has_claws = False
        predator.has_horns = False
        predator.is_apex_predator = False
        predator.is_carnivore_predator = False
        predator.is_scavenger_hunter_predator = False
        predator.is_giant_slayer = False
        predator.is_carnivorous_plant_predator = True
        predator.attack = 10
        predator.stamina = 50

        prey = Entity(name='TestEntity', x=5, y=5, energy=50, age=5, size=1, species='prey')
        prey.is_carnivorous_plant = True
        prey.defense = 10
        prey.is_protective = False
        prey.is_intimidating = False
        prey.is_smelly = False
        prey.is_scavenger = False
        prey.diet = 'herbivore'
        prey.is_aquatic = False
        prey.is_amphibious = False
        prey.has_shell = False
        prey.has_scales = False
        prey.is_giant_slayer = False
        prey.stamina = 50

        self.universe.entities = [predator, prey]
        predator.energy = predator.max_energy * 0.4

        for entity in self.universe.entities:
            entity.is_lucky = False
            entity.is_evasive = False
            entity.is_clairvoyant = False
            entity.is_telekinetic = False
            entity.is_ethereal = False

        self.universe.tick()

        self.assertNotIn(prey, self.universe.entities, "Prey should be eaten due to 1.5x attack multiplier")

        # Test 2: without multiplier, prey escapes
        predator2 = Entity(name='TestEntity', x=5, y=5, energy=50, age=5, size=1, perception_radius=5, diet='carnivore', species='carnivore')
        predator2.is_aerial_predator = False
        predator2.is_omnivore = False
        predator2.is_herbivore_predator = False
        predator2.is_omnivore_predator = False
        predator2.is_scavenger_predator = False
        predator2.is_amphibious_predator = False
        predator2.is_aquatic_predator = False
        predator2.has_claws = False
        predator2.has_horns = False
        predator2.is_apex_predator = False
        predator2.is_carnivore_predator = False
        predator2.is_scavenger_hunter_predator = False
        predator2.is_giant_slayer = False
        predator2.is_carnivorous_plant_predator = False # No multiplier
        predator2.attack = 10
        predator2.stamina = 50

        prey2 = Entity(name='TestEntity', x=5, y=5, energy=50, age=5, size=1, species='prey')
        prey2.is_carnivorous_plant = True
        prey2.defense = 10
        prey2.is_protective = False
        prey2.is_intimidating = False
        prey2.is_smelly = False
        prey2.is_scavenger = False
        prey2.diet = 'herbivore'
        prey2.is_aquatic = False
        prey2.is_amphibious = False
        prey2.has_shell = False
        prey2.has_scales = False
        prey2.is_giant_slayer = False
        prey2.stamina = 50

        self.universe.entities = [predator2, prey2]
        predator2.energy = predator2.max_energy * 0.4

        for entity in self.universe.entities:
            entity.is_lucky = False
            entity.is_evasive = False
            entity.is_clairvoyant = False
            entity.is_telekinetic = False
            entity.is_ethereal = False

        self.universe.tick()

        self.assertIn(prey2, self.universe.entities, "Prey should escape without the 1.5x attack multiplier")

    @patch('src.universe.engine.random.random')
    def test_is_carnivorous_plant_predator_mutation(self, mock_random):
        mock_random.return_value = 0.0 # Force mutation and successful reproduction
        parent = Entity(name='TestEntity', x=5, y=5, energy=900, size=1)
        parent.reproduction_threshold = 500
        parent.is_carnivorous_plant_predator = False

        # Disable all other mutations so that we are 100% sure we mutate the correct one
        parent.mutations = 0
        parent.is_lucky = False
        parent.is_evasive = False

        self.universe.entities = [parent]
        self.universe.tick()

        children = [e for e in self.universe.entities if e is not parent]
        self.assertGreater(len(children), 0, "A child should have been born")
        child = children[0]
        self.assertTrue(child.is_carnivorous_plant_predator, "Child should have mutated the is_carnivorous_plant_predator trait")

    def test_is_carnivorous_plant_predator_visualizer(self):
        vis = CLIVisualizer(None)
        predator = Entity(name='TestEntity', x=5, y=5, energy=50, age=5, size=1)
        predator.is_carnivorous_plant_predator = True

        vis.universe = self.universe
        self.universe.entities = [predator]
        rendered = vis.render()
        self.assertIn('❀', rendered, "Visualizer should render is_carnivorous_plant_predator entities as '❀'")

if __name__ == '__main__':
    unittest.main()
