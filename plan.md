1. Add `Supergiant` class in `src/universe/galaxy.py` to represent supergiant stars.
2. Add `generate_supergiants(self, num_supergiants)` method in `Galaxy` class in `src/universe/galaxy.py` to generate supergiants and add them to `self.supergiants`.
3. Add `supergiants = []` to `Galaxy.__init__` in `src/universe/galaxy.py`.
4. Add `test_supergiant_generation` in `TestGalaxy` class in `tests/test_galaxy.py` to test the procedural generation of supergiants.
5. Update `agents.md` to add `- [x] Implemented procedural supergiant generation for galaxies. Added \`Supergiant\` class and \`generate_supergiants\` method to \`Galaxy\`. Added tests and verified the test suite runs successfully.`
6. Update `CHANGELOG.md` with the new feature under `## [Unreleased]`.
7. Generate analytics in `analytics/analysis_495.md`.
8. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
9. Submit the change.
