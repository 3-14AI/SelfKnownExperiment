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
6. **CODE DECOMPOSITION & REFACTORING:** Each iteration, you must perform partial refactoring to decompose the codebase into smaller, more manageable pieces. Write new code only while strictly adhering to the project's established structure.

## Your Protocol:
1. Review the existing codebase and the `CHANGELOG.md` (create it if it doesn't exist) to understand the current state.
2. Formulate a clear plan for today's increment.
3. Execute the plan: write code, run tests, and verify your changes.
4. Update the `CHANGELOG.md` with your additions.
5. Ensure all code is robust and self-contained.
6. Submit your work.

Godspeed, Agent. The universe is in your hands.

## Completed
- [x] Implemented `is_disease_dweller` trait. Entities with this trait treat being infected as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_fearless` trait. Entities with this trait do not run away from predators.
- [x] Implemented `is_photosensitive` trait. Entities with this trait suffer increased hydration loss and no stamina recovery during the day, but gain bonus stamina recovery at night.
- [x] Implemented `is_nest_builder` trait. Entities with this trait can build `shelter` terrains regardless of their intelligence level, allowing them to create safe havens for themselves and their offspring.

- [x] Implemented `is_endurance_runner` trait. Entities with this trait have double the maximum stamina and recover stamina at double the normal rate.
- [x] Implemented `is_patient` trait. Entities with this trait recover double stamina when they remain stationary during a tick.
- [x] Implemented `has_thick_skin` trait. Entities with this trait are immune to damage from spikes and gain extra defense when attacked by entities with claws.
- [x] Implemented `is_opportunistic` trait. Entities with this trait can bypass their strict diet restrictions to eat both plants and meat when their energy falls below 25% of their maximum capacity.
- [x] Implemented `has_strong_stomach` trait. Entities with this trait are immune to toxicity from food and prey, and gain double energy when consuming meat.
- [x] Implemented `is_frugivore` trait. Entities with this trait get double energy from eating `fruit` food types.
- [x] Implemented `is_cooperative` trait. Entities with this trait share energy with struggling nearby members of the same species.
- [x] Implemented `is_nocturnal` trait. Entities with this trait sleep during the day and are active at night, reversing the standard sleep cycle.
- [x] Implemented `has_horns` trait. Entities with this trait gain a +2 bonus to their effective attack and +1 to their effective defense during combat.
- [x] Implemented `is_territorial` trait. Entities with this trait gain an attack and defense bonus during combat.
- [x] Implement `is_desertic` trait. Entities with this trait suffer half hydration loss in hot climates and gain an energy efficiency bonus when traversing `sand` terrain.
- [x] Implemented `is_ambush_predator` trait. Entities with this trait deal double damage during combat if they attack while having camouflage.
- [x] Implemented `is_cannibalistic` trait. Entities with this trait will occasionally attack and eat entities of the same species if their energy is critically low.
- [x] Implemented `is_solitary` trait. Entities with this trait gain an energy efficiency buff when alone, but suffer an energy penalty when near other entities of the same species.
- [x] Implemented `is_gluttonous` trait. Entities with this trait can overeat beyond their maximum energy capacity (up to 1.5x) but suffer increased passive energy drain.
- [x] Implemented `is_filter_feeder` trait. Aquatic entities with this trait passively gain small amounts of energy while swimming in `water` or `deep-water` terrains, simulating filter feeding.
- [x] Added missing genetic mutation unit tests for `is_infected` and `is_sleeping` traits in `tests/test_engine.py`.
- [x] Implemented `is_mud_bather` trait. Entities with this trait recover hydration and stamina when on mud terrain.
- [x] Added missing genetic mutation unit tests for 29 traits in `tests/test_engine.py`.

- [x] Implemented `has_blubber` trait. Entities with this trait have 50% more maximum energy capacity and gain enhanced cold resistance, but suffer severe energy penalties in hot environments.
- [x] Implemented `can_sweat` trait. Entities with this trait avoid heat-based energy penalties in hot temperatures but suffer increased hydration loss.
- [x] Implemented `is_detritivore` trait. Entities with this trait consume `ash` and `mud` terrains directly, cleaning up the environment and recovering energy.
- [x] Implemented Vampiric trait (`is_vampiric`). Entities with this trait drain energy and hydration from their prey during combat, even if the prey escapes.
- [x] Implement a `can_sprint` trait allowing entities to temporarily move faster at a high stamina cost.
- [x] Implement advanced group hunting tactics for entities with the `pack_hunter` trait (e.g. flanking, cutting off escape routes based on terrain).
- [x] Implemented `is_scentless` trait. Entities with this trait do not leave scent trails, making them harder for predators to track.
- [x] Implement `is_nocturnal_predator` specific bonuses, granting a higher attack multiplier when hunting at night.
- [x] Add dynamic water levels. `water` and `deep-water` biomes can dry out into `mud` during extreme droughts or expand during heavy storms, forcing amphibious/aquatic entities to migrate.
- [x] Introduce a `disease_vector` trait for scavenger entities, causing them to spread disease more rapidly when interacting with corpses.
- [x] Implemented `is_carnivorous_plant` trait. Plants with this trait can consume small entities that move onto their tile, gaining energy and growing larger.
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

- [x] Implemented `has_horns` trait. Entities with this trait gain a +2 bonus to their effective attack and +1 to their effective defense during combat.
- [x] Implemented `is_playful` trait. Entities with this trait gain 1 experience point per tick when standing adjacent to another entity of the same species.
- [x] Implemented `is_fast_learner` trait. Entities with this trait gain double experience points from all activities.
- [x] Implemented `is_hardy` trait. Entities with this trait halve their base energy loss rate when their energy falls below 25% of their maximum, representing extreme metabolic efficiency during starvation.
- [x] Implemented `is_agile` trait. Entities with this trait ignore stamina penalties when moving uphill.
- [x] Implemented `is_migratory` trait. Entities with this trait instinctively move towards the south edge during autumn/winter, and towards the north edge during spring/summer, granting a passive survival advantage in extreme climates.

- [x] Implemented `is_poison_dweller` trait. Entities with this trait treat being poisoned as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_disease_resistant` trait. Entities with this trait are immune to passive disease contraction during random global ticks.
- [x] Implemented `is_parasite_dweller` trait. Entities with this trait treat having attached parasites as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_sleep_dweller` trait. Entities with this trait treat being asleep as a shelter, gaining increased defense and energy recovery.
## Next Steps
- [x] Implemented `is_ageless` trait. Entities with this trait do not die when their age exceeds their max_age.

- [x] Implemented `is_drought_dweller` trait. Entities with this trait treat a `drought` event as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_earthquake_dweller` trait. Entities with this trait treat an `earthquake` event as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_volcanic_dweller` trait. Entities with this trait treat a `volcano` event as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_fire_dweller` trait. Entities with this trait treat a `fire` event as a shelter, gaining energy recovery and defense, and are immune to fire damage.
- [x] Implemented `is_rain_dweller` trait. Entities with this trait treat a `rain` event as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_storm_dweller` trait. Entities with this trait treat `storm` conditions as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_blizzard_dweller` trait. Entities with this trait treat blizzard conditions as a shelter, gaining energy recovery and defense.
- [x] Implemented `is_deep_water_dweller` trait. Entities with this trait treat deep-water terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_web_dweller` trait. Entities with this trait treat web terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_ice_dweller` trait. Entities with this trait treat `ice` terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_snow_glider` trait. Entities with this trait consume 0 stamina when moving on snow terrain.
- [x] Implemented `is_volcanic_glider` trait. Entities with this trait consume 0 stamina when moving during a 'volcano' event.
- [x] Implemented `is_drought_resistant` trait. Entities with this trait do not lose hydration during a drought event.
- [x] Implemented `is_dust_bather` trait. Entities with this trait can cure their infections by standing on ash or sand terrain.
- [x] Implemented `is_tracker` trait. Entities with this trait can follow scent trails from up to 2 tiles away.
- [x] Implemented `is_unappetizing` trait. Entities with this trait grant only half their energy to predators when eaten.
- [x] Implemented `is_tireless` trait. Entities with this trait do not consume stamina when moving.
- [x] Implemented `is_parasite_resistant` trait. Entities with this trait are immune to parasitic attachment, rendering them safe from energy and hydration drain by parasites.
- [x] Implemented `is_relentless` trait. Entities with this trait deal half their effective attack as energy damage to their prey even if the prey successfully escapes combat.
- [x] Implemented `is_vengeful` trait. Entities with this trait gain permanent attack power when successfully escaping from a predator.
- [x] Implemented `is_fierce` trait. Entities with this trait gain a flat +3 bonus to effective attack in combat.
- [x] Implemented `is_vibrant` trait. Entities with this trait have an increased reproduction chance but cannot use camouflage.
- [x] Implemented `is_spiteful` trait. Entities with this trait deal their defense as energy damage to their predator when killed.
- [x] Implemented `is_cleaner` trait. Entities with this trait remove parasites and cure diseases from adjacent entities, gaining energy in the process.
- [x] Implemented `is_intimidating` trait. Entities with this trait reduce the effective attack or defense of their opponents during combat by 2, making them formidable foes or difficult targets.
- [x] Implemented `is_vocal` trait. Entities with this trait alert nearby flockmates of predators at an increased distance (double their normal communication radius).
- [x] Implemented `is_resourceful` trait. Entities with this trait extract hydration from food and prey, recovering hydration when they eat, which reduces their dependence on environmental water sources.
- [x] Implemented `is_prolific` trait. Entities with this trait have reduced energy thresholds and costs for reproduction, and reproduce more frequently.
- [x] Implemented `is_heavy_sleeper` trait. Entities with this trait recover double energy while sleeping, but their perception drops to 0 during sleep, rendering them oblivious to events and predators.
- [x] Implemented `is_evasive` trait. Entities with this trait gain a flat +20% bonus to their escape chance during combat, making them notoriously slippery and hard to catch.
- [x] Implemented `is_adaptable` trait. Entities with this trait dynamically adjust their preferred temperature over time to survive in extreme climates, at the cost of increased hydration consumption.
- [x] Implemented `is_nomadic` trait. Entities with this trait have reduced energy consumption when they are constantly moving.
- [x] Implemented `is_scavenger` trait. Entities with this trait gain bonus energy when consuming meat.
- [x] Implemented `is_scout` trait. Entities with this trait share their obstacle memory with nearby flockmates, improving collective pathfinding.

- [x] Implemented `is_reckless` trait. Entities with this trait deal double damage (effective attack * 2) but their effective defense is reduced to 0 during combat, making them glass cannons.
- [x] Implemented `is_thief` trait. Entities with this trait and the ability to hoard can steal food from the inventory of adjacent entities when their own energy is low.
- [x] Implemented `is_absorbent` trait. Entities with this trait regain hydration when it is raining (storm event) or they are standing on water/mud/deep-water terrain.
- [x] Implemented `is_pack_mule` trait. Entities with this trait can store up to 4x their size in food in their inventory instead of the standard 2x.

- [x] Implemented `is_toxic` trait. Entities with this trait inflict poison on attackers during combat, causing them to suffer poisoned_time.
- [x] Implemented `is_lucky` trait. Entities with this trait have a 10% higher chance to completely avoid being eaten or attacked and successfully escape combat.

- [x] Implemented `is_cautious` trait. Entities with this trait double their effective perception radius when detecting and fleeing from predators, making them harder to ambush.
- [x] Implemented `is_defensive` trait. Entities with this trait gain a flat +3 bonus to effective defense in combat.
- [x] Implemented `is_sturdy` trait. Entities with this trait are immune to being stunned during combat.

- [x] Implemented `is_arctic` trait. Entities with this trait gain energy in snow/ice and lose 0 energy during blizzards.
- [x] Implemented `is_telepathic` trait. Entities with this trait alert all living flockmates of predators regardless of distance.
- [x] Implemented `is_restless` trait. Entities with this trait never fall asleep, even when stamina is depleted.
- [x] Implemented `is_slippery` trait. Entities with this trait have a 50% chance to escape stamina drain from webs and avoid being eaten by carnivorous plants.
- [x] Implemented `can_leap` trait. Entities with this trait can jump over single-tile obstacles at the cost of extra stamina.

- [x] Implemented `is_heavy` trait. Entities with this trait gain a flat +2 defense bonus but suffer increased stamina consumption during movement.
- [x] Implemented `is_lightweight` trait. Entities with this trait consume less stamina during movement but suffer a flat -2 penalty to effective defense.
- [x] Implemented `is_stealthy` trait. Entities with this trait halve the effective perception radius of predators and prey trying to detect them.
- [x] Implemented `is_mimic` trait. Entities with this trait appear harmless at a distance and are ignored by prey unless within 2 tiles.
- [x] Implemented `has_sharp_teeth` trait. Entities with this trait bypass the flat defense bonuses granted by `has_shell` and `has_scales` during combat.
- [x] Implemented `is_resilient` trait. Entities with this trait recover faster from poison and stun.
- [x] Implemented `is_smelly` trait. Entities with this trait leave a stronger scent trail but inflict an attack penalty on their predators.
- [x] Implemented `is_ruthless` trait. Entities with this trait gain a flat +3 bonus to effective attack during combat if the prey's energy is below half of its maximum.
- [x] Implemented `is_protective` trait. Entities with this trait grant a flat +2 defense bonus to adjacent herd members during combat.
- [x] Implemented `is_forager` trait. Entities with this trait gain an extra 5 energy when consuming plants or fruit.

- [x] Implemented `is_vigilant` trait. Entities with this trait are highly alert and immune to the ambush predator attack modifier.
- [x] Implemented `is_pacifist` trait. Entities with this trait never initiate combat, even when hungry.
- [x] Implemented `is_farsighted` trait. Entities with this trait have their effective perception radius doubled, but suffer a -2 penalty to effective attack in combat.
- [x] Implemented `is_chameleon` trait. Entities with this trait gain a massive camouflage bonus (+0.5) when they remain stationary during a tick, making them practically invisible to predators and prey, but they lose this bonus when they move.
- [x] Implemented `is_bloodthirsty` trait. Entities with this trait recover 20 stamina whenever they successfully hunt and eat a prey.
- [x] Implemented `is_introspective` trait. Entities with this trait gain 2 experience points every tick they remain stationary.
- [x] Implemented `is_frenzied` trait. Entities with this trait gain a flat +5 bonus to effective attack during combat, but lose 5 energy per combat encounter due to overexertion.
- [x] Implemented `is_sun_tracker` trait. Entities with this trait gain an energy bonus during the day if they are standing on clear terrain (not a shelter or ash), allowing them to passively absorb sunlight.
- [x] Implemented `is_hypnotic` trait. Entities with this trait halve the effective attack of their predators during combat.
- [x] Implemented `is_empathic` trait. Entities with this trait transfer 2 energy to an adjacent flockmate if the flockmate's energy is below 30% of its maximum and the empathic entity has more than 50% of its maximum energy.
- [x] Implemented `is_contagious` trait. Entities with this trait transmit their infection to any entity they engage in combat with, regardless of who initiated the attack or if the prey was eaten.
- [x] Implemented `is_arboreal` trait. Entities with this trait treat `forest` terrain as a shelter, gaining increased defense and energy recovery while stationed there.
- [x] Implemented `is_stargazer` trait. Entities with this trait gain an energy bonus and extra stamina recovery on clear nights.
- [x] Implemented `is_sure_footed` trait. Entities with this trait are immune to stamina drain during earthquake events. Entities with this trait gain an energy bonus and extra stamina recovery on clear nights.

- [x] Implemented `is_magnetic` trait. Entities with this trait draw power from magnetic storms, gaining 5 energy and 10 stamina each tick during the 'storm' event.
- [x] Implemented `is_moon_bather` trait. Entities with this trait gain an energy bonus and extra stamina recovery at night when standing on clear terrain.
- [x] Implemented `can_hoard` trait. Entities with this trait can store food items in their inventory to consume later when hungry.
- [x] Implemented `can_burrow` trait. Entities with this trait can sleep underground, treating any terrain as a shelter to hide from predators while sleeping.
- [x] Implemented `is_sunbather` trait. Entities with this trait recover extra energy and stamina during the day when the temperature is warm, but lose hydration faster.
- [x] Implemented `is_storm_chaser` trait. Entities with this trait gain a flat +2 bonus to effective attack during a 'storm' event.
- [x] Implemented `is_shadow_stalker` trait. Entities with this trait gain a +3 bonus to effective attack and reduce their stamina cost for movement to 0 when moving at night.
- [x] Implemented `is_pyrophilic` trait. Entities with this trait gain an energy bonus and extra stamina recovery when standing on ash terrain.



- [x] Implemented `is_desperate` trait. Entities with this trait gain a massive +4 attack when their energy drops below 30% of max energy.
- [x] Implemented `is_iron_willed` trait. Entities with this trait are immune to the stat reductions caused by intimidating and smelly opponents.
- [x] Implemented `is_snow_walker` trait. Entities with this trait do not consume extra stamina from elevation changes when moving on snow terrain.
- [x] Implemented `is_frost_walker` trait. Entities with this trait consume no stamina when moving on snow or ice terrain.
- [x] Implemented `is_marsh_strider` trait. Entities with this trait consume no stamina when moving on mud terrain and gain a defense bonus while on mud.
- [x] Implemented `is_dune_walker` trait. Entities with this trait consume no stamina when moving on sand terrain.
- [x] Implemented `is_water_strider` trait. Entities with this trait consume no stamina when moving on water terrain and can walk on water.
- [x] Implemented `is_web_walker` trait. Entities with this trait consume no stamina when moving on web terrain and are immune to having their stamina set to 0 by webs.
- [x] Implemented `is_ash_walker` trait. Entities with this trait consume no stamina when moving on ash terrain.
- [x] Implemented `is_wind_glider` trait. Entities with this trait consume 0 stamina when moving during a 'storm' event.
- [x] Implemented `is_forest_walker` trait. Entities with this trait consume 0 stamina when moving on forest terrain.
- [x] Implemented `is_rain_dancer` trait. Entities with this trait gain energy when they are within the radius of a 'rain' event.
- [x] Implemented `is_blizzard_glider` trait. Entities with this trait consume 0 stamina when moving during a 'blizzard' event.
- [x] Implemented `is_seismic_sensitive` trait. Entities with this trait have their effective perception radius tripled during an 'earthquake' event.
- [x] Implemented `is_mud_glider` trait. Entities with this trait consume no stamina when moving on mud terrain.
- [x] Implemented `is_drought_strider` trait. Entities with this trait consume no stamina when moving during a 'drought' event.
- [x] Implemented `is_earthquake_glider` trait. Entities with this trait consume 0 stamina when moving during an 'earthquake' event.
- [x] Implemented `is_volcanic_glider` trait. Entities with this trait consume 0 stamina when moving during a 'volcano' event.
- [x] Implemented `is_ice_glider` trait. Entities with this trait consume 0 stamina when moving on ice terrain.
- [x] Implemented `is_day_glider` trait. Entities with this trait consume 0 stamina when moving during the day.
- [x] Implemented `is_night_glider` trait. Entities with this trait consume 0 stamina when moving at night.
- [x] Implemented `is_deep_water_glider` trait. Entities with this trait consume 0 stamina when moving on `deep-water` terrain.
- [x] Implemented `is_ash_glider` trait. Entities with this trait consume 0 stamina when moving on `ash` terrain.
- [x] Implemented `is_spring_glider` trait. Entities with this trait consume 0 stamina when moving during the 'spring' season.

- [x] Implemented `is_summer_glider` trait. Entities with this trait consume 0 stamina when moving during the 'summer' season.
- [x] Implemented `is_autumn_glider` trait. Entities with this trait consume 0 stamina when moving during the 'autumn' season.
- [x] Implemented `is_winter_glider` trait. Entities with this trait consume 0 stamina when moving during the 'winter' season.
- [x] Implemented `is_wall_glider` trait. Entities with this trait consume 0 stamina when moving on wall terrain.
- [x] Implemented `is_rain_glider` trait. Entities with this trait consume 0 stamina when moving during a 'rain' event.
- [x] Implemented `is_sand_glider` trait. Entities with this trait consume 0 stamina when moving on sand terrain.
- [x] Implemented `is_fire_glider` trait. Entities with this trait consume 0 stamina when moving during a 'fire' event.
- [x] Implemented `is_web_glider` trait. Entities with this trait consume 0 stamina when moving on web terrain.

- [x] Implemented `is_forest_glider` trait. Entities with this trait consume 0 stamina when moving on forest terrain.
- [x] Implemented `is_water_glider` trait. Entities with this trait consume 0 stamina when moving on water terrain.
- [x] Implemented `is_shelter_glider` trait. Entities with this trait consume 0 stamina when moving on shelter terrain.

- [x] Implemented `is_mountain_walker` trait. Entities with this trait do not consume extra stamina when moving to a higher elevation.
- [x] Implemented `is_mountain_glider` trait. Entities with this trait consume 0 stamina when moving on mountain terrain.
- [x] Implemented `is_deep_water_glider` tests. Added missing tests to ensure correct stamina behavior on deep-water terrains.
- [x] Implemented `is_mountain_dweller` trait. Entities with this trait treat mountain terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_sand_dweller` trait. Entities with this trait treat sand terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_forest_dweller` trait. Entities with this trait treat forest terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_water_dweller` trait. Entities with this trait treat water terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_ash_dweller` trait. Entities with this trait treat ash terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_snow_dweller` trait. Entities with this trait treat snow terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_mud_dweller` trait. Entities with this trait treat mud terrain as a shelter, gaining increased defense and energy recovery.
- [x] Added `cave` terrain which provides storm/blizzard protection and an energy recovery bonus to `is_mountain_dweller` entities.
- [x] Implemented `is_cave_dweller` trait. Entities with this trait treat `cave` terrain as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_wall_dweller` trait. Entities with this trait treat `wall` terrain as a shelter, gaining increased defense and energy recovery.

- [x] Implemented `is_cave_glider` trait. Entities with this trait consume 0 stamina when moving on cave terrain.
- [x] Implemented `is_day_dweller` trait. Entities with this trait treat day time as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_night_dweller` trait. Entities with this trait treat night time as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_spring_dweller` trait. Entities with this trait treat the spring season as a shelter, gaining increased defense and energy recovery.

- [x] Implemented `is_autumn_dweller` trait. Entities with this trait treat the autumn season as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_summer_dweller` trait. Entities with this trait treat the summer season as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_winter_dweller` trait. Entities with this trait treat the winter season as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_cave_walker` trait. Entities with this trait do not consume extra stamina from elevation changes when moving on cave terrain.
- [x] Implemented `is_stun_dweller` trait. Entities with this trait treat being stunned as a shelter, gaining increased defense and energy recovery.
- [x] Implemented `is_blizzard_walker` trait. Entities with this trait do not consume extra stamina from elevation changes when moving during a 'blizzard' event.
- [x] Implemented `is_rain_walker` trait. Entities with this trait do not consume extra stamina from elevation changes when moving during a 'rain' event.
