import sys

with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'entity.is_alive = False' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 30)
        print("".join(lines[start:end]))
        break
