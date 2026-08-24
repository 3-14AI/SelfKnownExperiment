import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

pattern_init_assign = r"(self\.is_snow_glider = is_snow_glider\n)"
replacement_init_assign = r"\1        self.is_spring_glider = is_spring_glider\n"
content = re.sub(pattern_init_assign, replacement_init_assign, content, count=1)

# 2. Update stamina logic
pattern_stamina = r"(if getattr\(entity, 'is_snow_glider', False\) and any\(t\.terrain_type == 'snow' for t in terrains_here\):\n\s+stamina_cost = 0\n)"
replacement_stamina = r"\1            if getattr(entity, 'is_spring_glider', False) and self.current_season == 'spring':\n                stamina_cost = 0\n"
content = re.sub(pattern_stamina, replacement_stamina, content, count=1)

# 3. Update inheritance in tick
pattern_inherit = r"(child_is_snow_glider = getattr\(entity, \"is_snow_glider\", False\)\n)"
replacement_inherit = r"\1                    child_is_spring_glider = getattr(entity, 'is_spring_glider', False)\n"
content = re.sub(pattern_inherit, replacement_inherit, content, count=1)

# 4. Update mutation in tick
pattern_mutate = r"(child_is_snow_glider = not child_is_snow_glider\n\s+mutation_occurred = True\n)"
replacement_mutate = r"\1                    if random.random() < mutation_chance:\n                        child_is_spring_glider = not child_is_spring_glider\n                        mutation_occurred = True\n"
content = re.sub(pattern_mutate, replacement_mutate, content, count=1)

# 5. Update Entity instantiation in tick
pattern_instantiate = r"(is_night_glider=child_is_night_glider, is_snow_glider=child_is_snow_glider)\)"
replacement_instantiate = r"\1, is_spring_glider=child_is_spring_glider)"
content = re.sub(pattern_instantiate, replacement_instantiate, content, count=1)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
