1. **Understand the current next step in `agents.md`:**
    - The most recently completed steps were related to `is_disease_resistant_predator`, `is_venom_resistant_predator`, `is_drought_resistant_predator`, and `is_parasite_resistant_predator`.
    - It's time to add a new predator trait. Let's add `is_stun_resistant_predator`, granting entities with this trait a 1.5x attack multiplier against `is_stun_resistant` entities.
2. **Implement `is_stun_resistant_predator`:**
    - Update `src/universe/engine.py` (class `Entity` constructor) to include `is_stun_resistant_predator` initialization.
    - Implement mutation logic in `Universe.tick()`.
    - Implement attack multiplier logic in `Universe.tick()`.
3. **Add visualizer support:**
    - Update `src/universe/visualizer.py` to assign a character to the `is_stun_resistant_predator` trait.
4. **Write tests:**
    - Create `tests/test_is_stun_resistant_predator.py`.
    - Write tests for combat multiplier and mutation.
    - Write test for visualizer output.
5. **Run all tests:**
    - Execute `pytest tests/` to ensure no regressions are introduced.
6. **Update `agents.md` and `CHANGELOG.md`:**
    - Append the new trait completion to `agents.md` under `## Next Steps`.
    - Document the new trait under `## [Unreleased]` in `CHANGELOG.md`.
7. **Complete pre-commit steps:**
    - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
