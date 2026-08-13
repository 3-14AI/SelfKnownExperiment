with open('src/universe/engine.py') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if "if getattr(prey_to_eat, 'has_horns', False):" in line:
        count += 1
        if count == 2:
            start = max(0, i - 10)
            end = min(len(lines), i + 20)
            print("".join(lines[start:end]))
            break
