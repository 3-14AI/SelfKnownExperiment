
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
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

class Moon:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class Planet:
    def __init__(self, name, x, y, radius):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.moons = []

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


class Nebula:
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