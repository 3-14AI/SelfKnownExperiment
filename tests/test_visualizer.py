import unittest
from src.universe.engine import Universe, Entity, Food, Terrain
from src.universe.visualizer import CLIVisualizer

class TestCLIVisualizer(unittest.TestCase):
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

if __name__ == '__main__':

    unittest.main()
