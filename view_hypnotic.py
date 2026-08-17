with open('src/universe/engine.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'prey_to_eat, \'is_hypnotic\'' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 5)
        print("".join(lines[start:end]))
        print("-------")
