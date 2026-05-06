def aggregate_kdfs(kdfs):

    result = {
        "api": {},
        "tests": [],
        "rules": [],
        "context": [],
        "requirements": []
    }

    for k in kdfs:

        # API
        if k["type"] == "api":
            result["api"] = k.get("api", {})

            result["rules"].extend(k.get("rules", []))
            result["requirements"].extend(k.get("requirements", []))

        # TESTS
        if k["type"] == "test":
            result["tests"].extend(k.get("cases", []))

        # SYSTEM
        if k["type"] == "system":
            result["rules"].extend(k.get("rules", []))

        # FEATURE
        if k["type"] == "feature":
            result["requirements"].extend(k.get("requirements", []))

        # CONTEXT
        result["context"].extend(k.get("context", []))

    return result