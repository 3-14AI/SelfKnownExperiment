with open('src/universe/engine.py') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'best_pos = (step_dx, step_dy)' in line:
        print("".join(lines[i-20:i+10]))
        break
