# check why tracker didn't move
with open('tests/test_engine.py', 'r') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'def test_is_tracker_scent_detection' in line:
        print("".join(lines[i:i+20]))
        break
