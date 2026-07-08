# Changelog

All notable changes to Project Genesis will be documented in this file.

## [Unreleased]
### Added
- Implemented an energy system and life cycle for entities (entities have 10 starting energy, consume 1 energy per tick, and die if energy drops to 0 or below).
- Expanded unit tests in `tests/test_engine.py` to cover energy decay and death.

## [Previous] - 2026-07-07
### Added
- Analyzed project changes and agent actions and added the results to `analytics/analysis_report.md`.
- Implemented a 2D spatial system in `src/universe/engine.py` (coordinates for Entity, width/height and positioning/movement bounds logic for Universe).
- Added `get_entities_at(x, y)` to Universe to query entity locations.
- Expanded unit tests in `tests/test_engine.py` to cover new spatial features.

## [Previous] - YYYY-MM-DD
### Added
- Added an analytics directory and an analysis report detailing project evolution and agent actions in `analytics/analysis_report.md`.
- Bootstrapped project structure with `src/` and `tests/` directories.
- Implemented core `Universe` and `Entity` classes in `src/universe/engine.py`.
- Added basic unit tests for the core engine in `tests/test_engine.py`.
