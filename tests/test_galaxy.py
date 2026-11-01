import unittest
from src.universe.galaxy import PlanetaryRing, Galaxy, StarSystem, Planet, Moon, AsteroidBelt, Star, Comet, Nebula, BlackHole, Wormhole, Quasar, Pulsar, Supernova, Magnetar, RoguePlanet, StarCluster, GlobularCluster

class TestGalaxy(unittest.TestCase):
    def test_galaxy_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_star_systems(5)

        self.assertEqual(len(galaxy.star_systems), 5)

        for system in galaxy.star_systems:
            self.assertGreaterEqual(len(system.planets), 1)
            self.assertLessEqual(len(system.planets), 10)




    def test_planet_types(self):
        rocky_planet = Planet("Rocky", 0, 0, 1000, planet_type='rocky')
        self.assertEqual(rocky_planet.planet_type, 'rocky')
        self.assertEqual(rocky_planet.mass, 10000)
        self.assertEqual(rocky_planet.atmosphere, 'thin')

        gaseous_planet = Planet("Gaseous", 0, 0, 2000, planet_type='gaseous')
        self.assertEqual(gaseous_planet.planet_type, 'gaseous')
        self.assertEqual(gaseous_planet.mass, 10000)
        self.assertEqual(gaseous_planet.atmosphere, 'thick')

        oceanic_planet = Planet("Oceanic", 0, 0, 1000, planet_type='oceanic')
        self.assertEqual(oceanic_planet.planet_type, 'oceanic')
        self.assertEqual(oceanic_planet.mass, 8000)
        self.assertEqual(oceanic_planet.atmosphere, 'moderate')

        system = StarSystem("System1", 0, 0)
        import random
        random.seed(0)
        system.generate_planets(10)

        valid_types = ['rocky', 'gaseous', 'oceanic']
        for planet in system.planets:
            self.assertIn(planet.planet_type, valid_types)
            if planet.planet_type == 'rocky':
                self.assertEqual(planet.mass, planet.radius * 10)
                self.assertEqual(planet.atmosphere, 'thin')
            elif planet.planet_type == 'gaseous':
                self.assertEqual(planet.mass, planet.radius * 5)
                self.assertEqual(planet.atmosphere, 'thick')
            elif planet.planet_type == 'oceanic':
                self.assertEqual(planet.mass, planet.radius * 8)
                self.assertEqual(planet.atmosphere, 'moderate')


    def test_ring_generation(self):
        planet = Planet("Saturn", 0, 0, 6000)
        planet.generate_rings(2)
        self.assertEqual(len(planet.rings), 2)
        self.assertIsInstance(planet.rings[0], PlanetaryRing)
        self.assertEqual(planet.rings[0].name, "Saturn-Ring-1")

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

    def test_star_types(self):
        dwarf_star = Star("Dwarf", 1000, star_type='dwarf')
        self.assertEqual(dwarf_star.star_type, 'dwarf')
        self.assertEqual(dwarf_star.temperature, 5000)
        self.assertEqual(dwarf_star.luminosity, 2000)

        giant_star = Star("Giant", 2000, star_type='giant')
        self.assertEqual(giant_star.star_type, 'giant')
        self.assertEqual(giant_star.temperature, 20000)
        self.assertEqual(giant_star.luminosity, 40000)

        supergiant_star = Star("Supergiant", 5000, star_type='supergiant')
        self.assertEqual(supergiant_star.star_type, 'supergiant')
        self.assertEqual(supergiant_star.temperature, 100000)
        self.assertEqual(supergiant_star.luminosity, 500000)

        neutron_star = Star("Neutron", 100, star_type='neutron')
        self.assertEqual(neutron_star.star_type, 'neutron')
        self.assertEqual(neutron_star.temperature, 10000)
        self.assertEqual(neutron_star.luminosity, 500)

        system = StarSystem("System1", 0, 0)
        import random
        random.seed(0)
        system.generate_stars(10)

        valid_types = ['dwarf', 'giant', 'supergiant', 'neutron']
        for star in system.stars:
            self.assertIn(star.star_type, valid_types)
            if star.star_type == 'dwarf':
                self.assertEqual(star.temperature, star.radius * 5)
                self.assertEqual(star.luminosity, star.radius * 2)
            elif star.star_type == 'giant':
                self.assertEqual(star.temperature, star.radius * 10)
                self.assertEqual(star.luminosity, star.radius * 20)
            elif star.star_type == 'supergiant':
                self.assertEqual(star.temperature, star.radius * 20)
                self.assertEqual(star.luminosity, star.radius * 100)
            elif star.star_type == 'neutron':
                self.assertEqual(star.temperature, star.radius * 100)
                self.assertEqual(star.luminosity, star.radius * 5)


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


    def test_wormhole_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_wormholes(1)
        self.assertEqual(len(galaxy.wormholes), 1)
        self.assertIsInstance(galaxy.wormholes[0], Wormhole)
        self.assertEqual(galaxy.wormholes[0].name, "Wormhole-1")


    def test_quasar_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_quasars(1)
        self.assertEqual(len(galaxy.quasars), 1)
        self.assertIsInstance(galaxy.quasars[0], Quasar)
        self.assertEqual(galaxy.quasars[0].name, "Quasar-1")


    def test_pulsar_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_pulsars(1)
        self.assertEqual(len(galaxy.pulsars), 1)
        self.assertIsInstance(galaxy.pulsars[0], Pulsar)
        self.assertEqual(galaxy.pulsars[0].name, "Pulsar-1")


    def test_supernova_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_supernovas(1)
        self.assertEqual(len(galaxy.supernovas), 1)
        self.assertIsInstance(galaxy.supernovas[0], Supernova)
        self.assertEqual(galaxy.supernovas[0].name, "Supernova-1")



    def test_magnetar_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_magnetars(1)
        self.assertEqual(len(galaxy.magnetars), 1)
        self.assertIsInstance(galaxy.magnetars[0], Magnetar)
        self.assertEqual(galaxy.magnetars[0].name, "Magnetar-1")

    def test_rogue_planet_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_rogue_planets(1)
        self.assertEqual(len(galaxy.rogue_planets), 1)
        self.assertIsInstance(galaxy.rogue_planets[0], RoguePlanet)
        self.assertEqual(galaxy.rogue_planets[0].name, "RoguePlanet-1")

    def test_star_cluster_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_star_clusters(1)
        self.assertEqual(len(galaxy.star_clusters), 1)
        self.assertIsInstance(galaxy.star_clusters[0], StarCluster)
        self.assertEqual(galaxy.star_clusters[0].name, "StarCluster-1")


    def test_globular_cluster_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_globular_clusters(1)
        self.assertEqual(len(galaxy.globular_clusters), 1)
        self.assertIsInstance(galaxy.globular_clusters[0], GlobularCluster)
        self.assertEqual(galaxy.globular_clusters[0].name, "GlobularCluster-1")

if __name__ == '__main__':

    unittest.main()
