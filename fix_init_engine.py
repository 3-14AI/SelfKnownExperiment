import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# Fix __init__ signature
pattern = r"is_night_glider=False, is_snow_glider=False\):"
replacement = r"is_night_glider=False, is_snow_glider=False, is_spring_glider=False):"
content = re.sub(pattern, replacement, content)

with open('src/universe/engine.py', 'w') as f:
    f.write(content)
