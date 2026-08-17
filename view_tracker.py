with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'scent tracking behavior' in line.lower() or 'best_scent' in line:
        start = max(0, i - 15)
        end = min(len(lines), i + 35)
        print(f"Match around line {i}")
        print("".join(lines[start:end]))
        break
