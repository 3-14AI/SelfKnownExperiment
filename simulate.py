import os
import time
from src.universe.engine import Universe, Entity, Food, Terrain
from src.universe.visualizer import CLIVisualizer

def main():
    # Initialize a smaller universe for better CLI visualization
    universe = Universe(width=40, height=20, food_spawn_rate=0.2)

    # Add initial entities
    universe.add_entity(Entity(name="Adam", energy=30), x=10, y=10)
    universe.add_entity(Entity(name="Eve", energy=30), x=20, y=10)
    universe.add_entity(Entity(name="Bob", energy=20), x=5, y=5)

    # Add initial food
    for _ in range(10):
        universe.add_food(Food(energy=10), x=universe.width//2, y=universe.height//2) # This might be out of bounds if width/height is small, let's randomize

    # Add a terrain wall across the middle
    for x in range(10, 31):
        universe.add_terrain(Terrain(x=x, y=10, terrain_type='wall'))

    # Clear the foods added out of bounds or at same place and add them randomly
    universe.foods = []
    import random
    for _ in range(10):
        x = random.randint(0, universe.width - 1)
        y = random.randint(0, universe.height - 1)
        universe.add_food(Food(energy=10), x=x, y=y)

    visualizer = CLIVisualizer(universe)

    iterations = 100

    for _ in range(iterations):
        os.system('cls' if os.name == 'nt' else 'clear')
        visualizer.print_state()
        universe.tick()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
