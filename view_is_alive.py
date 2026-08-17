with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'def is_alive' in line:
        print("".join(lines[i:i+5]))
        break
