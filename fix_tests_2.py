with open('tests/test_engine.py', 'r') as f:
    content = f.read()

import re

# Fix random import in test_engine
content = content.replace("        original_random = random.random", "        import random\n        original_random = random.random")

with open('tests/test_engine.py', 'w') as f:
    f.write(content)
