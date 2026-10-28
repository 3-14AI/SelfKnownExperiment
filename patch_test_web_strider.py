with open('tests/test_engine_striders.py', 'r') as f:
    content = f.read()

search = "        pred = Entity(name=\"Pred\", x=1, y=1, size=2, diet='carnivore', attack=5, target_species=[\"PreyType\"], stamina=50)\n        prey = Entity(name=\"Prey\", species=\"PreyType\", x=1, y=1, size=1, defense=1000, energy=100, is_web_strider=True, is_ageless=True, is_immune=True, stamina=50)"
replace = "        pred = Entity(name=\"Pred\", x=1, y=1, size=2, energy=20)\n        pred.diet = 'carnivore'\n        pred.attack = 5\n        pred.target_species = [\"PreyType\"]\n        pred.stamina = 50\n        prey = Entity(name=\"Prey\", species=\"PreyType\", x=1, y=1, size=1, energy=100, is_web_strider=True, is_ageless=True, is_immune=True)\n        prey.defense = 1000\n        prey.stamina = 50"

content = content.replace(search, replace)
with open('tests/test_engine_striders.py', 'w') as f:
    f.write(content)
