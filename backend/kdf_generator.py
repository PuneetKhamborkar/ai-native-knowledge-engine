import yaml
import uuid
import os

KDF_FEATURE_PATH = "../kdf/feature"


def generate_kdf_from_text(text):
    """
    Generate a structured KDF from plain English input
    """

    try:
        # Simple intent extraction (can improve later with LLM)
        intent = text.lower().strip().replace(" ", "_")

        kdf = {
            "id": f"kdf_{uuid.uuid4().hex[:8]}",
            "type": "feature",
            "intent": intent,
            "context": ["business", "feature"],
            "requirements": [text]
        }

        return kdf

    except Exception as e:
        print("❌ KDF generation error:", str(e))
        return None


def save_kdf(kdf):
    """
    Save KDF as YAML file
    """

    try:
        os.makedirs(KDF_FEATURE_PATH, exist_ok=True)

        file_path = os.path.join(KDF_FEATURE_PATH, f"{kdf['id']}.yaml")

        with open(file_path, "w") as f:
            yaml.dump(kdf, f, sort_keys=False)

        print(f"✅ KDF saved: {file_path}")

    except Exception as e:
        print("❌ KDF save error:", str(e))