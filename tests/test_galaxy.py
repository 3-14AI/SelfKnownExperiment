import unittest
from src.universe.galaxy import Galaxy, StarSystem, Planet

class TestGalaxy(unittest.TestCase):
    def test_galaxy_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_star_systems(5)

        self.assertEqual(len(galaxy.star_systems), 5)

        for system in galaxy.star_systems:
            self.assertGreaterEqual(len(system.planets), 1)
            self.assertLessEqual(len(system.planets), 10)

if __name__ == '__main__':
    unittest.main()