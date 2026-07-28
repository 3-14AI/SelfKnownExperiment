import re
with open("agents.md", "r") as f:
    agents = f.read()

with open("tests/test_engine.py", "r") as f:
    tests = f.read()

traits = re.findall(r'`(is_[a-z_]+|has_[a-z_]+|can_[a-z_]+|lays_[a-z_]+)`', agents)
# add pack_hunter
traits.append("pack_hunter")

missing = []
for trait in set(traits):
    if trait not in tests:
        missing.append(trait)

print("Missing tests for traits:")
for m in missing:
    print(m)
