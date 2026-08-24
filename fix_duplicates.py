import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

dup_pattern = r"(            if getattr\(entity, 'is_snow_glider', False\) and any\(t\.terrain_type == 'snow' for t in terrains_here\):\n                stamina_cost = 0\n)(            if getattr\(entity, 'is_snow_glider', False\) and any\(t\.terrain_type == 'snow' for t in terrains_here\):\n                stamina_cost = 0\n)"
content = re.sub(dup_pattern, r"\1", content)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
