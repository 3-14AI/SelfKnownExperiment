with open('tests/test_engine.py', 'r') as f:
    content = f.read()

# Entity test initializations shouldn't set max_energy, set energy and size correctly
# Let's fix test_engine.py where I added max_energy
content = content.replace("energy=100, max_energy=100, size=2", "energy=100, size=2")

with open('tests/test_engine.py', 'w') as f:
    f.write(content)
