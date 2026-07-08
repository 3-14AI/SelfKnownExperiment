# Changelog

All notable changes to Project Genesis will be documented in this file.

## [Unreleased]
### Added
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
