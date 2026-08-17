with open('src/universe/engine.py', 'r') as f:
    content = f.read()

content = content.replace("is_hypnotic=False):", "is_hypnotic=False, is_tracker=False):")

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
