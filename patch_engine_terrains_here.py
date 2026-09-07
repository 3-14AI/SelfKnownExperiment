with open("src/universe/engine.py", "r") as f:
    text = f.read()

# Fix the terrains_here nitpick from code review
old_str = "or (getattr(entity, 'is_lava_dweller', False) and any(t.terrain_type == 'lava' for t in self.get_terrains_at(entity.x, entity.y)))"
new_str = "or (getattr(entity, 'is_lava_dweller', False) and any(t.terrain_type == 'lava' for t in terrains_here))"

text = text.replace(old_str, new_str)

with open("src/universe/engine.py", "w") as f:
    f.write(text)
