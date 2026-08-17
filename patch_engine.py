import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# 1. Add is_tracker to __init__
content = re.sub(
    r'(is_hypnotic=False):',
    r'\1, is_tracker=False):',
    content, count=1
)

content = re.sub(
    r'(self.is_hypnotic = is_hypnotic)',
    r'\1\n        self.is_tracker = is_tracker',
    content, count=1
)

# 2. Add to Universe.tick() mutations
content = re.sub(
    r'(child_is_hypnotic = getattr\(entity, \'is_hypnotic\', False\))',
    r'\1\n                    child_is_tracker = getattr(entity, \'is_tracker\', False)',
    content, count=1
)

content = re.sub(
    r'(child_is_hypnotic = not child_is_hypnotic)',
    r'\1\n                    if random.random() < mutation_chance:\n                        child_is_tracker = not child_is_tracker',
    content, count=1
)

content = re.sub(
    r'(is_hypnotic=child_is_hypnotic\))',
    r'is_hypnotic=child_is_hypnotic, is_tracker=child_is_tracker)',
    content, count=1
)

# 3. Scent tracking behavior
old_scent_loop = """                                    # Scent tracking behavior
                                    best_scent = 0
                                    best_pos = None
                                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                        nx, ny = entity.x + dx, entity.y + dy
                                        if (nx, ny) in self.scent_trails and self.scent_trails[(nx, ny)] > best_scent:
                                            if self.is_passable(nx, ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + dx * 2, entity.y + dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
                                                best_scent = self.scent_trails[(nx, ny)]
                                                best_pos = (dx, dy)
                                    if best_pos:"""

new_scent_loop = """                                    # Scent tracking behavior
                                    best_scent = 0
                                    best_pos = None
                                    import math
                                    search_radius = [(dx, dy) for dx in range(-2, 3) for dy in range(-2, 3) if 0 < abs(dx) + abs(dy) <= 2] if getattr(entity, 'is_tracker', False) else [(0, -1), (0, 1), (-1, 0), (1, 0)]
                                    for dx, dy in search_radius:
                                        nx, ny = entity.x + dx, entity.y + dy
                                        if (nx, ny) in self.scent_trails and self.scent_trails[(nx, ny)] > best_scent:
                                            # We just need any valid move towards the scent if it's further than 1 tile
                                            step_dx = int(math.copysign(1, dx)) if dx != 0 else 0
                                            step_dy = int(math.copysign(1, dy)) if dy != 0 else 0
                                            if abs(dx) > 0 and abs(dy) > 0:
                                                # Prefer moving along the larger difference if possible, but manhattan dist 2 means (1,1) or (2,0) or (0,2).
                                                # For (1,1) we can pick x or y.
                                                if random.random() < 0.5:
                                                    step_dy = 0
                                                else:
                                                    step_dx = 0
                                            check_nx = entity.x + step_dx
                                            check_ny = entity.y + step_dy
                                            if self.is_passable(check_nx, check_ny, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False)) or (getattr(entity, 'can_leap', False) and getattr(entity, 'stamina', 0) >= 5 and self.is_passable(entity.x + step_dx * 2, entity.y + step_dy * 2, getattr(entity, 'is_aquatic', False), getattr(entity, 'is_flying', False), getattr(entity, 'is_amphibious', False), is_climbing=getattr(entity, 'can_climb', False))):
                                                best_scent = self.scent_trails[(nx, ny)]
                                                best_pos = (step_dx, step_dy)
                                    if best_pos:"""

content = content.replace(old_scent_loop, new_scent_loop)


with open('src/universe/engine.py', 'w') as f:
    f.write(content)
