- `test_is_sand_dweller` in `tests/test_engine.py`
- `test_is_scavenger_mutation` in `tests/test_engine.py`
- `test_mud_dancer_energy_gain` in `tests/test_engine.py`

- `test_is_moon_bather_day_no_bonus` in `tests/test_engine.py`: Failed intermittently with `AssertionError: 9 != 12 : is_moon_bather should grant no bonus during the day`. Likely related to probabilistic energy/stamina drains during the day.
test_is_toxic_inflicts_poison_during_combat_not_just_eat

- `test_is_cave_dancer_mutation` (test_engine.TestIsCaveDancer)

- `test_is_resilient_stun_recovery` (test_engine.TestIsResilient)
- `test_is_wall_strider_defense` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Flaky combat/defense test due to RNG or entity state escaping.

- `test_disease_strider_mutation` in `tests/test_engine.py`: Failed intermittently with `AssertionError: False is not true`. Flaky mutation test.
- `test_is_web_dweller` in `tests/test_engine.py`
- `test_is_storm_dweller` in `tests/test_engine.py`
- `test_is_day_strider_mutation` in `tests/test_engine.py`
- `test_is_magnetic_walker_mutation` in `tests/test_engine.py`
- `test_is_web_strider_defense`: Known flaky test, sometimes prey dies
- `test_is_sleeping`: Known flaky test
- `test_is_night_dweller`: Known flaky test
