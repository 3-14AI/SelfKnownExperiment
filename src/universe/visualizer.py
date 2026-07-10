class CLIVisualizer:
    def __init__(self, universe):
        self.universe = universe

    def render(self):
        # Create an empty grid
        grid = [['.' for _ in range(self.universe.width)] for _ in range(self.universe.height)]

        # Add food
        for food in self.universe.foods:
            if 0 <= food.x < self.universe.width and 0 <= food.y < self.universe.height:
                grid[food.y][food.x] = 'f'

        # Add entities (entities overwrite food in visualization if on same spot)
        for entity in self.universe.entities:
            if 0 <= entity.x < self.universe.width and 0 <= entity.y < self.universe.height:
                grid[entity.y][entity.x] = 'E'

        # Join lines
        return '\n'.join(''.join(row) for row in grid)

    def print_state(self):
        print(f"Time: {self.universe.time}")
        print(self.render())
