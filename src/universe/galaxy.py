import random


class AsteroidBelt:
    def __init__(self, name, inner_radius, outer_radius, num_asteroids):
        self.name = name
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.num_asteroids = num_asteroids

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
            inner_radius = random.randint(10000, 20000)
            outer_radius = inner_radius + random.randint(1000, 5000)
            num_asteroids = random.randint(100, 1000)
            self.asteroid_belts.append(AsteroidBelt(name, inner_radius, outer_radius, num_asteroids))

class Galaxy:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.star_systems = []

    def generate_star_systems(self, num_systems):
        for i in range(num_systems):
            name = f"System-{i+1}"
            sx = random.randint(0, self.width)
            sy = random.randint(0, self.height)
            system = StarSystem(name, sx, sy)
            system.generate_planets(random.randint(1, 10))
            self.star_systems.append(system)