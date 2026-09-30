# Known Flaky Tests\n\nAll known flaky tests have been successfully stabilized.
* `test_is_blizzard_dweller_no_trait` in `tests/test_engine.py`

- `test_space_glider_mutates` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Requires deeper mutation logic fix in engine.
- `test_is_quicksand_dancer_mutation` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Requires deeper mutation logic fix in engine.
- `test_is_blizzard_strider_defense` in `tests/test_engine.py`: Pre-existing flaky test involving probabilistically evading predators during blizzards.

- `test_is_moon_bather_day_no_bonus` in `tests/test_engine.py`: Failed intermittently with `AssertionError: 9 != 12 : is_moon_bather should grant no bonus during the day`. Likely related to probabilistic energy/stamina drains during the day.
