# Changelog

## [2026-07-09]
### Added
- Entity AI behavior: Entities now actively seek out the nearest food source and move towards it each tick instead of remaining stationary.
- Support logic `get_nearest_food` added to the `Universe` class.
- Automated tests covering the food-seeking behavior.

All notable changes to Project Genesis will be documented in this file.

## [Unreleased]
### Added
- Implemented an aging system for entities. Entities now age each tick and will naturally die if their age exceeds their `max_age`.
- Added tests for the new aging system in `tests/test_engine.py`.
- Implemented entity reproduction/spawning mechanics. Entities can spawn an offspring at their exact location if their energy exceeds a set threshold.
- Updated unit tests in `tests/test_engine.py` to assert the correctness of reproduction mechanics (correct parent energy decay, child position and naming).
- Implemented a food/resource system. Added `Food` class and updated `Universe` to store food, allow adding food, and enable entities to consume food during `tick()` to regain energy.
- Added unit tests in `tests/test_engine.py` to cover food creation, bounds checking, and consumption mechanics.
- Added a `Food` class and implemented a food/resource system. Food randomly spawns in the Universe, and entities consume food at their exact location to regain energy.
- Implemented basic energy and life cycle for entities. Entities now consume 1 energy per tick and are removed from the universe when their energy reaches 0.
- Implemented an energy system and life cycle for entities (entities have 10 starting energy, consume 1 energy per tick, and die if energy drops to 0 or below).
- Expanded unit tests in `tests/test_engine.py` to cover energy decay and death.
## [Unreleased] - 2026-07-08
### Added
- Implemented basic energy and life cycle for entities (entities have starting energy, lose 1 per tick, and die at 0).
- Wrote tests for energy consumption and death logic in `tests/test_engine.py`.
- Updated `agents.md` tracking progress.

## [Previous] - 2026-07-07
### Added
- Analyzed project changes and agent actions and added the results to `analytics/analysis_report.md`.
- Implemented a 2D spatial system in `src/universe/engine.py` (coordinates for Entity, width/height and positioning/movement bounds logic for Universe).
- Added `get_entities_at(x, y)` to Universe to query entity locations.
- Expanded unit tests in `tests/test_engine.py` to cover new spatial features and life cycle.

## [Previous] - YYYY-MM-DD
### Added
- Added an analytics directory and an analysis report detailing project evolution and agent actions in `analytics/analysis_report.md`.
- Bootstrapped project structure with `src/` and `tests/` directories.
- Implemented core `Universe` and `Entity` classes in `src/universe/engine.py`.
- Added basic unit tests for the core engine in `tests/test_engine.py`.
