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
