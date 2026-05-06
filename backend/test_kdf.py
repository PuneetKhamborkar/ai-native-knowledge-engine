from kdf_loader import load_kdfs
from kdf_registry import KDFRegistry

print("🚀 Starting KDF Test...")

kdfs, errors = load_kdfs()

print("📦 Loaded KDFs:", kdfs)
print("❌ Errors:", errors)

registry = KDFRegistry(kdfs)

print("📊 Total KDFs:", len(kdfs))

print("🔍 Query create_task:")
print(registry.get_by_intent("create_task"))m