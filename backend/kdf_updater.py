def update_existing_kdf(existing_kdfs, intent, new_text):

    # priority order (very important)
    priority_types = ["feature", "api", "prd"]

    # try to find best match
    for p_type in priority_types:
        for k in existing_kdfs:
            if k["intent"] == intent and k["type"] == p_type:

                if "requirements" not in k:
                    k["requirements"] = []

                k["requirements"].append(new_text)

                return k

    return None