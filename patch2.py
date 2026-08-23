import re

with open('tests/test_engine.py', 'r') as f:
    content = f.read()

content = content.replace("        def test_is_volcanic_glider_effect(self):\n        from src.universe.engine import Entity", "    def test_is_volcanic_glider_effect(self):\n        from src.universe.engine import Entity")

with open('tests/test_engine.py', 'w') as f:
    f.write(content)
