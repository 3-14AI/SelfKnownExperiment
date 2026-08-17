import re

with open('src/universe/visualizer.py', 'r') as f:
    content = f.read()

replacement = """                    elif getattr(entity, 'is_hypnotic', False):
                        return '•'
                    elif getattr(entity, 'is_tracker', False):
                        return '↬'"""

content = re.sub(r'elif getattr\(entity, \'is_hypnotic\', False\):\n                        return \'•\'', replacement, content)

with open('src/universe/visualizer.py', 'w') as f:
    f.write(content)

with open('used_chars.txt', 'a') as f:
    f.write('\n↬')
