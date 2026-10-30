import random

class Planet:
    def __init__(self, name, x, y, radius):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius

class StarSystem:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.planets = []

    def generate_planets(self, num_planets):
        for i in range(num_planets):
            name = f"{self.name}-{i+1}"
            px = self.x + random.randint(-100, 100)
            py = self.y + random.randint(-100, 100)
            radius = random.randint(1000, 10000)
            self.planets.append(Planet(name, px, py, radius))

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