from input_processor import extract_intent
from kdf_loader import load_kdfs
from kdf_registry import KDFRegistry
from kdf_aggregator import aggregate_kdfs

query = "Create scalable task API with validation and test cases"

print("🧠 Query:", query)

intent = extract_intent(query)

kdfs, _ = load_kdfs()
registry = KDFRegistry(kdfs)

relevant_kdfs = registry.get_by_intent(intent)

print("\n📦 Retrieved KDFs:")
for k in relevant_kdfs:
    print("-", k["id"], "|", k["type"])

aggregated = aggregate_kdfs(relevant_kdfs)

print("\n🧩 Aggregated Output:")
print(aggregated)
print("🎯 Intent:", intent)