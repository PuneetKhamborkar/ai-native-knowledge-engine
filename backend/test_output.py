from input_processor import extract_intent, extract_query_type
from kdf_loader import load_kdfs
from kdf_registry import KDFRegistry
from kdf_aggregator import aggregate_kdfs
from output_formatter import format_output

query = "How to validate task API?"

print("🧠 Query:", query)

intent = extract_intent(query)
mode = extract_query_type(query)

kdfs, _ = load_kdfs()
registry = KDFRegistry(kdfs)

relevant_kdfs = registry.get_by_intent(intent)

aggregated = aggregate_kdfs(relevant_kdfs)

final_output = format_output(aggregated, mode)

print("\n🚀 FINAL OUTPUT:\n")
print(final_output)
print("\nDEBUG DATA:", aggregated)