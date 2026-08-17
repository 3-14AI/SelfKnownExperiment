with open("agents.md") as f:
    lines = f.readlines()

for i in range(len(lines)-1, -1, -1):
    if lines[i].startswith("- [x] Implemented `is_"):
        print(lines[i].strip())
        break
