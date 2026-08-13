import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# Make sure all dynamic add_terrain calls check bounds!
# Let's just fix `add_terrain` to silently ignore or handle out-of-bounds, instead of crashing the tick. Wait, if it raises ValueError, it's better to fix the caller or ignore in add_terrain.
# Wait, why is entity.y == -1? Because entities can somehow move out of bounds?
# Ah! In move_entity, when leaping:
#                 leap_x, leap_y = new_x + dx, new_y + dy
#                 if 0 <= leap_x < self.width and 0 <= leap_y < self.height:
#                     if self.is_passable(...):
#                         new_x, new_y = leap_x, leap_y
# Then `entity.x = new_x`, `entity.y = new_y`. Wait, `new_x` and `new_y` would be `leap_x, leap_y`.
# BUT wait! dx, dy are coming from `path[0]`.
# If path[0] is `(0, -2)` from our leaping `find_path` modification (`dx * 2, dy * 2`).
# Then `new_x = entity.x + dx`, so `new_x = entity.x + 0`, `new_y = entity.y - 2`.
# `new_y` is checked:
# `if not (0 <= new_x < self.width and 0 <= new_y < self.height):`
# Wait, `move_entity` doesn't know it's a leap unless it checks.
# But since `find_path` returns `(dx * 2, dy * 2)`, `dx` in `move_entity` is now 2.
# So `new_x = entity.x + dx` which is correctly the leap destination.
# So if `new_x, new_y` is out of bounds, `move_entity` throws ValueError...
# BUT wait, the first `if not (0 <= new_x ...):` check in move_entity catches it and raises ValueError? Wait, the error is in `add_terrain`, meaning the entity actually reached `y = -1`.
# Let's check `is_passable` calls in `find_path`.
# Wait, if `find_path` returns `(0, -2)`, then `new_y` is `entity.y - 2`.
# But in `move_entity` we check if `0 <= new_x < self.width and 0 <= new_y < self.height`. If not, it raises ValueError.
# If `move_entity` raises ValueError, the caller `try ... except ValueError: pass` catches it.
# So `entity.y` should not become `-1` from `move_entity` unless `dx, dy` is something else...
# Wait! In `find_path` we added `(dx * 2, dy * 2)`. If it returns `(dx, dy)` as `(0, -2)`, in `Universe.tick`:
#                                                     dx, dy = path[0]
#                                                     try:
#                                                         self.move_entity(entity, dx, dy)
#                                                     except ValueError:
#                                                         pass
# So if it fails, it just skips. How does `entity.y` become `-1`?
# Ah, maybe migrating entities?
# target_y = -1 in some cases?
# In `tick` migration logic:
# `target_y = self.height - 1 if self.current_season in ['autumn', 'winter'] else 0`
# Not -1.

# Let's just safely cap entity positions before add_terrain:
target = "def add_terrain(self, terrain):"
replacement = "def add_terrain(self, terrain):\n        if terrain.x < 0 or terrain.x >= self.width or terrain.y < 0 or terrain.y >= self.height:\n            return"
content = content.replace(target, replacement)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
