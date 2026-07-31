import unittest
from src.universe.engine import Universe, Entity, Food, Terrain
from src.universe.visualizer import CLIVisualizer

class TestCLIVisualizer(unittest.TestCase):
    def test_visualizer_disease_vector(self):
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
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
        expected_output = "...\n.c.\n..."
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


    def test_render_is_social(self):
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestSocial", x=1, y=1, is_social=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.p.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_forestal(self):
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestForestal", x=1, y=1, is_forestal=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.t.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_desertic(self):
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestDesertic", x=1, y=1, is_desertic=True))
        visualizer = CLIVisualizer(universe)
        expected_output = "...\n.d.\n..."
        self.assertEqual(visualizer.render(), expected_output)

    def test_render_is_volcanic(self):
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
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

    def test_visualizer_is_nocturnal_predator(self):
        universe = Universe(width=3, height=3)
        entity = Entity("NocturnalPred", x=1, y=1, is_nocturnal_predator=True)
        universe.add_entity(entity)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('N', output)





    def test_visualizer_is_scentless(self):
        from universe.engine import Universe, Entity, Terrain
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
        from universe.engine import Universe, Entity
        from universe.visualizer import CLIVisualizer
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


    def test_render_is_gluttonous(self):
        universe = Universe(10, 10)
        e = Entity("Glutton", x=2, y=2, is_gluttonous=True)
        universe.add_entity(e)
        visualizer = CLIVisualizer(universe)
        output = visualizer.render()
        self.assertIn('x', output)


    def test_render_can_hoard(self):
        universe = Universe(width=3, height=3)
        universe.add_entity(Entity("TestHoarder", x=1, y=1, can_hoard=True))
        viz = CLIVisualizer(universe)
        out = viz.render()
        self.assertIn('h', out)

if __name__ == '__main__':



    unittest.main()
