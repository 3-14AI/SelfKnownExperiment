1. Create and execute a Python patch script to append the `Microquasar` class and inject the `generate_microquasars` method into the `Galaxy` class in `src/universe/galaxy.py`, and add initialization to `Galaxy.__init__`.
2. Run `grep -A 10 'class Microquasar:' src/universe/galaxy.py` and `grep -A 10 'def generate_microquasars' src/universe/galaxy.py` to confirm the changes were applied correctly.
3. Create and execute a Python script to update the import statement and inject the `test_microquasar_generation` method into the `TestGalaxy` class in `tests/test_galaxy.py`.
4. Run `tail -n 25 tests/test_galaxy.py` to ensure the new test was appended correctly and without syntax errors.
5. Run the test suite (`python3 run_tests.py`) to verify the new feature works and doesn't break existing tests.
6. Execute `echo '- [x] Implemented procedural microquasar generation for galaxies. Added `Microquasar` class and `generate_microquasars` method to `Galaxy`. Added tests and verified the test suite runs successfully.' >> agents.md`.
7. Verify `agents.md` update using `tail -n 5 agents.md`.
8. Create and execute a Python script to idempotently replace `## [Unreleased]\n` with `## [Unreleased]\n- Implemented procedural microquasar generation for galaxies.\n` in `CHANGELOG.md`.
9. Verify `CHANGELOG.md` update using `grep -A 5 "## \[Unreleased\]" CHANGELOG.md`.
10. Use a bash `cat > analytics/analysis_485.md << 'EOF'` command to create the file with the required Russian analysis content documenting the new microquasar generation feature.
11. Verify `analytics/analysis_485.md` was created using `cat analytics/analysis_485.md`.
12. Complete pre commit steps to make sure proper testing, verifications, reviews and reflections are done.
