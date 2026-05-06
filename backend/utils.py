def clean_code_output(text):
    if not text:
        return ""

    text = text.strip()

    # Extract from markdown blocks
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            if "python" in part:
                return part.replace("python", "").strip()

        if len(parts) > 1:
            return parts[1].strip()

    # Remove common junk
    unwanted = [
        "Here is the code:",
        "Here’s the code:",
        "Below is the code:",
        "Sure, here is the code:"
    ]

    for u in unwanted:
        text = text.replace(u, "")

    return text.strip()