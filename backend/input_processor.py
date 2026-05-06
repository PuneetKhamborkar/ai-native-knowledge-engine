def extract_intent(text):

    text = text.lower()

    # primary intents
    if "task" in text and "create" in text:
        return "create_task"

    if "task" in text and "update" in text:
        return "update_task"

    # 🔥 fallback (VERY IMPORTANT)
    if "task" in text:
        return "create_task"

    return "general"


def extract_query_type(text):

    text = text.lower()

    if "validate" in text or "validation" in text:
        return "validation"

    if "test" in text:
        return "test"

    if "api" in text:
        return "api"

    return "full"