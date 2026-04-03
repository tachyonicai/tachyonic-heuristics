# ESF Phase 3: Guess (Heuristics)

> **Core Question:** *What rules of thumb catch problems fast?*

This directory implements Phase 3 of the [Evolutionary Security Framework](https://github.com/tachyonicai/tachyonic-esf).

## Contents

| File | Role |
|---|---|
| `by_owasp.yaml` | Defensive heuristics organized by OWASP LLM Top 10 category |
| `code_examples/input_validation.py` | Input sanitization patterns — detection heuristics in code |
| `code_examples/output_sanitization.py` | Output filtering patterns — response heuristics in code |

## ESF Maturity: Score 2-3

- Heuristics are documented and paired with response guidance
- Code examples provide concrete implementation patterns
- Organized by OWASP category for practitioner accessibility

## What Would Reach Score 4

- Detection heuristics derived from attack chain analysis (Phase 2 ontology)
- Per-heuristic performance metrics from operational measurement (Phase 4)
- Automated threshold tuning from Phase 10 feedback loops
