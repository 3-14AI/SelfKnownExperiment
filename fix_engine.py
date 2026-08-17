with open('src/universe/engine.py', 'r') as f:
    content = f.read()

content = content.replace("getattr(entity, \\'is_tracker\\', False)", "getattr(entity, 'is_tracker', False)")
content = content.replace("\\n                    child_is_tracker = getattr(entity, 'is_tracker', False)", "\n                    child_is_tracker = getattr(entity, 'is_tracker', False)")
content = content.replace("\\n                    if random.random() < mutation_chance:\\n                        child_is_tracker = not child_is_tracker", "\n                    if random.random() < mutation_chance:\n                        child_is_tracker = not child_is_tracker")

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
