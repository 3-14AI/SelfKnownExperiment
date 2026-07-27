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

- [x] Implemented `is_carnivorous_plant` trait. Plants with this trait can consume small entities that move onto their tile, gaining energy and growing larger.
- [x] Implement `is_desertic` trait. Entities with this trait suffer half hydration loss in hot climates and gain an energy efficiency bonus when traversing `sand` terrain.
- [x] Implemented `has_bioluminescence` trait. Entities with this trait bypass night vision penalties for themselves, but are easily spotted by predators at night.
- [x] Implemented elevation and height map mechanics. Entities are affected by elevation changes (uphill costs more stamina, steep downhill causes slight damage), while flying entities ignore elevation.
- [x] Implement a `can_climb` trait allowing entities to traverse 'wall' terrain blocks, simulating climbing over obstacles.
- [x] Implement `pack_hunter` trait allowing predatory entities to share target tracking and coordinate attacks with nearby entities of the same species.
- [x] Implemented `has_scales` trait. Entities with this trait lose hydration at half the normal rate and receive a small flat bonus to effective defense during combat.
- [x] Implemented `has_claws` trait. Entities with this trait gain an attack bonus during combat.
- [x] Implemented deep-water biome and aquatic entities. Entities with `is_aquatic` can navigate deep-water while others cannot, adding more varied terrain traversal.
- [x] Implemented Electric trait (`is_electric`) and stunned mechanics. Entities with this trait stun their attackers during combat, rendering them unable to move or act for several ticks.
- [x] Implemented `is_cold_blooded` trait. Entities with this trait gain an energy efficiency advantage in hot temperatures but suffer energy and movement penalties in cold temperatures.
- [x] Implemented Fruiting trait (`is_fruiting`). Entities with this trait can passively drop food (fruit) when well-fed, allowing them to support symbiotic species or act as anglerfish-like predators that bait herbivores.
- [x] Implemented aging growth mechanics where newly born entities start at a smaller size and gradually grow to their genetic maximum as they age.
- [x] Implemented Aposematism trait (`is_aposematic`) which makes predators ignore the entity unless they are starving.
- [x] Implemented echolocation trait (`has_echolocation`). Entities with this trait bypass camouflage and night-time vision penalties.
- [x] Implemented `has_shell` trait. Entities with this trait gain a significant defense bonus during combat to simulate thick armor.
- [x] Implemented Photosynthesis trait (`can_photosynthesize`). Entities with this trait gain energy during the daytime, simulating plant-like behavior.
- [x] Implemented venomous trait (`is_venomous`) where entities have a chance to poison their opponent during combat.
- [x] Implemented web building mechanics allowing entities with `can_spin_webs` to place stamina-draining traps.
- [x] Implemented defensive spikes/thorns trait. Entities with `has_spikes` damage their attackers during combat.
- [x] Implemented burrowing mechanics allowing entities to sleep underground, gaining shelter benefits and avoiding predators.
- [x] Implemented Oviparity/Egg-Laying mechanics. Entities with `lays_eggs` lay an egg object instead of spawning children directly.
- [x] Implemented organic plant spreading allowing flora to naturally grow into patches over time.
- [x] Implemented hibernation mechanics allowing entities to preserve energy and hydration during winter if they possess the `can_hibernate` trait.
- [x] Implemented toxicity and poison mechanics for food and entities.
- [x] Implemented sleep mechanism where entities recover energy when resting.
- [x] Implemented Hydration System where entities lose hydration over time, seek out water when thirsty, and drink when adjacent to water tiles.
- [x] Developed more complex environmental interaction, such as shelter building.
- [x] Implemented complex ecosystem dependencies (e.g. specialized predators that only eat specific species, or herbivores that require specific plants).
- [x] Introduced tool usage or simple crafting mechanics for intelligent entities.
- [x] Implemented a combat system where entities can gain experience or strength from surviving encounters.
- [x] Implemented a communication system where entities can alert others of predators.
- [x] Implemented a combat or defense system for entities to protect against predators.
- [x] Implemented a symbiotic relationship system where certain entity species benefit from being near each other.
- [x] Implemented a disease or plague system that spreads between entities when they are in close proximity.
- [x] Implemented natural disasters (volcanoes, earthquakes) that affect terrain globally.
- [x] Implemented temperature zones or biomes that affect different entity types.
- [x] Implemented a day/night cycle affecting entity vision and movement.
- [x] Implemented localized weather events like rain (increasing food spawn locally) or fire (destroying entities/food and turning terrain to ash).
- [x] Implemented seasonal changes that dynamically affect food spawn rates and terrain.
- [x] Implemented ecosystem balancing via a population limit that restricts entities from reproducing when a threshold is met.
- [x] Implemented different entity species or diets (e.g. Herbivore vs Carnivore) to create ecosystem dynamics.
- [x] Implemented Entity Genetics and Mutations allowing child entities to inherit and slightly mutate traits (max_age, perception_radius).
- [x] Implemented entity memory for remembering seen obstacle locations.
- [x] Implemented entity perception so they only see food and obstacles within a certain radius.
- [x] Implemented environmental events (e.g. storms or droughts) that affect entity energy decay.
- [x] Implemented intelligent pathfinding allowing entities to navigate and route around impassable terrain and obstacles when seeking food.
- [x] Implemented different types of terrain or obstacles in the universe (e.g. walls, water) to add complexity to the simulation.
- [x] Implemented a simulation loop script (`simulate.py`) to run the universe and visualize it in real-time in the terminal.
- [x] Implemented a basic CLI visualizer (`CLIVisualizer`) for the universe to display entities and food on a grid.
- [x] Implemented an aging system for entities (e.g. entities naturally die after reaching a certain maximum age).
- [x] Implemented entity reproduction/spawning mechanics (e.g. entities spawn offspring if they have enough energy).
- [x] Implemented basic behavior/AI for entities to seek out food rather than just staying still.
- [x] Implemented a 2D grid/spatial system to allow entities to have positions and move.
- [x] Implemented basic energy/life cycle for entities (e.g. entities consume energy each tick and die when energy reaches 0).
- [x] Implemented a food/resource system allowing entities to consume resources to regain energy.
- [x] Implemented predators tracking prey by scent trails left over time.
- [x] Implemented group behavior or flocking for entities.
- [x] Implemented dynamic terrain generation based on temperature and weather over time.
- [x] Expanded entity mutations to allow evolving different diets over generations.
- [x] Implemented biome-specific entities that thrive in sand/mud or require specific terrain.
- [x] Implemented an entity size/mass attribute that affects movement speed and energy consumption.
- [x] Implemented carnivorous entities preferring to target smaller/weaker entities first.
- [x] Implemented a more complex weather system with distinct seasons affecting terrain and food growth differently.
- [x] Implemented an evolution system where entity species slowly change over time based on successful genetic mutations and environmental fitness.
- [x] Implemented a system where entities can heal or recover energy over time when in a shelter
- [x] Implemented scavenger diet and corpse mechanic where entities leave behind meat when dying of natural causes.
- [x] Implemented dynamic seasons that affect food growth rates differently.
- [x] Implemented omnivore diet, allowing entities to consume both food (plants/meat) and prey.
- [x] Implemented a camouflage trait for entities allowing them to avoid detection by reducing the effective perception range of others.
- [x] Implemented a food spoilage or rotting system where food disappears after a certain amount of time, affected by temperature (e.g. rots faster in heat, preserved in cold).
- [x] Implemented flight mechanics. Entities can mutate an `is_flying` trait allowing them to bypass impassable terrain like walls and water during movement and pathfinding.
- [x] Implemented `max_energy` attribute (scaling by `size`) to restrict infinite energy accumulation from overeating.
- [x] Implemented an experience and leveling system where entities gain XP for surviving days, escaping predators, or successfully hunting, and level up to gain stat boosts.
- [x] Implemented amphibious trait (`is_amphibious`) allowing entities to freely traverse both land and water tiles.
- [x] Implemented `is_immune` trait. Entities can now gain immunity after recovering from disease, and offspring can inherit this trait or mutate to gain it. This adds an immunological layer to natural selection.
- [x] Implemented `is_regenerative` trait. Entities with this trait regenerate energy at the cost of hydration.
- [x] Implemented Parasitism (`is_parasitic`) trait. Parasites actively seek out and attach to larger hosts, continually draining their energy and hydration to sustain themselves.
- [x] Implemented `has_fur` trait. Entities with this trait gain enhanced cold resistance but suffer increased energy loss and movement penalties in hot environments.

- [x] Implemented `is_volcanic` trait. Entities with this trait thrive in extreme heat, gain energy when standing on `ash` terrain, and are immune to `fire` events.
- [x] Implemented `is_forestal` trait. Entities with this trait gain defense in forest/wooded terrain.
- [x] Implemented `is_social` trait. Entities with this trait gain an energy efficiency buff when near other entities of the same species.

## Next Steps

- [x] Implement advanced group hunting tactics for entities with the `pack_hunter` trait (e.g. flanking, cutting off escape routes based on terrain).
- [ ] Introduce a `disease_vector` trait for scavenger entities, causing them to spread disease more rapidly when interacting with corpses.
- [ ] Add dynamic water levels. `water` and `deep-water` biomes can dry out into `mud` during extreme droughts or expand during heavy storms, forcing amphibious/aquatic entities to migrate.
- [ ] Implement `is_nocturnal_predator` specific bonuses, granting a higher attack multiplier when hunting at night.