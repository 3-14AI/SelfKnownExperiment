1. Implement `is_fire_resistant` trait. Entities with this trait do not take damage from fire terrain.
2. Implement `is_fire_resistant_predator` trait. Entities with this trait gain an attack multiplier of 1.5x when attacking entities with the `is_fire_resistant` trait.
3. Update `src/universe/engine.py` to add `is_fire_resistant` and `is_fire_resistant_predator` traits, modify entity logic for damage calculation and reproduction logic for mutation.
4. Update `src/universe/visualizer.py` to map these traits to render characters.
5. Create tests in `tests/test_engine_traits.py` or a suitable file for testing `is_fire_resistant` mechanics.
6. Create tests in `tests/test_engine_predators.py` for testing `is_fire_resistant_predator` mechanics.
7. Update `agents.md` with the completed step.
8. Run pre-commit checks.
9. Submit changes.
