import re

with open("src/universe/engine.py", "r") as f:
    engine_code = f.read()

with open("tests/test_visualizer.py", "r") as f:
    test_code = f.read()

traits = set(re.findall(r"(is_[a-z_]+|has_[a-z_]+|can_[a-z_]+)", engine_code))

for trait in sorted(traits):
    if trait in engine_code and trait not in test_code:
        print(f"Missing in test_visualizer.py: {trait}")
