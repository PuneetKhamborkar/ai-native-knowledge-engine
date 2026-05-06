REQUIRED_FIELDS = ["id", "type", "intent"]

ALLOWED_TYPES = [
    "api", "database", "test", "guide",
    "prd", "frd", "srs", "config",
    "kb", "code", "system", "feature"
]

def validate_kdf(kdf):

    errors = []

    for field in REQUIRED_FIELDS:
        if field not in kdf:
            errors.append(f"Missing field: {field}")

    if kdf.get("type") not in ALLOWED_TYPES:
        errors.append(f"Invalid type: {kdf.get('type')}")

    if not isinstance(kdf.get("intent", ""), str):
        errors.append("Intent must be string")

    return errors