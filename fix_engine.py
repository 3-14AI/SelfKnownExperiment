with open("src/universe/engine.py", "r") as f:
    content = f.read()

# Fix duplicates injected by previous script
content = content.replace("is_dust_bather=child_is_dust_bather, is_dust_bather=child_is_dust_bather", "is_dust_bather=child_is_dust_bather")
content = content.replace("self.is_dust_bather = is_dust_bather\n        self.is_dust_bather = is_dust_bather", "self.is_dust_bather = is_dust_bather")
content = content.replace("child_is_dust_bather = getattr(entity, 'is_dust_bather', False)\n                    child_is_dust_bather = getattr(entity, 'is_dust_bather', False)", "child_is_dust_bather = getattr(entity, 'is_dust_bather', False)")

content = content.replace("if random.random() < mutation_chance:\n                        child_is_dust_bather = not child_is_dust_bather\n                        mutation_occurred = True\n                    if random.random() < mutation_chance:\n                        child_is_dust_bather = not child_is_dust_bather\n                        mutation_occurred = True", "if random.random() < mutation_chance:\n                        child_is_dust_bather = not child_is_dust_bather\n                        mutation_occurred = True")



with open("src/universe/engine.py", "w") as f:
    f.write(content)
