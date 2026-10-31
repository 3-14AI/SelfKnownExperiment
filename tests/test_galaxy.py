import unittest
from src.universe.galaxy import Galaxy, StarSystem, Planet, Moon, AsteroidBelt, Star, Comet, Nebula, BlackHole

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


    def test_star_generation(self):
        system = StarSystem("Solar System", 0, 0)
        system.generate_stars(1)
        self.assertEqual(len(system.stars), 1)
        self.assertIsInstance(system.stars[0], Star)
        self.assertEqual(system.stars[0].name, "Solar System-Star-1")


    def test_comet_generation(self):
        system = StarSystem("Solar System", 0, 0)
        system.generate_comets(1)
        self.assertEqual(len(system.comets), 1)
        self.assertIsInstance(system.comets[0], Comet)
        self.assertEqual(system.comets[0].name, "Solar System-Comet-1")

    def test_nebula_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_nebulas(1)
        self.assertEqual(len(galaxy.nebulas), 1)
        self.assertIsInstance(galaxy.nebulas[0], Nebula)
        self.assertEqual(galaxy.nebulas[0].name, "Nebula-1")


    def test_black_hole_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_black_holes(1)
        self.assertEqual(len(galaxy.black_holes), 1)
        self.assertIsInstance(galaxy.black_holes[0], BlackHole)
        self.assertEqual(galaxy.black_holes[0].name, "BlackHole-1")

if __name__ == '__main__':

    unittest.main()
