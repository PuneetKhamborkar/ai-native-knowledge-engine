def format_output(data, mode="full"):

    output = ""

    if mode == "validation":
        output += "⚙️ Validation Rules:\n"
        for r in data["rules"]:
            output += f"- {r}\n"
        return output

    if mode == "test":
        output += "🧪 Test Cases:\n"
        for t in data["tests"]:
            output += f"- {t}\n"
        return output

    if mode == "api":
        output += "🛠 API Design:\n"
        output += f"- Endpoint: {data['api'].get('endpoint')}\n"
        output += f"- Method: {data['api'].get('method')}\n"
        return output

    # FULL MODE (default)
    output += "✅ Solution: Create Scalable Task API\n\n"

    if data["requirements"]:
        output += "📌 Requirements:\n"
        for req in data["requirements"]:
            output += f"- {req}\n"
        output += "\n"

    if data["api"]:
        output += "🛠 API Design:\n"
        output += f"- Endpoint: {data['api'].get('endpoint')}\n"
        output += f"- Method: {data['api'].get('method')}\n\n"

    if data["rules"]:
        output += "⚙️ Validation & Rules:\n"
        for r in data["rules"]:
            output += f"- {r}\n"
        output += "\n"

    if data["tests"]:
        output += "🧪 Test Cases:\n"
        for t in data["tests"]:
            output += f"- {t}\n"
        output += "\n"

    return output