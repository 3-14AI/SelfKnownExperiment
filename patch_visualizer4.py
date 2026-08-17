with open('src/universe/visualizer.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "char = '•'" in line and "char = '↬'" in new_lines[-1]:
        continue
    new_lines.append(line)

with open('src/universe/visualizer.py', 'w') as f:
    f.writelines(new_lines)
