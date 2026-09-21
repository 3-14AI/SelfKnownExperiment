1. **Implement `is_earthquake_strider` trait.**
   - In `src/universe/engine.py`, add `is_earthquake_strider=child_is_earthquake_strider` to `Entity.__init__`.
   - Update `stamina_cost` calculation in `Universe.move_entity()` to consume 0 stamina during an `earthquake` event for entities with this trait.
   - Update `effective_defense` calculation in `Universe.tick()` to add `+2` defense during an `earthquake` event for entities with this trait.
2. **Implement `is_earthquake_strider` visualizer rendering.**
   - In `src/universe/visualizer.py`, assign a unique character (e.g., `'ē'`) for entities with the `is_earthquake_strider` trait.
3. **Add tests for `is_earthquake_strider`.**
   - Add unit tests in `tests/test_engine.py` for stamina cost, defense bonus, and mutation logic.
   - Add a rendering test in `tests/test_visualizer.py`.
4. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
   - Ensure all tests pass successfully.
5. **Submit the change.**
   - Once verified, document the change in `CHANGELOG.md` and `agents.md` and submit.
