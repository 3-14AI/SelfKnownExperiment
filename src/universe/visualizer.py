class CLIVisualizer:
    def __init__(self, universe):
        self.universe = universe

    def render(self):
        # Create an empty grid
        grid = [['.' for _ in range(self.universe.width)] for _ in range(self.universe.height)]

        # Add terrain
        for terrain in self.universe.terrains:
            if 0 <= terrain.x < self.universe.width and 0 <= terrain.y < self.universe.height:
                if terrain.terrain_type == 'wall':
                    grid[terrain.y][terrain.x] = '#'
                elif terrain.terrain_type == 'water':
                    grid[terrain.y][terrain.x] = '~'
                elif terrain.terrain_type == 'ice':
                    grid[terrain.y][terrain.x] = '*'
                elif terrain.terrain_type == 'ash':
                    grid[terrain.y][terrain.x] = ':'
                elif terrain.terrain_type == 'mud':
                    grid[terrain.y][terrain.x] = 'm'
                elif terrain.terrain_type == 'sand':
                    grid[terrain.y][terrain.x] = ','
                elif terrain.terrain_type == 'snow':
                    grid[terrain.y][terrain.x] = 's'
                elif terrain.terrain_type == 'shelter':
                    grid[terrain.y][terrain.x] = '^'

        # Add food
        for food in self.universe.foods:
            if 0 <= food.x < self.universe.width and 0 <= food.y < self.universe.height:
                grid[food.y][food.x] = 'f'

        # Add entities (entities overwrite food in visualization if on same spot)
        for entity in self.universe.entities:
            if 0 <= entity.x < self.universe.width and 0 <= entity.y < self.universe.height:
                if getattr(entity, 'is_infected', False):
                    grid[entity.y][entity.x] = 'X' if getattr(entity, 'diet', 'herbivore') == 'carnivore' else 'S'
                else:
                    grid[entity.y][entity.x] = 'C' if getattr(entity, 'diet', 'herbivore') == 'carnivore' else 'E'

        # Join lines
        return '\n'.join(''.join(row) for row in grid)

    def print_state(self):
        print(f"Time: {self.universe.time}")
        if hasattr(self.universe, 'is_day'):
            day_night = "Day" if self.universe.is_day else "Night"
            print(f"Time of Day: {day_night}")
        if hasattr(self.universe, 'current_season'):
            print(f"Season: {self.universe.current_season.capitalize()}")
        if hasattr(self.universe, 'current_event') and self.universe.current_event:
            print(f"Event: {self.universe.current_event.upper()} ({self.universe.event_remaining_time} ticks left)")
        if hasattr(self.universe, 'localized_events') and self.universe.localized_events:
            event_strs = [f"{e.event_type.capitalize()} at ({e.x},{e.y}) r={e.radius}" for e in self.universe.localized_events]
            print(f"Localized Events: {', '.join(event_strs)}")
        if hasattr(self.universe, 'temperature_zones') and self.universe.temperature_zones:
            tz_strs = [f"Zone at ({tz.x},{tz.y}) r={tz.radius} mod={tz.temperature_modifier:+}°C" for tz in self.universe.temperature_zones]
            print(f"Temperature Zones: {', '.join(tz_strs)}")
        print(self.render())
