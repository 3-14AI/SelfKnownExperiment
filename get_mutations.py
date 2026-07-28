import re

with open("tests/test_engine.py", "r") as f:
    tests = f.read()

# Get missing tests for mutations of traits

with open("src/universe/engine.py", "r") as f:
    engine = f.read()

match = re.search(r'def __init__\(self, name,[^)]*\):', engine)
traits = re.findall(r'(is_[a-z_]+|has_[a-z_]+|can_[a-z_]+|lays_[a-z_]+|disease_vector|pack_hunter)=', match.group(0))

for trait in traits:
    if not re.search(f'def test_{trait}_mutation', tests, re.IGNORECASE) and not re.search(f'def test_.*{trait}.*mutat', tests, re.IGNORECASE):
        print(trait)
