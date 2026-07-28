import re

with open("src/universe/engine.py", "r") as f:
    engine_content = f.read()

with open("tests/test_engine.py", "r") as f:
    tests = f.read()

# Extract traits from Entity.__init__
match = re.search(r'def __init__\(self, name,[^)]*\):', engine_content)
if match:
    init_sig = match.group(0)
    traits = re.findall(r'(is_[a-z_]+|has_[a-z_]+|can_[a-z_]+|lays_[a-z_]+|disease_vector|pack_hunter)=', init_sig)

    print("Checking tests for traits...")
    for trait in traits:
        # Check if there is a test that mentions this trait
        if trait not in tests:
            print(f"MISSING COMPLETELY: {trait}")
        else:
            # Check if there's a test specifically named for it
            if not re.search(r'def test_.*' + trait, tests, re.IGNORECASE):
                print(f"NO DEDICATED TEST: {trait}")
