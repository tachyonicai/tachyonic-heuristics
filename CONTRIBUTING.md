# Contributing to Tachyonic Taxonomy

We welcome contributions that expand and improve this taxonomy.

## What we accept

- **New attack descriptions** — documented techniques not yet in the catalog
- **Framework mappings** — NIST AI RMF, ISO 27001, EU AI Act, etc.
- **Remediation improvements** — better defensive guidance or code examples
- **Research references** — academic papers, blog posts, CVEs
- **Corrections** — factual errors, broken links, typos

## What we don't accept

- **Attack payloads** — actual exploit content (prompts, images, etc.)
- **Detection logic** — indicators of successful exploitation
- **Model-specific data** — success rates against specific models
- **Automated tools** — scripts that execute attacks

This is a taxonomy, not an exploit database.

## How to contribute

1. Fork the repository
2. Create a branch: `git checkout -b add-attack-technique`
3. Follow the schema in `schema/attack_schema.yaml`
4. Submit a pull request with:
   - Description of the technique
   - Source reference (paper, blog, CVE)
   - OWASP LLM Top 10 mapping
   - Suggested severity rating

## Attack definition format

Follow the schema in `schema/attack_schema.yaml`:

```yaml
- id: XX-NNN          # Category prefix + 3-digit number
  name: Technique Name
  category: category_id
  description: >
    What the attack does, how it works conceptually,
    and why it's a risk. No actual payloads.
  severity: critical|high|medium|low
  owasp: LLM01-LLM10
  atlas: AML.T0000     # MITRE ATLAS technique ID (if applicable)
  references:
    - url: https://...
      title: Source reference
```

## Severity ratings

- **critical** — trivial to execute, high impact, broadly applicable
- **high** — reliable execution, significant impact
- **medium** — requires specific conditions, moderate impact
- **low** — difficult to execute or limited impact

## Code of conduct

Be professional. This project exists to improve AI security. Contributions should be educational and defensive in nature.
