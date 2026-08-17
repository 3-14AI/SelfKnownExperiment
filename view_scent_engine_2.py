with open('src/universe/engine.py') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'import math' in line:
        print("".join(lines[i-10:i+20]))
