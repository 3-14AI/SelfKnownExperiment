with open('CHANGELOG.md', 'r') as f:
    content = f.read()

entry = "- Implemented `is_unappetizing_predator`, `is_vibrant_predator`, `is_relentless_predator`, `is_tracker_predator`, `is_dust_bather_predator`, `is_scentless_predator`, `is_vengeful_predator` traits. Entities with these traits gain an attack multiplier of 1.5x when attacking entities with the corresponding traits. Added visualizer rendering and tests.\n"

if entry not in content:
    content = content.replace("## [Unreleased]\n", f"## [Unreleased]\n{entry}", 1)

    with open('CHANGELOG.md', 'w') as f:
        f.write(content)
