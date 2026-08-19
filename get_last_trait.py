import re

with open('agents.md') as f:
    text = f.read()

completed_items = re.findall(r'- \[x\] Implemented `([^`]+)` trait\.', text)
print("Last 10 completed traits:")
for item in completed_items[-10:]:
    print(item)
