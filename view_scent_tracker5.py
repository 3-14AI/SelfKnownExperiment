with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'best_scent = 0' in line and i > 2400:
        start = max(0, i - 5)
        end = min(len(lines), i + 20)
        print(f"Match around line {i}")
        print("".join(lines[start:end]))
        break
