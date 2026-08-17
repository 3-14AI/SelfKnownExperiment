import re

with open('src/universe/engine.py', 'r') as f:
    content = f.read()

# is_tracker in __init__ didn't get added correctly due to regex mismatch or syntax issues. Let's fix it safely.
# Wait, let's check what __init__ signature looks like.
