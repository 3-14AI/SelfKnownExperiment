import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()


mut_search = "child_is_parasite_resistant_predator = not child_is_parasite_resistant_predator\n                    elif mutation_type < 0.99999:\n                        child_is_stun_resistant_predator = not child_is_stun_resistant_predator"
mut_replace = "child_is_parasite_resistant_predator = not child_is_parasite_resistant_predator\n                        mutation_occurred = True\n                    if random.random() < mutation_chance:\n                        child_is_stun_resistant_predator = not child_is_stun_resistant_predator\n                        mutation_occurred = True"
content = content.replace(mut_search, mut_replace)

mut_search2 = "child_is_stun_resistant_predator = not child_is_stun_resistant_predator\n                        mutation_occurred = True\n                    elif mutation_type < 0.999995:\n                        child_is_stun_resistant = not child_is_stun_resistant"
mut_replace2 = "child_is_stun_resistant_predator = not child_is_stun_resistant_predator\n                        mutation_occurred = True\n                    if random.random() < mutation_chance:\n                        child_is_stun_resistant = not child_is_stun_resistant"
content = content.replace(mut_search2, mut_replace2)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
