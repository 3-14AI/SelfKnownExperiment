import re

with open('tests/test_engine.py', 'r') as f:
    content = f.read()

content = content.replace("    def test_is_volcanic_glider_effect(self):\n        from src.universe.engine import Entity, Food", "    def test_is_volcanic_glider_effect(self):\n        from src.universe.engine import Entity, Food")

# Wait, check indentation!
match = re.search(r"    def test_is_volcanic_glider_effect\(self\):.*?from src\.universe\.engine import Entity", content, re.DOTALL)
if match:
    # 4 spaces for def, 8 spaces for from
    print(repr(match.group(0)))
