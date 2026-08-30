class CLIVisualizer:
    def __init__(self, universe):
        self.universe = universe

    def render(self):
        # Create an empty grid
        grid = [['.' for _ in range(self.universe.width)] for _ in range(self.universe.height)]

        # Add terrain
        for terrain in self.universe.terrains:
            if 0 <= terrain.x < self.universe.width and 0 <= terrain.y < self.universe.height:
                if terrain.terrain_type == 'wall':
                    grid[terrain.y][terrain.x] = '#'
                elif terrain.terrain_type == 'water':
                    grid[terrain.y][terrain.x] = '~'
                elif terrain.terrain_type == 'deep-water':
                    grid[terrain.y][terrain.x] = '≈'
                elif terrain.terrain_type == 'ice':
                    grid[terrain.y][terrain.x] = '*'
                elif terrain.terrain_type == 'ash':
                    grid[terrain.y][terrain.x] = ':'
                elif terrain.terrain_type == 'mud':
                    grid[terrain.y][terrain.x] = 'm'
                elif terrain.terrain_type == 'sand':
                    grid[terrain.y][terrain.x] = ','
                elif terrain.terrain_type == 'snow':
                    grid[terrain.y][terrain.x] = 's'
                elif terrain.terrain_type == 'shelter':
                    grid[terrain.y][terrain.x] = '^'
                elif terrain.terrain_type == 'web':
                    grid[terrain.y][terrain.x] = 'x'
                elif terrain.terrain_type == 'forest':
                    grid[terrain.y][terrain.x] = 'Y'
                elif terrain.terrain_type == 'cave':
                    grid[terrain.y][terrain.x] = 'c'

        # Add food
        for food in self.universe.foods:
            if 0 <= food.x < self.universe.width and 0 <= food.y < self.universe.height:
                grid[food.y][food.x] = 'o' if getattr(food, 'hatch_entity', None) is not None else ('T' if getattr(food, 'toxicity', 0) > 0 else ('+' if getattr(food, 'plant_type', 'generic') == 'medicinal' else ('%' if getattr(food, 'plant_type', 'generic') == 'meat' else 'f')))

        # Add entities (entities overwrite food in visualization if on same spot)
        for entity in self.universe.entities:
            if 0 <= entity.x < self.universe.width and 0 <= entity.y < self.universe.height:

                diet = getattr(entity, 'diet', 'herbivore')
                is_hibernating = getattr(entity, 'is_hibernating', False)

                if getattr(entity, 'is_infected', False):
                    if getattr(entity, 'is_photosensitive', False):
                        char = '!'
                    elif diet == 'carnivore':
                        char = 'X'
                    elif diet == 'scavenger':
                        char = 'W'
                    elif diet == 'omnivore':
                        char = 'Q'
                    else:
                        char = 'S'
                else:
                    if getattr(entity, 'is_spiteful', False):
                        char = '%'
                    elif getattr(entity, 'is_ice_dweller', False):
                        char = 'I'
                    elif getattr(entity, 'is_ash_dweller', False):
                        char = 'J'
                    elif getattr(entity, 'is_snow_dweller', False):
                        char = 'K'
                    elif getattr(entity, 'is_mud_dweller', False):
                        char = 'L'
                    elif getattr(entity, 'is_sleeping', False):
                        char = '0'
                    elif getattr(entity, 'is_bloodthirsty', False):
                        char = '¢'
                    elif getattr(entity, 'is_chameleon', False):
                        char = '`'
                    elif getattr(entity, 'is_pacifist', False):
                        char = '¥'
                    elif getattr(entity, 'is_farsighted', False):
                        char = '€'
                    elif getattr(entity, 'is_cleaner', False):
                        char = '+'
                    elif getattr(entity, 'is_flying', False):
                        char = '1'
                    elif getattr(entity, 'can_hibernate', False):
                        char = '2'
                    elif getattr(entity, 'lays_eggs', False):
                        char = '3'
                    elif getattr(entity, 'can_hoard', False):
                        char = '4'
                    elif getattr(entity, 'can_burrow', False):
                        char = '5'
                    elif getattr(entity, 'is_territorial', False):
                        char = '6'
                    elif getattr(entity, 'is_forager', False):
                        char = "'"
                    elif getattr(entity, 'is_protective', False):
                        char = '('
                    elif getattr(entity, 'is_playful', False):
                        char = '-'
                    elif getattr(entity, 'is_agile', False):
                        char = '7'
                    elif getattr(entity, 'is_fast_learner', False):
                        char = '='
                    elif getattr(entity, 'is_opportunistic', False):
                        char = '8'
                    elif getattr(entity, 'is_hardy', False):
                        char = '|'
                    elif getattr(entity, 'has_thick_skin', False):
                        char = '9'
                    elif getattr(entity, 'is_aposematic', False):
                        char = 'A'
                    elif getattr(entity, 'can_photosynthesize', False):
                        char = 'P'
                    elif getattr(entity, 'is_parasitic', False):
                        char = 'D'
                    elif getattr(entity, 'has_scales', False):
                        char = 'R'
                    elif getattr(entity, 'has_claws', False):
                        char = 'K'
                    elif getattr(entity, 'has_fur', False):
                        char = 'U'
                    elif getattr(entity, 'can_climb', False):
                        char = 'L'
                    elif getattr(entity, 'pack_hunter', False):
                        char = 'W'
                    elif getattr(entity, 'is_mountain_dweller', False):
                        char = 'G'
                    elif getattr(entity, 'is_regenerative', False):
                        char = 'G'
                    elif getattr(entity, 'is_immune', False):
                        char = 'I'
                    elif getattr(entity, 'is_amphibious', False):
                        char = 'B'
                    elif getattr(entity, 'has_bioluminescence', False):
                        char = 'l'
                    elif getattr(entity, 'is_aquatic', False):
                        char = 'a'
                    elif getattr(entity, 'is_electric', False):
                        char = 'e'
                    elif getattr(entity, 'is_cold_blooded', False):
                        char = 'b'
                    elif getattr(entity, 'is_fruiting', False):
                        char = 'F'
                    elif getattr(entity, 'has_echolocation', False):
                        char = 'E'
                    elif getattr(entity, 'has_shell', False):
                        char = 'H'
                    elif getattr(entity, 'has_horns', False):
                        char = 'Y'
                    elif getattr(entity, 'is_fearless', False):
                        char = 'f'
                    elif getattr(entity, 'is_scavenger', False):
                        char = '?'
                    elif getattr(entity, 'is_vampiric', False):
                        char = 'y'
                    elif getattr(entity, 'is_venomous', False):
                        char = 'v'
                    elif getattr(entity, 'can_spin_webs', False):
                        char = 'w'
                    elif getattr(entity, 'is_volcanic', False):
                        char = 'j'
                    elif getattr(entity, 'is_forestal', False):
                        char = 't'
                    elif getattr(entity, 'is_desertic', False):
                        char = 'd'
                    elif getattr(entity, 'is_social', False):
                        char = 'p'
                    elif getattr(entity, 'is_scentless', False):
                        char = 'Z'
                    elif getattr(entity, 'disease_vector', False):
                        char = 'M'
                    elif getattr(entity, 'is_nocturnal_predator', False):
                        char = 'N'
                    elif getattr(entity, 'is_nocturnal', False):
                        char = 'n'
                    elif getattr(entity, 'is_carnivorous_plant', False):
                        char = 'c'
                    elif getattr(entity, 'is_detritivore', False):
                        char = 'g'
                    elif getattr(entity, 'is_scout', False):
                        char = '['
                    elif getattr(entity, 'is_reckless', False):
                        char = '<'
                    elif getattr(entity, 'is_intimidating', False):
                        char = ']'
                    elif getattr(entity, 'can_sweat', False):
                        char = 'q'
                    elif getattr(entity, 'has_blubber', False):
                        char = '@'
                    elif getattr(entity, 'is_mud_bather', False):
                        char = 'n'
                    elif getattr(entity, 'has_spikes', False):
                        char = 'k'
                    elif getattr(entity, 'is_filter_feeder', False):
                        char = 'u'
                    elif getattr(entity, 'is_gluttonous', False):
                        char = 'x'
                    elif getattr(entity, 'is_ambush_predator', False):
                        char = 'm'
                    elif getattr(entity, 'is_cannibalistic', False):
                        char = 'J'
                    elif getattr(entity, 'is_solitary', False):
                        char = 'h'
                    elif getattr(entity, 'can_sprint', False):
                        char = 'r'
                    elif getattr(entity, 'is_migratory', False):
                        char = 'z'
                    elif getattr(entity, 'is_frugivore', False):
                        char = 'T'
                    elif getattr(entity, 'is_restless', False):
                        char = ':'
                    elif getattr(entity, 'is_vengeful', False):
                        char = ';'
                    elif getattr(entity, 'is_cooperative', False):
                        char = 'i'
                    elif getattr(entity, 'has_strong_stomach', False):
                        char = 's'
                    elif getattr(entity, 'is_patient', False):
                        char = '*'
                    elif getattr(entity, 'is_heavy', False):
                        char = 'H'
                    elif getattr(entity, 'is_lightweight', False):
                        char = 'Q'
                    elif getattr(entity, 'is_stealthy', False):
                        char = '}'
                    elif getattr(entity, 'is_mimic', False):
                        char = '\\'
                    elif getattr(entity, 'has_sharp_teeth', False):
                        char = ')'
                    elif getattr(entity, 'can_leap', False):
                        char = 'J'
                    elif getattr(entity, 'is_endurance_runner', False):
                        char = '~'
                    elif getattr(entity, 'is_evasive', False):
                        char = '^'
                    elif getattr(entity, 'is_prolific', False):
                        char = '&'
                    elif getattr(entity, 'is_resourceful', False):
                        char = '$'
                    elif getattr(entity, 'is_nomadic', False):
                        char = '}'
                    elif getattr(entity, 'is_vocal', False):
                        char = 'o'
                    elif getattr(entity, 'is_sunbather', False):
                        char = '#'
                    elif getattr(entity, 'is_stargazer', False):
                        char = '✧'
                    elif getattr(entity, 'is_moon_bather', False):
                        char = '☾'
                    elif getattr(entity, 'is_storm_chaser', False):
                        char = '¿'
                    elif getattr(entity, 'is_shadow_stalker', False):
                        char = '♞'
                    elif getattr(entity, 'is_sure_footed', False):
                        char = '▽'
                    elif getattr(entity, 'is_photosensitive', False):
                        char = '!'
                    elif getattr(entity, 'is_thief', False):
                        char = '_'
                    elif getattr(entity, 'is_absorbent', False):
                        char = '/'
                    elif getattr(entity, 'is_lucky', False):
                        char = ','
                    elif getattr(entity, 'is_telepathic', False):
                        char = '~'
                    elif getattr(entity, 'is_defensive', False):
                        char = 'D'
                    elif diet == 'carnivore':
                        char = 'C'
                    elif diet == 'scavenger':
                        char = 'V'
                    elif getattr(entity, 'is_smelly', False):
                        char = ';'
                        color = '\033[38;5;130m'
                    elif getattr(entity, 'is_relentless', False):
                        char = '>'
                    elif getattr(entity, 'is_resilient', False):
                        char = '{'
                    elif getattr(entity, 'is_parasite_resistant', False):
                        char = '"'
                    elif getattr(entity, 'is_ruthless', False):
                        char = '.'
                    elif getattr(entity, 'is_tireless', False):
                        char = '▲'
                    elif diet == 'omnivore':
                        char = 'O'
                    elif getattr(entity, 'is_vigilant', False):
                        char = '£'
                    elif getattr(entity, 'is_unappetizing', False):
                        char = '§'
                    elif getattr(entity, 'is_introspective', False):
                        char = 'Ω'
                    elif getattr(entity, 'is_frenzied', False):
                        char = 'ç'
                    elif getattr(entity, 'is_sun_tracker', False):
                        char = '¤'
                    elif getattr(entity, 'is_empathic', False):
                        char = '±'
                    elif getattr(entity, 'is_hypnotic', False):
                        char = '•'
                    elif getattr(entity, 'is_tracker', False):
                        char = '↬'
                    elif getattr(entity, 'is_contagious', False):
                        char = 'ñ'
                    elif getattr(entity, 'is_arboreal', False):
                        char = '♣'
                    elif getattr(entity, 'is_dust_bather', False):
                        char = 'β'
                    elif getattr(entity, 'is_drought_strider', False):
                        char = 'Ð'
                    elif getattr(entity, 'is_earthquake_glider', False):
                        char = 'Ç'
                    elif getattr(entity, 'is_volcanic_glider', False):
                        char = '∨'
                    elif getattr(entity, 'is_magnetic', False):
                        char = '⚡'
                    elif getattr(entity, 'is_pyrophilic', False):
                        char = '%'
                    elif getattr(entity, 'is_drought_resistant', False):
                        char = '∆'
                    else:
                        char = 'E'

                grid[entity.y][entity.x] = char.lower() if is_hibernating else (char.upper() if getattr(entity, 'level', 1) >= 3 else char)

        # Join lines
        return '\n'.join(''.join(row) for row in grid)

    def print_state(self):
        print(f"Time: {self.universe.time}")
        if hasattr(self.universe, 'is_day'):
            day_night = "Day" if self.universe.is_day else "Night"
            print(f"Time of Day: {day_night}")
        if hasattr(self.universe, 'current_season'):
            print(f"Season: {self.universe.current_season.capitalize()}")
        if hasattr(self.universe, 'current_event') and self.universe.current_event:
            print(f"Event: {self.universe.current_event.upper()} ({self.universe.event_remaining_time} ticks left)")
        if hasattr(self.universe, 'localized_events') and self.universe.localized_events:
            event_strs = [f"{e.event_type.capitalize()} at ({e.x},{e.y}) r={e.radius}" for e in self.universe.localized_events]
            print(f"Localized Events: {', '.join(event_strs)}")
        if hasattr(self.universe, 'temperature_zones') and self.universe.temperature_zones:
            tz_strs = [f"Zone at ({tz.x},{tz.y}) r={tz.radius} mod={tz.temperature_modifier:+}°C" for tz in self.universe.temperature_zones]
            print(f"Temperature Zones: {', '.join(tz_strs)}")
        print(self.render())
