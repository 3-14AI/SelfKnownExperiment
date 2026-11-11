
class DwarfPlanet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Exoplanet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class AsteroidBelt:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
import random

class StellarStream:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class TidalTail:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class GalacticDisk:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class GalacticHalo:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class GalacticBar:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class GalacticCore:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class GalacticBulge:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class SpiralArm:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class HIIRegion:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class StellarAssociation:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class OpenCluster:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class RoguePlanet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Meteor:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Comet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class KuiperBelt:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class OortCloud:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Star:
    def __init__(self, name, radius, star_type=None):
        self.name = name
        self.radius = radius
        self.star_type = star_type or random.choice(['dwarf', 'giant', 'supergiant', 'neutron'])

        if self.star_type == 'dwarf':
            self.temperature = radius * 5
            self.luminosity = radius * 2
        elif self.star_type == 'giant':
            self.temperature = radius * 10
            self.luminosity = radius * 20
        elif self.star_type == 'supergiant':
            self.temperature = radius * 20
            self.luminosity = radius * 100
        elif self.star_type == 'neutron':
            self.temperature = radius * 100
            self.luminosity = radius * 5

class Moon:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius



class PlanetaryRing:
    def __init__(self, name, radius, width):
        self.name = name
        self.radius = radius
        self.width = width

class Planet:
    def __init__(self, name, x, y, radius, planet_type=None):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.moons = []
        self.rings = []
        self.planet_type = planet_type or random.choice(['rocky', 'gaseous', 'oceanic'])

        if self.planet_type == 'rocky':
            self.mass = radius * 10
            self.atmosphere = 'thin'
        elif self.planet_type == 'gaseous':
            self.mass = radius * 5
            self.atmosphere = 'thick'
        else: # oceanic
            self.mass = radius * 8
            self.atmosphere = 'moderate'


    def generate_rings(self, num_rings):
        import random
        for i in range(num_rings):
            name = f"{self.name}-Ring-{i+1}"
            radius = self.radius + random.randint(1000, 5000)
            width = random.randint(100, 1000)
            self.rings.append(PlanetaryRing(name, radius, width))

    def generate_moons(self, num_moons):
        for i in range(num_moons):
            name = f"{self.name}-Moon-{i+1}"
            radius = random.randint(100, 1000)
            self.moons.append(Moon(name, radius))

class StarSystem:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.planets = []
        self.dwarf_planets = []
        self.asteroid_belts = []
        self.kuiper_belts = []
        self.oort_clouds = []
        self.meteors = []
        self.comets = []
        self.stars = []

    def generate_dwarf_planets(self, num_dwarf_planets):
        for i in range(num_dwarf_planets):
            name = f"{self.name}-Dwarf-{i+1}"
            radius = random.uniform(500, 2000)
            self.dwarf_planets.append(DwarfPlanet(name, radius))

    def generate_planets(self, num_planets):
        for i in range(num_planets):
            name = f"{self.name}-{i+1}"
            px = self.x + random.randint(-100, 100)
            py = self.y + random.randint(-100, 100)
            radius = random.randint(1000, 10000)
            self.planets.append(Planet(name, px, py, radius))

    def generate_asteroid_belts(self, num_belts):
        for i in range(num_belts):
            name = f"{self.name}-Belt-{i+1}"
            radius = random.randint(1000, 10000)
            self.asteroid_belts.append(AsteroidBelt(name, radius))


    def generate_meteors(self, num_meteors):
        for i in range(num_meteors):
            name = f"{self.name}-Meteor-{i+1}"
            radius = random.randint(1, 20)
            self.meteors.append(Meteor(name, radius))

    def generate_comets(self, num_comets):
        for i in range(num_comets):
            name = f"{self.name}-Comet-{i+1}"
            radius = random.randint(10, 100)
            self.comets.append(Comet(name, radius))

    def generate_stars(self, num_stars):
        for i in range(num_stars):
            name = f"{self.name}-Star-{i+1}"
            radius = random.randint(10000, 100000)
            self.stars.append(Star(name, radius))


    def generate_kuiper_belts(self, num_belts):
        for i in range(num_belts):
            name = f"{self.name}-KuiperBelt-{i+1}"
            radius = random.uniform(30, 50)
            self.kuiper_belts.append(KuiperBelt(name, radius))

    def generate_oort_clouds(self, num_clouds):
        for i in range(num_clouds):
            name = f"{self.name}-OortCloud-{i+1}"
            radius = random.randint(50000, 100000)
            self.oort_clouds.append(OortCloud(name, radius))



class WhiteHole:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class BlackHole:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Nebula:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class Wormhole:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius



class Pulsar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Quasar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius



class Supernova:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Magnetar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Hypernova:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
class EmissionNebula:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class MolecularCloud:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class BokGlobule:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class SatelliteGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class RingGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Protogalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class RadioGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class SeyfertGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class StarburstGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class PeculiarGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class DarkGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class InteractingGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class LuminousInfraredGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Galaxy:
    def generate_protogalaxies(self, num_protogalaxies):
        import random
        for i in range(num_protogalaxies):
            name = f"Protogalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.protogalaxies.append(Protogalaxy(name, radius))

    def generate_radio_galaxies(self, num_radio_galaxies):
        import random
        for i in range(num_radio_galaxies):
            name = f"RadioGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.radio_galaxies.append(RadioGalaxy(name, radius))

    def generate_seyfert_galaxies(self, num_seyfert_galaxies):
        import random
        for i in range(num_seyfert_galaxies):
            name = f"SeyfertGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.seyfert_galaxies.append(SeyfertGalaxy(name, radius))

    def generate_starburst_galaxies(self, num_starburst_galaxies):
        import random
        for i in range(num_starburst_galaxies):
            name = f"StarburstGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.starburst_galaxies.append(StarburstGalaxy(name, radius))

    def generate_elliptical_galaxies(self, num_elliptical_galaxies):
        import random
        for i in range(num_elliptical_galaxies):
            name = f"EllipticalGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.elliptical_galaxies.append(EllipticalGalaxy(name, radius))

    def generate_ring_galaxies(self, num_ring_galaxies):
        import random
        for i in range(num_ring_galaxies):
            name = f"RingGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.ring_galaxies.append(RingGalaxy(name, radius))

    def generate_spiral_galaxies(self, num_spiral_galaxies):
        import random
        for i in range(num_spiral_galaxies):
            name = f"SpiralGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.spiral_galaxies.append(SpiralGalaxy(name, radius))

    def generate_irregular_galaxies(self, num_irregular_galaxies):
        import random
        for i in range(num_irregular_galaxies):
            name = f"IrregularGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.irregular_galaxies.append(IrregularGalaxy(name, radius))

    def generate_lenticular_galaxies(self, num_lenticular_galaxies):
        import random
        for i in range(num_lenticular_galaxies):
            name = f"LenticularGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.lenticular_galaxies.append(LenticularGalaxy(name, radius))

    def generate_dwarf_galaxies(self, num_dwarf_galaxies):
        import random
        for i in range(num_dwarf_galaxies):
            name = f"DwarfGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.dwarf_galaxies.append(DwarfGalaxy(name, radius))

    def generate_satellite_galaxies(self, num_satellites):
        import random
        for i in range(num_satellites):
            name = f"SatelliteGalaxy-{i+1}"
            radius = random.randint(1000, 5000)
            self.satellite_galaxies.append(SatelliteGalaxy(name, radius))

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.star_systems = []
        self.nebulas = []
        self.black_holes = []
        self.white_holes = []
        self.wormholes = []
        self.quasars = []
        self.pulsars = []
        self.supernovas = []
        self.magnetars = []
        self.rogue_planets = []
        self.star_clusters = []
        self.globular_clusters = []
        self.dark_matter_halos = []
        self.cosmic_strings = []
        self.stellar_nurseries = []
        self.supermassive_black_holes = []
        self.blazars = []
        self.microquasars = []
        self.protoplanetary_disks = []
        self.brown_dwarfs = []
        self.cosmic_voids = []
        self.hypernovas = []
        self.neutron_stars = []
        self.yellow_dwarfs = []
        self.red_dwarfs = []
        self.black_dwarfs = []
        self.white_dwarfs = []
        self.red_giants = []
        self.blue_giants = []
        self.red_supergiants = []
        self.blue_supergiants = []
        self.wolf_rayet_stars = []
        self.supernova_remnants = []
        self.exoplanets = []
        self.protostars = []
        self.flare_stars = []
        self.carbon_stars = []
        self.binary_star_systems = []
        self.pulsar_planets = []
        self.planetary_nebulas = []
        self.intergalactic_stars = []
        self.hypervelocity_stars = []
        self.interstellar_dust_clouds = []
        self.dark_nebulas = []
        self.reflection_nebulas = []
        self.emission_nebulas = []
        self.molecular_clouds = []
        self.bok_globules = []
        self.open_clusters = []
        self.stellar_associations = []
        self.hii_regions = []
        self.spiral_arms = []
        self.galactic_halos = []
        self.galactic_bars = []
        self.galactic_cores = []
        self.galactic_bulges = []
        self.galactic_disks = []
        self.stellar_streams = []
        self.tidal_tails = []
        self.satellite_galaxies = []
        self.dwarf_galaxies = []
        self.lenticular_galaxies = []
        self.irregular_galaxies = []
        self.spiral_galaxies = []
        self.elliptical_galaxies = []
        self.ring_galaxies = []
        self.starburst_galaxies = []
        self.seyfert_galaxies = []
        self.radio_galaxies = []
        self.protogalaxies = []
        self.peculiar_galaxies = []
        self.dark_galaxies = []
        self.interacting_galaxies = []
        self.luminous_infrared_galaxies = []






    def generate_red_giants(self, num_red_giants):
        import random
        for i in range(num_red_giants):
            name = f"RedGiant-{i+1}"
            radius = random.randint(100, 1000)
            self.red_giants.append(RedGiant(name, radius))

    def generate_supernova_remnants(self, num_remnants):
        import random
        for i in range(num_remnants):
            name = f"SupernovaRemnant-{i+1}"
            radius = random.randint(100, 1000)
            self.supernova_remnants.append(SupernovaRemnant(name, radius))

    def generate_red_supergiants(self, num_red_supergiants):
        import random
        for i in range(num_red_supergiants):
            name = f"{self.name}-RedSupergiant-{i+1}"
            radius = random.randint(500000, 2000000)
            self.red_supergiants.append(RedSupergiant(name, radius))

    def generate_blue_supergiants(self, num_blue_supergiants):
        import random
        for i in range(num_blue_supergiants):
            name = f"{self.name}-BlueSupergiant-{i+1}"
            radius = random.randint(500000, 2000000)
            self.blue_supergiants.append(BlueSupergiant(name, radius))

    def generate_wolf_rayet_stars(self, num_wolf_rayet_stars):
        import random
        for i in range(num_wolf_rayet_stars):
            name = f"{self.name}-WolfRayetStar-{i+1}"
            radius = random.randint(1000000, 5000000)
            self.wolf_rayet_stars.append(WolfRayetStar(name, radius))

    def generate_blue_giants(self, num_blue_giants):
        import random
        for i in range(num_blue_giants):
            name = f"BlueGiant-{i+1}"
            radius = random.randint(100, 1000)
            self.blue_giants.append(BlueGiant(name, radius))

    def generate_yellow_dwarfs(self, num_yellow_dwarfs):
        import random
        for i in range(num_yellow_dwarfs):
            name = f"YellowDwarf-{i+1}"
            radius = random.randint(50, 200)
            self.yellow_dwarfs.append(YellowDwarf(name, radius))

    def generate_red_dwarfs(self, num_red_dwarfs):
        import random
        for i in range(num_red_dwarfs):
            name = f"RedDwarf-{i+1}"
            radius = random.randint(10, 50)
            self.red_dwarfs.append(RedDwarf(name, radius))


    def generate_black_dwarfs(self, num_black_dwarfs):
        import random
        for i in range(num_black_dwarfs):
            name = f"BlackDwarf-{i+1}"
            radius = random.randint(10, 50)
            self.black_dwarfs.append(BlackDwarf(name, radius))

    def generate_white_dwarfs(self, num_white_dwarfs):
        import random
        for i in range(num_white_dwarfs):
            name = f"WhiteDwarf-{i+1}"
            radius = random.randint(10, 50)
            self.white_dwarfs.append(WhiteDwarf(name, radius))

    def generate_neutron_stars(self, num_neutron_stars):
        import random
        for i in range(num_neutron_stars):
            name = f"NeutronStar-{i+1}"
            radius = random.randint(10, 50)
            self.neutron_stars.append(NeutronStar(name, radius))

    def generate_hypernovas(self, num_hypernovas):
        import random
        for i in range(num_hypernovas):
            name = f"Hypernova-{i+1}"
            radius = random.randint(100, 1000)
            self.hypernovas.append(Hypernova(name, radius))

    def generate_cosmic_voids(self, num_voids):
        import random
        for i in range(num_voids):
            name = f"CosmicVoid-{i+1}"
            radius = random.randint(100000, 1000000)
            self.cosmic_voids.append(CosmicVoid(name, radius))

    def generate_brown_dwarfs(self, num_brown_dwarfs):
        import random
        for i in range(num_brown_dwarfs):
            name = f"BrownDwarf-{i+1}"
            radius = random.randint(100, 10000)
            self.brown_dwarfs.append(BrownDwarf(name, radius))

    def generate_protoplanetary_disks(self, num_disks):
        import random
        for i in range(num_disks):
            name = f"ProtoplanetaryDisk-{i+1}"
            radius = random.randint(100, 10000)
            self.protoplanetary_disks.append(ProtoplanetaryDisk(name, radius))

    def generate_microquasars(self, num_microquasars):
        import random
        for i in range(num_microquasars):
            name = f"Microquasar-{i+1}"
            radius = random.randint(100, 10000)
            self.microquasars.append(Microquasar(name, radius))

    def generate_blazars(self, num_blazars):
        import random
        for i in range(num_blazars):
            name = f"Blazar-{i+1}"
            radius = random.randint(10000, 100000)
            self.blazars.append(Blazar(name, radius))

    def generate_supermassive_black_holes(self, num_smbhs):
        import random
        for i in range(num_smbhs):
            name = f"SupermassiveBlackHole-{i+1}"
            mass = random.randint(1000000, 1000000000)
            self.supermassive_black_holes.append(SupermassiveBlackHole(name, mass))

    def generate_flare_stars(self, num_flare_stars):
        import random
        for i in range(num_flare_stars):
            name = f"FlareStar-{i+1}"
            radius = random.randint(10, 100)
            self.flare_stars.append(FlareStar(name, radius))

    def generate_pulsar_planets(self, num_pulsar_planets):
        import random
        for i in range(num_pulsar_planets):
            name = f"PulsarPlanet-{i+1}"
            radius = random.randint(10, 500)
            self.pulsar_planets.append(PulsarPlanet(name, radius))

    def generate_binary_star_systems(self, num_binary_star_systems):
        import random
        for i in range(num_binary_star_systems):
            name = f"BinaryStarSystem-{i+1}"
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.binary_star_systems.append(BinaryStarSystem(name, x, y))

    def generate_planetary_nebulas(self, num_planetary_nebulas):
        import random
        for i in range(num_planetary_nebulas):
            name = f"PlanetaryNebula-{i+1}"
            radius = random.uniform(0.1, 10.0)
            self.planetary_nebulas.append(PlanetaryNebula(name, radius))

    def generate_carbon_stars(self, num_carbon_stars):
        import random
        for i in range(num_carbon_stars):
            name = f"CarbonStar-{i+1}"
            radius = random.randint(100, 1000)
            self.carbon_stars.append(CarbonStar(name, radius))


    def generate_protostars(self, num_protostars):
        import random
        for i in range(num_protostars):
            name = f"{self.name}-Protostar-{i+1}"
            radius = random.randint(100, 1000)
            self.protostars.append(Protostar(name, radius))

    def generate_stellar_nurseries(self, num_nurseries):
        import random
        for i in range(num_nurseries):
            name = f"StellarNursery-{i+1}"
            radius = random.randint(500, 5000)
            self.stellar_nurseries.append(StellarNursery(name, radius))

    def generate_cosmic_strings(self, num_strings):
        import random
        for i in range(num_strings):
            name = f"CosmicString-{i+1}"
            length = random.randint(10000, 100000)
            self.cosmic_strings.append(CosmicString(name, length))

    def generate_dark_matter_halos(self, num_halos):
        for i in range(num_halos):
            name = f"DarkMatterHalo-{i+1}"
            mass = random.randint(100000, 1000000)
            self.dark_matter_halos.append(DarkMatterHalo(name, mass))

    def generate_globular_clusters(self, num_globular_clusters):
        for i in range(num_globular_clusters):
            name = f"GlobularCluster-{i+1}"
            radius = random.randint(100, 1000)
            self.globular_clusters.append(GlobularCluster(name, radius))

    def generate_wormholes(self, num_wormholes):
        for i in range(num_wormholes):
            name = f"Wormhole-{i+1}"
            radius = random.randint(100, 1000)
            self.wormholes.append(Wormhole(name, radius))

    def generate_nebulas(self, num_nebulas):
        for i in range(num_nebulas):
            name = f"Nebula-{i+1}"
            radius = random.randint(1000, 10000)
            self.nebulas.append(Nebula(name, radius))


    def generate_exoplanets(self, num_exoplanets):
        import random
        for i in range(num_exoplanets):
            name = f"Exoplanet-{i+1}"
            radius = random.uniform(50, 500)
            self.exoplanets.append(Exoplanet(name, radius))

    def generate_interstellar_dust_clouds(self, num_interstellar_dust_clouds):
        import random
        for i in range(num_interstellar_dust_clouds):
            name = f"InterstellarDustCloud-{i+1}"
            radius = random.randint(100, 1000)
            self.interstellar_dust_clouds.append(InterstellarDustCloud(name, radius))

    def generate_dark_nebulas(self, num_dark_nebulas):
        import random
        for i in range(num_dark_nebulas):
            name = f"DarkNebula-{i+1}"
            radius = random.randint(100, 1000)
            self.dark_nebulas.append(DarkNebula(name, radius))

    def generate_reflection_nebulas(self, num_reflection_nebulas):
        import random
        for i in range(num_reflection_nebulas):
            name = f"ReflectionNebula-{i+1}"
            radius = random.randint(100, 1000)
            self.reflection_nebulas.append(ReflectionNebula(name, radius))

    def generate_stellar_associations(self, num_associations):
        import random
        for i in range(num_associations):
            name = f"StellarAssociation-{i+1}"
            radius = random.randint(100, 1000)
            self.stellar_associations.append(StellarAssociation(name, radius))

    def generate_galactic_halos(self, num_halos):
        import random
        for i in range(num_halos):
            name = f"GalacticHalo-{i+1}"
            radius = random.randint(10000, 100000)
            self.galactic_halos.append(GalacticHalo(name, radius))

    def generate_stellar_streams(self, num_streams):
        import random
        for i in range(num_streams):
            name = f"StellarStream-{i+1}"
            length = random.randint(1000, 10000)
            self.stellar_streams.append(StellarStream(name, length))

    def generate_tidal_tails(self, num_tails):
        import random
        for i in range(num_tails):
            name = f"TidalTail-{i+1}"
            length = random.randint(1000, 10000)
            self.tidal_tails.append(TidalTail(name, length))

    def generate_galactic_disks(self, num_disks):
        import random
        for i in range(num_disks):
            name = f"GalacticDisk-{i+1}"
            radius = random.randint(1000, 10000)
            self.galactic_disks.append(GalacticDisk(name, radius))

    def generate_galactic_bars(self, num_bars):
        import random
        for i in range(num_bars):
            name = f"GalacticBar-{i+1}"
            length = random.randint(500, 5000)
            self.galactic_bars.append(GalacticBar(name, length))

    def generate_galactic_cores(self, num_cores):
        import random
        for i in range(num_cores):
            name = f"GalacticCore-{i+1}"
            radius = random.randint(10, 100)
            self.galactic_cores.append(GalacticCore(name, radius))

    def generate_galactic_bulges(self, num_bulges):
        import random
        for i in range(num_bulges):
            name = f"GalacticBulge-{i+1}"
            radius = random.randint(100, 1000)
            self.galactic_bulges.append(GalacticBulge(name, radius))

    def generate_spiral_arms(self, num_arms):
        import random
        for i in range(num_arms):
            name = f"SpiralArm-{i+1}"
            length = random.randint(1000, 10000)
            self.spiral_arms.append(SpiralArm(name, length))

    def generate_hii_regions(self, num_regions):
        import random
        for i in range(num_regions):
            name = f"HIIRegion-{i+1}"
            radius = random.randint(100, 1000)
            self.hii_regions.append(HIIRegion(name, radius))

    def generate_open_clusters(self, num_open_clusters):
        import random
        for i in range(num_open_clusters):
            name = f"OpenCluster-{i+1}"
            radius = random.randint(100, 1000)
            self.open_clusters.append(OpenCluster(name, radius))

    def generate_bok_globules(self, num_bok_globules):
        import random
        for i in range(num_bok_globules):
            name = f"BokGlobule-{i+1}"
            radius = random.randint(100, 1000)
            self.bok_globules.append(BokGlobule(name, radius))

    def generate_molecular_clouds(self, num_molecular_clouds):
        import random
        for i in range(num_molecular_clouds):
            name = f"MolecularCloud-{i+1}"
            radius = random.randint(100, 1000)
            self.molecular_clouds.append(MolecularCloud(name, radius))

    def generate_emission_nebulas(self, num_emission_nebulas):
        import random
        for i in range(num_emission_nebulas):
            name = f"EmissionNebula-{i+1}"
            radius = random.randint(100, 1000)
            self.emission_nebulas.append(EmissionNebula(name, radius))

    def generate_peculiar_galaxies(self, num_peculiar_galaxies):
        import random
        for i in range(num_peculiar_galaxies):
            name = f"PeculiarGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.peculiar_galaxies.append(PeculiarGalaxy(name, radius))

    def generate_dark_galaxies(self, num_dark_galaxies):
        import random
        for i in range(num_dark_galaxies):
            name = f"DarkGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.dark_galaxies.append(DarkGalaxy(name, radius))

    def generate_interacting_galaxies(self, num_interacting_galaxies):
        import random
        for i in range(num_interacting_galaxies):
            name = f"InteractingGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.interacting_galaxies.append(InteractingGalaxy(name, radius))

    def generate_luminous_infrared_galaxies(self, num_luminous_infrared_galaxies):
        import random
        for i in range(num_luminous_infrared_galaxies):
            name = f"LuminousInfraredGalaxy-{i+1}"
            radius = random.randint(100, 1000)
            self.luminous_infrared_galaxies.append(LuminousInfraredGalaxy(name, radius))

    def generate_star_systems(self, num_systems):
        for i in range(num_systems):
            name = f"System-{i+1}"
            sx = random.randint(0, self.width)
            sy = random.randint(0, self.height)
            system = StarSystem(name, sx, sy)
            system.generate_planets(random.randint(1, 10))
            self.star_systems.append(system)
    def generate_white_holes(self, num_white_holes):
        for i in range(num_white_holes):
            name = f"WhiteHole-{i+1}"
            radius = random.randint(5000, 50000)
            self.white_holes.append(WhiteHole(name, radius))

    def generate_black_holes(self, num_black_holes):
        for i in range(num_black_holes):
            name = f"BlackHole-{i+1}"
            radius = random.randint(5000, 50000)
            self.black_holes.append(BlackHole(name, radius))

    def generate_quasars(self, num_quasars):
        for i in range(num_quasars):
            name = f"Quasar-{i+1}"
            radius = random.randint(10000, 100000)
            self.quasars.append(Quasar(name, radius))

    def generate_pulsars(self, num_pulsars):
        for i in range(num_pulsars):
            name = f"Pulsar-{i+1}"
            radius = random.randint(100, 1000)
            self.pulsars.append(Pulsar(name, radius))

    def generate_supernovas(self, num_supernovas):
        for i in range(num_supernovas):
            name = f"Supernova-{i+1}"
            radius = random.randint(100, 1000)
            self.supernovas.append(Supernova(name, radius))


    def generate_magnetars(self, num_magnetars):
        for i in range(num_magnetars):
            name = f"Magnetar-{i+1}"
            radius = random.randint(100, 1000)
            self.magnetars.append(Magnetar(name, radius))

    def generate_rogue_planets(self, num_rogue_planets):
        for i in range(num_rogue_planets):
            name = f"RoguePlanet-{i+1}"
            radius = random.randint(1000, 10000)
            self.rogue_planets.append(RoguePlanet(name, radius))



    def generate_star_clusters(self, num_star_clusters):
        for i in range(num_star_clusters):
            name = f"StarCluster-{i+1}"
            radius = random.randint(100, 1000)
            self.star_clusters.append(StarCluster(name, radius))


    def generate_intergalactic_stars(self, num_intergalactic_stars):
        import random
        for i in range(num_intergalactic_stars):
            name = f"IntergalacticStar-{i+1}"
            radius = random.randint(100, 1000)
            self.intergalactic_stars.append(IntergalacticStar(name, radius))

    def generate_hypervelocity_stars(self, num_hypervelocity_stars):
        import random
        for i in range(num_hypervelocity_stars):
            name = f"HypervelocityStar-{i+1}"
            radius = random.randint(100, 1000)
            self.hypervelocity_stars.append(HypervelocityStar(name, radius))

class DwarfGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class HypervelocityStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class StarCluster:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class GlobularCluster:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius



class CosmicString:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class DarkMatterHalo:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class StellarNursery:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class SupermassiveBlackHole:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

class Blazar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Microquasar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class BrownDwarf:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class ProtoplanetaryDisk:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class CosmicVoid:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class YellowDwarf:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class RedDwarf:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class BlackDwarf:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class WhiteDwarf:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class NeutronStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class RedGiant:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class RedSupergiant:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class BlueGiant:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class SupernovaRemnant:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class BlueSupergiant:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class WolfRayetStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Protostar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
class PulsarPlanet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class FlareStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class CarbonStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class BinaryStarSystem:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.primary_star = None
        self.secondary_star = None

class PlanetaryNebula:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class IntergalacticStar:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class InterstellarDustCloud:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class DarkNebula:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class ReflectionNebula:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class IrregularGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class LenticularGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class EllipticalGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class SpiralGalaxy:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
