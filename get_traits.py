import re

with open("src/universe/engine.py", "r") as f:
    engine_content = f.read()

with open("tests/test_engine.py", "r") as f:
    tests = f.read()

# Extract traits from Entity.__init__
match = re.search(r'def __init__\(self, name,[^)]*\):', engine_content)
traits = re.findall(r'(is_[a-z_]+|has_[a-z_]+|can_[a-z_]+|lays_[a-z_]+|disease_vector|pack_hunter)=', match.group(0))

for trait in traits:
    if not re.search(r'def test_.*' + trait, tests, re.IGNORECASE):
        print(trait)
