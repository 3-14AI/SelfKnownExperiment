import re

with open('src/universe/engine.py', 'r') as f:
    text = f.read()

# Defense duplicates
text = re.sub(
    r"(if getattr\(prey_to_eat, 'is_shelter_dweller', False\) and any\(t\.terrain_type == 'shelter' for t in self\.get_terrains_at\(prey_to_eat\.x, prey_to_eat\.y\)\):\n\s+effective_defense \+= 2\n\s+){2,}",
    r"if getattr(prey_to_eat, 'is_shelter_dweller', False) and any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):\n                                effective_defense += 2\n                            ",
    text, count=1
)
text = re.sub(
    r"(if getattr\(prey_to_eat, 'is_shelter_dweller', False\) and any\(t\.terrain_type == 'shelter' for t in self\.get_terrains_at\(prey_to_eat\.x, prey_to_eat\.y\)\):\n\s+effective_defense \+= 2\n\s+){2,}",
    r"if getattr(prey_to_eat, 'is_shelter_dweller', False) and any(t.terrain_type == 'shelter' for t in self.get_terrains_at(prey_to_eat.x, prey_to_eat.y)):\n                            effective_defense += 2\n                        ",
    text, count=1
)

with open('src/universe/engine.py', 'w') as f:
    f.write(text)
