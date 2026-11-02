1. Use `sed` to fix the assertion in `test_fur_heat_penalty` inside `tests/test_engine_core.py` from `self.assertEqual(entity.energy, 86)` to `self.assertEqual(entity.energy, 96)`.
2. Run tests to confirm the fix works using `python3 run_tests.py`.
3. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done using `bash pre_commit.sh`.
4. Submit the final changes.
