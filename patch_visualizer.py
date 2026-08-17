with open("src/universe/visualizer.py", "r") as f:
    content = f.read()

target_search = """                    elif getattr(entity, 'is_sun_tracker', False):
                        char = '¤'"""
target_replace = """                    elif getattr(entity, 'is_sun_tracker', False):
                        char = '¤'
                    elif getattr(entity, 'is_empathic', False):
                        char = '±'"""
content = content.replace(target_search, target_replace)

with open("src/universe/visualizer.py", "w") as f:
    f.write(content)

