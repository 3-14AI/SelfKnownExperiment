with open('src/universe/visualizer.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if "elif getattr(entity, 'is_hypnotic', False):" in line:
        new_lines.append("                        char = '•'\n")
        new_lines.append("                    elif getattr(entity, 'is_tracker', False):\n")
        new_lines.append("                        char = '↬'\n")

# filter out the incorrect one
cleaned = []
skip = False
for i, line in enumerate(new_lines):
    if skip:
        skip = False
        continue
    if "elif getattr(entity, 'is_tracker', False):" in line and "return" in new_lines[i+1]:
        skip = True
        continue
    if "char = '•'" in line and "char = '•'" in new_lines[i-1] if i > 0 else False:
        continue
    if "return '↬'" in line:
        continue
    cleaned.append(line)

with open('src/universe/visualizer.py', 'w') as f:
    f.writelines(cleaned)
