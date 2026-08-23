import re

with open('tests/test_engine.py', 'r') as f:
    content = f.read()

# Replace the incorrect test method with the tick-based one
new_test = """    def test_is_volcanic_glider_effect(self):
        from src.universe.engine import Entity, Food
        entity = Entity(name="glider", x=1, y=1, is_volcanic_glider=True, is_sure_footed=True, stamina=50, energy=50)
        self.universe.entities = [entity]
        self.universe.current_event = 'volcano'
        self.universe.event_remaining_time = 5
        self.universe.time = 0

        from unittest import mock
        with mock.patch.object(self.universe, 'find_path', return_value=[(1, 1), (1, 2)]):
            entity.energy = 10
            self.universe.foods = [Food(x=1, y=2, energy=10)]
            self.universe.tick()

        stamina_glider = entity.stamina

        entity_no = Entity(name="no_glider", x=1, y=1, is_volcanic_glider=False, is_sure_footed=True, stamina=50, energy=50)
        self.universe.entities = [entity_no]
        self.universe.current_event = 'volcano'
        self.universe.event_remaining_time = 5
        self.universe.time = 0

        with mock.patch.object(self.universe, 'find_path', return_value=[(1, 1), (1, 2)]):
            entity_no.energy = 10
            self.universe.foods = [Food(x=1, y=2, energy=10)]
            self.universe.tick()

        self.assertTrue(stamina_glider > entity_no.stamina)
"""

match = re.search(r"def test_is_volcanic_glider_effect\(self\):.*?self\.assertTrue\(stamina_glider > entity_no\.stamina\)\n", content, re.DOTALL)
if match:
    content = content[:match.start()] + new_test + content[match.end():]
    with open('tests/test_engine.py', 'w') as f:
        f.write(content)
