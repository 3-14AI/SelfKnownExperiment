with open('tests/test_engine.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == 'import random' and len(new_lines) > 0 and new_lines[-1].strip() == 'import random':
        continue
    new_lines.append(line)

with open('tests/test_engine.py', 'w') as f:
    f.writelines(new_lines)
