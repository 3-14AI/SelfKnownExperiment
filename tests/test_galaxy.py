import unittest
from src.universe.galaxy import StellarNursery, WhiteDwarf, BlackDwarf, DarkMatterHalo, CosmicString, PlanetaryRing, Galaxy, StarSystem, Planet, Moon, AsteroidBelt, Star, Comet, Nebula, BlackHole, WhiteHole, Wormhole, Quasar, Pulsar, Supernova, Magnetar, RoguePlanet, StarCluster, GlobularCluster

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


    def test_white_hole_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_white_holes(1)
        self.assertEqual(len(galaxy.white_holes), 1)
        self.assertIsInstance(galaxy.white_holes[0], WhiteHole)
        self.assertEqual(galaxy.white_holes[0].name, "WhiteHole-1")

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

    def test_dark_matter_halo_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_dark_matter_halos(1)
        self.assertEqual(len(galaxy.dark_matter_halos), 1)
        self.assertIsInstance(galaxy.dark_matter_halos[0], DarkMatterHalo)
        self.assertEqual(galaxy.dark_matter_halos[0].name, "DarkMatterHalo-1")


    def test_cosmic_string_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_cosmic_strings(1)
        self.assertEqual(len(galaxy.cosmic_strings), 1)
        self.assertIsInstance(galaxy.cosmic_strings[0], CosmicString)
        self.assertEqual(galaxy.cosmic_strings[0].name, "CosmicString-1")


    def test_stellar_nursery_generation(self):
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_stellar_nurseries(1)
        self.assertEqual(len(galaxy.stellar_nurseries), 1)
        self.assertIsInstance(galaxy.stellar_nurseries[0], StellarNursery)
        self.assertEqual(galaxy.stellar_nurseries[0].name, "StellarNursery-1")


    def test_supermassive_black_hole_generation(self):
        from src.universe.galaxy import SupermassiveBlackHole
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_supermassive_black_holes(1)
        self.assertEqual(len(galaxy.supermassive_black_holes), 1)
        self.assertIsInstance(galaxy.supermassive_black_holes[0], SupermassiveBlackHole)
        self.assertEqual(galaxy.supermassive_black_holes[0].name, "SupermassiveBlackHole-1")


    def test_microquasar_generation(self):
        from src.universe.galaxy import Microquasar
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_microquasars(1)
        self.assertEqual(len(galaxy.microquasars), 1)
        self.assertIsInstance(galaxy.microquasars[0], Microquasar)
        self.assertEqual(galaxy.microquasars[0].name, "Microquasar-1")

    def test_blazar_generation(self):
        from src.universe.galaxy import Blazar
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_blazars(1)
        self.assertEqual(len(galaxy.blazars), 1)
        self.assertIsInstance(galaxy.blazars[0], Blazar)
        self.assertEqual(galaxy.blazars[0].name, "Blazar-1")


    def test_brown_dwarf_generation(self):
        from src.universe.galaxy import BrownDwarf
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_brown_dwarfs(1)
        self.assertEqual(len(galaxy.brown_dwarfs), 1)
        self.assertIsInstance(galaxy.brown_dwarfs[0], BrownDwarf)
        self.assertEqual(galaxy.brown_dwarfs[0].name, "BrownDwarf-1")

    def test_protoplanetary_disk_generation(self):
        from src.universe.galaxy import ProtoplanetaryDisk
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_protoplanetary_disks(1)
        self.assertEqual(len(galaxy.protoplanetary_disks), 1)
        self.assertIsInstance(galaxy.protoplanetary_disks[0], ProtoplanetaryDisk)
        self.assertEqual(galaxy.protoplanetary_disks[0].name, "ProtoplanetaryDisk-1")

    def test_cosmic_void_generation(self):
        from src.universe.galaxy import CosmicVoid
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_cosmic_voids(1)
        self.assertEqual(len(galaxy.cosmic_voids), 1)
        self.assertIsInstance(galaxy.cosmic_voids[0], CosmicVoid)
        self.assertEqual(galaxy.cosmic_voids[0].name, "CosmicVoid-1")


    def test_hypernova_generation(self):
        from src.universe.galaxy import Hypernova
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_hypernovas(1)
        self.assertEqual(len(galaxy.hypernovas), 1)
        self.assertIsInstance(galaxy.hypernovas[0], Hypernova)
        self.assertEqual(galaxy.hypernovas[0].name, "Hypernova-1")


    def test_neutron_star_generation(self):
        from src.universe.galaxy import NeutronStar
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_neutron_stars(1)
        self.assertEqual(len(galaxy.neutron_stars), 1)
        self.assertIsInstance(galaxy.neutron_stars[0], NeutronStar)
        self.assertEqual(galaxy.neutron_stars[0].name, "NeutronStar-1")



    def test_black_dwarf_generation(self):
        from src.universe.galaxy import BlackDwarf
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_black_dwarfs(1)
        self.assertEqual(len(galaxy.black_dwarfs), 1)
        self.assertIsInstance(galaxy.black_dwarfs[0], BlackDwarf)
        self.assertEqual(galaxy.black_dwarfs[0].name, "BlackDwarf-1")

    def test_white_dwarf_generation(self):
        from src.universe.galaxy import WhiteDwarf
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_white_dwarfs(1)
        self.assertEqual(len(galaxy.white_dwarfs), 1)
        self.assertIsInstance(galaxy.white_dwarfs[0], WhiteDwarf)
        self.assertEqual(galaxy.white_dwarfs[0].name, "WhiteDwarf-1")

    def test_yellow_dwarf_generation(self):
        from src.universe.galaxy import YellowDwarf
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_yellow_dwarfs(1)
        self.assertEqual(len(galaxy.yellow_dwarfs), 1)
        self.assertIsInstance(galaxy.yellow_dwarfs[0], YellowDwarf)
        self.assertEqual(galaxy.yellow_dwarfs[0].name, "YellowDwarf-1")

    def test_red_dwarf_generation(self):
        from src.universe.galaxy import RedDwarf
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_red_dwarfs(1)
        self.assertEqual(len(galaxy.red_dwarfs), 1)
        self.assertIsInstance(galaxy.red_dwarfs[0], RedDwarf)
        self.assertEqual(galaxy.red_dwarfs[0].name, "RedDwarf-1")


    def test_blue_giant_generation(self):
        from src.universe.galaxy import BlueGiant
        galaxy = Galaxy("Test Galaxy", 100, 100)
        galaxy.generate_blue_giants(2)
        self.assertEqual(len(galaxy.blue_giants), 2)
        self.assertEqual(galaxy.blue_giants[0].name, "BlueGiant-1")
        self.assertEqual(galaxy.blue_giants[1].name, "BlueGiant-2")
        self.assertTrue(100 <= galaxy.blue_giants[0].radius <= 1000)



    def test_red_giant_generation(self):
        from src.universe.galaxy import RedGiant
        galaxy = Galaxy("Test Galaxy", 100, 100)
        galaxy.generate_red_giants(2)
        self.assertEqual(len(galaxy.red_giants), 2)
        self.assertEqual(galaxy.red_giants[0].name, "RedGiant-1")
        self.assertEqual(galaxy.red_giants[1].name, "RedGiant-2")
        self.assertTrue(100 <= galaxy.red_giants[0].radius <= 1000)


    def test_exoplanet_generation(self):
        from src.universe.galaxy import Galaxy, Exoplanet
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_exoplanets(3)
        self.assertEqual(len(galaxy.exoplanets), 3)
        for exoplanet in galaxy.exoplanets:
            self.assertIsInstance(exoplanet, Exoplanet)
            self.assertGreaterEqual(exoplanet.radius, 50)
            self.assertLessEqual(exoplanet.radius, 500)

if __name__ == '__main__':
    unittest.main()

    def test_supernova_remnant_generation(self):
        from src.universe.galaxy import Galaxy, SupernovaRemnant
        galaxy = Galaxy("Milky Way", 1000, 1000)
        galaxy.generate_supernova_remnants(3)
        self.assertEqual(len(galaxy.supernova_remnants), 3)
        for remnant in galaxy.supernova_remnants:
            self.assertIsInstance(remnant, SupernovaRemnant)
            self.assertGreaterEqual(remnant.radius, 100)
            self.assertLessEqual(remnant.radius, 1000)
