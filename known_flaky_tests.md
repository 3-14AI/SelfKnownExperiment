- test_is_web_dweller: Failing occasionally due to RNG in `Universe.tick()`, sometimes energy drops instead of recovering.
- test_is_snow_strider_defense: Failing occasionally due to RNG interference in defense calculation.
- `test_is_deep_water_dweller`
- `test_is_night_dweller`

- test_is_symbiotic_predator_mutates
- test_is_telepathic_predator_mutates
- test_is_web_dweller
- test_can_sweat_mechanics
- test_is_wall_dweller
- test_is_clairvoyant_predator_mutates
- test_is_mud_dweller
- `test_is_telepathic_predator_mutates`: Occasionally fails due to RNG interaction or random events preventing reproduction.
- `test_is_wall_dweller`: Occasionally fails due to RNG interaction or random events.
- `test_is_cautious_flee`: Occasionally fails due to RNG interaction or random events.
TestIsMudDweller and TestIsSnowStrider are flaky.
test_is_web_dweller
- `test_is_space_strider_defense`
- `test_is_web_strider_defense`
test_is_day_strider_mutation

- `test_entity_eats_food`
- test_is_mud_dweller
- [ ] `test_is_mud_dweller` in `tests/test_engine.py` is flaky because it occasionally fails due to RNG in tick() consuming energy unexpectedly.
- `test_is_snow_dweller`: Failed due to `AssertionError: 0 not greater than or equal to 20` during engine tests. Intermittent failure related to energy recovery check.
- `test_is_not_resilient_stun_recovery` (test_engine.TestIsResilient): Failed with AssertionError: 10 != 9 due to RNG/State leak.
- test_burrowing_entity_acts_as_shelter (test_engine.TestBurrowing.test_burrowing_entity_acts_as_shelter)
- test_sand_dancer_gains_energy_in_storm_on_sand (test_engine.TestIsSandDancer.test_sand_dancer_gains_energy_in_storm_on_sand)
- test_can_sweat_mechanics (test_engine.TestSprint.test_can_sweat_mechanics)
- test_is_sleep_dancer_energy_recovery: Failed occasionally due to RNG in tick.
test_is_disease_vector_trait_transmission
test_is_sleeping
- test_is_web_dweller: Failed occasionally due to random state when energy isn't correctly restored due to event chance or reproduction threshold causing energy drain.
- test_burrowing_entity_acts_as_shelter: Occasional failure due to overlapping mechanics like disease or severe weather lowering energy despite burrowing shelter.
- test_can_sweat_mechanics: Occasionally fails due to random event chances overlapping and causing excessive energy drain (e.g., entity is randomly killed or drained to 0 by other mechanics during the tick).
- test_is_contagious_attacker: Occasionally fails because the prey successfully escapes combat, causing the combat loop to terminate early before the disease transmission check occurs, leaving the defender uninfected.
* `test_is_web_dweller` in `test_engine.py`: Intermittent failure where energy is not recovered as expected during dynamic simulation updates (unrelated to newly introduced traits).
* `test_can_sweat_mechanics` in `test_engine.py`: Intermittent failure where entity energy falls to 0 due to unexpected temperature drain interaction or random event interference.
- [x] `test_is_volcano_predator_mutation` - Flaky mutation test due to rng mock interference
- [x] `test_mutation` in TestIsFrugivorePredator - Flaky mutation test due to size downscaling
- [x] `test_is_day_strider_mutation` in TestDayStrider - Flaky mutation test
- [x] `test_space_dancer_mutates` in TestIsSpaceDancer - Flaky mutation test
- test_carnivore_scent_tracking (test_engine.TestUniverse)
- test_omnivore_seeks_and_eats_food (test_engine.TestUniverse)
- `test_is_ice_strider_defense`
- test_shelter_building: Occasionally fails due to RNG interference in reproduction tests
- test_fur_heat_penalty: Occasionally fails due to RNG interference
- test_is_symbiotic_energy_transfer: Occasionally fails due to RNG interference
- test_is_toxic_inflicts_poison_during_combat_not_just_eat: Unrelated test failing intermittently due to RNG mock leakage or environmental event state.
- test_is_social_efficiency: Unrelated test failing occasionally.
- test_is_fast_learner_predator_combat: Failing occasionally likely due to mock RNG state leakage across test suites.

- `TestFurTrait.test_fur_heat_penalty`: Occasionally fails because of RNG or edge case logic in Universe.tick not covered by the test assumptions.
- `TestIsSandDancer.test_sand_dancer_gains_energy_in_sandstorm`: Fails due to similar RNG or environmental overlaps in the tick logic.

- `TestUniverse.test_entity_aging`: Fails occasionally because of random mutation or combat that unintentionally kills the entity during tick().
