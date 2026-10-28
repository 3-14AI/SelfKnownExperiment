import re

with open('src/universe/visualizer.py', 'r') as f:
    content = f.read()

# Add visualizer mapping
search = "                    elif getattr(entity, 'is_parasite_resistant_predator', False):\n                        char = 'Ƥ'"
replace = "                    elif getattr(entity, 'is_parasite_resistant_predator', False):\n                        char = 'Ƥ'\n                    elif getattr(entity, 'is_stun_resistant_predator', False):\n                        char = 'Ŝ'"

content = content.replace(search, replace)

with open('src/universe/visualizer.py', 'w') as f:
    f.write(content)
