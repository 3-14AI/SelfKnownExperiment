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

### Analysis 232: Mud Camouflaged Trait
**Overview:** Implemented the `is_mud_camouflaged` trait for entities.
**Details:** Entities with this trait gain a +0.5 camouflage bonus when standing on mud terrain, effectively hiding them from predators and prey.
