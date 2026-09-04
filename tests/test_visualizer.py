import unittest
from src.universe.engine import Universe, Entity, Food, Terrain
from src.universe.visualizer import CLIVisualizer

class TestCLIVisualizer(unittest.TestCase):

    def test_render_is_snow_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Snow Dweller", x=5, y=5, is_snow_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('K', output)

    def test_render_is_wall_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Wall Dweller", x=5, y=5, is_wall_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('W', output)

    def test_visualizer_disease_vector(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=5, height=5)

        entity = Entity("Vector", x=2, y=2, disease_vector=True, energy=100, max_age=100)
        universe.add_entity(entity)

        vis = CLIVisualizer(universe)
        output = vis.render()

        self.assertIn('M', output)

    def test_render_terrain(self):
        universe = Universe(width=3, height=3)
        universe.add_terrain(Terrain(x=0, y=0, terrain_type='wall'))
        universe.add_terrain(Terrain(x=2, y=2, terrain_type='water'))
        visualizer = CLIVisualizer(universe)
        expected_output = "#..\n...\n..~"
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_empty(self):
        universe = Universe(width=3, height=3)
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n...\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_food(self):
        universe = Universe(width=3, height=3)
        universe.add_food(Food(x=1, y=1))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.f.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=2, y=0))
        visualizer = CLIVisualizer(universe)
        expected_output = "..E\n...\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity_and_food(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=0, y=0))
        universe.add_food(Food(x=2, y=2))
        visualizer = CLIVisualizer(universe)
        expected_output = "E..\n...\n..f"
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_entity_on_food(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("Test", x=1, y=1))
        universe.add_food(Food(x=1, y=1))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.E.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_carnivore(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestCarnivore", x=1, y=1, diet='carnivore'))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.C.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_infected(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestInfected", x=1, y=1, is_infected=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.S.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_aposematic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestApos", x=1, y=1, is_aposematic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.A.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_photosynthesize(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestPhoto", x=1, y=1, can_photosynthesize=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.P.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_hibernating(self):
        universe = Universe(width=3, height=3)
        entity = Entity("TestHiber", x=1, y=1, diet='carnivore', can_hibernate=True)
        entity.is_hibernating = True
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.2.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_level(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestLevel", x=1, y=1, diet='omnivore', level=3))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.O.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_has_claws(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestClaws", x=1, y=1, diet='carnivore', has_claws=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.K.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_parasitic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestParasite", x=1, y=1, diet='carnivore', is_parasitic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.D.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_has_scales(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestScales", x=1, y=1, diet='herbivore', has_scales=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.R.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_has_fur(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestFur", x=1, y=1, diet='herbivore', has_fur=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.U.\n..."
        self.assertEqual(visualizer.render(), expected_output)





    def test_render_can_climb(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestClimb", x=1, y=1, diet='herbivore', can_climb=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.L.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_regenerative(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestRegen", x=1, y=1, diet='herbivore', is_regenerative=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.G.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_immune(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestImmune", x=1, y=1, diet='herbivore', is_immune=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.I.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_amphibious(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestAmphi", x=1, y=1, diet='herbivore', is_amphibious=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.B.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_is_aquatic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestAquatic", x=1, y=1, is_aquatic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.a.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_electric(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestElectric", x=1, y=1, is_electric=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.e.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_cold_blooded(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestColdBlooded", x=1, y=1, is_cold_blooded=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.b.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_fruiting(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestFruiting", x=1, y=1, is_fruiting=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.F.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_has_echolocation(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestEcho", x=1, y=1, has_echolocation=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.E.\n..."
        self.assertEqual(visualizer.render(), expected_output)


    def test_render_has_horns(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestHorns", x=1, y=1, has_horns=True))
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('Y', output)

    def test_render_has_shell(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestShell", x=1, y=1, has_shell=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.H.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_venomous(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestVenomous", x=1, y=1, is_venomous=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.v.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_can_spin_webs(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSpinWebs", x=1, y=1, can_spin_webs=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.w.\n..."
        self.assertEqual(visualizer.render(), expected_output)



    def test_render_is_ambush_predator(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestAmbushPredator", x=1, y=1, is_ambush_predator=True))
        output = CLIVisualizer(universe).render()
        # Verify the character we assign in the visualizer for ambush predator (e.g., 'a') is present
        self.assertIn('m', output)

    def test_render_is_social(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSocial", x=1, y=1, is_social=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.p.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_forestal(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestForestal", x=1, y=1, is_forestal=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.t.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_desertic(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestDesertic", x=1, y=1, is_desertic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.d.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_volcanic(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestVolcanic", x=1, y=1, is_volcanic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.j.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_has_spikes(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSpikes", x=1, y=1, has_spikes=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.k.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_has_bioluminescence(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestBio", x=1, y=1, has_bioluminescence=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.l.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_pack_hunter(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestPack", x=1, y=1, pack_hunter=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.W.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_visualizer_is_nocturnal(self):
        universe = Universe(width=3, height=3)
        entity = Entity("Nocturnal", x=1, y=1, is_nocturnal=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('n', output)

    def test_visualizer_is_nocturnal_predator(self):
        universe = Universe(width=3, height=3)
        entity = Entity("NocturnalPred", x=1, y=1, is_nocturnal_predator=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('N', output)





    def test_visualizer_is_scentless(self):
        from src.universe.engine import Universe, Entity, Terrain
        universe = Universe(width=10, height=10)
        entity = Entity("Scentless", x=1, y=1, is_scentless=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('Z', output)




    def test_render_is_vampiric(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestVampire", x=1, y=1, is_vampiric=True))
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('y', output)


    def test_render_is_detritivore(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=5, height=5)
        universe.add_entity(Entity("TestDetritivore", x=1, y=1, is_detritivore=True))
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('g', output)

    def test_render_can_sweat(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSweat", x=1, y=1, can_sweat=True))
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('q', output)


    def test_render_has_blubber(self):
        universe = Universe(3, 3)
        universe.add_entity(Entity("TestBlubber", x=1, y=1, has_blubber=True))
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('@', output)

    def test_render_is_filter_feeder(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestFilterFeeder", x=1, y=1, is_filter_feeder=True))
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('u', output)



    def test_render_is_solitary(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSolitary", x=1, y=1, is_solitary=True))
        output = CLIVisualizer(universe).render()
        self.assertIn('h', output)

    def test_render_is_cannibalistic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestCannibal", x=1, y=1, is_cannibalistic=True))
        output = CLIVisualizer(universe).render()
        self.assertIn('J', output)

    def test_render_is_mud_bather(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestMudBather", x=1, y=1, is_mud_bather=True))
        output = CLIVisualizer(universe).render()
        self.assertIn('n', output)

    def test_render_can_sprint(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSprinting", x=1, y=1, can_sprint=True))
        output = CLIVisualizer(universe).render()
        self.assertIn('r', output)

    def test_render_is_carnivorous_plant(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestCarnPlant", x=1, y=1, is_carnivorous_plant=True))
        output = CLIVisualizer(universe).render()
        self.assertIn('c', output)

    def test_render_is_gluttonous(self):
        universe = Universe(10, 10)
        e = Entity("Glutton", x=2, y=2, is_gluttonous=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('x', output)


    def test_render_is_cooperative(self):
        universe = Universe(10, 10)
        e = Entity("Coop", x=2, y=2, is_cooperative=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('i', output)


    def test_render_is_frugivore(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(10, 10)
        e = Entity("Frug", x=2, y=2, is_frugivore=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('T', output)


    def test_visualizer_has_strong_stomach(self):
        universe = Universe(width=5, height=5)
        e = Entity("Strong", x=1, y=1, has_strong_stomach=True, diet="herbivore")
        universe.add_entity(e)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('s', output)


    def test_render_is_sleeping(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSleeping", x=1, y=1, is_sleeping=True))
        vis = CLIVisualizer(universe)
        self.assertIn('0', vis.render())

    def test_render_is_flying(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestFlying", x=1, y=1, is_flying=True))
        vis = CLIVisualizer(universe)
        self.assertIn('1', vis.render())

    def test_render_can_hibernate(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestHibernate", x=1, y=1, can_hibernate=True))
        vis = CLIVisualizer(universe)
        self.assertIn('2', vis.render())

    def test_render_lays_eggs(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestEggs", x=1, y=1, lays_eggs=True))
        vis = CLIVisualizer(universe)
        self.assertIn('3', vis.render())

    def test_render_can_hoard(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestHoard", x=1, y=1, can_hoard=True))
        vis = CLIVisualizer(universe)
        self.assertIn('4', vis.render())

    def test_render_can_burrow(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestBurrow", x=1, y=1, can_burrow=True))
        vis = CLIVisualizer(universe)
        self.assertIn('5', vis.render())

    def test_render_is_territorial(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestTerritorial", x=1, y=1, is_territorial=True))
        vis = CLIVisualizer(universe)
        self.assertIn('6', vis.render())

    def test_render_is_agile(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestAgile", x=1, y=1, is_agile=True))
        vis = CLIVisualizer(universe)
        self.assertIn('7', vis.render())

    def test_render_is_opportunistic(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestOpportunistic", x=1, y=1, is_opportunistic=True))
        vis = CLIVisualizer(universe)
        self.assertIn('8', vis.render())

    def test_render_has_thick_skin(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestThickSkin", x=1, y=1, has_thick_skin=True))
        vis = CLIVisualizer(universe)
        self.assertIn('9', vis.render())

    def test_render_is_patient(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestPatient", x=1, y=1, is_patient=True))
        vis = CLIVisualizer(universe)
        self.assertIn('*', vis.render())

    def test_visualizer_is_endurance_runner(self):
        from src.universe.engine import Entity, Universe
        universe = Universe(width=5, height=5)
        vis = CLIVisualizer(universe)
        entity = Entity("EnduranceRunner", x=1, y=1, is_endurance_runner=True)
        vis.universe.add_entity(entity)
        output = vis.render()
        self.assertIn('~', output)

    def test_prolific_entity(self):
        universe = Universe(width=5, height=5)
        visualizer = CLIVisualizer(universe)
        e = Entity("P", x=0, y=0, is_prolific=True)
        universe.add_entity(e)
        output = visualizer.render()
        self.assertIn('&', output)


    def test_render_is_resourceful(self):
        universe = Universe(width=5, height=5)
        vis = CLIVisualizer(universe)
        entity = Entity("Resourceful", x=1, y=1, is_resourceful=True)
        vis.universe.add_entity(entity)
        output = vis.render()
        self.assertIn('$', output)


    def test_visualizer_is_vocal(self):
        universe = Universe(width=3, height=3)
        entity = Entity("Vocal", x=1, y=1, is_vocal=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('o', output)


    def test_render_is_nomadic(self):
        universe = Universe(width=3, height=3)
        entity = Entity("Nomadic", x=1, y=1, is_nomadic=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('}', output)

    def test_visualize_photosensitive(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=5, height=5)
        e = Entity('Test', is_photosensitive=True)
        universe.add_entity(e)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('!', output)

    def test_visualize_fearless(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=5, height=5)
        e = Entity('Test', is_fearless=True)
        universe.add_entity(e)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('f', output)

    def test_visualize_is_scavenger(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Scavenger", x=0, y=0, is_scavenger=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('?', output)

    def test_visualize_is_cleaner(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Cleaner", x=0, y=0, is_cleaner=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('+', output)


    def test_render_is_spiteful(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Spiteful", x=0, y=0, is_spiteful=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('%', output)

    def test_render_is_intimidating(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Intimidating", x=0, y=0, is_intimidating=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn(']', output)

    def test_render_is_sunbather(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Sunbather", x=0, y=0, is_sunbather=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('#', output)



    def test_render_is_reckless(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Reckless", x=0, y=0, is_reckless=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('<', output)

    def test_render_is_thief(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Thief", x=0, y=0, is_thief=True)
        universe.add_entity(e)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('_', output)

    def test_render_is_absorbent(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Absorbent", x=0, y=0, is_absorbent=True, intelligence=1, is_nest_builder=False)
        universe.add_entity(e)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('/', output)


    def test_render_is_lucky(self):
        from src.universe.engine import Entity, Universe
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=1, height=1)
        entity = Entity("Lucky", x=0, y=0, is_lucky=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn(',', output)



    def test_render_is_vengeful(self):
        universe = Universe(width=1, height=1)
        vis = CLIVisualizer(universe)
        entity = Entity(name="E", x=0, y=0, energy=100, is_vengeful=True)
        universe.add_entity(entity)
        output = vis.render()
        self.assertIn(';', output)

    def test_render_is_restless(self):
        universe = Universe(width=1, height=1)
        vis = CLIVisualizer(universe)
        entity = Entity(name="E", x=0, y=0, energy=100, is_restless=True)
        universe.add_entity(entity)

        output = vis.render()
        self.assertIn(':', output)

    def test_render_is_defensive(self):
        from src.universe.engine import Entity, Universe
        u = Universe(width=10, height=10)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(u)
        e = Entity("Defensive", x=0, y=0, energy=10, age=0, max_age=50, perception_radius=10, diet='herbivore', preferred_temperature=20, temperature_tolerance=40, is_infected=False, infection_time=0, species=None, symbiotic_with=None, attack=1, defense=1, preferred_terrain=None, size=1, intelligence=1, inventory=None, target_species=None, target_plants=None, generation=0, mutations=0, hydration=50, max_hydration=50, is_sleeping=False, is_aquatic=False, is_flying=False, toxicity=0, poison_resistance=0, poisoned_time=0, camouflage=0.0, vision_type='normal', can_hibernate=False, lays_eggs=False, level=1, experience=0, can_hoard=False, max_stamina=50, stamina=50, is_nocturnal=False, can_burrow=False, has_spikes=False, can_spin_webs=False, is_venomous=False, can_photosynthesize=False, is_amphibious=False, has_shell=False, has_echolocation=False, is_aposematic=False, is_fruiting=False, is_immune=False, is_cold_blooded=False, is_electric=False, stunned_time=0, is_regenerative=False, has_claws=False, is_parasitic=False, has_scales=False, has_fur=False, can_climb=False, pack_hunter=False, has_bioluminescence=False, is_volcanic=False, is_forestal=False, is_desertic=False, is_social=False, is_carnivorous_plant=False, disease_vector=False, is_nocturnal_predator=False, is_scentless=False, can_sprint=False, is_vampiric=False, is_detritivore=False, can_sweat=False, has_blubber=False, is_mud_bather=False, is_filter_feeder=False, is_gluttonous=False, is_solitary=False, is_cannibalistic=False, is_ambush_predator=False, is_territorial=False, has_horns=False, is_migratory=False, is_cooperative=False, is_frugivore=False, is_agile=False, has_strong_stomach=False, is_opportunistic=False, has_thick_skin=False, is_hardy=False, is_fast_learner=False, is_playful=False, is_heavy_sleeper=False, is_patient=False, is_endurance_runner=False, is_evasive=False, is_prolific=False, is_adaptable=False, is_resourceful=False, is_vocal=False, is_nest_builder=False, is_nomadic=False, is_photosensitive=False, is_fearless=False, is_scavenger=False, is_scout=False, is_intimidating=False, is_cleaner=False, is_spiteful=False, is_sunbather=False, is_pack_mule=False, is_reckless=False, is_thief=False, is_absorbent=False, is_toxic=False, is_vibrant=False, is_arctic=False, is_fierce=False, is_lucky=False, is_telepathic=False, is_cautious=False, is_restless=False, is_vengeful=False, is_defensive=True)
        u.add_entity(e)
        output = visualizer.render()
        self.assertIn('D', output)

    def test_render_is_intimidating(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Intimidating", x=0, y=0, is_intimidating=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn(']', output)

    def test_render_has_sharp_teeth(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Teeth", x=0, y=0, has_sharp_teeth=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn(')', output)


    def test_render_is_parasite_resistant(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("Resistant", x=0, y=0, is_parasite_resistant=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('"', output)

    def test_render_is_forager(self):
        from src.universe.engine import Entity, Universe
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=1, height=1, food_spawn_rate=0.0)
        entity = Entity("Test", x=0, y=0, is_forager=True)
        universe.entities.append(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn("'", output)


    def test_render_is_ice_dweller(self):
        universe = Universe(10, 10)
        entity = Entity("Ice Dweller", x=5, y=5, is_ice_dweller=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('I', output)

    def test_draw_pacifist_entity(self):
        universe = Universe(10, 10)
        entity = Entity("Pacifist", x=5, y=5, is_pacifist=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('¥', output)


    def test_render_farsighted(self):
        universe = Universe(10, 10)
        entity = Entity("Farsighted", x=5, y=5, is_farsighted=True)
        universe.add_entity(entity)
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('€', output)

    def test_render_is_volcanic_glider(self):
        from src.universe.engine import Universe, Entity
        from src.universe.visualizer import CLIVisualizer
        universe = Universe(width=10, height=10)
        e = Entity("VGlider", x=0, y=0, is_volcanic_glider=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('∨', output)


    def test_render_is_mud_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Mud Dweller", x=5, y=5, is_mud_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("L", captured_output.getvalue())

    def test_render_cave_terrain(self):
        from src.universe.engine import Universe, Terrain
        universe = Universe(10, 10)
        universe.add_terrain(Terrain(x=5, y=5, terrain_type='cave'))
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("c", captured_output.getvalue())

    def test_render_is_mountain_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Mountain Dweller", x=5, y=5, is_mountain_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("G", captured_output.getvalue())

    def test_render_is_ash_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Ash Dweller", x=5, y=5, is_ash_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        vis = CLIVisualizer(universe)
        output = vis.render()
        self.assertIn('J', output)

    def test_render_is_cave_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Cave Dweller", x=5, y=5, is_cave_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("C", captured_output.getvalue())


    def test_render_is_spring_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Spring Dweller", x=5, y=5, is_spring_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("p", captured_output.getvalue())

    def test_render_is_summer_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Summer Dweller", x=5, y=5, is_summer_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("u", captured_output.getvalue())

    def test_render_is_autumn_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Autumn Dweller", x=5, y=5, is_autumn_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("a", captured_output.getvalue())

    def test_render_is_winter_dweller(self):
        from src.universe.engine import Universe, Entity
        universe = Universe(10, 10)
        entity = Entity("Winter Dweller", x=5, y=5, is_winter_dweller=True)
        universe.add_entity(entity)
        from src.universe.visualizer import CLIVisualizer
        visualizer = CLIVisualizer(universe)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn("i", captured_output.getvalue())

    def test_render_is_ageless(self):
        from src.universe.engine import Entity, Universe
        universe = Universe(10, 10)
        e = Entity(name="E", x=1, y=1, is_ageless=True)
        universe.add_entity(e)
        from src.universe.visualizer import CLIVisualizer
        import io, sys
        visualizer = CLIVisualizer(universe)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        visualizer.print_state()
        sys.stdout = sys.__stdout__
        out = captured_output.getvalue()
        self.assertIn("A", out)

    def test_render_is_disease_resistant(self):
        u = Universe(width=3, height=3)
        e = Entity(name="E", x=1, y=1, is_disease_resistant=True)
        u.entities.append(e)
        v = CLIVisualizer(u)
        output = v.render()
        self.assertIn('r', output)




    def test_render_is_stun_dweller(self):
        u = Universe(width=3, height=3)
        e = Entity(name="E", x=1, y=1, is_stun_dweller=True)
        u.entities.append(e)
        v = CLIVisualizer(u)
        output = v.render()
        self.assertIn('D', output)


    def test_visualize_is_fire_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_fire_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('q', captured.getvalue())


    def test_visualize_is_drought_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_drought_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('d', captured.getvalue())


    def test_visualize_is_mud_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_mud_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('m', captured.getvalue())

    def test_visualize_is_earthquake_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_earthquake_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('E', captured.getvalue())

    def test_visualize_is_volcanic_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_volcanic_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('V', captured.getvalue())

    def test_visualize_is_snow_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_snow_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('S', captured.getvalue())

    def test_visualize_is_blizzard_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_blizzard_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('B', captured.getvalue())

    def test_visualize_is_storm_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_storm_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('Z', captured.getvalue())

    def test_visualize_is_rain_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_rain_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('R', captured.getvalue())

    def test_visualize_is_mountain_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_mountain_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('M', captured.getvalue())

    def test_visualize_is_cave_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_cave_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('c', captured.getvalue())

    def test_visualize_is_dune_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_dune_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('u', captured.getvalue())

    def test_visualize_is_frost_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_frost_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('f', captured.getvalue())

    def test_visualize_is_web_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_web_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('b', captured.getvalue())

    def test_visualize_is_ash_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_ash_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('h', captured.getvalue())

    def test_visualize_is_forest_walker(self):
        u = Universe(width=10, height=10)
        v = CLIVisualizer(u)
        u.entities.clear()
        entity = Entity(name="test", x=5, y=5, is_forest_walker=True)
        u.add_entity(entity)
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        v.print_state()
        sys.stdout = sys.__stdout__
        self.assertIn('r', captured.getvalue())

if __name__ == '__main__':
    unittest.main()
