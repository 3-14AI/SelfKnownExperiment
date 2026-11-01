
class AsteroidBelt:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
import random

class Comet:
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
        self.asteroid_belts = []
        self.comets = []
        self.stars = []

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

class Galaxy:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.star_systems = []
        self.nebulas = []
        self.black_holes = []
        self.wormholes = []
        self.quasars = []
        self.pulsars = []

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

    def generate_star_systems(self, num_systems):
        for i in range(num_systems):
            name = f"System-{i+1}"
            sx = random.randint(0, self.width)
            sy = random.randint(0, self.height)
            system = StarSystem(name, sx, sy)
            system.generate_planets(random.randint(1, 10))
            self.star_systems.append(system)
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
