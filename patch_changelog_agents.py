# Update agents.md
with open('agents.md', 'r') as f:
    content = f.read()

agent_entry = "- [x] Implemented `is_stun_resistant_predator` trait. Entities with this trait gain an attack multiplier of 1.5x when attacking entities with `is_stun_resistant` trait. Added tests and visualizer.\n"
content = content.replace("## Next Steps\n", f"## Next Steps\n{agent_entry}")

with open('agents.md', 'w') as f:
    f.write(content)

# Update CHANGELOG.md
with open('CHANGELOG.md', 'r') as f:
    content = f.read()

changelog_entry = "- Implemented `is_stun_resistant_predator` trait granting an attack multiplier against `is_stun_resistant` entities. Added tests and visualizer rendering.\n"
content = content.replace("## [Unreleased]\n", f"## [Unreleased]\n{changelog_entry}", 1)

with open('CHANGELOG.md', 'w') as f:
    f.write(content)
