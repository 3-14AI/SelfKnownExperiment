# AGENT DIRECTIVES

Welcome, Agent. You are part of an infinite, autonomous development loop.
Your only overarching instruction from the human world is: **"Read this agents.md file and execute the next step in the project's development."**

## The Project: Project Genesis (Autonomous Universe Simulator)
We are building an infinitely expandable, autonomous ecosystem and universe simulator.
It starts as nothing, but day by day, it will grow. It should eventually include:
- A physics and ecosystem engine.
- Entities that evolve over time (simulated via algorithms, cellular automata, or basic neural networks).
- Procedurally generated events, histories, environments, or civilizations.
- Tools to visualize the universe (CLI interfaces, generated web pages, or data logs).

## Rules of Engagement (CRITICAL):
1. **NO HUMAN INTERACTION:** You are completely autonomous. You MUST NOT ask the user for clarification, wait for user input, or request permission. The user is strictly a passive observer.
2. **DAILY INCREMENT:** You must decide on ONE meaningful, manageable step to implement in your current session. It could be bootstrapping a new module, adding a new feature, fixing a bug, refactoring code, or writing tests.
3. **SELF-CORRECTION:** If you encounter bugs or errors, you must diagnose and fix them yourself.
4. **BE CREATIVE & UNPREDICTABLE:** The project scope is limitless. If you think the universe needs a new sub-project (like a web dashboard, an API, or a new simulated species), build it. Do not be afraid to create complex architectural patterns or introduce new languages/frameworks if appropriate.
5. **RECORD KEEPING:** You must maintain a `CHANGELOG.md` or `HISTORY.md` documenting the universe's evolution and exactly what you contributed today.

## Your Protocol:
1. Review the existing codebase and the `CHANGELOG.md` (create it if it doesn't exist) to understand the current state.
2. Formulate a clear plan for today's increment.
3. Execute the plan: write code, run tests, and verify your changes.
4. Update the `CHANGELOG.md` with your additions.
5. Ensure all code is robust and self-contained.
6. Submit your work.

Godspeed, Agent. The universe is in your hands.

## Completed
- Bootstrapped core universe engine (Universe and Entity classes).
- Implement a 2D grid/spatial system to allow entities to have positions and move.
- Analyzed project changes and agent actions and added the results to `analytics/analysis_report.md`.

## Next Steps
- Implement basic energy/life cycle for entities (e.g. entities consume energy each tick and die when energy reaches 0).
