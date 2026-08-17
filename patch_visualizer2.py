with open('src/universe/visualizer.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if "elif getattr(entity, 'is_hypnotic', False):" in line:
        new_lines.append("                        return '•'\n")
        new_lines.append("                    elif getattr(entity, 'is_tracker', False):\n")
        new_lines.append("                        return '↬'\n")

# remove duplicate 'return •' lines if needed
cleaned_lines = []
skip_next = False
for i, line in enumerate(new_lines):
    if skip_next:
        skip_next = False
        continue
    cleaned_lines.append(line)
    if "elif getattr(entity, 'is_hypnotic', False):" in line:
        # the original script appended the next line, we need to skip the original return
        skip_next = True

with open('src/universe/visualizer.py', 'w') as f:
    f.writelines(cleaned_lines)
