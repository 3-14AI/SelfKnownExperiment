import re

with open('tests/test_engine.py', 'r') as f:
    text = f.read()

# Fix Spring: it was testing summer instead of spring?
text = re.sub(
    r"(class TestIsSpringDancer.*?def test_no_energy_gain_not_dancer\(self\):.*?self\.universe\.time = )self\.universe\.season_length # summer",
    r"\1 0 # spring",
    text,
    flags=re.DOTALL
)

# Fix Autumn: it was testing summer instead of autumn?
text = re.sub(
    r"(class TestIsAutumnDancer.*?def test_no_energy_gain_not_dancer\(self\):.*?self\.universe\.time = )self\.universe\.season_length # summer",
    r"\1 self.universe.season_length * 2 # autumn",
    text,
    flags=re.DOTALL
)

# Fix Winter: it was testing summer instead of winter?
text = re.sub(
    r"(class TestIsWinterDancer.*?def test_no_energy_gain_not_dancer\(self\):.*?self\.universe\.time = )self\.universe\.season_length # summer",
    r"\1 self.universe.season_length * 3 # winter",
    text,
    flags=re.DOTALL
)

# Unskip tests
text = re.sub(r"    @unittest\.skip\('Flaky mock'\)\n(    def test_no_energy_gain_not_spring\(self\):)", r"\1", text)
text = re.sub(r"    @unittest\.skip\('Flaky mock'\)\n(    def test_no_energy_gain_not_summer\(self\):)", r"\1", text)
text = re.sub(r"    @unittest\.skip\('Flaky mock'\)\n(    def test_no_energy_gain_not_autumn\(self\):)", r"\1", text)
text = re.sub(r"    @unittest\.skip\('Flaky mock'\)\n(    def test_no_energy_gain_not_winter\(self\):)", r"\1", text)
text = re.sub(r"    @unittest\.skip\('Flaky mock'\)\n(    def test_mutation_and_inheritance\(self\):)", r"\1", text)


with open('tests/test_engine.py', 'w') as f:
    f.write(text)
