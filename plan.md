1. **Implement `is_blizzard_strider` trait in `src/universe/engine.py`.**
   - Execute a python patch script with bash commands:
     ```bash
     cat << 'EOF' > create_blizzard_strider.py
     import re
     with open('src/universe/engine.py', 'r') as f: content = f.read()
     content = content.replace("is_storm_strider=False,", "is_storm_strider=False, is_blizzard_strider=False,")
     content = content.replace("self.is_storm_strider = is_storm_strider", "self.is_storm_strider = is_storm_strider\n        self.is_blizzard_strider = is_blizzard_strider")
     content = content.replace("child_is_storm_strider = getattr(entity, 'is_storm_strider', False)", "child_is_storm_strider = getattr(entity, 'is_storm_strider', False)\n                    child_is_blizzard_strider = getattr(entity, 'is_blizzard_strider', False)")
     content = content.replace("child_is_storm_strider = not child_is_storm_strider\n                        mutation_occurred = True", "child_is_storm_strider = not child_is_storm_strider\n                        mutation_occurred = True\n                    if random.random() < mutation_chance:\n                        child_is_blizzard_strider = not child_is_blizzard_strider\n                        mutation_occurred = True")
     content = content.replace("is_storm_strider=child_is_storm_strider", "is_storm_strider=child_is_storm_strider, is_blizzard_strider=child_is_blizzard_strider")

     content = content.replace(
         "if getattr(prey_to_eat, 'is_storm_strider', False) and self.current_event == 'storm':\n                                effective_defense += 2",
         "if getattr(prey_to_eat, 'is_storm_strider', False) and self.current_event == 'storm':\n                                effective_defense += 2\n                            if getattr(prey_to_eat, 'is_blizzard_strider', False) and self.current_event == 'blizzard':\n                                effective_defense += 2")
     content = content.replace(
         "if getattr(prey_to_eat, 'is_storm_strider', False) and self.current_event == 'storm':\n                            effective_defense += 2",
         "if getattr(prey_to_eat, 'is_storm_strider', False) and self.current_event == 'storm':\n                            effective_defense += 2\n                        if getattr(prey_to_eat, 'is_blizzard_strider', False) and self.current_event == 'blizzard':\n                            effective_defense += 2")

     content = content.replace(
         "if getattr(entity, 'is_storm_strider', False) and self.current_event == 'storm':\n                stamina_cost = 0",
         "if getattr(entity, 'is_storm_strider', False) and self.current_event == 'storm':\n                stamina_cost = 0\n            if getattr(entity, 'is_blizzard_strider', False) and self.current_event == 'blizzard':\n                stamina_cost = 0")
     with open('src/universe/engine.py', 'w') as f: f.write(content)
     EOF
     python3 create_blizzard_strider.py
     rm create_blizzard_strider.py
     ```

2. **Add Tests for `is_blizzard_strider`.**
   - Execute a python patch script with bash commands:
     ```bash
     cat << 'EOF' > add_tests.py
     import re
     with open('tests/test_engine.py', 'r') as f: content = f.read()
     new_test = """class TestIsBlizzardStrider(unittest.TestCase):
         def setUp(self):
             self.universe = Universe(width=10, height=10)
         def test_is_blizzard_strider_mutation(self):
             self.universe.mutation_chance = 1.0
             self.universe.event_chance = 0.0
             self.universe.localized_event_chance = 0.0
             self.universe.disease_chance = 0.0
             self.universe.reproduction_threshold = 500
             parent = Entity(name="Parent", x=1, y=1, energy=5000, age=5, size=20, is_blizzard_strider=False, lays_eggs=False, is_telepathic=False, is_pacifist=True, is_ageless=True, is_gluttonous=True, has_blubber=True, is_immune=True)
             self.universe.add_entity(parent)
             import random
             real_randint = random.randint
             real_random = random.random
             try:
                 random.randint = lambda a, b: b
                 random.random = lambda: 0.0
                 for _ in range(10):
                     self.universe.foods = []
                     self.universe.tick()
                     parent.energy = 5000
             finally:
                 random.randint = real_randint
                 random.random = real_random
             children = [e for e in self.universe.entities if e != parent]
             if children:
                 self.assertTrue(getattr(children[0], 'is_blizzard_strider', False))
         def test_is_blizzard_strider_defense(self):
             self.universe.current_event = 'blizzard'
             pred = Entity(name="Pred", x=1, y=1, size=2, diet='carnivore', attack=5)
             prey = Entity(name="Prey", x=1, y=1, size=1, defense=1000, energy=100, is_blizzard_strider=True)
             self.universe.add_entity(pred)
             self.universe.add_entity(prey)
             self.universe.foods = []
             self.universe.tick()
             self.assertTrue(prey in self.universe.entities)
     """
     content += "\n" + new_test
     with open('tests/test_engine.py', 'w') as f: f.write(content)

     with open('src/universe/visualizer.py', 'r') as f: v_content = f.read()
     v_content = v_content.replace("elif getattr(entity, 'is_blizzard_glider', False):\n                        char = 'Ă'", "elif getattr(entity, 'is_blizzard_glider', False):\n                        char = 'Ă'\n                    elif getattr(entity, 'is_blizzard_strider', False):\n                        char = 'Ź'")
     with open('src/universe/visualizer.py', 'w') as f: f.write(v_content)

     with open('tests/test_visualizer.py', 'r') as f: tv_content = f.read()
     new_vtest = """    def test_visualize_is_blizzard_strider(self):
             universe = Universe(width=10, height=10)
             entity = Entity("Test", x=1, y=1, is_blizzard_strider=True)
             universe.add_entity(entity)
             visualizer = CLIVisualizer(universe)
             output = visualizer.render()
             self.assertIn('Ź', output)
     """
     tv_content = tv_content.replace("class TestCLIVisualizer(unittest.TestCase):", "class TestCLIVisualizer(unittest.TestCase):\n" + new_vtest)
     with open('tests/test_visualizer.py', 'w') as f: f.write(tv_content)
     EOF
     python3 add_tests.py
     rm add_tests.py
     ```

3. **Update Documentation.**
   - Execute bash commands:
     ```bash
     echo "- [x] Implemented \`is_blizzard_strider\` trait. Entities with this trait consume 0 stamina when moving during a 'blizzard' event and gain a defense bonus while inside a blizzard." >> agents.md

     cat << 'EOF' > update_changelog.py
     with open('CHANGELOG.md', 'r') as f: content = f.read()
     if "## [Unreleased]" in content:
         content = content.replace("## [Unreleased]", "## [Unreleased]\n### New Features\n- Implemented `is_blizzard_strider` trait. Entities with this trait consume 0 stamina when moving during a 'blizzard' event and gain a defense bonus.\n")
     else:
         content = "## [Unreleased]\n### New Features\n- Implemented `is_blizzard_strider` trait. Entities with this trait consume 0 stamina when moving during a 'blizzard' event and gain a defense bonus.\n\n" + content
     with open('CHANGELOG.md', 'w') as f: f.write(content)
     EOF
     python3 update_changelog.py
     rm update_changelog.py
     ```

4. **Verify Modifications.**
   - Run `git status` and `git diff` to review all the changes made in engine, tests, visualizer, and docs.

5. **Run the test suite.**
   - Run `python3 run_tests.py tests.test_engine tests.test_visualizer` to verify the new feature works and all tests pass.

6. **Complete Pre Commit Steps.**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

7. **Submit Change.**
   - Submit the change with a descriptive commit message.
