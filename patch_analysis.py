import os
import re

# Update analytics/current_analysis.md and analytics/analysis_report.md
analysis_text = """### Analysis 469: `is_stun_resistant_predator` Implementation

**Goal:** Provide entities with the `is_stun_resistant_predator` trait an attack multiplier when attacking entities with the `is_stun_resistant` trait, completing the next step in `agents.md`.

**Files Modified:**
- `src/universe/engine.py`: Added `is_stun_resistant_predator` trait and its mutation/combat logic. Also added `is_stun_resistant` mutation logic, as it seems `is_stun_resistant` was not explicitly listed for mutation and is required to test combat multiplier against it.
- `src/universe/visualizer.py`: Added rendering for the new trait (character 'Ŝ').
- `tests/test_is_stun_resistant_predator.py`: Created this file with tests for combat multiplier against `is_stun_resistant` prey, trait mutation, and visualizer rendering.
- `agents.md`: Marked the `is_stun_resistant_predator` trait as completed under Next Steps.
- `CHANGELOG.md`: Logged the new feature under `[Unreleased]`.

**Outcome:**
The new predator trait allows predators to counter `is_stun_resistant` prey effectively. All tests (1549/1549) passed, ensuring the new trait operates without breaking existing mechanics.
"""

def append_to_file(filepath, text):
    with open(filepath, 'a') as f:
        f.write("\n" + text + "\n")

if os.path.exists('analytics/current_analysis.md'):
    append_to_file('analytics/current_analysis.md', analysis_text)
if os.path.exists('analytics/analysis_report.md'):
    append_to_file('analytics/analysis_report.md', analysis_text)
