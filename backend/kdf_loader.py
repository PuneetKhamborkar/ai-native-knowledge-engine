import os
import yaml

# 📁 Get project root (go one level up from backend)
BASE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "kdf",
    "software_product"
)


def load_kdfs():
    kdfs = []

    print("📂 Loading from:", BASE_PATH)

    if not os.path.exists(BASE_PATH):
        print("❌ KDF folder NOT found:", BASE_PATH)
        return kdfs

    for root, _, files in os.walk(BASE_PATH):
        for file in files:
            if file.endswith(".yaml"):
                path = os.path.join(root, file)

                print("📄 Found:", path)

                try:
                    with open(path, "r") as f:
                        data = yaml.safe_load(f)

                        if isinstance(data, dict):
                            kdfs.append(data)

                except Exception as e:
                    print(f"⚠️ Error loading {file}: {e}")

    print(f"✅ Loaded {len(kdfs)} KDFs")

    return kdfs