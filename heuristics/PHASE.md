# ESF Phase 3: Guess (Heuristics) — Strategic Layer

> **Core Question:** *What rules of thumb catch problems fast?*

This directory implements the **strategic layer** of ESF Phase 3. It describes *what to look for* and *how to respond* — not the specific detection logic, thresholds, or scoring that power production systems.

The `remediation/` directory in the repo root provides complementary guidance — defensive strategies and code examples organized by OWASP category. This directory organizes heuristics by attack chain (Phase 2 ontology) rather than by OWASP category.

## Contents

| File | Role |
|---|---|
| `detection_strategies.yaml` | What observable signals indicate each attack chain is being traversed |
| `response_playbooks.yaml` | What response actions to take for each detection signal |

## Open vs. Proprietary Boundary

**Open (this directory):** Detection *strategies* — what kinds of signals to monitor, at which trust boundaries, for which attack chains.

**Proprietary:** Detection *implementation* — specific patterns, regex, thresholds, scoring algorithms, model-specific tuning. These stay in the private pipeline because they are the competitive moat.

## ESF Maturity: Score 2-3

- Detection and response strategies are documented and paired
- Organized by attack chain for structural coverage
- Code examples in `remediation/` provide implementation starting points
