with open("src/universe/engine.py", "r") as f:
    engine_code = f.read()

patch = """                    if random.random() < mutation_chance:
                        child_is_fire_strider = not child_is_fire_strider
                        mutation_occurred = True
                    if random.random() < mutation_chance:
                        child_is_quicksand_glider = not child_is_quicksand_glider
                        mutation_occurred = True"""

engine_code = engine_code.replace("""                    if random.random() < mutation_chance:
                        child_is_fire_strider = not child_is_fire_strider
                    if random.random() < mutation_chance:
                        child_is_quicksand_glider = not child_is_quicksand_glider
                        mutation_occurred = True
                        mutation_occurred = True""", patch)

with open("src/universe/engine.py", "w") as f:
    f.write(engine_code)
