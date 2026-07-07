# Changelog

All notable changes to Project Genesis will be documented in this file.

## [Unreleased] - 2026-07-07
### Added
- Implemented a 2D spatial system in `src/universe/engine.py` (coordinates for Entity, width/height and positioning/movement bounds logic for Universe).
- Added `get_entities_at(x, y)` to Universe to query entity locations.
- Expanded unit tests in `tests/test_engine.py` to cover new spatial features.

## [Previous] - YYYY-MM-DD
### Added
- Bootstrapped project structure with `src/` and `tests/` directories.
- Implemented core `Universe` and `Entity` classes in `src/universe/engine.py`.
- Added basic unit tests for the core engine in `tests/test_engine.py`.
