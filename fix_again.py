import re

with open("src/universe/engine.py", "r") as f:
    text = f.read()

# Fix duplicates in defense block 1 again. The problem was I replaced with the duplicates again before.
text = text.replace("""                            if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                                effective_defense += 2""", """                            if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                                effective_defense += 2
                            if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                                effective_defense += 2""")

# Fix duplicates in defense block 2 again
text = text.replace("""                        if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                            effective_defense += 2
                        if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                            effective_defense += 2
                        if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                            effective_defense += 2
                        if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                            effective_defense += 2""", """                        if getattr(prey_to_eat, 'is_water_strider', False) and any(t.terrain_type == 'water' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):
                            effective_defense += 2
                        if getattr(prey_to_eat, 'is_drought_strider', False) and self.current_event == 'drought':
                            effective_defense += 2""")

with open("src/universe/engine.py", "w") as f:
    f.write(text)
