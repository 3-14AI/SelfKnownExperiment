with open("src/universe/engine.py") as f:
    content = f.read()

# 1. Add is_empathic to Entity.__init__
target_init_search = ", is_hypnotic=False, is_tracker=False):"
target_init_replace = ", is_hypnotic=False, is_tracker=False, is_empathic=False):"
content = content.replace(target_init_search, target_init_replace)

target_assign_search = "        self.is_tracker = is_tracker"
target_assign_replace = "        self.is_tracker = is_tracker\n        self.is_empathic = is_empathic"
content = content.replace(target_assign_search, target_assign_replace)

# 2. child_is_empathic initialization
target_child_init_search = "                    child_is_tracker = getattr(entity, 'is_tracker', False)"
target_child_init_replace = "                    child_is_tracker = getattr(entity, 'is_tracker', False)\n                    child_is_empathic = getattr(entity, 'is_empathic', False)"
content = content.replace(target_child_init_search, target_child_init_replace)

# 3. child_is_empathic mutation
target_child_mut_search = "                    if random.random() < mutation_chance:\n                        child_is_tracker = not child_is_tracker\n                        mutation_occurred = True"
target_child_mut_replace = "                    if random.random() < mutation_chance:\n                        child_is_tracker = not child_is_tracker\n                        mutation_occurred = True\n\n                    if random.random() < mutation_chance:\n                        child_is_empathic = not child_is_empathic\n                        mutation_occurred = True"
content = content.replace(target_child_mut_search, target_child_mut_replace)

# 4. pass is_empathic in new Entity
target_child_pass_search = "is_tracker=child_is_tracker)"
target_child_pass_replace = "is_tracker=child_is_tracker, is_empathic=child_is_empathic)"
content = content.replace(target_child_pass_search, target_child_pass_replace)

# 5. implement is_empathic behavior in Universe.tick main entity loop
target_behavior_search = "                if getattr(entity, 'is_cooperative', False) and entity.energy > entity.max_energy * 0.6:"
target_behavior_replace = """                if getattr(entity, 'is_empathic', False) and entity.energy > entity.max_energy * 0.5:
                    flockmates = self.get_nearby_flockmates(entity, 1)
                    for flockmate in flockmates:
                        if flockmate.energy < flockmate.max_energy * 0.3:
                            flockmate.energy += 2
                            entity.energy -= 2
                            break

                if getattr(entity, 'is_cooperative', False) and entity.energy > entity.max_energy * 0.6:"""
content = content.replace(target_behavior_search, target_behavior_replace)

with open("src/universe/engine.py", "w") as f:
    f.write(content)
