with open('CHANGELOG.md', 'r') as f:
    content = f.read()

entry = "- Added Ecosystem interaction tests for predator-prey dynamics.\n"

if entry not in content:
    content = content.replace("## [Unreleased]\n", f"## [Unreleased]\n{entry}", 1)

    with open('CHANGELOG.md', 'w') as f:
        f.write(content)
