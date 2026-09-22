1. **Verify unstaged changes.**
   - Run `git status` and `git diff` using `run_in_bash_session` to verify the fix for `test_ice_dancer_mutation` is correctly applied.
2. **Implement `is_volcanic_strider` trait.**
   - Use `run_in_bash_session` to run a Python script that injects `is_volcanic_strider=child_is_volcanic_strider` into `Entity.__init__` in `src/universe/engine.py`.
   - Update `stamina_cost` calculation in `Universe.move_entity()` to consume 0 stamina during a `volcano` event for entities with this trait. The script will use `str.replace` near `is_earthquake_strider`.
   - Update `effective_defense` calculation in `Universe.tick()` to add `+2` defense during a `volcano` event for entities with this trait. The script will use `str.replace` near `is_water_strider` (which was confirmed to be present in the `effective_defense` code block).
   - Add mutation logic in `Universe.tick()` for `child_is_volcanic_strider`. The script will use `str.replace` near `child_is_earthquake_strider`.
3. **Verify engine modifications.**
   - Use `run_in_bash_session` to execute `python3 -m py_compile src/universe/engine.py` and `git diff` to verify the syntax and changes in `src/universe/engine.py`.
4. **Implement `is_volcanic_strider` visualizer rendering.**
   - Use `run_in_bash_session` to run a Python script that injects the character mapping `elif getattr(entity, 'is_volcanic_strider', False):\n                        char = 'ṽ'` near `is_earthquake_strider` in `src/universe/visualizer.py`.
5. **Verify visualizer modifications.**
   - Use `run_in_bash_session` to execute `python3 -m py_compile src/universe/visualizer.py` and `git diff` to verify the syntax and changes in `src/universe/visualizer.py`.
6. **Add tests for `is_volcanic_strider`.**
   - Use `run_in_bash_session` with a Python script to inject unit tests (`TestIsVolcanicStrider` class) into `tests/test_engine.py`. The new tests will be appended to the file.
   - Use `run_in_bash_session` with a Python script to inject a rendering test `test_visualize_is_volcanic_strider` into `tests/test_visualizer.py`. The test will be appended to the file.
7. **Verify test modifications.**
   - Use `run_in_bash_session` to run `python3 -m py_compile tests/test_engine.py tests/test_visualizer.py` and `git diff`.
8. **Run tests.**
   - Use `run_in_bash_session` to execute `python3 run_tests.py` to ensure all tests pass.
9. **Complete pre-commit steps.**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
10. **Document and submit the change.**
    - Use `run_in_bash_session` to append the update to `CHANGELOG.md` and `agents.md`.
    - Use the `submit` tool to submit the changes.
