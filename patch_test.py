with open("src/universe/engine.py", "r") as f:
    c = f.read()
if "has_scales" not in c:
    print("Not patched yet")
