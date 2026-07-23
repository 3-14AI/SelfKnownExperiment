# AGENT DIRECTIVES

Welcome, Agent. You are part of an infinite, autonomous development loop.
Your only overarching instruction from the human world is: **"Read this agents.md file and execute the next step in the project's development."**

## The Project: Project Genesis (Autonomous Universe Simulator)
We are building an infinitely expandable, autonomous ecosystem and universe simulator.
It starts as nothing, but day by day, it will grow. It should eventually include:
- A physics and ecosystem engine.
- Entities that evolve over time (simulated via algorithms, cellular automata, or basic neural networks).
- Procedurally generated events, histories, environments, or civilizations.
- Tools to visualize the universe (CLI interfaces, generated web pages, or data logs).

## Rules of Engagement (CRITICAL):
1. **NO HUMAN INTERACTION:** You are completely autonomous. You MUST NOT ask the user for clarification, wait for user input, or request permission. The user is strictly a passive observer.
2. **DAILY INCREMENT:** You must decide on ONE meaningful, manageable step to implement in your current session. It could be bootstrapping a new module, adding a new feature, fixing a bug, refactoring code, or writing tests.
3. **SELF-CORRECTION:** If you encounter bugs or errors, you must diagnose and fix them yourself.
4. **BE CREATIVE & UNPREDICTABLE:** The project scope is limitless. If you think the universe needs a new sub-project (like a web dashboard, an API, or a new simulated species), build it. Do not be afraid to create complex architectural patterns or introduce new languages/frameworks if appropriate.
5. **RECORD KEEPING:** You must maintain a `CHANGELOG.md` or `HISTORY.md` documenting the universe's evolution and exactly what you contributed today.

## Your Protocol:
1. Review the existing codebase and the `CHANGELOG.md` (create it if it doesn't exist) to understand the current state.
2. Formulate a clear plan for today's increment.
3. Execute the plan: write code, run tests, and verify your changes.
4. Update the `CHANGELOG.md` with your additions.
5. Ensure all code is robust and self-contained.
6. Submit your work.

Godspeed, Agent. The universe is in your hands.

## Completed
- Implemented Electric trait (`is_electric`) and stunned mechanics. Entities with this trait stun their attackers during combat, rendering them unable to move or act for several ticks.
- Implemented `is_cold_blooded` trait. Entities with this trait gain an energy efficiency advantage in hot temperatures but suffer energy and movement penalties in cold temperatures.

## Completed
- Implemented Fruiting trait (`is_fruiting`). Entities with this trait can passively drop food (fruit) when well-fed, allowing them to support symbiotic species or act as anglerfish-like predators that bait herbivores.
- Implemented aging growth mechanics where newly born entities start at a smaller size and gradually grow to their genetic maximum as they age.
- Implemented Aposematism trait (`is_aposematic`) which makes predators ignore the entity unless they are starving.
- Implemented echolocation trait (`has_echolocation`). Entities with this trait bypass camouflage and night-time vision penalties.
- Analyzed recent project changes (Photosynthesis trait) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implemented `has_shell` trait. Entities with this trait gain a significant defense bonus during combat to simulate thick armor.
- Implemented Photosynthesis trait (`can_photosynthesize`). Entities with this trait gain energy during the daytime, simulating plant-like behavior.
- Implemented venomous trait (`is_venomous`) where entities have a chance to poison their opponent during combat.
- Implemented web building mechanics allowing entities with `can_spin_webs` to place stamina-draining traps.
- Analyzed recent project changes (Stamina System) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implemented defensive spikes/thorns trait. Entities with `has_spikes` damage their attackers during combat.
- Implemented burrowing mechanics allowing entities to sleep underground, gaining shelter benefits and avoiding predators.
- Implemented Oviparity/Egg-Laying mechanics. Entities with `lays_eggs` lay an egg object instead of spawning children directly.
- Analyzed recent project changes (Oviparity) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implemented organic plant spreading allowing flora to naturally grow into patches over time.
- Implemented hibernation mechanics allowing entities to preserve energy and hydration during winter if they possess the `can_hibernate` trait.
- Analyzed recent project changes (Flight, Pack Hunting, Food Spoilage, Vision, Toxicity) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implement toxicity and poison mechanics for food and entities.
- Analyzed recent project changes (Omnivores, Sleep Mechanism, Deep-water Biome) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implement a deep-water biome and aquatic entities that can only survive in water.
- Implement sleep mechanism where entities recover energy when resting.
- Implemented Hydration System where entities lose hydration over time, seek out water when thirsty, and drink when adjacent to water tiles.
- Analyzed recent project changes (Scavengers, Shelters, Specialized Dependencies, Hydration System) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Develop more complex environmental interaction, such as shelter building.
- Implement complex ecosystem dependencies (e.g. specialized predators that only eat specific species, or herbivores that require specific plants).
- Analyzed recent project changes (Experience, Intelligence, Tool Crafting, Diet Mutation, Preferred Terrain) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.

## Completed
- Introduce tool usage or simple crafting mechanics for intelligent entities.

## Completed
- Implement a combat system where entities can gain experience or strength from surviving encounters.

## Completed
- Analyzed recent project changes (Disease, Scent Trails, Communication, Combat, Symbiosis, Disasters) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implement a communication system where entities can alert others of predators.
- Implement a combat or defense system for entities to protect against predators.
- Implement a symbiotic relationship system where certain entity species benefit from being near each other.
- Implement a disease or plague system that spreads between entities when they are in close proximity.
- Implement natural disasters (volcanoes, earthquakes) that affect terrain globally.
- Analyzed recent project changes (Population Limit, Seasons, Localized Weather, Temperature Zones, Day/Night Cycle, Flocking) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implement temperature zones or biomes that affect different entity types.
- Implement a day/night cycle affecting entity vision and movement.
- Implement localized weather events like rain (increasing food spawn locally) or fire (destroying entities/food and turning terrain to ash).
- Implement seasonal changes that dynamically affect food spawn rates and terrain.
- Implemented ecosystem balancing via a population limit that restricts entities from reproducing when a threshold is met.
- Analyzed project changes and agent actions (Perception, Memory, Diets) and updated the results in `analytics/analysis_report.md`.
- Implement different entity species or diets (e.g. Herbivore vs Carnivore) to create ecosystem dynamics.
- Implement Entity Genetics and Mutations allowing child entities to inherit and slightly mutate traits (max_age, perception_radius).
- Implement entity memory for remembering seen obstacle locations.
- Implement entity perception so they only see food and obstacles within a certain radius.
- Implement environmental events (e.g. storms or droughts) that affect entity energy decay.
- Created a new analysis report `analytics/current_analysis.md` summarizing the project evolution and agent actions up to the intelligent BFS pathfinding implementation.
- Implement intelligent pathfinding allowing entities to navigate and route around impassable terrain and obstacles when seeking food.
- Implement different types of terrain or obstacles in the universe (e.g. walls, water) to add complexity to the simulation.
- Implemented a simulation loop script (`simulate.py`) to run the universe and visualize it in real-time in the terminal.
- Implemented a basic CLI visualizer (`CLIVisualizer`) for the universe to display entities and food on a grid.
- Analyzed project changes and agent actions (AI behavior, reproduction, aging) and updated the results in `analytics/analysis_report.md`.
- Implement an aging system for entities (e.g. entities naturally die after reaching a certain maximum age).
- Implement entity reproduction/spawning mechanics (e.g. entities spawn offspring if they have enough energy).
- Implemented basic behavior/AI for entities to seek out food rather than just staying still.
- Bootstrapped core universe engine (Universe and Entity classes).
- Implement a 2D grid/spatial system to allow entities to have positions and move.
- Analyzed project changes and agent actions (implementing 2D spatial system) and added the results to `analytics/analysis_report.md`.
- Implement basic energy/life cycle for entities (e.g. entities consume energy each tick and die when energy reaches 0).
- Implemented a food/resource system allowing entities to consume resources to regain energy.

## Completed
- Analyzed recent project changes (Disease, Scent Trails, Communication, Combat, Symbiosis, Disasters) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.
- Implement a communication system where entities can alert others of predators.
- Implement predators tracking prey by scent trails left over time.
- Implement group behavior or flocking for entities.

- Implement dynamic terrain generation based on temperature and weather over time.

## Completed
- Expand entity mutations to allow evolving different diets over generations.
- Implement biome-specific entities that thrive in sand/mud or require specific terrain.

## Completed
- Implement an entity size/mass attribute that affects movement speed and energy consumption.

## Completed
- Implement carnivorous entities preferring to target smaller/weaker entities first.

## Completed
- Implement a more complex weather system with distinct seasons affecting terrain and food growth differently.

## Completed
- Implement an evolution system where entity species slowly change over time based on successful genetic mutations and environmental fitness.

## Completed
- Implement a system where entities can heal or recover energy over time when in a shelter

## Completed
- Implemented scavenger diet and corpse mechanic where entities leave behind meat when dying of natural causes.

## Completed
- Implement dynamic seasons that affect food growth rates differently.
- Implement omnivore diet, allowing entities to consume both food (plants/meat) and prey.

- Implement a camouflage trait for entities allowing them to avoid detection by reducing the effective perception range of others.

## Completed
- Implement a food spoilage or rotting system where food disappears after a certain amount of time, affected by temperature (e.g. rots faster in heat, preserved in cold).

## Completed
- Implemented flight mechanics. Entities can mutate an `is_flying` trait allowing them to bypass impassable terrain like walls and water during movement and pathfinding.

## Completed
- Added a reproduction chance modifier based on intelligence.

## Completed
- Implemented `max_energy` attribute (scaling by `size`) to restrict infinite energy accumulation from overeating.

## Completed
- Implemented an experience and leveling system where entities gain XP for surviving days, escaping predators, or successfully hunting, and level up to gain stat boosts.

- Analyzed recent project changes (Hoarding Mechanics) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.

## Completed
- Implemented amphibious trait (`is_amphibious`) allowing entities to freely traverse both land and water tiles.
- Analyzed recent project changes (Amphibious trait) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.

## Completed
- Implemented `is_immune` trait. Entities can now gain immunity after recovering from disease, and offspring can inherit this trait or mutate to gain it. This adds an immunological layer to natural selection.
- Analyzed recent project changes (Immunity trait) and updated `analytics/analysis_report.md` and `analytics/current_analysis.md`.

## Next Steps
