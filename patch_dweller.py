import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# Add missing mutation block
content = content.replace(
    "                    if random.random() < mutation_chance:\n                        child_is_poison_dweller = not child_is_poison_dweller\n                        mutation_occurred = True",
    "                    if random.random() < mutation_chance:\n                        child_is_disease_dweller = not child_is_disease_dweller\n                        mutation_occurred = True\n                    if random.random() < mutation_chance:\n                        child_is_poison_dweller = not child_is_poison_dweller\n                        mutation_occurred = True"
)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
