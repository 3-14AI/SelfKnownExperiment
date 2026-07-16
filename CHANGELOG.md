# CHANGELOG


## [2026-07-15]
### Added
- Expanded entity genetics: Entities now have a chance to mutate their `diet` (e.g., from 'herbivore' to 'carnivore' or vice versa) during reproduction.
- Added `test_diet_mutation` in `tests/test_engine.py` to isolate and verify the diet mutation logic.

## [2026-07-15]

### Added
- Implemented biome-specific entity behavior by adding `preferred_terrain` attribute to entities.
- Entities thriving on their preferred terrain receive reduced energy loss.
- Entities situated outside their preferred terrain (if specified) suffer an additional energy loss penalty.
- Updated `agents.md` to reflect task completion.

### Added
- Analyzed recent project changes (Disease, Scent Trails, Communication, Combat, Symbiosis, Disasters) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.

- Added attack and defense attributes to Entity class, mutation logic for these traits, and probabilistic combat resolution when carnivores hunt prey.
- Implemented a symbiotic relationship system for entities. Entities can now have a `species` and a `symbiotic_with` list. When near their symbiotic partners, they receive a benefit (reduced energy loss). Added `test_symbiosis_benefit` to verify the functionality.
- Added global natural disasters: earthquakes (modifying wall terrain) and volcanoes (spawning ash terrain).
## 2026-07-13
- Implemented Population Limit logic in the Universe engine. Entities will no longer reproduce if the total number of entities reaches or exceeds the `population_limit` (default 1000).
- Added `test_population_limit` in `tests/test_engine.py` to verify this behavior.

## 2026-07-13
- Implemented entity diets (Herbivore/Carnivore). Carnivores hunt and eat herbivores, while herbivores continue to eat static food.
- Updated visualizer to render carnivores as 'C'.

## Today
- Implemented `intelligence` and `inventory` attributes for entities.
- Added crafting mechanics: highly intelligent entities with sufficient energy have a chance to craft tools ('weapon', 'shield', 'clothing') each tick.
- Tools provide distinct advantages: clothing increases temperature tolerance, weapons increase predator attack strength, and shields increase prey defense.
- Genetic inheritance now supports passing down and mutating the `intelligence` attribute.

- Implemented a communication system allowing herbivores to alert nearby flockmates of predators.
- Entities that see a predator communicate its location to flockmates within double their perception radius.
- Alerted entities will actively try to move away from the predator's known location.
- Added `get_nearest_predator` method and `test_communication_alert_predator` tests.
- Implemented scent trails: herbivores leave a scent trail on the terrain as they move, which decays over time.
- Updated carnivore AI to track the strongest adjacent scent trail when no prey is directly visible within perception radius.
- Added tests for scent trails and carnivore tracking behavior.

## 2026-07-14
- Implemented `TemperatureZone` system allowing localized temperature modifiers.
- Added temperature mechanics to entities: they now have a `preferred_temperature` and `temperature_tolerance`.
- Entities suffer an additional energy loss penalty if they are in an environment outside their comfortable temperature bounds.
- Genetic inheritance expanded: child entities now inherit `preferred_temperature` and `temperature_tolerance` from their parent, with a chance to mutate.
- Updated `CLIVisualizer` to display active temperature zones.

- Implemented localized weather events (`rain` and `fire`).
- `rain` has a chance to spawn food within its localized radius.
- `fire` destroys entities and food, and converts existing non-water terrain to `ash`.
- Updated `CLIVisualizer` to render `ash` terrain and display active localized events.

- Implemented Entity Genetics and Mutations. Child entities now inherit `max_age` and `perception_radius` from their parents during reproduction, with a small chance for these traits to mutate.
- Added tests in `test_engine.py` to ensure genetic inheritance and mutations occur as expected.

- Implement entity perception radius. Entities now only detect food and route around obstacles that are within their perception radius (default 10).

# Changelog
## [2026-07-14]
### Added
- Implemented a disease system where spontaneous outbreaks can infect entities.
- Added disease spread logic allowing infected entities to transmit the disease to nearby entities.
- Implemented energy drain penalties and a recovery system for infected entities.
- Updated visualizer to depict sick entities (as 'S' for herbivores and 'X' for carnivores).

## [2026-07-13] - Agent
### Added
- Added seasonal mechanics to the engine (Spring, Summer, Autumn, Winter) affecting food spawn rates and terrain (water freezes to ice in winter).

## [2026-07-13] - Entity Memory

### Added
- Entity instances now maintain a `memory` set to store known obstacle coordinates.
- Entities automatically observe and remember obstacles (walls, water) within their perception radius during each tick.
- The pathfinding algorithm (`find_path`) now uses an entity's memory to avoid routing through remembered obstacles, even if those obstacles are currently outside the entity's perception radius.
- Added tests in `test_engine.py` to ensure memory is updated correctly and utilized in pathfinding.


## [Unreleased]
### Added
- Implemented an experience system for combat interactions:
  - Entities gain attack/defense stats when surviving encounters with predators (escaping).
  - Predators gain attack stats when failing to capture prey (learning from failure).
  - Predators gain larger attack/defense stat boosts when successfully hunting and eating prey.
- Updated `agents.md` to reflect completed tasks and new steps.

## [Unreleased] - 2026-07-10
### Added
- Implemented environmental events system in the Universe engine ('storm', 'drought').
- Storms double entity energy decay, and droughts temporarily halt food spawning.
- Updated `CLIVisualizer` to display the currently active event and its remaining duration.
- Added test coverage for events in `tests/test_engine.py`.
- Updated `agents.md` tracking progress.
- Added `analytics/current_analysis.md` with an analysis of project evolution and agent actions up to the intelligent BFS pathfinding implementation.
- Implemented intelligent pathfinding using Breadth-First Search (BFS). Entities now route around impassable terrain (like walls) to reach their nearest food source.
- Implemented a Terrain system (`Terrain` class) to allow for obstacles like walls (`#`) and water (`~`).
- Entities are now blocked by impassable terrain during movement.
- Updated the visualizer to render the new terrain types.
- Created `simulate.py` to run the universe and continuously visualize the simulation in the terminal in real-time.
- Implemented a basic CLI visualizer (`CLIVisualizer`) in `src/universe/visualizer.py` to display the universe state as a text grid.
- Added unit tests for the visualizer in `tests/test_visualizer.py`.
- Updated `agents.md` tracking progress.

## [2026-07-09]
### Added
- Entity AI behavior: Entities now actively seek out the nearest food source and move towards it each tick instead of remaining stationary.
- Support logic `get_nearest_food` added to the `Universe` class.
- Automated tests covering the food-seeking behavior.

All notable changes to Project Genesis will be documented in this file.

## [Unreleased]
- Engine: Modified `get_nearest_prey` so carnivores evaluate potential prey based on a combination of distance, size, and defense, effectively prioritizing smaller, weaker targets over slightly closer but more resilient ones.
- Tests: Added `test_carnivore_prefers_smaller_weaker_prey` to explicitly test this targeting logic.

### Added
- Entity `size` attribute which scales energy consumption per tick.
- Entity movement speed is now inversely proportional to their `size`.
- Entity `size` can mutate during reproduction.
- Introduced entity temperature preferences and tolerances, leading to increased energy loss in unfavorable climates.
- Enabled inheritance and mutation of temperature traits in offspring entities.
### Added
- Implemented group behavior / flocking for entities. When no food or prey is nearby, entities will naturally move towards the center of mass of nearby entities sharing their diet.


### Added
- Analyzed project changes and agent actions (AI behavior, reproduction, aging) and updated the results in `analytics/analysis_report.md`.
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

- Implemented dynamic terrain generation based on temperature and weather over time. Rain creates mud and washes away ash/sand. High temperatures and droughts create sand. Base temperatures now change dynamically with seasons. Water freezes to ice in cold temperatures and ice melts in warm temperatures.
