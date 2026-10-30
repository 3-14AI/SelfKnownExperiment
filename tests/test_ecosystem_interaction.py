import unittest
from unittest.mock import patch
from src.universe.engine import Universe, Entity, Food

class TestEcosystemInteraction(unittest.TestCase):
    def test_predator_prey_population_dynamics(self):
        """
        Verify that predators effectively hunt prey, reducing prey population and increasing predator energy/population,
        and that prey consumes resources (food) to survive and reproduce.
        """
        universe = Universe(width=10, height=10, food_spawn_rate=0.0)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.reproduction_threshold = 999999
        universe.population_limit = 0
        universe.reproduction_threshold = 20
        universe.reproduction_cost = 10

        # Add food for prey
        universe.foods.append(Food(x=0, y=0, energy=30, plant_type='grass'))
        universe.foods.append(Food(x=0, y=1, energy=30, plant_type='grass'))

        # Add prey (herbivore)
        prey = Entity("Prey", x=0, y=0, diet='herbivore', energy=15, attack=0, defense=0)
        prey.reproduction_threshold = 20
        prey.reproduction_cost = 10
        universe.add_entity(prey)

        # Give it a couple of ticks to eat food and potentially reproduce
        # Mock random so it doesn't fail reproduction (always mutates or similar)
        with patch('random.random', return_value=0.5):
            universe.tick() # Eats food at 0,0, energy 15 -> 45
            universe.tick() # Reproduces (energy 45 -> 35), moves maybe?
            universe.tick()

        prey_population = len([e for e in universe.entities if e.diet == 'herbivore'])
        self.assertGreaterEqual(prey_population, 1, "Prey should survive and potentially reproduce")

        # Add predator (carnivore)
        predator = Entity("Predator", x=0, y=0, diet='carnivore', energy=15, attack=100, defense=10)
        predator.reproduction_threshold = 20
        predator.reproduction_cost = 10
        universe.add_entity(predator)

        # Force all prey to be at (0,0) for predator to eat them
        for e in universe.entities:
            e.x = 0
            e.y = 0

        # Predator eats prey
        with patch('random.random', return_value=0.99): # 0.99 > 0.0 (escape chance) -> prey eaten
            universe.tick() # Predator eats one prey

        final_prey_population = len([e for e in universe.entities if e.diet == 'herbivore'])
        self.assertLess(final_prey_population, prey_population, "Predator should have eaten at least one prey")

        final_predator = [e for e in universe.entities if e.diet == 'carnivore'][0]
        self.assertGreater(final_predator.energy, 15, "Predator should gain energy from eating prey")


    def test_herbivore_starvation_dynamics(self):
        """
        Verify that herbivores exhaust their food source and eventually starve, ensuring the engine correctly handles population decline due to starvation.
        """
        universe = Universe(width=10, height=10, food_spawn_rate=0.0)
        universe.event_chance = 0.0
        universe.disease_chance = 0.0
        universe.reproduction_threshold = 999999
        universe.population_limit = 0

        # Add single food
        universe.foods.append(Food(x=5, y=5, energy=10, plant_type='grass'))

        # Add herbivore
        prey = Entity("Prey", x=5, y=5, diet='herbivore', energy=10, is_photosensitive=False)
        prey.lays_eggs = False
        prey.reproduction_threshold = 999999
        prey.is_contagious_predator = False # safety measure, not needed but let's lock rep down
        universe.add_entity(prey)

        # Herbivore eats
        universe.tick()

        # Simulate many ticks to starve
        for _ in range(100):
            universe.tick()

        self.assertFalse(prey.is_alive, "Herbivore should starve when food runs out")
        self.assertEqual(len(universe.entities), 0, "Universe should be empty after starvation")

if __name__ == '__main__':
    unittest.main()
