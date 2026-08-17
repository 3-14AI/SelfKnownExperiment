# The entity in the test didn't move because there is a condition before scent tracking:
# if target_species in entity.target_species ...
# Scent tracking only happens for predators looking for prey, but we initialized it with diet='herbivore' probably.
with open('tests/test_engine.py', 'r') as f:
    content = f.read()

# Make it a predator so it tracks scents
content = content.replace('entity = Entity(name="tracker", x=5, y=5, is_tracker=True, stamina=50, max_stamina=50, energy=100)', 'entity = Entity(name="tracker", x=5, y=5, is_tracker=True, stamina=50, max_stamina=50, energy=100, diet="carnivore", target_species=["prey"])')

with open('tests/test_engine.py', 'w') as f:
    f.write(content)
