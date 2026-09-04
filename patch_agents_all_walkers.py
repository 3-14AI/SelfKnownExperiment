import re
with open('agents.md', 'r') as f:
    text = f.read()

# Let's add the missing traits from engine that are not in agents.md
engine_traits = set([
    'is_blizzard_walker', 'is_rain_walker', 'is_volcanic_walker', 'is_earthquake_walker',
    'is_drought_walker', 'is_mud_walker', 'is_sand_walker', 'is_mountain_walker', 'is_cave_walker',
    'is_snow_walker', 'is_frost_walker', 'is_dune_walker', 'is_web_walker', 'is_ash_walker', 'is_forest_walker'
])

agents_text_set = set(re.findall(r'- \[x\] Implemented `is_[a-z_]*_walker`', text))

new_lines = []
for trait in engine_traits:
    if f'- [x] Implemented `{trait}`' not in text:
        new_lines.append(f"- [x] Implemented `{trait}` trait.")

# also add venom resistant, storm_walker, fire_walker if they were somehow missed, though we already added them.
# The reviewer notes: "the agent missed most of them despite the user's explicit instruction to document all ("все существующие") traits. "
# Ah wait, `is_snow_walker` was already documented as: - [x] Implemented `is_snow_walker` trait. Entities with this trait do not consume extra stamina from elevation changes when moving on snow terrain.
# Let's check which ones are actually missing in agents.md.
