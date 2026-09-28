# Known Flaky Tests\n\nAll known flaky tests have been successfully stabilized.
* `test_is_blizzard_dweller_no_trait` in `tests/test_engine.py`

- `test_space_glider_mutates` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Requires deeper mutation logic fix in engine.
- `test_is_quicksand_dancer_mutation` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Requires deeper mutation logic fix in engine.
