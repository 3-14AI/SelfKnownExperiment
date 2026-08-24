import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# Add logic for is_snow_glider stamina cost reduction
pattern_stamina = r"(if getattr\(entity, 'is_ice_glider', False\) and any\(t\.terrain_type == 'ice' for t in terrains_here\):\n\s+stamina_cost = 0)"
replacement_stamina = r"\1\n            if getattr(entity, 'is_snow_glider', False) and any(t.terrain_type == 'snow' for t in terrains_here):\n                stamina_cost = 0"
if re.search(pattern_stamina, content):
    content = re.sub(pattern_stamina, replacement_stamina, content, count=1)
    print("Patched stamina logic for is_snow_glider")
else:
    print("Could not find stamina logic pattern")

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
