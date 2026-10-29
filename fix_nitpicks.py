import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# Fix duplicated assignment
content = content.replace(
    'self.is_cold_blooded_predator = is_cold_blooded_predator\n        self.is_cold_blooded_predator = is_cold_blooded_predator',
    'self.is_cold_blooded_predator = is_cold_blooded_predator'
)

# Fix empty mutation block if it exists
# We need to find the empty block and remove it carefully.
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'if random.random() < mutation_chance:' in line:
        # Check next line
        if i + 1 < len(lines) and 'mutation_occurred = True' in lines[i+1] and (i+2 >= len(lines) or 'child_' not in lines[i+2] and 'if random' not in lines[i+2] and 'mutated_' not in lines[i+2]):
            # Let's be careful. The empty block looks like:
            # if random.random() < mutation_chance:
            #     mutation_occurred = True
            # if the next line is the start of another block or we can just look for the exact sequence.
            pass
    i += 1

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
