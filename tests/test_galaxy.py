import unittest
from src.universe.galaxy import Galaxy, StarSystem, Planet, Moon, AsteroidBelt

class TestGalaxy(unittest.TestCase):
    def test_galaxy_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_star_systems(5)

        self.assertEqual(len(galaxy.star_systems), 5)

        for system in galaxy.star_systems:
            self.assertGreaterEqual(len(system.planets), 1)
            self.assertLessEqual(len(system.planets), 10)


    def test_moon_generation(self):
        planet = Planet("Earth", 0, 0, 5000)
        planet.generate_moons(1)
        self.assertEqual(len(planet.moons), 1)
        self.assertIsInstance(planet.moons[0], Moon)
        self.assertEqual(planet.moons[0].name, "Earth-Moon-1")



    def test_asteroid_belt_generation(self):
        system = StarSystem("Solar System", 0, 0)
        system.generate_asteroid_belts(1)
        self.assertEqual(len(system.asteroid_belts), 1)
        self.assertEqual(system.asteroid_belts[0].name, "Solar System-Belt-1")

if __name__ == '__main__':

    unittest.main()