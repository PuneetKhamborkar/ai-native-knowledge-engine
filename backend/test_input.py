from input_processor import extract_intent
from kdf_generator import generate_kdf
from kdf_saver import save_kdf
from kdf_loader import load_kdfs
from kdf_registry import KDFRegistry
from kdf_updater import update_existing_kdf

text = "User should be able to create task with validation"

print("🧠 Input:", text)

intent = extract_intent(text)
print("🎯 Intent:", intent)

kdfs, _ = load_kdfs()
registry = KDFRegistry(kdfs)

existing = registry.get_by_intent(intent)

updated = update_existing_kdf(existing, intent, text)

if updated:
    print("♻️ Updated existing KDF:", updated["id"])
else:
    new_kdf = generate_kdf(text, intent)
    path = save_kdf(new_kdf)
    print("🆕 New KDF created at:", path)