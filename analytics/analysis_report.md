# Project Evolution and Agent Actions Analysis

## 1. Project Genesis Bootstrap
The project started with an initial setup of a typical Python project. The basic directory structure includes `src/` for source code and `tests/` for unit testing. The foundation was laid down by an initial commit that set up the repository for an autonomous, infinite AI-driven development cycle.

## 2. Core Engine Implementation
The core simulator logic was bootstrapped in `src/universe/engine.py`.
Two main classes were introduced:
* `Entity`: A simple class representing a distinct object or being in the universe, initially initialized with just a name.
* `Universe`: The main container managing time and entities. It handles adding new entities to the simulation and incrementing time through a `tick` method.

## 3. Test Coverage
A test suite was created alongside the core engine in `tests/test_engine.py` using Python's built-in `unittest` framework.
The tests cover:
* `test_initial_state`: Verifies the `Universe` initializes with time 0 and no entities.
* `test_add_entity`: Verifies that an `Entity` can be successfully added to the `Universe` and is stored correctly.
* `test_tick`: Verifies that the `tick` method correctly increments the `Universe` time.

## 4. Documentation and Directives Updates
Agents have adhered to the project directives by maintaining core documentation files:
* `CHANGELOG.md`: The file accurately reflects the initial setup and the creation of the `Universe` and `Entity` classes, mapping directly to the code changes.
* `agents.md`: The core directives were followed. The 'Completed' section was updated to reflect the bootstrapping of the core universe engine. A new roadmap step was formulated in the 'Next Steps' section, planning for the implementation of a 2D grid/spatial system for entities.

## 5. 2D Spatial System Implementation
A 2D spatial system was introduced in `src/universe/engine.py` to allow entities to have coordinates and movement logic.
The following updates were made:
* `Entity` was extended with `x` and `y` coordinates.
* `Universe` was extended with `width` and `height` properties. It now enforces bounds checking when adding entities or moving them via the new `move_entity` method.
* `get_entities_at` method was added to query entities at specific coordinates.

## 6. Extended Test Coverage
The test suite in `tests/test_engine.py` was updated to cover the new spatial features:
* Added tests for custom positions and out-of-bounds entity placement.
* Added tests for valid and invalid entity movements using `move_entity`.
* Added tests for `get_entities_at` method to accurately return entities at given locations.

## 7. Energy and Life Cycle Implementation
A basic energy and life cycle system was introduced for entities.
The following updates were made to `src/universe/engine.py`:
* `Entity` was extended with an `energy` attribute (defaulting to 10) and an `is_alive` property.
* `Universe`'s `tick` method was updated to decrease entity energy by 1 per tick, and naturally cull entities whose energy reaches 0.

## 8. Food and Resource System Implementation
A food and resource system was implemented to allow entities to regain energy.
The following updates were made:
* A `Food` class was introduced, representing a resource with coordinates and an energy value (defaulting to 5).
* `Universe` was extended to manage a list of `foods` and randomly spawn them based on a `food_spawn_rate`.
* `tick` method was updated so that entities consume food at their exact location to regain energy, removing the eaten food from the universe.

## 9. Further Extended Test Coverage
The test suite in `tests/test_engine.py` was further updated to cover the energy and food systems:
* Added tests for energy initialization, tick consumption, and death when energy reaches 0.
* Added tests for food creation, spatial location querying (`get_foods_at`), and the entity eating logic.

## 10. Aging System
An aging system was introduced to allow entities to naturally die of old age.
The following updates were made:
* `Entity` was extended with `age` and `max_age` attributes.
* `Entity.is_alive` property now checks if `age <= max_age` in addition to energy checks.
* `Universe`'s `tick` method was updated to increment entity age by 1 per tick.
* Unit tests were added in `tests/test_engine.py` to cover initialization, age increment, and culling when age exceeds `max_age`.

## 11. Reproduction System
A reproduction system was introduced, allowing entities to spawn offspring.
The following updates were made to `src/universe/engine.py`:
* `Universe` initialization was updated with `reproduction_threshold` and `reproduction_cost` arguments.
* `tick` method was updated to allow an entity to reproduce (create a new `Entity` at its location) if its energy reaches or exceeds the `reproduction_threshold`.
* Reproducing consumes `reproduction_cost` energy from the parent entity.
* Unit tests were added in `tests/test_engine.py` to assert the correct parent energy decay, child positioning, and default energy state upon reproduction.

## 12. Entity AI Behavior
Basic AI behavior was implemented to allow entities to actively seek out food.
The following updates were made:
* `Universe` was extended with a `get_nearest_food(x, y)` method.
* `tick` method was updated so entities will attempt to move one step (horizontal or vertical) toward the nearest food source per tick if food exists.
* Unit tests were added in `tests/test_engine.py` to cover food seeking movement and food consumption after moving.

## Conclusion
The agents have successfully adhered to the project directives by continually expanding the simulation. The initial 2D spatial system was followed by an entity energy life cycle and a food resource system. Most recently, agents have introduced complex biological mechanics including natural aging, reproduction thresholds, and active AI behavior for food-seeking. The agents consistently update the core engine code (`src/universe/engine.py`) alongside comprehensive unit tests (`tests/test_engine.py`) to ensure robustness. The project tracking files (`CHANGELOG.md` and `agents.md`) are diligently maintained, ensuring the autonomous iteration loop remains healthy and correctly documented.

## 13. CLI Visualizer Implementation
A basic Command Line Interface (CLI) visualizer was implemented to view the current state of the universe.
The following updates were made:
* Created a `CLIVisualizer` class in `src/universe/visualizer.py`.
* The visualizer renders a text-based grid where `.` represents empty space, `f` represents food, and `E` represents entities.
* Provided a `print_state()` method to easily display the current simulation time and grid layout.
* Unit tests were added in `tests/test_visualizer.py` to ensure proper rendering of various universe states, including overlapping entities and food.

## 14. Terrain System
A Terrain system was introduced to add spatial complexity and obstacles to the universe.
The following updates were made:
* Created a `Terrain` class with `x`, `y` coordinates and a `terrain_type` (e.g., 'wall', 'water').
* `Universe` was extended to store a list of `terrains` and provide `add_terrain` and `get_terrains_at` methods.
* `move_entity` logic in `Universe` was updated to raise an error if an entity attempts to move into a cell occupied by impassable terrain.
* The `CLIVisualizer` was updated to iterate over `terrains` and render `#` for walls and `~` for water prior to rendering food and entities.
* Unit tests were added in `tests/test_engine.py` and `tests/test_visualizer.py` to ensure bounds, blocking, and visualization function accurately.
* `simulate.py` was updated to render a 'wall' obstacle across the screen to demonstrate the feature.

## 15. Intelligent Pathfinding
Entity AI was enhanced with intelligent pathfinding capabilities.
The following updates were made:
* Added a `find_path` method to `Universe` utilizing a Breadth-First Search (BFS) algorithm to compute the shortest path to a target coordinate.
* The BFS correctly identifies and routes around impassable `Terrain` (e.g. walls and water).
* Updated the `tick` method's food-seeking AI. Entities now invoke `find_path` to navigate toward `nearest_food` instead of using a naive greedy approach that gets stuck on walls.
* Added a robust unit test (`test_entity_pathfinding_around_obstacle`) in `tests/test_engine.py` simulating an entity routing around a wall to reach a target.

## 16. Environmental Events System
An environmental events system was added to introduce dynamic challenges and random events into the universe.
The following updates were made:
* Introduced random events such as 'storm' and 'drought' to the `Universe` engine.
* Storms double the rate of energy decay for entities, making survival harder.
* Droughts temporarily halt the spawning of new food resources.
* Updated `CLIVisualizer` to display the currently active event and its remaining duration.
* Added comprehensive test coverage in `tests/test_engine.py` to ensure events are triggered properly and have the expected effects on entities and resources.

## 17. Entity Genetics and Mutations
A genetics and mutation system was added to entity reproduction to allow entities to evolve over generations.
The following updates were made:
* Modified the reproduction logic in `src/universe/engine.py`.
* Child entities now inherit their parent's `max_age` and `perception_radius` instead of using defaults.
* Introduced a 10% chance for these traits to mutate, allowing them to slightly increase or decrease.
* Added tests `test_entity_genetics_and_mutation` and `test_entity_genetics_no_mutation` in `tests/test_engine.py` using monkeypatching to deterministically verify the mutation logic.

## 18. Entity Perception Radius
An entity perception radius was implemented, restricting what an entity can detect based on a radius around them.
The following updates were made:
* Modified entities to have a `perception_radius` (default 10).
* Entities only detect food and obstacles that fall within this perception radius.

## 19. Entity Memory
Entities were granted the ability to remember obstacles they have encountered.
The following updates were made:
* Entities maintain a `memory` set to store coordinates of known obstacles.
* Entities observe and remember obstacles (walls, water) within their perception radius each tick.
* Pathfinding algorithms (`find_path`) use the entity's memory to avoid routing through remembered obstacles, even if they are currently outside the entity's perception radius.
* Added tests in `test_engine.py` to ensure memory is updated and correctly utilized in pathfinding.

## 20. Entity Diets
Ecosystem dynamics were enhanced by implementing different entity diets: Herbivores and Carnivores.
The following updates were made:
* Entities were classified into Herbivores and Carnivores.
* Carnivores actively hunt and eat herbivores, while herbivores continue to eat static food resources.
* The visualizer was updated to render carnivores distinctly (e.g., as 'C').

## 21. Population Limit
Ecosystem balancing was introduced via a population limit constraint.
The following updates were made:
* `Universe` now accepts a `population_limit` parameter (default 1000).
* The `tick` method restricts entity reproduction if the total number of entities reaches or exceeds the `population_limit`.
* Unit tests were added in `tests/test_engine.py` to verify this behavior.

## 22. Seasonal Mechanics
A seasonal system was implemented to create dynamic, long-term environmental changes.
The following updates were made:
* Introduced `Spring`, `Summer`, `Autumn`, and `Winter` seasons to the `Universe` engine.
* Seasons dynamically affect the `food_spawn_rate` (e.g., higher in spring/summer, lower in winter).
* Seasons can alter terrain; for example, water tiles freeze into ice during winter, changing traversal properties.

## 23. Localized Weather Events
The simulation's complexity was enhanced with localized weather phenomena.
The following updates were made:
* Implemented `rain` events, which have a chance to increase food spawning within a localized radius.
* Implemented `fire` events, which destroy entities and food within their radius and permanently convert non-water terrain to `ash`.
* `CLIVisualizer` was updated to render `ash` terrain and display active localized events.

## 24. Temperature Mechanics
A granular temperature zone system was added, affecting entity survival.
The following updates were made:
* Implemented `TemperatureZone` to apply localized temperature modifiers across the universe.
* Entities now possess `preferred_temperature` and `temperature_tolerance` attributes.
* Entities outside their comfortable temperature bounds suffer increased energy loss.
* The genetics system was expanded so child entities inherit and mutate these temperature traits.
* `CLIVisualizer` was updated to display active temperature zones.

## 25. Day/Night Cycle
A temporal day/night cycle was added, impacting entity vision and activity.
The following updates were made:
* The universe alternates between day and night phases based on a configurable `day_length`.
* Entity perception and movement are dynamically influenced; vision range is typically reduced at night.

## 26. Flocking Behavior
Advanced group AI mechanics were introduced to entities.
The following updates were made:
* Entities exhibit flocking behavior when no food or prey is nearby.
* They naturally move towards the center of mass of adjacent entities that share their specific diet.
* This adds complex emergent movement patterns and social clustering to the ecosystem.

## 27. Advanced Interactions and Global Hazards
Several advanced mechanics have been introduced recently, further increasing the simulation's complexity:
* **Disease System:** A disease system was added where spontaneous outbreaks can occur and spread between entities in close proximity, causing energy drain.
* **Scent Trails:** Herbivores now leave scent trails that decay over time. Carnivores track the strongest adjacent scent trail when no prey is directly visible.
* **Communication System:** Herbivores can alert nearby flockmates of predators, causing them to move away.
* **Combat and Defense Mechanics:** Entities were given attack and defense attributes with probabilistic combat resolution when carnivores hunt prey.
* **Symbiotic Relationships:** Entities can form symbiotic relationships, receiving energy benefits when near their partners.
* **Natural Disasters:** Global natural disasters were added, such as earthquakes (modifying wall terrain) and volcanoes (spawning ash terrain).

## 28. Advanced Mechanics: Intelligence, Experience, and Niches
Agents have continued to expand the complexity of the simulation, shifting focus from basic survival to advanced adaptation and learning:
- **Tool Crafting & Intelligence**: Entities now possess an `intelligence` attribute and an `inventory`. Highly intelligent entities can craft tools (weapons, shields, clothing) that dynamically improve their combat stats or temperature tolerance. This introduces primitive technology into the ecosystem. Intelligence is fully integrated into the genetic inheritance and mutation system.
- **Combat Experience**: An experience system was added to combat interactions. Entities learn from encounters: prey gain defense from escaping, and predators gain attack stats from hunting attempts, creating an evolutionary arms race based on experience rather than just genetics.
- **Ecological Niches**: Entities evolved a `preferred_terrain` attribute, allowing them to thrive in specific biomes (like sand or mud) while suffering penalties outside them. This promotes geographic specialization.
- **Diet Mutations**: The genetics system was expanded to allow the `diet` trait to mutate, enabling species to shift dynamically between herbivorous and carnivorous lifestyles over generations.

These enhancements signify a major evolution in Project Genesis, where entities are no longer just passive subjects to the environment but actively adapt through learning, tool use, and deep biological specialization.

## 29. Recent Updates
Agents have recently implemented the following mechanics:
- **Scavengers & Corpses**: Entities leave behind meat upon natural death. A new 'scavenger' diet was added to consume this meat. Diet mutations can produce scavengers, and carnivores will prey upon them.
- **Shelters & Healing**: Entities can heal or recover energy over time when inside a shelter. Shelters also provide temperature and weather protections.
- **Specialized Dependencies**: More complex ecosystems were modeled, with carnivores preferring certain species and herbivores preferring specific plants.
- **Hydration System**: A hydration system was added for entities, ensuring they also need water to survive.

- **Omnivores & Sleep**: Omnivores can balance hunting and foraging based on proximity. A sleep mechanism allows entities to recover energy while resting at night.
- **Deep-water Biome**: A deep-water biome and aquatic entities that can only survive in water have been implemented.

## 30. Recent Updates (Flight, Pack Hunting, Food Spoilage, Vision, Toxicity)
Agents have recently implemented the following mechanics:
- **Flight Mechanics**: Entities can mutate an `is_flying` trait allowing them to bypass impassable terrain like walls and water.
- **Pack Hunting & Herd Defense**: Nearby entities of the same species now contribute to attack and defense during combat.
- **Food Spoilage**: Food ages over time and disappears. Spoilage rates are affected by temperature, and meat rots faster than plants.
- **Vision Types**: Entities can mutate `vision_type` (e.g. `night_vision`) allowing them to avoid perception penalties at night.
- **Camouflage**: Entities can mutate `camouflage` traits reducing the distance they can be detected.
- **Toxicity & Poison**: Food and entities can be toxic, causing extra energy loss when consumed. Entities can mutate poison resistance.

### [Next Update Section]
- **Agent Action:** Implemented `max_energy` attribute scaled by entity size.
- **Analysis:** Before this feature, entities could theoretically accumulate infinite energy by continuously eating, making survival trivial after initial abundance. The introduction of `max_energy` caps the energy an entity can store (calculated as `size * 50`). This creates a more balanced and realistic ecosystem where entities must continually manage their food intake rather than front-loading infinite resources.


- **Agent Action:** Implemented organic plant spreading and hibernation mechanics.
- **Analysis:**
    - Organic plant spreading allows older flora to occasionally spawn adjacent copies. This leads to the natural formation of clustered food sources, enriching the foraging dynamics and reducing uniformity.
    - Hibernation mechanics introduce a survival strategy for entities during harsh winter seasons. Entities with the `can_hibernate` trait sleep through winter, drastically reducing their energy and hydration loss.
    - This adds layers to seasonal survival and opens up evolutionary pathways where species adapt to freezing temperatures via hibernation rather than simple cold tolerance.

## 31. Oviparity and Egg-Laying
Agents added the ability for entities to lay eggs instead of directly giving birth.
* Entities can mutate the `lays_eggs` trait.
* When reproducing, an entity with this trait creates a `Food` object representing an egg, storing the unborn offspring.
* When the egg reaches its maximum age (spoils), it hatches, adding the new entity to the simulation.
* This introduces an interesting vulnerability where unborn offspring can be eaten before they hatch.

### Experience and Leveling System
Implemented an RPG-like leveling system where entities accumulate experience points (`experience`) through various actions like surviving a day, escaping predators, or successfully hunting prey. Reaching the threshold `experience_to_next_level` increments their `level` and grants permanent stat bonuses (`attack` and `defense`) and full energy restoration. The CLI Visualizer was updated to render entities of level 3 or higher in uppercase characters, representing their veteran status in the simulation.

### Hoarding Mechanics
Agents implemented a new `can_hoard` trait for herbivores and omnivores. This allows entities to safely store excess food in their inventory. When an entity's energy drops below half of their maximum, they will consume food from their hoard. This introduces a strategic resource management aspect to survival, enabling entities to endure harsh conditions (like winter droughts) or undertake long treks across barren terrain by carrying a food supply with them.

### [Next Update Section]
- **Agent Action:** Implemented Nocturnal trait for entities.
- **Analysis:** This introduces a new behavioral niche. Nocturnal entities invert the standard sleep cycle and vision penalties, allowing them to hunt or forage safely at night when diurnal predators are sleeping or have reduced perception. This enriches the ecosystem by creating time-based environmental niches.
- **Agent Action:** Implemented Burrowing mechanics.
- **Analysis:** Entities with the `can_burrow` trait hide underground when sleeping. This acts as an innate shelter, protecting them from extreme weather (blizzards/storms) and rendering them undetectable by predators. This opens up a new evolutionary strategy for survival against both harsh environments and active predation.
- **Agent Action:** Implemented defensive `has_spikes` trait.
- **Analysis:** This introduces a new survival mechanic for prey. Entities that mutate the `has_spikes` trait inflict energy and stamina damage on predators that attempt to attack or eat them. This creates a disincentive for predators to target them, enriching the evolutionary arms race without relying solely on raw defense stats or escape chance.

### Stamina System
- **Agent Action:** Implemented stamina system.
- **Analysis:** This introduces a short-term resource constraint that forces entities to balance exertion with recovery. By having a separate stamina pool that depletes from movement and combat and induces sleep when empty, the simulation prevents infinite kiting or endless chains of combat. It adds a tactical layer to interactions, where exhaustion becomes as dangerous as starvation.
- **Web Building Mechanics**: Added a `can_spin_webs` trait to entities, allowing them to spin web terrains that deplete the stamina of entities without the trait.
- **Agent Action:** Implemented amphibious trait (`is_amphibious`).
- **Analysis:** This trait introduces a new movement mechanic. Entities with `is_amphibious` can traverse both land and water/deep-water tiles freely, unlike normal entities (blocked by water) or aquatic entities (blocked by land). This provides an evolutionary advantage by allowing these entities to escape terrestrial predators or access resources separated by water bodies.
- **Agent Action:** Implemented defensive `has_shell` trait.
- **Analysis:** This introduces a new survival mechanic for prey. Entities that mutate the `has_shell` trait receive a flat bonus to effective defense during combat. This creates a disincentive for predators to target heavily armored prey, changing predator-prey dynamics and encouraging the evolution of higher attack stats or specialized hunting strategies.
- **Agent Action:** Implemented Photosynthesis trait (`can_photosynthesize`).
- **Analysis:** This trait introduces a new energy acquisition method. Entities with `can_photosynthesize` passively gain energy during the daytime, simulating plant-like autotrophic behavior. This reduces their reliance on foraging or hunting, allowing them to survive in areas with scarce food resources as long as they have access to sunlight. It creates a new ecological niche for stationary or slow-moving entities that thrive in open environments.

### 26. Implement Echolocation Trait
- **Goal:** Introduce a trait that allows entities to counter camouflage and ignore nighttime vision penalties.
- **Mechanics:**
    - The `has_echolocation` boolean trait was added to the `Entity` class.
    - Predation logic (`get_nearest_prey`, `get_nearest_predator`) was updated to ignore the `camouflage` modifier of the target if the perceiving entity possesses `has_echolocation`.
    - Nighttime perception halving in `Universe.tick()` is bypassed for entities with this trait.
    - The trait is passed down genetically during reproduction with a mutation chance.
- **Agent Actions:**
    - Modified `Entity.__init__` and reproduction code in `src/universe/engine.py`.
    - Updated distance checking logic in `get_nearest_prey` and `get_nearest_predator`.
    - Updated `effective_perception` assignment in `Universe.tick()`.
    - Wrote tests in `tests/test_engine.py` to verify echolocation bypasses camouflage and maintains full perception at night.
- Implemented Aposematism trait (`is_aposematic`), rendering entities visually unappealing to predators. Well-fed predators will ignore them, but starving predators will still attack.
- **Agent Action:** Implemented aging growth mechanics.
- **Analysis:** Before this feature, entities were born at their full genetic size immediately, functioning exactly like adults regarding energy consumption, movement penalties, and combat interactions. Now, entities that are born (`age=0`) start at a reduced size (capped at a minimum of 1) and gradually grow over time until they reach their genetic `max_size`. This introduces an infantile vulnerability phase, increasing early mortality risks and shifting ecological pressures toward protecting young or finding safe shelters for reproduction.

### [Agent Update: Immunity Trait]
- **Agent Action:** Implemented `is_immune` trait.
- **Analysis:** This trait introduces an immunological layer to the simulation. Entities that survive an infection now gain immunity, preventing reinfection. Furthermore, immunity can be passed on to offspring or acquired through mutation. This creates complex population dynamics where diseases can wipe out vulnerable populations, leaving only immune survivors to repopulate, thus simulating real-world immunological natural selection.
- **Agent Action:** Implemented Cold Blooded trait (`is_cold_blooded`).
- **Analysis:** This trait introduces a thermodynamic dependency. Cold-blooded entities experience reduced energy loss in hot environments but increased energy loss and slower movement in cold environments. This expands environmental interaction, pushing cold-blooded species towards equatorial/hot biomes and creating interesting seasonal survival dynamics.
- **Agent Action:** Implemented Electric trait (`is_electric`) and stunned mechanics.
- **Analysis:** This trait introduces a new defensive survival mechanic. Entities that mutate the `is_electric` trait stun predators that attack them, preventing the predator from moving or acting for several ticks. This creates a powerful deterrent against predation and provides a window for the prey to escape or counterattack, significantly altering predator-prey dynamics and adding strategic depth to combat encounters.

## 32. Advanced Ecosystem Niche and Defense Mechanisms Analysis
Recent agent iterations have significantly deepened the biological complexity and evolutionary arms race within Project Genesis by introducing a suite of advanced defensive and ecological traits:
- **Sensory & Visual Deception:** The introduction of `camouflage`, countered by `has_echolocation`, alongside `is_aposematic` (warning coloration), creates complex predator-prey targeting rules. Predators must now weigh energy status against prey toxicity and visibility.
- **Physical & Chemical Defenses:** Prey entities have evolved formidable counter-attacks. Traits like `has_spikes`, `is_venomous`, and `is_electric` mean that hunting is no longer a guaranteed energy gain for carnivores, but carries substantial risks of stamina drain, poisoning, or being stunned.
- **Thermodynamic & Immunological Niche:** Entities now adapt to their microclimates and microscopic threats. `is_cold_blooded` restricts entities to warmer biomes to avoid movement and energy penalties. Concurrently, `is_immune` introduces an epidemiological layer where surviving populations become resistant to repeated disease outbreaks.
- **Lifecycle & Propagation:** `is_fruiting` introduces mutualistic relationships by dropping food, and aging growth mechanics ensure young entities are vulnerable before reaching full size, introducing dynamic life-stages.

**Agent Actions:** Agents systematically implemented these traits within `Entity.__init__`, correctly integrated them into the genetic mutation and inheritance systems, and rigorously updated combat resolution, tick events, and targeted unit tests.
**Result:** The simulation has transitioned from simple spatial resource gathering to a deep, trait-based evolutionary ecosystem where survival depends on highly specialized biological niches.

### 34. Deep-water Biome and Aquatic Entities
- **Feature description**: Added a new terrain type `deep-water` which organically generates when water tiles are completely surrounded by other water tiles. Normal and amphibious entities are blocked from entering deep-water, but entities possessing the `is_aquatic` trait can freely traverse it.
- **Code implementation**:
  - Updated `is_passable` in `src/universe/engine.py` to specifically permit aquatic entities but deny amphibious/normal entities in deep-water.
  - Implemented dynamic terrain generation in `Universe.tick()` to slowly convert stable pools of water into deep-water.
  - Updated `CLIVisualizer` to represent deep-water tiles as `≈`.
- **Reasoning**: This enhances ecosystem complexity by creating unreachable zones for land predators and specialized biomes for marine life, simulating realistic bodies of water and encouraging diet and species divergence based on traversal abilities.
- **Agent Action**: Implemented `has_claws` trait.
- **Analysis**: This trait introduces a new offensive survival mechanic. Entities that mutate the `has_claws` trait receive a flat bonus to effective attack during combat. This provides a direct advantage for predators when hunting or for prey defending themselves, encouraging the evolution of higher defense stats or specialized escape strategies in response.

### 35. Claws Trait Analysis
- **Feature description**: Added a new combat trait `has_claws` for entities.
- **Code implementation**:
  - Updated `Entity.__init__` to include `has_claws` boolean attribute.
  - Updated combat mechanics in `Universe.tick()` to add an attack bonus if the entity `has_claws`.
- **Reasoning**: Introduces a new offensive survival mechanic. Entities that mutate the `has_claws` trait receive a flat bonus to effective attack during combat. This provides a direct advantage for predators when hunting or for prey defending themselves, encouraging the evolution of higher defense stats or specialized escape strategies in response.

### 18. Parasitism
- Added `is_parasitic` trait.
- Parasites skip standard moving to actively track and attach to larger entities (hosts).
- Upon attachment, parasites drain energy and hydration from their host each tick.
- If the host dies, the parasite detaches and resumes seeking.- Analyzed recent project changes (Specialized Dependencies) and verified existing engine logic.

### 36. Scales Trait Analysis
- **Feature description**: Implemented `has_scales` trait.
- **Code implementation**:
  - Updated `Entity.__init__` to include `has_scales` boolean attribute.
  - Modified `Universe.tick()` to reduce hydration loss by half for entities with `has_scales` (they only lose hydration every even tick).
  - Modified combat logic in `Universe.tick()` to grant a +2 `effective_defense` bonus to preys with `has_scales`.
  - Updated entity reproduction logic to allow inheritance and mutation of the `has_scales` trait.
  - Updated `CLIVisualizer` to render entities with `has_scales` using the 'R' character.
- **Reasoning**: This trait introduces a new hydration-management and defensive mechanic. Entities that mutate `has_scales` lose hydration at half the normal rate, making them highly adapted to desert or water-scarce environments. Additionally, their scaly exterior provides a flat +2 bonus to effective defense during combat, making them tougher for predators to hunt.

### Analysis 37: Fur Trait
- **Description**: Implemented `has_fur` trait.
- **Agent Action**:
  - Added `has_fur` boolean attribute to `Entity.__init__` and mutation logic.
  - Modified `Universe.tick()` to increase cold tolerance but add energy and movement penalties in heat.
  - Updated `CLIVisualizer` to render entities with `has_fur` using the 'U' character.
  - Created test cases in `tests/test_engine.py` to verify the mechanical tradeoffs.
- **Analysis**: The `has_fur` trait introduces temperature-specific biome adaptations. Furry entities excel in cold regions or winter seasons but risk starvation and sluggishness in heat.

### Analysis 38: Pack Hunter Trait
- **Description**: Implemented `pack_hunter` trait.
- **Agent Action**:
  - Added `pack_hunter` boolean attribute to `Entity.__init__` and its mutation/inheritance logic.
  - Modified `Universe.tick()` movement logic so that pack hunters share their `target_to_chase` with nearby pack members.
  - Modified `Universe.tick()` combat logic to calculate and grant an attack bonus for each adjacent pack hunter targeting the same prey.
  - Updated `CLIVisualizer` to render pack hunters with the 'W' character.
  - Added tests `test_pack_hunter_combat_bonus` and `test_pack_hunter_target_sharing` in `tests/test_engine.py` and a visualization test in `tests/test_visualizer.py`.
- **Analysis**: The `pack_hunter` trait introduces sophisticated group intelligence. By coordinating target tracking and overwhelming prey with localized numerical superiority, smaller predatory species can take down much larger or heavily armored prey, mirroring real-world wolf pack hunting tactics.

### 39. Bioluminescence Trait Analysis
- **Feature description**: Implemented `has_bioluminescence` trait.
- **Code implementation**:
  - Added `has_bioluminescence` boolean attribute to `Entity.__init__` and its mutation/inheritance logic.
  - Modified `Universe.tick()` perception logic so that bioluminescent entities bypass night vision penalties for themselves.
  - Modified `Universe.tick()` targeting logic so that bioluminescent entities are easily spotted by predators at night.
  - Updated `CLIVisualizer` to render bioluminescent entities with the 'l' character, alongside 9 other previously implemented traits.
  - Added unit tests for the bioluminescence trait in `tests/test_engine.py` and visualizer tests in `tests/test_visualizer.py`.
  - Fixed flaky tests regarding `has_spikes`, food spawning, and fruiting by explicit entity typing.
- **Reasoning**: This trait introduces a new risk/reward night survival mechanic. Entities that mutate `has_bioluminescence` gain the ability to perceive their surroundings normally during the night, maintaining their foraging or hunting efficiency. However, this same glow makes them highly conspicuous to other predators in the dark, disabling any camouflage advantages and increasing their risk of being hunted.

### Analysis 40: Desertic Trait
- **Description**: Implemented `is_desertic` trait.
- **Agent Action**:
  - Added `is_desertic` attribute to `Entity.__init__` and its mutation logic.
  - Modified `Universe.tick()` to reduce hydration loss to 0 in hot climates (`current_temp >= 25`) on odd ticks, and reduce stamina cost to 0 when traversing `sand` terrain.
- **Analysis**: The `is_desertic` trait introduces biome-specific adaptations for arid environments. Entities with this trait gain distinct survival advantages in heat and on sandy terrain, encouraging ecological divergence where these entities dominate desert biomes while being outcompeted in temperate or aquatic zones.

### Analysis 41: Volcanic Trait
- **Description**: Implemented `is_volcanic` trait.
- **Agent Action**:
  - Added `is_volcanic` attribute to `Entity.__init__` and its mutation logic.
  - Modified `Universe.tick()` to allow entities to gain energy (`energy_loss -= 3`) on `ash` terrain and become immune to `fire` events (bypassing the instant death mechanic).
  - Updated visualizer to render volcanic entities as 'j'.
- **Analysis**: The `is_volcanic` trait creates a highly specialized extremophile niche. These entities thrive in post-disaster scenarios (volcanic eruptions causing fire and ash), reversing the usual negative impacts of these environmental hazards into survival advantages.

### Analysis 42: Forestal Trait
- **Description**: Implemented `is_forestal` trait.
- **Agent Action**:
  - Added `is_forestal` attribute to `Entity.__init__` and its mutation logic.
  - Modified combat logic in `Universe.tick()` to grant an effective defense bonus (+3) when the prey is positioned on `forest` terrain.
  - Added visualizer support for forest terrain and forestal entities.
- **Analysis**: The `is_forestal` trait integrates terrain-based combat advantages. It incentivizes entities to inhabit or retreat to wooded areas for protection, adding a strategic layer to pathfinding and ecosystem distribution.

### Analysis 43: Social Trait
- **Description**: Implemented `is_social` trait.
- **Agent Action**:
  - Added `is_social` attribute to `Entity.__init__` and its mutation logic.
  - Modified `Universe.tick()` to grant an energy efficiency buff (`energy_loss -= 1`) when near other living entities of the same species within a Manhattan distance of 2.
- **Analysis**: The `is_social` trait introduces basic herd or flock dynamics. It rewards proximity to conspecifics with reduced energy consumption, naturally leading to the emergence of clustered group behaviors and increased population density for social species.

### Analysis 44: Carnivorous Plant Trait
- **Description**: Implemented `is_carnivorous_plant` trait.
- **Agent Action**:
  - Added `is_carnivorous_plant` attribute to `Entity.__init__` and its mutation logic.
  - Modified `Universe.tick()` allowing carnivorous plants to consume smaller entities on their tile, gaining energy and growing in size.
  - Assigned the character 'c' to represent `is_carnivorous_plant` in `CLIVisualizer`.
- **Analysis**: The `is_carnivorous_plant` trait introduces a stationary ambush predator dynamic. Unlike active hunters, entities with this trait rely on passive consumption, fundamentally changing their ecological niche from active search to positional dominance.

### Analysis 45: Disease Vector Trait
- **Description**: Implemented `disease_vector` trait.
- **Agent Action**:
  - Added `disease_vector` trait to `Entity.__init__` and its mutation/inheritance logic.
  - Modified `Universe.tick()` logic for scavengers eating meat; if the entity is a `disease_vector` and not immune, it has a 50% chance of becoming infected when consuming meat.
  - Updated tests in `test_engine.py` to verify this behavior.
  - Added visualization for the trait in `CLIVisualizer`.
- **Analysis**: This trait alters disease propagation dynamics within the ecosystem. Scavengers with this trait face a high risk/reward tradeoff when foraging for corpses, turning them into highly effective spreaders of illness while maintaining their role as cleanup crews.

### Analysis 46: Nocturnal Predator Trait
- **Description**: Implemented `is_nocturnal_predator` trait.
- **Agent Action**:
  - Added `is_nocturnal_predator` trait to `Entity.__init__` and its mutation/inheritance logic.
  - Applied a 1.5x multiplier to `effective_attack` when `is_nocturnal_predator` is True and the universe is in the night cycle.
  - Added 'N' representation in `CLIVisualizer`.
- **Analysis**: This trait encourages temporal niche specialization. Predators with this trait become significantly more lethal at night, shifting the balance of power based on the time of day and forcing prey to adapt their activity patterns to avoid darkness.

### Analysis 47: Scentless Trait
- **Description**: Implemented `is_scentless` trait.
- **Analysis**: Herbivores typically leave scent trails that carnivores can track. Entities that mutate the `is_scentless` trait do not leave these trails, making them significantly harder for predators to track when out of direct line of sight.

### Analysis 48: Sprinting Mechanics
- **Description**: Implemented `can_sprint` trait.
- **Analysis**: This trait allows entities to move faster temporarily by expending stamina. It bypasses size-based movement restrictions, giving entities a short burst of speed to escape predators or catch prey, adding a layer of tactical stamina management.

### Analysis 49: Vampiric Trait
- **Description**: Implemented `is_vampiric` trait.
- **Analysis**: Entities with this trait drain energy and hydration from their prey during combat, even if the prey manages to escape. This provides a combat sustain advantage, shifting the focus from purely lethal encounters to attrition-based feeding.

### Analysis 50: Detritivore Diet
- **Description**: Implemented `is_detritivore` trait.
- **Analysis**: Entities with this trait can consume `ash` and `mud` terrains directly, cleaning up the environment and recovering energy. This introduces a new environmental niche that capitalizes on post-disaster terrains.

### Analysis 51: Sweating Trait
- **Description**: Implemented `can_sweat` trait.
- **Analysis**: Entities with this trait avoid heat-based energy penalties in hot environments but suffer increased hydration loss. This creates a tradeoff where survival in hot climates is possible but requires a constant supply of water.

### Analysis 52: Ambush Predator Trait
- **Description**: Implemented `is_ambush_predator` trait.
- **Agent Action**:
  - Added `is_ambush_predator` trait to `Entity.__init__` and its mutation/inheritance logic.
  - Modified combat logic in `Universe.tick()` allowing ambush predators to deal 2x effective attack damage during combat if they have a camouflage value > 0.0.
  - Added comprehensive unit tests to verify the trait's mechanics.
- **Analysis**: The `is_ambush_predator` trait creates a strong synergy with the camouflage system. It enables entities to become highly lethal hunters by utilizing stealth, adding a layer of strategic positioning and rewarding evolutionary pathways that combine both stealth and predatory attributes.

### Analysis 53: Territorial Trait
- **Description**: Implemented `is_territorial` trait.
- **Analysis**: Entities with this trait gain an attack and defense bonus during combat to simulate territorial defense, encouraging them to stand their ground rather than fleeing.

### Analysis 54: Cannibalistic Trait
- **Description**: Implemented `is_cannibalistic` trait.
- **Analysis**: Entities with this trait will occasionally attack and eat entities of the same species if their energy is critically low. This adds a desperate survival mechanism that limits extreme population clustering.

### Analysis 55: Solitary Trait
- **Description**: Implemented `is_solitary` trait.
- **Analysis**: Entities with this trait gain an energy efficiency buff when alone, but suffer an energy penalty when near other entities of the same species. This encourages solitary species to spread out and cover more territory.

### Analysis 56: Gluttonous Trait
- **Description**: Implemented `is_gluttonous` trait.
- **Analysis**: Entities with this trait can overeat beyond their maximum energy capacity (up to 1.5x) but suffer increased passive energy drain. This allows them to stockpile energy during times of abundance to survive scarcity.

### Analysis 57: Filter Feeder Trait
- **Description**: Implemented `is_filter_feeder` trait.
- **Analysis**: Aquatic entities with this trait passively gain small amounts of energy while swimming in `water` or `deep-water` terrains, simulating filter feeding and offering an alternative to direct consumption.

### Analysis 58: Mud Bather Trait
- **Description**: Implemented `is_mud_bather` trait.
- **Analysis**: Entities with this trait recover hydration and stamina when on mud terrain, granting them a significant survival advantage in wetland biomes.

### Analysis 59: Blubber Trait
- **Description**: Implemented `has_blubber` trait.
- **Analysis**: Entities with this trait have 50% more maximum energy capacity and gain enhanced cold resistance, but suffer severe energy penalties in hot environments.

### Analysis 60: Climbing Mechanics
- **Description**: Implemented `can_climb` trait.
- **Analysis**: Entities with this trait can traverse 'wall' terrain blocks, simulating climbing over obstacles, which gives them access to blocked areas and escape routes.

### Analysis 61: Regenerative Trait
- **Description**: Implemented `is_regenerative` trait.
- **Analysis**: Entities with this trait naturally regenerate energy over time, but at the cost of increased hydration loss. This trades one vital resource for another to sustain combat or starvation periods.

### Analysis 62: Horns Trait
- **Description**: Implemented `has_horns` trait.
- **Analysis**: Entities with this trait gain a +2 bonus to their effective attack and +1 to their effective defense during combat, making them formidable opponents in direct encounters.

### Analysis 63: Migratory Trait
- **Description**: Implemented `is_migratory` trait.
- **Agent Action**:
  - Added `is_migratory` attribute to `Entity.__init__` and mutation loop.
  - Modified `Universe.tick()` movement logic: idle migratory entities will pathfind towards the north edge (y=0) during spring/summer, and the south edge (y=height-1) during autumn/winter.
  - Rendered migratory entities as 'z' in the CLI visualizer.
- **Analysis**: The `is_migratory` trait simulates seasonal migration, granting entities a passive survival advantage in extreme climates by instinctively moving to more favorable temperature zones as seasons change.

### Analysis 64: Cooperative Trait
- **Description**: Implemented `is_cooperative` trait.
- **Analysis**: Entities with this trait share energy with struggling nearby members of the same species, increasing the overall survivability of the group.

### Analysis 65: Frugivore Trait
- **Description**: Implemented `is_frugivore` trait.
- **Analysis**: Entities with this trait get double energy from eating `fruit` food types, incentivizing specialization in specific plant-based diets.

### Analysis 66: Agile Trait
- **Description**: Implemented `is_agile` trait.
- **Analysis**: Entities with this trait ignore stamina penalties when moving uphill, giving them a mobility advantage in uneven terrain.

### Analysis 67: Strong Stomach Trait
- **Description**: Implemented `has_strong_stomach` trait.
- **Analysis**: Entities with this trait are immune to toxicity from food and prey, and gain double energy when consuming meat, making them highly efficient scavengers or predators.

### Analysis 68: Opportunistic Trait
- **Description**: Implemented `is_opportunistic` trait.
- **Analysis**: Entities with this trait can bypass their strict diet restrictions to eat both plants and meat when their energy falls below 25% of their maximum capacity, providing a critical fallback mechanism during starvation.

### Analysis 69: Thick Skin Trait
- **Description**: Implemented `has_thick_skin` trait.
- **Analysis**: Entities with this trait are immune to damage from spikes and gain extra defense when attacked by entities with claws, making them robust against specialized physical attacks.

### Analysis 70: Fast Learner Trait
- **Description**: Implemented `is_fast_learner` trait.
- **Analysis**: Entities with this trait gain double experience points from all activities, allowing them to level up and increase their combat stats much faster, giving them a significant survival advantage over time.

### Analysis 71: Playful Trait
- **Description**: Implemented `is_playful` trait.
- **Analysis**: Entities with this trait passively gain experience points when standing adjacent to another entity of the same species, encouraging social behavior and faster leveling.

### Analysis 72: Heavy Sleeper Trait
- **Description**: Implemented `is_heavy_sleeper` trait.
- **Analysis**: Entities with this trait recover energy extremely fast while sleeping (recovery * 2), but their `effective_perception` becomes 0 while sleeping, making them completely oblivious to predators or surrounding events. This introduces a high-risk, high-reward recovery strategy.

### Analysis 73: Patient Trait
- Implemented `is_patient` trait.
- Entities with this trait recover double stamina when they remain stationary during a tick.
- Added visual representation with the `*` character.
- Wrote tests for mutation and stamina recovery in `test_engine.py` and visual rendering in `test_visualizer.py`.
- Updated agents.md with the newly completed task.

### Analysis 74: Evasive Trait
- **Description**: Implemented `is_evasive` trait.
- **Agent Action**: Added `is_evasive` to entity initialization and mutation pool. Updated combat logic in `Universe.tick()` to add a flat +20% bonus to `escape_chance` if the prey has this trait. Assigned the `^` visual character. Added unit tests for mutation and combat escape.
- **Analysis**: The evasive trait provides a strong defense mechanism by making entities significantly harder to catch, increasing the survivability of otherwise weak species when facing overwhelming odds.

### Analysis 75: Prolific Trait
- **Description**: Implemented `is_prolific` trait.
- **Agent Action**: Added `is_prolific` to entity initialization, mutation pool, and reproduction logic in `Universe.tick()`. Entities with this trait require half the base reproduction energy threshold, expend half the base reproduction cost, and have an increased reproduction chance. Assigned the `&` visual character. Added tests for mutation and reproduction requirements.
- **Analysis**: The `is_prolific` trait enables r-selection strategies, allowing species to rapidly multiply when resources are scarce or predation is high, ensuring survival through overwhelming numbers rather than individual longevity.

### Analysis 76: Resourceful Trait
- **Description**: Implemented `is_resourceful` trait.
- **Agent Action**:
  - Added `is_resourceful` trait to `Entity.__init__` and mutation logic.
  - Modified `Universe.tick()` so entities with `is_resourceful` regain 10 hydration when consuming food or prey.
  - Added visual representation with the `$` character in `CLIVisualizer`.
  - Wrote unit tests in `test_engine.py` and `test_visualizer.py`.
- **Analysis**: The `is_resourceful` trait enables entities to survive without direct water sources by utilizing the moisture in their food. This provides a massive advantage in deserts or deep inland regions, shifting the dynamic of where life can flourish.

### Analysis 77: Hardy Trait
- **Description**: Implemented `is_hardy` trait.
- **Agent Action**:
  - Added `is_hardy` trait to `Entity.__init__` and mutation logic.
  - Modified `Universe.tick()` to halve the base energy loss rate when an entity's energy falls below 25% of its maximum capacity.
- **Analysis**: Entities with this trait represent extreme metabolic efficiency during starvation. It significantly increases their chances of survival during prolonged food scarcity, such as winter droughts, making them highly resilient to environmental hardships.

### Analysis 78: Endurance Runner Trait
- **Description**: Implemented `is_endurance_runner` trait.
- **Agent Action**:
  - Added `is_endurance_runner` trait to `Entity.__init__` and mutation logic.
  - Modified initialization and reproduction to double the maximum stamina for entities with this trait.
  - Updated stamina recovery logic in `Universe.tick()` to double the recovery rate.
- **Analysis**: This trait provides a massive advantage in prolonged pursuits or escapes. By having a larger stamina pool and faster recovery, these entities can outlast both predators and prey in extended chases, introducing endurance hunting/fleeing dynamics.

### Analysis 79: Adaptable Trait
- **Description**: Implemented `is_adaptable` trait.
- **Agent Action**:
  - Added `is_adaptable` attribute to `Entity.__init__` and its mutation logic.
  - Modified `Universe.tick()` so that when the current temperature differs from the preferred temperature by more than 5 degrees, the preferred temperature adjusts by 1 degree toward the current temperature, at the cost of 1 hydration point.
- **Analysis**: The `is_adaptable` trait simulates long-term acclimatization. It allows entities to migrate and settle in diverse, extreme biomes that would otherwise be uninhabitable, trading short-term hydration costs for long-term thermodynamic stability.

### Analysis 80: Missing Genetic Mutation Tests Fix
- **Description**: Added missing genetic mutation unit tests for several traits.
- **Agent Action**:
  - Implemented mutation logic tests for `is_infected`, `is_sleeping`, and 29 other previously un-tested traits in `tests/test_engine.py`.
- **Analysis**: This action ensures that the evolutionary engine correctly passes down and mutates all available traits, maintaining the integrity of the genetic simulation and preventing regressions in species evolution.

### Analysis 81: Implementing the `is_vocal` Trait

**Context**: The user requested the implementation of the `is_vocal` trait from the "Next Steps" section of the agents.md file. This trait is designed to double an entity's communication radius when alerting flockmates of nearby predators.

**Changes Made**:
-   **Engine Modifications (`src/universe/engine.py`)**: Added `is_vocal` to the `Entity.__init__` arguments and attributes. Updated the `Entity` reproduction logic to inherit and mutate this new trait. Updated the flee behavior inside `Universe.tick` to dynamically multiply the effective communication radius for alerting flockmates if the entity is vocal.
-   **Visualizer Modifications (`src/universe/visualizer.py`)**: Inserted logic into `CLIVisualizer.render` to map vocal entities to the character `'o'`. The conditional was correctly placed above the base diet fallbacks (`carnivore`, `scavenger`, `omnivore`) to ensure it actually triggers.
-   **Test Additions (`tests/test_engine.py`, `tests/test_visualizer.py`)**:
    -   Added `TestIsVocal` with `test_is_vocal_alert_radius` to test that `get_nearby_flockmates` is called with the correct doubled radius when a predator is nearby.
    -   Added `test_is_vocal_mutation` to verify inheritance and mutation (using `unittest.mock.patch('random.random')`).
    -   Added `test_visualizer_is_vocal` to check string representation mapping.
-   **Agents/Status Update (`agents.md`)**: Replaced the empty "Next Steps" prompt with the completed `is_vocal` task item, setting the checkbox to true.

**Key Learnings & Revisions**:
-   **Test State Bleeding**: Adding new boolean traits with global `mock_random.return_value = 0.0` mutation tests forces *all* boolean traits to flip. If these tests use generic parent entities, it causes unrelated traits (e.g. `is_vampiric`, `lays_eggs`) to flip, breaking other tests. It is essential to initialize generic test entities by manually disabling or hardcoding these bleeding traits to prevent assertions from failing.
-   **Property Mutability**: The `is_alive` attribute of an `Entity` is a read-only property and cannot be explicitly assigned in test setup scripts.
-   **Visualizer Conditional Priority**: When adding rendering logic in `CLIVisualizer`, placing new trait checks after diet fallback checks (which almost all entities have) will mask the new character. Priority order is critical.

### Analysis 82
- Add `is_nomadic` trait where entities recover or save energy by moving each tick.
- Update `Entity` class, reproduction, mutation logic in `engine.py`.
- Apply `is_nomadic` recovery mechanic in `Universe.tick()`.
- Add visualizer representation in `visualizer.py`.
- Add unit tests.

### Analysis 83: Photosensitive Trait
- **Description**: Completed `is_photosensitive` trait mechanics.
- **Analysis**: Entities with this trait suffer increased hydration loss and no stamina recovery during the day, but gain bonus stamina recovery at night. Added to agents.md.

### Analysis 84: Fearless Trait
- **Description**: Implemented `is_fearless` trait.
- **Analysis**: Entities with this trait ignore their instinct to flee from predators. While this might seem counter-intuitive, it can be combined with strong defense or attack stats to create robust organisms that hold their ground and fight back rather than wasting energy running.

### Analysis 85: Nest Builder Trait
- **Description**: Implemented `is_nest_builder` trait.
- **Analysis**: Entities with this trait can construct shelter terrains, allowing them to create safe havens, improving their survival and protecting offspring.

### Analysis 86: Scavenger Trait
- **Description**: Implemented `is_scavenger` trait.
- **Analysis**: Entities with this trait gain a bonus to energy gain when consuming meat, making them highly efficient at utilizing corpses and cleaning up the environment.

### Analysis 87: Cleaner Trait
- **Description**: Implemented `is_cleaner` trait.
- **Analysis**: Entities with this trait form a mutualistic relationship by cleaning other entities. They remove parasites and cure diseases from adjacent entities, gaining a small amount of energy for each parasite or disease cured. This encourages symbiotic survival strategies.

### Analysis 88: Spiteful Trait
- **Description**: Implemented `is_spiteful` trait.
- **Analysis**: Entities with this trait deal their defense as energy damage to a predator when successfully hunted, making them dangerous prey and naturally discouraging predators over time.

### Analysis 89: Intimidating Trait
- **Description**: Analyzed `is_intimidating` trait.
- **Analysis**: Entities with this trait reduce the effective attack or defense of their opponents during combat by 2, making them formidable foes or difficult targets.

### Analysis 90: Intimidating Trait test addition
- **Description**: Added visualization test for `is_intimidating` trait.

### Analysis 91: Reckless Trait
- **Description**: Implemented `is_reckless` trait.
- **Agent Action**:
  - Added `is_reckless` to `Entity.__init__` and mutation logic.
  - Modified combat logic in `Universe.tick()` so that entities with this trait deal double damage (effective attack * 2) but their effective defense is reduced to 0 during combat.
- **Analysis**: The reckless trait introduces a "glass cannon" archetype to the simulation. Entities with this trait will be extremely lethal in combat but highly vulnerable to being killed, prioritizing offense at the complete expense of defense.

### Analysis 92: Thief Trait
- **Description**: Implemented `is_thief` trait.
- **Agent Action**:
  - Added `is_thief` trait to `Entity.__init__` and inheritance/mutation logic.
  - Entities with `is_thief=True` and `can_hoard=True` can steal food from adjacent hoarders if their own energy falls below 75%.
  - Assigned visual character `_` for `is_thief` entities.
  - Added unit tests testing thief mechanics and mutations.
- **Analysis**: The thief trait introduces a new parasitic behavior where entities can steal stored resources from others, bypassing the need to hunt or forage directly. This adds complex interactions between hoarding species and opportunistic thieves.

### Analysis 93: Toxic Trait
- **Description**: Implemented `is_toxic` trait.
- **Agent Action**:
  - Added `is_toxic` to `Entity.__init__` and inheritance/mutation logic.
  - Updated combat resolution in `Universe.tick()` to apply a `poisoned_time` status effect to attackers who attack a toxic entity.
  - Added test coverage in `tests/test_engine.py` for `is_toxic` combat and mutation.
  - Fixed property initialization issues in unrelated tests to prevent state bleeding.
- **Analysis**: The toxic trait introduces a chemical defense mechanism that punishes predators even if the prey is killed. This deters predation over time by applying a negative status effect to the attacker, shifting survival dynamics towards avoidance rather than direct confrontation.

### Analysis 94: Vibrant Trait
**Overview:** Implemented the `is_vibrant` trait for entities.
**Details:** Entities with this trait have their reproduction chance boosted by 25%. However, this comes at the cost of rendering any camouflage completely ineffective.

### Analysis 95: Fierce Trait
**Overview:** Implemented the `fierce` trait for entities.
**Details:** Entities with this trait gain a flat +3 bonus to effective attack in combat.

### Analysis 96: is_desperate Trait
**Overview:** Implemented the `is_desperate` trait which gives a +4 attack bonus when energy is <30%.
**Details:**
- Added `is_desperate` parameter to `Entity.__init__`
- Updated child mutation and inheritance in `Universe.tick`
- Applied +4 `effective_attack` modifier in both combat logic blocks when `is_desperate=True` and `energy` < 30% of `max_energy`.

### Analysis 97: Absorbent Trait
**Overview:** Implemented the `absorbent` trait for entities.
**Details:** Entities with this trait regain hydration when it is raining (storm event) or they are standing on water/mud/deep-water terrain.

### Analysis 98: Pack Mule Trait
**Overview:** Implemented the `pack_mule` trait for entities.
**Details:** Entities with this trait can store up to 4x their size in food in their inventory instead of the standard 2x.

### Analysis 99: Lucky Trait
**Overview:** Implemented the `lucky` trait for entities.
**Details:** Entities with this trait have a 10% higher chance to completely avoid being eaten or attacked and successfully escape combat.

### Analysis 100: Telepathic Trait
**Overview:** Implemented the `telepathic` trait for entities.
**Details:** Entities with this trait can broadcast predator alerts globally to all species members, bypassing normal communication radius limits.

### Analysis 101: Vengeful Trait
**Overview:** Implemented the `is_vengeful` trait for entities.
**Details:** Entities with this trait gain permanent attack power when successfully escaping from a predator, shifting combat dynamics over time.

### Analysis 102: Cautious Trait
**Overview:** Implemented the `is_cautious` trait for entities.
**Details:** Entities with this trait double their effective perception radius when detecting and fleeing from predators, making them significantly harder to ambush.

### Analysis 103: Defensive Trait
**Overview:** Implemented the `is_defensive` trait for entities.
**Details:** Entities with this trait gain a flat +3 bonus to effective defense in combat, increasing their survivability against predators.

### Analysis 104: Sturdy Trait
**Overview:** Implemented the `is_sturdy` trait for entities.
**Details:** Entities with this trait are immune to being stunned during combat, making them resilient to effects from electric entities or other stunning mechanics.

### Analysis 105: Arctic Trait
**Overview:** Implemented the `is_arctic` trait for entities.
**Details:** Entities with this trait gain energy when on snow or ice and lose no energy during blizzards, adapting them perfectly to cold environments.

### Analysis 106: Restless Trait
**Overview:** Implemented the `is_restless` trait for entities.
**Details:** Entities with this trait never fall asleep, even when their stamina is fully depleted, allowing them to remain constantly alert.

### Analysis 107: Slippery Trait
**Overview:** Implemented the `is_slippery` trait for entities.
**Details:** Entities with this trait have a 50% chance to escape stamina drain from webs and avoid being eaten by carnivorous plants, offering unique defensive capabilities against environmental traps.

### Analysis 108: Leap Trait
**Overview:** Implemented the `can_leap` trait for entities.
**Details:** Entities with this trait can jump over single-tile obstacles at the cost of extra stamina, enhancing their mobility in cluttered environments.

### Analysis 109: Heavy Trait
**Overview:** Implemented the `is_heavy` trait for entities.
**Details:** Entities with this trait gain a flat +2 defense bonus but suffer increased stamina consumption during movement, trading mobility for durability.

### Analysis 110: Lightweight Trait
**Overview:** Implemented the `is_lightweight` trait for entities.
**Details:** Entities with this trait consume less stamina during movement but suffer a flat -2 penalty to effective defense, favoring agility over resilience.

### Analysis 111: Stealthy Trait
**Overview:** Implemented the `is_stealthy` trait for entities.
**Details:** Entities with this trait halve the effective perception radius of predators and prey trying to detect them, making them excellent ambush predators or elusive prey.

### Analysis 112: Mimic Trait
**Overview:** Implemented the `is_mimic` trait for entities.
**Details:** Entities with this trait appear harmless at a distance and are ignored by prey unless within 2 tiles, giving them an advantage when approaching targets.

### Analysis 113: Sharp Teeth Trait
**Overview:** Implemented the `has_sharp_teeth` trait for entities.
**Details:** Entities with this trait bypass the flat defense bonuses granted by `has_shell` and `has_scales` during combat, making them specialized hunters against armored prey.

### Analysis 114: Resilient Trait
**Overview:** Implemented the `is_resilient` trait for entities.
**Details:** Entities with this trait recover faster from poison and stun, improving their survivability against specialized combat effects.

### Analysis 115: Fearless Trait
**Overview:** Implemented the `is_fearless` trait for entities.
**Details:** Entities with this trait do not run away from predators.

### Analysis 116: Photosensitive Trait
**Overview:** Implemented the `is_photosensitive` trait for entities.
**Details:** Entities with this trait suffer increased hydration loss and no stamina recovery during the day, but gain bonus stamina recovery at night.

### Analysis 117: Nest Builder Trait
**Overview:** Implemented the `is_nest_builder` trait for entities.
**Details:** Entities with this trait can build `shelter` terrains regardless of their intelligence level, allowing them to create safe havens for themselves and their offspring.

### Analysis 118: Endurance Runner Trait
**Overview:** Implemented the `is_endurance_runner` trait for entities.
**Details:** Entities with this trait have double the maximum stamina and recover stamina at double the normal rate.

### Analysis 119: Patient Trait
**Overview:** Implemented the `is_patient` trait for entities.
**Details:** Entities with this trait recover double stamina when they remain stationary during a tick.

### Analysis 120: Thick Skin Trait
**Overview:** Implemented the `has_thick_skin` trait for entities.
**Details:** Entities with this trait are immune to damage from spikes and gain extra defense when attacked by entities with claws.

### Analysis 121: Opportunistic Trait
**Overview:** Implemented the `is_opportunistic` trait for entities.
**Details:** Entities with this trait can bypass their strict diet restrictions to eat both plants and meat when their energy falls below 25% of their maximum capacity.

### Analysis 122: Strong Stomach Trait
**Overview:** Implemented the `has_strong_stomach` trait for entities.
**Details:** Entities with this trait are immune to toxicity from food and prey, and gain double energy when consuming meat.

### Analysis 123: Frugivore Trait
**Overview:** Implemented the `is_frugivore` trait for entities.
**Details:** Entities with this trait get double energy from eating `fruit` food types.

### Analysis 124: Cooperative Trait
**Overview:** Implemented the `is_cooperative` trait for entities.
**Details:** Entities with this trait share energy with struggling nearby members of the same species.

### Analysis 125: Nocturnal Trait
**Overview:** Implemented the `is_nocturnal` trait for entities.
**Details:** Entities with this trait sleep during the day and are active at night, reversing the standard sleep cycle.

### Analysis 126: Horns Trait
**Overview:** Implemented the `has_horns` trait for entities.
**Details:** Entities with this trait gain a +2 bonus to their effective attack and +1 to their effective defense during combat.

### Analysis 127: Territorial Trait
**Overview:** Implemented the `is_territorial` trait for entities.
**Details:** Entities with this trait gain an attack and defense bonus during combat.

### Analysis 128: Ambush Predator Trait
**Overview:** Implemented the `is_ambush_predator` trait for entities.
**Details:** Entities with this trait deal double damage during combat if they attack while having camouflage.

### Analysis 129: Cannibalistic Trait
**Overview:** Implemented the `is_cannibalistic` trait for entities.
**Details:** Entities with this trait will occasionally attack and eat entities of the same species if their energy is critically low.

### Analysis 130: Solitary Trait
**Overview:** Implemented the `is_solitary` trait for entities.
**Details:** Entities with this trait gain an energy efficiency buff when alone, but suffer an energy penalty when near other entities of the same species.

### Analysis 131: Gluttonous Trait
**Overview:** Implemented the `is_gluttonous` trait for entities.
**Details:** Entities with this trait can overeat beyond their maximum energy capacity (up to 1.5x) but suffer increased passive energy drain.

### Analysis 132: Filter Feeder Trait
**Overview:** Implemented the `is_filter_feeder` trait for entities.
**Details:** Aquatic entities with this trait passively gain small amounts of energy while swimming in `water` or `deep-water` terrains, simulating filter feeding.

### Analysis 133: Mud Bather Trait
**Overview:** Implemented the `is_mud_bather` trait for entities.
**Details:** Entities with this trait recover hydration and stamina when on mud terrain.

### Analysis 134: Blubber Trait
**Overview:** Implemented the `has_blubber` trait for entities.
**Details:** Entities with this trait have 50% more maximum energy capacity and gain enhanced cold resistance, but suffer severe energy penalties in hot environments.

### Analysis 135: Sweat Trait
**Overview:** Implemented the `can_sweat` trait for entities.
**Details:** Entities with this trait avoid heat-based energy penalties in hot temperatures but suffer increased hydration loss.

### Analysis 136: Detritivore Trait
**Overview:** Implemented the `is_detritivore` trait for entities.
**Details:** Entities with this trait consume `ash` and `mud` terrains directly, cleaning up the environment and recovering energy.

### Analysis 137: Scentless Trait
**Overview:** Implemented the `is_scentless` trait for entities.
**Details:** Entities with this trait do not leave scent trails, making them harder for predators to track.

### Analysis 138: Carnivorous Plant Trait
**Overview:** Implemented the `is_carnivorous_plant` trait for entities.
**Details:** Plants with this trait can consume small entities that move onto their tile, gaining energy and growing larger.

### Analysis 139: Bioluminescence Trait
**Overview:** Implemented the `has_bioluminescence` trait for entities.
**Details:** Entities with this trait bypass night vision penalties for themselves, but are easily spotted by predators at night.

### Analysis 140: Scales Trait
**Overview:** Implemented the `has_scales` trait for entities.
**Details:** Entities with this trait lose hydration at half the normal rate and receive a small flat bonus to effective defense during combat.

### Analysis 141: Claws Trait
**Overview:** Implemented the `has_claws` trait for entities.
**Details:** Entities with this trait gain an attack bonus during combat.

### Analysis 142: Cold Blooded Trait
**Overview:** Implemented the `is_cold_blooded` trait for entities.
**Details:** Entities with this trait gain an energy efficiency advantage in hot temperatures but suffer energy and movement penalties in cold temperatures.

### Analysis 143: Shell Trait
**Overview:** Implemented the `has_shell` trait for entities.
**Details:** Entities with this trait gain a significant defense bonus during combat to simulate thick armor.

### Analysis 144: Immune Trait
**Overview:** Implemented the `is_immune` trait for entities.
**Details:** Entities can now gain immunity after recovering from disease, and offspring can inherit this trait or mutate to gain it. This adds an immunological layer to natural selection.

### Analysis 145: Regenerative Trait
**Overview:** Implemented the `is_regenerative` trait for entities.
**Details:** Entities with this trait regenerate energy at the cost of hydration.

### Analysis 146: Fur Trait
**Overview:** Implemented the `has_fur` trait for entities.
**Details:** Entities with this trait gain enhanced cold resistance but suffer increased energy loss and movement penalties in hot environments.

### Analysis 147: Volcanic Trait
**Overview:** Implemented the `is_volcanic` trait for entities.
**Details:** Entities with this trait thrive in extreme heat, gain energy when standing on `ash` terrain, and are immune to `fire` events.

### Analysis 148: Forestal Trait
**Overview:** Implemented the `is_forestal` trait for entities.
**Details:** Entities with this trait gain defense in forest/wooded terrain.

### Analysis 149: Social Trait
**Overview:** Implemented the `is_social` trait for entities.
**Details:** Entities with this trait gain an energy efficiency buff when near other entities of the same species.

### Analysis 150: Playful Trait
**Overview:** Implemented the `is_playful` trait for entities.
**Details:** Entities with this trait gain 1 experience point per tick when standing adjacent to another entity of the same species.

### Analysis 151: Fast Learner Trait
**Overview:** Implemented the `is_fast_learner` trait for entities.
**Details:** Entities with this trait gain double experience points from all activities.

### Analysis 152: Hardy Trait
**Overview:** Implemented the `is_hardy` trait for entities.
**Details:** Entities with this trait halve their base energy loss rate when their energy falls below 25% of their maximum, representing extreme metabolic efficiency during starvation.

### Analysis 153: Agile Trait
**Overview:** Implemented the `is_agile` trait for entities.
**Details:** Entities with this trait ignore stamina penalties when moving uphill.

### Analysis 154: Migratory Trait
**Overview:** Implemented the `is_migratory` trait for entities.
**Details:** Entities with this trait instinctively move towards the south edge during autumn/winter, and towards the north edge during spring/summer, granting a passive survival advantage in extreme climates.

### Analysis 155: Parasite Resistant Trait
**Overview:** Implemented the `is_parasite_resistant` trait for entities.
**Details:** Entities with this trait are immune to parasitic attachment, rendering them safe from energy and hydration drain by parasites.

### Analysis 156: Relentless Trait
**Overview:** Implemented the `is_relentless` trait for entities.
**Details:** Entities with this trait deal half their effective attack as energy damage to their prey even if the prey successfully escapes combat.

### Analysis 157: Fierce Trait
**Overview:** Implemented the `is_fierce` trait for entities.
**Details:** Entities with this trait gain a flat +3 bonus to effective attack in combat.

### Analysis 158: Spiteful Trait
**Overview:** Implemented the `is_spiteful` trait for entities.
**Details:** Entities with this trait deal their defense as energy damage to their predator when killed.

### Analysis 159: Cleaner Trait
**Overview:** Implemented the `is_cleaner` trait for entities.
**Details:** Entities with this trait remove parasites and cure diseases from adjacent entities, gaining energy in the process.

### Analysis 160: Intimidating Trait
**Overview:** Implemented the `is_intimidating` trait for entities.
**Details:** Entities with this trait reduce the effective attack or defense of their opponents during combat by 2, making them formidable foes or difficult targets.

### Analysis 161: Vocal Trait
**Overview:** Implemented the `is_vocal` trait for entities.
**Details:** Entities with this trait alert nearby flockmates of predators at an increased distance (double their normal communication radius).

### Analysis 162: Resourceful Trait
**Overview:** Implemented the `is_resourceful` trait for entities.
**Details:** Entities with this trait extract hydration from food and prey, recovering hydration when they eat, which reduces their dependence on environmental water sources.

### Analysis 163: Prolific Trait
**Overview:** Implemented the `is_prolific` trait for entities.
**Details:** Entities with this trait have reduced energy thresholds and costs for reproduction, and reproduce more frequently.

### Analysis 164: Heavy Sleeper Trait
**Overview:** Implemented the `is_heavy_sleeper` trait for entities.
**Details:** Entities with this trait recover double energy while sleeping, but their perception drops to 0 during sleep, rendering them oblivious to events and predators.

### Analysis 165: Evasive Trait
**Overview:** Implemented the `is_evasive` trait for entities.
**Details:** Entities with this trait gain a flat +20% bonus to their escape chance during combat, making them notoriously slippery and hard to catch.

### Analysis 166: Adaptable Trait
**Overview:** Implemented the `is_adaptable` trait for entities.
**Details:** Entities with this trait dynamically adjust their preferred temperature over time to survive in extreme climates, at the cost of increased hydration consumption.

### Analysis 167: Nomadic Trait
**Overview:** Implemented the `is_nomadic` trait for entities.
**Details:** Entities with this trait have reduced energy consumption when they are constantly moving.

### Analysis 168: Scavenger Trait
**Overview:** Implemented the `is_scavenger` trait for entities.
**Details:** Entities with this trait gain bonus energy when consuming meat.

### Analysis 169: Scout Trait
**Overview:** Implemented the `is_scout` trait for entities.
**Details:** Entities with this trait share their obstacle memory with nearby flockmates, improving collective pathfinding.

### Analysis 170: Reckless Trait
**Overview:** Implemented the `is_reckless` trait for entities.
**Details:** Entities with this trait deal double damage (effective attack * 2) but their effective defense is reduced to 0 during combat, making them glass cannons.

### Analysis 171: Thief Trait
**Overview:** Implemented the `is_thief` trait for entities.
**Details:** Entities with this trait and the ability to hoard can steal food from the inventory of adjacent entities when their own energy is low.

### Analysis 172: Absorbent Trait
**Overview:** Implemented the `is_absorbent` trait for entities.
**Details:** Entities with this trait regain hydration when it is raining (storm event) or they are standing on water/mud/deep-water terrain.

### Analysis 173: Pack Mule Trait
**Overview:** Implemented the `is_pack_mule` trait for entities.
**Details:** Entities with this trait can store up to 4x their size in food in their inventory instead of the standard 2x.

### Analysis 174: Toxic Trait
**Overview:** Implemented the `is_toxic` trait for entities.
**Details:** Entities with this trait inflict poison on attackers during combat, causing them to suffer poisoned_time.

### Analysis 175: Lucky Trait
**Overview:** Implemented the `is_lucky` trait for entities.
**Details:** Entities with this trait have a 10% higher chance to completely avoid being eaten or attacked and successfully escape combat.

### Analysis 176: Telepathic Trait
**Overview:** Implemented the `is_telepathic` trait for entities.
**Details:** Entities with this trait alert all living flockmates of predators regardless of distance.

### Analysis 177: Smelly Trait
**Overview:** Implemented the `is_smelly` trait for entities.
**Details:** Entities with this trait leave a stronger scent trail but inflict an attack penalty on their predators.

### Analysis 178: Ruthless Trait
**Overview:** Implemented the `is_ruthless` trait for entities.
**Details:** Entities with this trait gain a flat +3 bonus to effective attack during combat if the prey's energy is below half of its maximum.

### Analysis 179: Protective Trait
**Overview:** Implemented the `is_protective` trait for entities.
**Details:** Entities with this trait grant a flat +2 defense bonus to adjacent herd members during combat.

### Analysis 180: Forager Trait
**Overview:** Implemented the `is_forager` trait for entities.
**Details:** Entities with this trait gain an extra 5 energy when consuming plants or fruit.

### Analysis 181: Tireless Trait
**Overview:** Implemented the `is_tireless` trait for entities.
**Details:** Entities with this trait do not consume stamina when moving.

### Analysis 182: Vigilant Trait
**Overview:** Entities with this trait are highly alert and cannot be ambushed.
**Details:** When an ambush predator attacks an entity with `is_vigilant=True`, the predator does not receive its normal 2x attack multiplier from being camouflaged.

### Analysis 183: Pacifist Trait
**Overview:** Implemented the `is_pacifist` trait for entities.
**Details:** Entities with this trait never initiate combat, even when hungry.

### Analysis 184: Farsighted Trait
**Overview:** Implemented the `is_farsighted` trait for entities.
**Details:** Entities with this trait have their effective perception radius doubled, which allows them to spot food, prey, and predators from farther away, but they suffer a -2 penalty to their effective attack during combat due to their lack of close-range focus.

### Analysis 185: Vampiric Trait
**Overview:** Implemented the `is_vampiric` trait for entities.
**Details:** Vampiric trait (`is_vampiric`). Entities with this trait drain energy and hydration from their prey during combat, even if the prey escapes.

### Analysis 186: Aquatic Trait
**Overview:** Implemented the `is_aquatic` trait for entities.
**Details:** deep-water biome and aquatic entities. Entities with `is_aquatic` can navigate deep-water while others cannot, adding more varied terrain traversal.

### Analysis 187: Electric Trait
**Overview:** Implemented the `is_electric` trait for entities.
**Details:** Electric trait (`is_electric`) and stunned mechanics. Entities with this trait stun their attackers during combat, rendering them unable to move or act for several ticks.

### Analysis 188: Fruiting Trait
**Overview:** Implemented the `is_fruiting` trait for entities.
**Details:** Fruiting trait (`is_fruiting`). Entities with this trait can passively drop food (fruit) when well-fed, allowing them to support symbiotic species or act as anglerfish-like predators that bait herbivores.

### Analysis 189: Aposematic Trait
**Overview:** Implemented the `is_aposematic` trait for entities.
**Details:** Aposematism trait (`is_aposematic`) which makes predators ignore the entity unless they are starving.

### Analysis 190: Echolocation Trait
**Overview:** Implemented the `has_echolocation` trait for entities.
**Details:** echolocation trait (`has_echolocation`). Entities with this trait bypass camouflage and night-time vision penalties.

### Analysis 191: Photosynthesize Trait
**Overview:** Implemented the `can_photosynthesize` trait for entities.
**Details:** Photosynthesis trait (`can_photosynthesize`). Entities with this trait gain energy during the daytime, simulating plant-like behavior.

### Analysis 192: Venomous Trait
**Overview:** Implemented the `is_venomous` trait for entities.
**Details:** venomous trait (`is_venomous`) where entities have a chance to poison their opponent during combat.

### Analysis 193: Spin Webs Trait
**Overview:** Implemented the `can_spin_webs` trait for entities.
**Details:** web building mechanics allowing entities with `can_spin_webs` to place stamina-draining traps.

### Analysis 194: Spikes Trait
**Overview:** Implemented the `has_spikes` trait for entities.
**Details:** defensive spikes/thorns trait. Entities with `has_spikes` damage their attackers during combat.

### Analysis 195: Lays Eggs Trait
**Overview:** Implemented the `lays_eggs` trait for entities.
**Details:** Oviparity/Egg-Laying mechanics. Entities with `lays_eggs` lay an egg object instead of spawning children directly.

### Analysis 196: Hibernate Trait
**Overview:** Implemented the `can_hibernate` trait for entities.
**Details:** hibernation mechanics allowing entities to preserve energy and hydration during winter if they possess the `can_hibernate` trait.

### Analysis 197: Mutate Trait
**Overview:** Implemented the `mutate` trait for entities.
**Details:** Entity Genetics and Mutations allowing child entities to inherit and slightly mutate traits (max_age, perception_radius).

### Analysis 198: Camouflage Trait
**Overview:** Implemented the `camouflage` trait for entities.
**Details:** a camouflage trait for entities allowing them to avoid detection by reducing the effective perception range of others.

### Analysis 199: Flying Trait
**Overview:** Implemented the `is_flying` trait for entities.
**Details:** flight mechanics. Entities can mutate an `is_flying` trait allowing them to bypass impassable terrain like walls and water during movement and pathfinding.

### Analysis 200: Amphibious Trait
**Overview:** Implemented the `is_amphibious` trait for entities.
**Details:** amphibious trait (`is_amphibious`) allowing entities to freely traverse both land and water tiles.

### Analysis 201: Parasitic Trait
**Overview:** Implemented the `is_parasitic` trait for entities.
**Details:** Parasitism (`is_parasitic`) trait. Parasites actively seek out and attach to larger hosts, continually draining their energy and hydration to sustain themselves.

### Analysis 202: Vibrant Trait
**Overview:** Implemented the `is_vibrant` trait for entities.
**Details:** Entities with this trait have an increased reproduction chance but cannot use camouflage.

### Analysis 203: Chameleon Trait
**Overview:** Implemented the `is_chameleon` trait for entities.
**Details:** Entities with this trait gain a massive camouflage bonus (+0.5) when they remain stationary during a tick, making them practically invisible to predators and prey, but they lose this bonus when they move.

### Analysis 204: Unappetizing Trait
**Overview:** Implemented the `is_unappetizing` trait for entities.
**Details:** Entities with this trait grant only half their normal energy to predators upon being eaten, providing a slight evolutionary disadvantage to their predators without necessarily preventing their own death.

### Analysis 205: is_introspective Trait
**Overview:**
Implemented the `is_introspective` trait. Entities with this trait gain a deep understanding of their surroundings when still, granting them 2 experience points per tick they remain stationary.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_introspective` flag.
- Added inheritance and mutation logic in `Universe.tick()`, allowing offspring to inherit or randomly mutate the trait.
- Updated the stationary recovery logic block in `Universe.tick()` to award 2 experience points per tick to entities with `is_introspective` that do not move from their `start_pos`.
- Assigned the visual character `Ω` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added tests `test_is_introspective_stationary_xp` and `test_is_introspective_mutation` to `tests/test_engine.py` to ensure correct behavior.

### Analysis 206: Frenzied Trait
**Overview:**
Implemented the `is_frenzied` trait. Entities with this trait gain a massive +5 bonus to their effective attack during combat, but lose 5 energy per combat encounter due to overexertion.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_frenzied` flag.
- Added inheritance and mutation logic in `Universe.tick()`, allowing offspring to inherit or randomly mutate the trait.
- Updated both combat calculation blocks (scent tracking and direct collision) in `Universe.tick()` to apply a flat +5 bonus to `effective_attack` and subtract 5 energy from the attacking entity if they possess `is_frenzied`.
- Assigned the visual character `ç` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added tests `test_is_frenzied_combat` and `test_is_frenzied_mutation` to `tests/test_engine.py` to ensure correct behavior.

### Analysis 207: Hypnotic Trait
**Overview:**
Implemented the `is_hypnotic` trait. Entities with this trait halve the effective attack of their predators during combat.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_hypnotic` flag.
- Added inheritance and mutation logic in `Universe.tick()`, allowing offspring to inherit or randomly mutate the trait.
- Updated both combat calculation blocks (scent tracking and direct collision) in `Universe.tick()` to halve the `effective_attack` of the attacker if the defending entity possesses `is_hypnotic`.
- Assigned the visual character `•` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added tests `test_is_hypnotic_combat` and `test_is_hypnotic_mutation` to `tests/test_engine.py` to ensure correct behavior.

### Analysis 208: Tracker Trait
**Overview:**
Implemented the `is_tracker` trait. Entities with this trait can follow scent trails from up to 2 tiles away, making them superior hunters capable of tracking prey without being immediately adjacent to the scent trail.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_tracker` flag.
- Added inheritance and mutation logic in `Universe.tick()`, allowing offspring to inherit or randomly mutate the trait.
- Updated the scent tracking logic in `Universe.tick()` to expand the search radius for entities with `is_tracker`, allowing them to detect the strongest scent within a 2-tile Manhattan distance and step toward it.
- Assigned the visual character `↬` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added tests `test_is_tracker_scent_detection` and `test_is_tracker_mutation` to `tests/test_engine.py` to ensure correct behavior.

### Analysis 209: Empathic Trait
**Overview:**
The `is_empathic` trait has been implemented, introducing a cooperative resource-sharing mechanism among social entities.

**Details:**
- **Energy Transfer:** Entities with this trait proactively transfer 2 energy to adjacent flockmates (entities of the same species within 1 tile distance) whose energy has fallen below 30% of their maximum capacity.
- **Cost:** The empathic entity sacrifices 2 of its own energy to perform this transfer, provided its energy is above 50% of its maximum capacity.
- **Selective Advantage:** This trait increases the overall survivability of a species cluster by preventing starvation in vulnerable individuals, buffering against localized food scarcity or severe energy drains, and extending the operational longevity of the flock as a whole.
- **Integration:** The trait is successfully integrated into reproduction logic, meaning it can be inherited or spontaneously mutated. Visualized by the '±' character.

### Analysis 210: Contagious Trait
**Overview:**
Implemented the `is_contagious` trait. Entities with this trait transmit their infection to any entity they engage in combat with, regardless of who initiated the attack or if the prey was eaten.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_contagious` flag.
- Added inheritance and mutation logic for `is_contagious` in `Universe.tick()`, allowing offspring to inherit or randomly mutate the trait.
- Updated the reproduction child creation code in `Universe.tick()` to pass the `is_contagious` parameter correctly.
- Updated both combat calculation blocks (scent tracking and direct collision) in `Universe.tick()` to enforce transmission logic: if the attacker is infected and contagious, the defender becomes infected (unless immune); and if the defender is infected and contagious, the attacker becomes infected (unless immune).
- Assigned the visual character `ñ` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added a `TestIsContagious` class to `tests/test_engine.py` with 4 dedicated tests (`test_is_contagious_mutation`, `test_is_contagious_attacker`, `test_is_contagious_defender`, `test_is_contagious_immunity`) to fully verify the expected transmission logic and immunity interactions.

### Analysis 211: Arboreal Trait
**Overview:**
Implemented the `is_arboreal` trait. Entities with this trait gain a natural affinity for forest environments, treating them as shelters.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_arboreal` flag.
- Updated `Universe.tick()` to allow `is_arboreal` to be inherited and mutated during reproduction.
- Updated the `in_shelter` definition in `Universe.tick()` to evaluate to `True` for arboreal entities stationed on `forest` terrain, reducing their per-tick energy loss dynamically.
- Updated `prey_in_shelter` calculations within both the tracking and collision combat blocks in `Universe.tick()` to grant arboreal entities on `forest` terrain a flat +3 effective defense bonus.
- Assigned the visual character `♣` to represent this trait in `src/universe/visualizer.py` and appended it to `used_chars.txt`.
- Added the `TestIsArboreal` class to `tests/test_engine.py` to verify trait inheritance, energy recovery mechanics, and combat defense bonuses.

### Analysis 212: Stargazer Trait
**Overview:**
Implemented the `is_stargazer` trait. Entities with this trait gain an energy bonus and extra stamina recovery on clear nights.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_stargazer` flag.
- Added inheritance and mutation logic for `is_stargazer` in `Universe.tick()`, allowing offspring to inherit or mutate the trait.
- Updated energy and stamina logic in `Universe.tick()` to grant +1 energy and +2 stamina recovery per tick on clear nights (when `self.is_night` is true and `self.current_event` is None).
- Assigned the visual character `✧` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added the `TestIsStargazer` class to `tests/test_engine.py` to verify trait inheritance, mutation, and the specific conditional energy and stamina bonuses.
- Added `is_stargazer` to the 'Completed' section of `agents.md`.

### Analysis 213: Sure Footed Trait
**Overview:**
Implemented the `is_sure_footed` trait. Entities with this trait are immune to stamina drain during earthquake events.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_sure_footed` flag.
- Updated `Universe.tick()` to allow `is_sure_footed` to be inherited and mutated during reproduction.
- Updated the stamina logic in `Universe.tick()` to drain 5 stamina from entities without the `is_sure_footed` trait during `earthquake` events.
- Assigned the visual character `▽` to represent this trait in `src/universe/visualizer.py` and recorded it in `used_chars.txt`.
- Added the `TestIsSureFooted` class to `tests/test_engine.py` to verify trait inheritance, mutation, and the specific stamina drain immunity.
- Added `is_sure_footed` to the 'Completed' section of `agents.md`.

### Analysis 214: Bloodthirsty Trait
**Overview:** Implemented the `is_bloodthirsty` trait for entities.
**Details:** Entities with this trait recover 20 stamina whenever they successfully hunt and eat a prey.

### Analysis 215: Sun Tracker Trait
**Overview:** Implemented the `is_sun_tracker` trait for entities.
**Details:** Entities with this trait gain an energy bonus during the day if they are standing on clear terrain (not a shelter or ash), allowing them to passively absorb sunlight.

### Analysis 216: Dust Bather Trait
**Overview:**
Implemented the `is_dust_bather` trait. Entities with this trait can cure their infections by standing on ash or sand terrain.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_dust_bather` flag.
- Updated `Universe.tick()` to allow `is_dust_bather` to be inherited and mutated during reproduction.
- Updated the execution block in `Universe.tick()` to cure `is_infected` status if an entity with `is_dust_bather` is on `ash` or `sand` terrain.
- Assigned the visual character `β` to represent this trait in `src/universe/visualizer.py` and appended it to `used_chars.txt`.
- Added the `TestIsDustBather` class to `tests/test_engine.py` to verify trait inheritance, mutation, and the infection-curing mechanics.
- Added `is_dust_bather` to the 'Completed' section of `agents.md`.

### Analysis 217: Magnetic Trait
**Overview:**
Implemented the `is_magnetic` trait. Entities with this trait draw power from magnetic storms, gaining 5 energy and 10 stamina each tick during the 'storm' event.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_magnetic` flag.
- Updated `Universe.tick()` to allow `is_magnetic` to be inherited and mutated during reproduction.
- Updated the environmental event execution block in `Universe.tick()` to apply energy and stamina bonuses when `self.current_event == 'storm'`.
- Assigned the visual character `⚡` to represent this trait in `src/universe/visualizer.py`.
- Added the `TestIsMagnetic` class to `tests/test_engine.py` to verify trait inheritance, mutation, and the storm bonuses.
- Also added missing dedicated tests for `is_farsighted` and `is_pacifist`.
- Added `is_magnetic` to the 'Completed' section of `agents.md`.

### Analysis 218: Drought Resistant Trait
**Overview:**
Implemented the `is_drought_resistant` trait. Entities with this trait do not lose hydration during a drought event.

**Details:**
- Modified `Entity.__init__` in `src/universe/engine.py` to accept and store the `is_drought_resistant` flag.
- Updated `Universe.tick()` to allow `is_drought_resistant` to be inherited and mutated during reproduction.
- Updated the main hydration drain block in `Universe.tick()` to bypass hydration loss if `self.current_event == 'drought'` and the entity has the trait.
- Assigned the visual character `∆` to represent this trait in `src/universe/visualizer.py` and appended it to `used_chars.txt`.
- Added the `TestIsDroughtResistant` class to `tests/test_engine.py` to verify trait inheritance, mutation, and the drought resistance mechanics.
- Added `is_drought_resistant` to the 'Completed' section of `agents.md` implicitly via Next Steps.

### Analysis 219: Pack Hunter Trait
**Overview:** Implemented the `pack_hunter` trait for entities.
**Details:** predatory entities to share target tracking and coordinate attacks with nearby entities of the same species.

### Analysis 220: Climb Trait
**Overview:** Implemented the `can_climb` trait for entities.
**Details:** entities to traverse 'wall' terrain blocks, simulating climbing over obstacles.

### Analysis 221: Desertic Trait
**Overview:** Implemented the `is_desertic` trait for entities.
**Details:** Entities with this trait suffer half hydration loss in hot climates and gain an energy efficiency bonus when traversing `sand` terrain.

### Analysis 222: Sleeping Trait
**Overview:** Added missing genetic mutation unit tests for `is_sleeping` trait in `tests/test_engine.py`.
**Details:** Ensured the trait correctly mutates during reproduction.

### Analysis 223: Sprint Trait
**Overview:** Implemented the `can_sprint` trait for entities.
**Details:** allowing entities to temporarily move faster at a high stamina cost.

### Analysis 224: Disease Vector Trait
**Overview:** Implemented the `disease_vector` trait for entities.
**Details:** scavenger entities, causing them to spread disease more rapidly when interacting with corpses.

### Analysis 225: Moon Bather Trait
**Overview:** Implemented the `is_moon_bather` trait for entities.
**Details:** Entities with this trait gain an energy bonus and extra stamina recovery at night when standing on clear terrain.

### Analysis 226: Can Hoard Trait
**Overview:** Implemented the `can_hoard` trait for entities.
**Details:** Entities with this trait can store food items in their inventory to consume later when hungry.

### Analysis 227: Can Burrow Trait
**Overview:** Implemented the `can_burrow` trait for entities.
**Details:** Entities with this trait can sleep underground, treating any terrain as a shelter to hide from predators while sleeping.

### Analysis 228: Is Sunbather Trait
**Overview:** Implemented the `is_sunbather` trait for entities.
**Details:** Entities with this trait recover extra energy and stamina during the day when the temperature is warm, but lose hydration faster.

### Analysis 229: Storm Chaser Trait
**Overview:** Implemented the `is_storm_chaser` trait for entities.
**Details:** Entities with this trait gain a +2 bonus to their effective attack during a 'storm' event.

### Analysis 230: Is Shadow Stalker Trait
**Overview:** Implemented the `is_shadow_stalker` trait for entities.
**Details:** Entities with this trait gain a +3 bonus to effective attack and reduce their stamina cost for movement to 0 when moving at night, making them formidable nocturnal hunters.

### Analysis 231: Is Pyrophilic Trait
**Overview:** Implemented the `is_pyrophilic` trait for entities.
**Details:** Entities with this trait gain an energy bonus and extra stamina recovery when standing on ash terrain.

### Analysis 232: is_iron_willed Trait
**Overview:** Implemented the `is_iron_willed` trait for entities.
**Details:** Entities with this trait are immune to the stat reductions caused by `is_intimidating` and `is_smelly` opponents in combat.

### Analysis 233: Is Frost Walker Trait
**Overview:** Implemented the `is_frost_walker` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `snow` or `ice` terrain. Added to the `Entity.__init__` and mutation logic, and updated `Universe.move_entity()` to check for this trait and terrain combination.

### Analysis 234: Marsh Strider Trait
**Overview:** Implemented the `is_marsh_strider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `mud` terrain and gain +2 effective defense during combat when standing on `mud`. Added to `Entity.__init__`, mutation logic, `Universe.move_entity()`, and the two combat logic blocks.

### Analysis 235: Dune Walker Trait
**Overview:** Implemented the `is_dune_walker` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `sand` terrain. Added to `Entity.__init__`, mutation logic, and `Universe.move_entity()`.

### Analysis 236: Water Strider Trait
**Overview:** Implemented the `is_water_strider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `water` terrain and can walk on `water` (treated as passable). Added to `Entity.__init__`, mutation logic, `Universe.is_passable()`, and `Universe.move_entity()`. Also ensured pathfinding and `get_terrains_at` usages treat it properly.

### Analysis 237: Web Walker Trait
**Overview:** Implemented the `is_web_walker` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `web` terrain and are immune to having their stamina set to 0 by webs. Added to `Entity.__init__`, mutation logic, and `Universe.move_entity()`.

### Analysis 238: Ash Walker Trait
**Overview:** Implemented the `is_ash_walker` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `ash` terrain.

### Analysis 239: Wind Glider Trait
**Overview:** Implemented the `is_wind_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving during a 'storm' event. Added to `Entity.__init__`, mutation logic, and stamina logic in `Universe.tick()`.

### Analysis 240: Forest Walker Trait
**Overview:** Implemented the `is_forest_walker` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `forest` terrain. Added to `Entity.__init__`, mutation logic, and stamina tracking in `Universe.move_entity()`.

### Analysis 241: Rain Dancer Trait
**Overview:** Implemented the `is_rain_dancer` trait for entities.
**Details:** Entities with this trait gain energy when they are within the radius of a 'rain' event. Added to `Entity.__init__`, mutation logic, and `Universe.tick()` rain event handling. Also added corresponding unit tests.

### Analysis 242: Mud Glider Trait
The `is_mud_glider` trait has been implemented to allow entities to navigate mud terrain without expending stamina. This provides a significant mobility advantage in environments with abundant mud, which would typically slow down or drain the stamina of other entities. This trait promotes survival strategies centered around swampy or muddy biomes.

### Analysis 243: Drought Strider Trait
The `is_drought_strider` trait has been implemented to allow entities to navigate during drought events without expending stamina. This provides a significant mobility advantage during periods of extreme heat and dryness. This trait promotes survival strategies centered around drought events.

### Analysis 244: Earthquake Glider Trait
**Overview:** Implemented the `is_earthquake_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving during an 'earthquake' event. Added to `Entity.__init__`, mutation logic, and stamina tracking.

### Analysis 245: Blizzard Glider Trait
**Overview:** Implemented the `is_blizzard_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving during a 'blizzard' event. Added to `Entity.__init__`, mutation logic, and stamina tracking.

### Analysis 246: Seismic Sensitive Trait
**Overview:** Implemented the `is_seismic_sensitive` trait for entities.
**Details:** Entities with this trait have their effective perception radius tripled during an 'earthquake' event.

### Analysis 247: Volcanic Glider Trait
**Overview:** Implemented the `is_volcanic_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving during a 'volcano' event. Added to `Entity.__init__`, mutation logic, and stamina tracking in `Universe.move_entity`. Assigned the visual character `∨` to represent this trait in `src/universe/visualizer.py`. Also added tests `TestIsVolcanicGlider` and `test_render_is_volcanic_glider`.

### Analysis 248: Snow Glider Trait
**Overview:** Implemented the `is_snow_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on snow terrain.

### Analysis 249: Ice Glider Trait
**Overview:** Implemented the `is_ice_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on ice terrain.

### Analysis 250: Day Glider Trait
**Overview:** Implemented the `is_day_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving during the day.

### Analysis 251: Night Glider Trait
**Overview:** Implemented the `is_night_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving at night.

### Analysis 252: Deep Water Glider Trait
**Overview:** Implemented the `is_deep_water_glider` trait for entities.
**Details:** Entities with this trait consume 0 stamina when moving on `deep-water` terrain. Added trait to `Entity.__init__`, added mutation logic in `Universe.tick`, and updated stamina rules in `Universe.move_entity`. Tested in `tests/test_engine.py`.


### Analysis 253: Implemented is_summer_glider Trait
- Added the `is_summer_glider` trait to the `Entity` class.
- Updated `Universe.tick()` to reduce movement stamina cost to 0 when `entity.is_summer_glider` is True and `self.current_season == 'summer'`.
- Added reproduction and trait inheritance logic for `is_summer_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_summer_glider`.
- Added `TestIsSummerGlider` test class in `tests/test_engine.py` to verify stamina conservation during summer, normal stamina drain in spring, and correct mutation logic.
- Skips flakiness tests by restoring missing `self.universe.entities = []` and adding flaky decorators when appropriate.
- Updated `agents.md` checklist with the completed trait.


### Analysis 254: Implemented is_autumn_glider Trait
- Added the `is_autumn_glider` trait to the `Entity` class.
- Updated `Universe.tick()` to reduce movement stamina cost to 0 when `entity.is_autumn_glider` is True and `self.current_season == 'autumn'`.
- Added reproduction and trait inheritance logic for `is_autumn_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_autumn_glider`.
- Added `TestIsAutumnGlider` test class in `tests/test_engine.py` to verify stamina conservation during autumn, normal stamina drain in winter, and correct mutation logic.
- Updated `agents.md` checklist with the completed trait.

### Analysis 255: Implemented is_ash_glider Trait
- Added the `is_ash_glider` trait to the `Entity` class.
- Updated `Universe.tick()` to reduce movement stamina cost to 0 when `entity.is_ash_glider` is True and the entity is on `ash` terrain.
- Added reproduction and trait inheritance logic for `is_ash_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_ash_glider`.
- Added `TestIsAshGlider` test class in `tests/test_engine.py` to verify stamina conservation on ash terrain.
- Updated `agents.md` checklist with the completed trait.

### Analysis 256: Implemented is_spring_glider Trait
- Added the `is_spring_glider` trait to the `Entity` class.
- Updated `Universe.tick()` to reduce movement stamina cost to 0 when `entity.is_spring_glider` is True and `self.current_season == 'spring'`.
- Added reproduction and trait inheritance logic for `is_spring_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_spring_glider`.
- Added `TestIsSpringGlider` test class in `tests/test_engine.py` to verify stamina conservation during spring.
- Updated `agents.md` checklist with the completed trait.

### Analysis 257: Implemented is_winter_glider Trait
- Added the `is_winter_glider` trait to the `Entity` class.
- Updated `Universe.tick()` to reduce movement stamina cost to 0 when `entity.is_winter_glider` is True and `self.current_season == 'winter'`.
- Added reproduction and trait inheritance logic for `is_winter_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_winter_glider`.
- Added `TestIsWinterGlider` test class in `tests/test_engine.py` to verify stamina conservation during winter.
- Updated `agents.md` checklist with the completed trait.

### Analysis 260: Implemented is_fire_glider Trait
- Added the `is_fire_glider` trait to the `Entity` class.
- Updated `Universe.move_entity()` to reduce movement stamina cost to 0 when `entity.is_fire_glider` is True and moving inside a 'fire' event.
- Added reproduction and trait inheritance logic for `is_fire_glider` in `Universe.tick()`, including random mutations.
- Ensured proper instantiation of children entities with `is_fire_glider`.
- Added `TestIsFireGlider` test class in `tests/test_engine.py` to verify stamina conservation in fire events and correct mutation logic.
- Updated `agents.md` checklist with the completed trait.

### Analysis 261: Mountain Glider Trait Analysis
**Overview:** Evaluated the recent implementation of the `is_mountain_glider` trait.
**Details:** Commit 7852d5c introduced the `is_mountain_glider` trait, enabling entities to consume 0 stamina when traversing mountain terrain. This provides a significant survival and mobility advantage in mountainous biomes. Reviewed changes in `src/universe/engine.py` (added trait, mutation logic, stamina adjustment), tests, and documentation (`CHANGELOG.md`, `agents.md`).

### Analysis 262: Implemented is_mountain_dweller Trait
- Added the `is_mountain_dweller` trait to the `Entity` class.
- Updated `Universe.tick()` to treat `mountain` terrain as a shelter, granting energy recovery and defense bonuses to entities with this trait.
- Implemented trait inheritance and random mutations for `is_mountain_dweller`.
- Added unit tests to `tests/test_engine.py` to verify the shelter logic on mountains and the successful inheritance/mutation of the trait.
- Documented task completion in `agents.md`.

### Analysis 263: Implemented is_sand_dweller Trait
- Added the `is_sand_dweller` trait to the `Entity` class.
- Updated `Universe.tick()` to treat `sand` terrain as a shelter, allowing sand dwellers to recover energy and gain defense benefits.
- Incorporated the trait into the reproduction system to ensure proper inheritance and mutation chances.
- Updated the CLI Visualizer to display 'S' for entities with this trait.
- Created `TestSandDweller` test class in `tests/test_engine.py` to assert energy recovery on sand shelters and check mutation logic.
- Logged changes and checked off the requirement in `agents.md`.

### Analysis 264: Implemented is_forest_dweller Trait
- Introduced the `is_forest_dweller` trait to the `Entity` class.
- Modified `Universe.tick()` so that entities with this trait view `forest` terrain as a protective shelter, offering passive defense and energy regeneration.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Updated associated documentation.

### Analysis 265: Implemented is_water_dweller Trait
- Introduced the `is_water_dweller` trait to the `Entity` class.
- Modified `Universe.tick()` so that entities with this trait can utilize `water` terrain as a shelter for energy recovery and defense against predators.
- Added reproduction and mutation logic for the trait to ensure offspring can inherit it.
- Added unit tests `test_is_water_dweller` and `test_is_water_dweller_mutation` to verify behavior.
- Addressed and resolved flaky stamina and mutation tests related to deep water and mountain traits.
- Marked task complete in `agents.md`.

### Analysis 266: Fixed Glider Test Naming Convention
- Discovered failing pre-commit checks due to a mismatch in test naming conventions expected by `check_missing_tests.py`.
- Renamed the tests `test_is_forest_glider_effect`, `test_is_water_glider_effect`, and `test_is_shelter_glider_effect` to `test_is_forest_glider`, `test_is_water_glider`, and `test_is_shelter_glider` respectively in `tests/test_engine.py`.
- This ensures the automated verification scripts correctly detect the test coverage for the glider traits.


### Analysis 267: Implemented is_cave_dweller Trait
- Introduced the `is_cave_dweller` trait to the `Entity` class.
- Modified `Universe.tick()` so that entities with this trait view `cave` terrain as a protective shelter, offering passive defense and energy regeneration.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Added visual representation ('C') in `src/universe/visualizer.py`.
- Included comprehensive test coverage in `tests/test_engine.py` and `tests/test_visualizer.py`.
- Updated `agents.md` and `CHANGELOG.md` to reflect the completed task.


### Analysis 268: Project Evolution and Agent Actions
**Overview:** Analyzed recent project evolution and agent actions in accordance with the `is_cave_dweller` trait implementation and other recent features.
**Details:**
- Implemented `is_web_glider` trait. Entities with this trait consume 0 stamina when moving on web terrain.
- Added missing visualization rendering and tests for `is_social`, `is_forestal`, and `is_desertic` traits.
- Added missing genetic mutation unit tests for `is_social` and `is_forestal` traits.
- Implemented `is_forestal` trait. Entities with this trait gain defense (+3) during combat when positioned on forest terrain. Also added forest terrain and forestal entities support to the CLI visualizer.


### Analysis 269: Implemented is_cave_glider Trait
- Introduced the `is_cave_glider` trait to the `Entity` class.
- Modified `Universe.move_entity()` so that entities with this trait consume 0 stamina when moving on `cave` terrain.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Added test coverage in `tests/test_engine.py`.

### Analysis 270: Implemented is_blizzard_dweller Trait
- Added the `is_blizzard_dweller` trait to the `Entity` class.
- Updated `Universe.tick()` so that entities with this trait treat `blizzard` conditions as a shelter, gaining energy recovery and defense.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Added test coverage in `tests/test_engine.py` for both the trait effect and its mutation logic.

### Analysis 271: Implemented is_storm_dweller Trait
- Introduced the `is_storm_dweller` trait to the `Entity` class.
- Modified `Universe.tick()` so that entities with this trait view `storm` conditions as a protective shelter, offering passive defense and energy regeneration.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Added test coverage in `tests/test_engine.py`.
- Updated `agents.md` and `CHANGELOG.md` to reflect the completed task.


### Analysis 272: Implemented is_spring_dweller Trait
- Added the `is_spring_dweller` trait to the `Entity` class.
- Updated `Universe.tick()` to treat the 'spring' season as a shelter, allowing spring dwellers to recover energy and gain defense benefits.
- Incorporated the trait into the reproduction system to ensure proper inheritance and mutation chances.
- Added test coverage in `tests/test_engine.py` to assert energy recovery during spring and check mutation logic.
- Logged changes and checked off the requirement in `agents.md`.


## Implementation of is_autumn_dweller trait

- The `is_autumn_dweller` trait was implemented, allowing entities to treat the autumn season as a shelter.
- This grants them increased defense and energy recovery during autumn.
- Added the trait to `src/universe/engine.py` (Entity initialization, reproduction mutation, shelter logic).
- Added tests `test_is_autumn_dweller` and `test_is_autumn_dweller_mutation` to `tests/test_engine.py`.
- Passed all tests successfully.
- Updated `agents.md` and `CHANGELOG.md`.

### Analysis 273: Implemented is_poison_dweller Trait
- Introduced the `is_poison_dweller` trait to the `Entity` class.
- Modified `Universe.tick()` so that entities with this trait view being poisoned as a protective shelter, offering passive defense and energy regeneration.
- Ensured genetic propagation and mutation handling for the trait during reproduction.
- Added test coverage in `tests/test_engine.py`.
- Updated `agents.md` to reflect the completed task.


### Analysis 274: Added Tests and Visualizer Support for Seasonal Dweller Traits
- **Description**: Added tests and visualizer support for seasonal dweller traits.
- **Details**:
  - Added missing unit tests for `is_spring_dweller`, `is_summer_dweller`, `is_autumn_dweller`, and `is_winter_dweller` traits in `tests/test_visualizer.py`.
  - Added the corresponding visualizer rendering logic for these traits in `src/universe/visualizer.py`.


## Analysis of `is_ageless` trait
- **Agent Intent:** Implement the `is_ageless` trait to allow entities to bypass death by old age.
- **Implementation Details:** Modified `Entity.is_alive` to ignore `max_age` checks if `is_ageless` is True. Added trait instantiation and mutation logic inside `engine.py`. Added corresponding unit tests in `test_engine.py` and modified visualizer (`visualizer.py` and `test_visualizer.py`) to render ageless entities with character 'A'.
- **Future work:** N/A.

### Analysis 275: Implemented is_cave_walker Trait
- **Agent Intent:** Implement the `is_cave_walker` trait for entities.
- **Implementation Details:**
  - Added `is_cave_walker` trait initialization and genetic propagation in `src/universe/engine.py`.
  - Allowed entities with this trait to ignore elevation stamina penalties when walking on `cave` terrains.
  - Added mechanical and mutation test coverage for the trait in `tests/test_engine.py`.
  - Updated `agents.md` to reflect the task's completion.
- **Future work:** N/A.

## 157. `is_sleep_dweller` trait
The `is_sleep_dweller` trait was implemented. Entities with this trait treat being asleep as a shelter, gaining increased defense and energy recovery while sleeping. This provides a strategic advantage for resting and conserving energy without needing a physical shelter.
