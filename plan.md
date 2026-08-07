1. Add `is_reckless` trait logic.
    - Entities with this trait deal double damage (effective attack * 2) but their effective defense is reduced to 0 during combat, making them glass cannons.
2. Add `is_reckless` rendering to Visualizer.
    - Modify `src/universe/visualizer.py` to add a new visual representation `<`.
3. Update tests.
    - Add tests to ensure `is_reckless` correctly doubles attack and zeros out defense during combat.
    - Ensure it is correctly tested in mutation and rendering.
4. Complete pre commit steps
    - Complete pre commit steps to make sure proper testing, verifications, reviews and reflections are done.
5. Submit the change.
    - Once all tests pass, I will submit the change with a descriptive commit message.
