with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'scent' in line.lower() and 'def tick' in "".join(lines[max(0, i-500):i]):
        start = max(0, i - 15)
        end = min(len(lines), i + 35)
        print(f"Match around line {i}")
        print("".join(lines[start:end]))
        break
