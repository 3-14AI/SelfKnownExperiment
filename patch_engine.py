import re

with open('src/universe/engine.py', 'r') as f:
    text = f.read()

# 1. Add to Entity.__init__ signature
old_init_sig = "is_day_glider=False, is_night_glider=False, is_snow_glider=False):"
new_init_sig = "is_day_glider=False, is_night_glider=False, is_snow_glider=False, is_deep_water_glider=False):"
text = text.replace(old_init_sig, new_init_sig, 1)

# 2. Add to Entity.__init__ body
old_init_body = "        self.is_snow_glider = is_snow_glider\n"
new_init_body = "        self.is_snow_glider = is_snow_glider\n        self.is_deep_water_glider = is_deep_water_glider\n"
text = text.replace(old_init_body, new_init_body, 1)

# 3. Add to Universe.tick mutation
old_mut = """                    if random.random() < mutation_chance:
                        child_is_night_glider = not child_is_night_glider
                        mutation_occurred = True"""
new_mut = """                    if random.random() < mutation_chance:
                        child_is_night_glider = not child_is_night_glider
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_deep_water_glider = not child_is_deep_water_glider
                        mutation_occurred = True"""
text = text.replace(old_mut, new_mut, 1)

# 4. Add to move_entity stamina logic
old_stamina = """            if getattr(entity, 'is_snow_glider', False) and any(t.terrain_type == 'snow' for t in terrains_here):
                stamina_cost = 0
"""
new_stamina = """            if getattr(entity, 'is_snow_glider', False) and any(t.terrain_type == 'snow' for t in terrains_here):
                stamina_cost = 0
            if getattr(entity, 'is_deep_water_glider', False) and any(t.terrain_type == 'deep-water' for t in terrains_here):
                stamina_cost = 0
"""
text = text.replace(old_stamina, new_stamina, 1)

# 5. Extract child_is_* variable setup in Universe.tick
old_child_setup = "                    child_is_snow_glider = getattr(entity, \"is_snow_glider\", False)\n"
new_child_setup = "                    child_is_snow_glider = getattr(entity, \"is_snow_glider\", False)\n                    child_is_deep_water_glider = getattr(entity, 'is_deep_water_glider', False)\n"
text = text.replace(old_child_setup, new_child_setup, 1)

# 6. Pass to Entity creation in Universe.tick
old_spawn = "                            is_snow_glider=child_is_snow_glider\n"
new_spawn = "                            is_snow_glider=child_is_snow_glider,\n                            is_deep_water_glider=child_is_deep_water_glider\n"
text = text.replace(old_spawn, new_spawn, 1)

with open('src/universe/engine.py', 'w') as f:
    f.write(text)

print("Engine Patched")
