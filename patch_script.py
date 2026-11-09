import sys

def patch_galaxy():
    try:
        with open("src/universe/galaxy.py", "r") as f:
            content = f.read()

        # Add TidalTail class
        if "class TidalTail:" not in content:
            anchor = "class StellarStream:\n    def __init__(self, name, length):\n        self.name = name\n        self.length = length\n"
            replacement = anchor + "\nclass TidalTail:\n    def __init__(self, name, length):\n        self.name = name\n        self.length = length\n"
            content = content.replace(anchor, replacement)

        # Add to Galaxy.__init__
        if "self.tidal_tails = []" not in content:
            anchor = "        self.stellar_streams = []\n"
            replacement = anchor + "        self.tidal_tails = []\n"
            content = content.replace(anchor, replacement)

        # Add generate method
        if "def generate_tidal_tails" not in content:
            anchor = "    def generate_stellar_streams(self, num_streams):\n        import random\n        for i in range(num_streams):\n            name = f\"StellarStream-{i+1}\"\n            length = random.randint(1000, 10000)\n            self.stellar_streams.append(StellarStream(name, length))\n"
            replacement = anchor + "\n    def generate_tidal_tails(self, num_tails):\n        import random\n        for i in range(num_tails):\n            name = f\"TidalTail-{i+1}\"\n            length = random.randint(1000, 10000)\n            self.tidal_tails.append(TidalTail(name, length))\n"
            content = content.replace(anchor, replacement)

        with open("src/universe/galaxy.py", "w") as f:
            f.write(content)

    except Exception as e:
        print(f"Error patching galaxy.py: {e}")

def patch_tests():
    try:
        with open("tests/test_galaxy.py", "r") as f:
            content = f.read()

        if "def test_generate_tidal_tails" not in content:
            anchor = "    def test_generate_stellar_streams(self):\n        from src.universe.galaxy import StellarStream, Galaxy\n        galaxy = Galaxy(\"Test Galaxy\", 1000, 1000)\n        galaxy.generate_stellar_streams(5)\n        self.assertEqual(len(galaxy.stellar_streams), 5)\n        for stream in galaxy.stellar_streams:\n            self.assertIsInstance(stream, StellarStream)\n"
            replacement = anchor + "\n    def test_generate_tidal_tails(self):\n        from src.universe.galaxy import TidalTail, Galaxy\n        galaxy = Galaxy(\"Test Galaxy\", 1000, 1000)\n        galaxy.generate_tidal_tails(5)\n        self.assertEqual(len(galaxy.tidal_tails), 5)\n        for tail in galaxy.tidal_tails:\n            self.assertIsInstance(tail, TidalTail)\n"
            content = content.replace(anchor, replacement)

        with open("tests/test_galaxy.py", "w") as f:
            f.write(content)

    except Exception as e:
        print(f"Error patching test_galaxy.py: {e}")

if __name__ == '__main__':
    patch_galaxy()
    patch_tests()
