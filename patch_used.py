with open("used_chars.txt", "r") as f:
    lines = f.read().splitlines()

# the last line seems corrupted. Let's fix it
lines = [l.replace('↬±', '↬') for l in lines if l]
if '±' not in lines:
    lines.append('±')

with open("used_chars.txt", "w") as f:
    f.write('\n'.join(lines) + '\n')
