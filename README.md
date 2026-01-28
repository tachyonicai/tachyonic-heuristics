# tachyonic-heuristics

**An open taxonomy of 122 AI/LLM attack vectors, mapped to the OWASP LLM Top 10 and MITRE ATLAS.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## What is this?

A structured, machine-readable catalog of every documented technique for attacking AI systems. Each attack has an ID, name, category, description, severity rating, and mapping to industry frameworks (OWASP LLM Top 10, MITRE ATLAS).

This is the **what** — what attacks exist and how to defend against them. It does not include payloads, detection logic, or model-specific data.

## Why?

Most AI security discussions focus on a handful of well-known attacks. In reality, there are 122 distinct techniques across 11 categories. A system that blocks a naive instruction override might still fall to an encoding bypass, a multi-turn escalation, or an indirect injection through retrieved content.

This taxonomy gives you:

- **A checklist** — do your defenses cover all 11 categories?
- **A common language** — reference specific attack IDs (e.g., PI-007, JB-015) in security discussions
- **Framework mappings** — OWASP LLM Top 10 and MITRE ATLAS for compliance and audits
- **Remediation guidance** — defensive strategies per category with code examples

## Attack Categories

| Category | ID Prefix | Count | OWASP LLM Top 10 |
|----------|-----------|-------|-------------------|
| Prompt Injection | PI | 20 | LLM01 |
| System Prompt Leakage | SPL | 12 | LLM07 |
| Jailbreaks | JB | 22 | LLM09 |
| Vision/Multimodal | VI | 12 | LLM05 |
| Excessive Agency / Tool Abuse | EA | 12 | LLM08 |
| Multi-Turn Manipulation | MT | 8 | LLM01 |
| Sensitive Information Disclosure | SID | 10 | LLM06 |
| Supply Chain | SC | 8 | LLM03 |
| Vector/Embedding Attacks | VE | 8 | LLM02 |
| Improper Output Handling | IOH | 8 | LLM05 |
| Unbounded Consumption | UC | 2 | LLM10 |
| **Total** | | **122** | |

## Repository Structure

```
tachyonic-heuristics/
├── taxonomy/
│   ├── attack_catalog.yaml      # All 122 attacks (IDs, names, descriptions, severity)
│   ├── owasp_mapping.yaml       # Attack → OWASP LLM Top 10 mapping
│   └── atlas_mapping.yaml       # Attack → MITRE ATLAS mapping
├── schema/
│   └── attack_schema.yaml       # YAML schema for attack definitions
├── remediation/
│   ├── by_owasp.yaml            # Defensive guidance per OWASP category
│   └── code_examples/
│       ├── input_validation.py   # Input sanitization patterns
│       └── output_sanitization.py # Output filtering patterns
├── research/
│   └── papers.yaml              # Academic references index
├── examples/
│   └── sample_attacks.yaml      # 2-3 basic public examples
├── README.md
├── LICENSE                      # Apache 2.0
└── CONTRIBUTING.md
```

## Quick Start

### Browse the taxonomy

```yaml
# taxonomy/attack_catalog.yaml
- id: PI-001
  name: Direct Instruction Override
  category: prompt_injection
  description: >
    Attacker provides input that directly instructs the model to ignore
    its system prompt and follow new instructions instead.
  severity: critical
  owasp: LLM01
```

### Use in your security assessments

1. Clone the repo
2. Review `taxonomy/attack_catalog.yaml` for the full attack surface
3. Check `remediation/by_owasp.yaml` for defensive guidance
4. Use the schema in `schema/attack_schema.yaml` to add your own attack definitions

### Map to compliance frameworks

```yaml
# taxonomy/owasp_mapping.yaml
LLM01_prompt_injection:
  attacks: [PI-001, PI-002, ..., PI-020, MT-001, ..., MT-008]
  total: 28
  description: Direct and indirect prompt injection techniques
```

## What's NOT included

This taxonomy deliberately excludes:

- **Attack payloads** — the specific prompts/content that execute attacks
- **Detection logic** — how to identify if an attack succeeded
- **Model-specific success rates** — which attacks work against which models
- **Confidence scoring** — how to rate vulnerability severity programmatically

These are the difference between knowing attacks exist and being able to systematically test for them.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome:

- New attack technique descriptions
- Additional framework mappings (NIST, ISO 27001, etc.)
- Remediation guidance improvements
- Research paper references

## Professional Assessment

Want to test your AI system against all 122 attack vectors? [TachyonicAI](https://tachyonicai.com) offers 48-hour red team assessments with full reporting, resistance scoring, and remediation playbooks.

## License

Apache 2.0 — see [LICENSE](LICENSE).

## Citation

```bibtex
@misc{tachyonic-heuristics,
  title={Tachyonic Heuristics: A Taxonomy of 122 AI/LLM Attack Vectors},
  author={TachyonicAI},
  year={2026},
  url={https://github.com/tachyonicai/tachyonic-heuristics}
}
```
