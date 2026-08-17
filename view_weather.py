with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'weather == ' in line:
        start = max(0, i - 2)
        end = min(len(lines), i + 20)
        print("".join(lines[start:end]))
        break
