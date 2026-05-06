import os

# Lazy load Whisper (no startup crash)
whisper_model = None


def load_whisper():
    global whisper_model

    if whisper_model is None:
        try:
            import whisper
            whisper_model = whisper.load_model("base")
            print("✅ Whisper model loaded")
        except Exception as e:
            print(f"⚠️ Whisper not available: {e}")
            whisper_model = False


def process_input(query=None, image_path=None, audio_path=None):
    """
    Multimodal handler:
    - Text → direct
    - Image → placeholder (safe)
    - Audio → Whisper (lazy)
    """

    # TEXT
    if query and isinstance(query, str) and query.strip():
        return query.strip()

    # IMAGE (safe fallback)
    if image_path and os.path.exists(image_path):
        return "image input detected"

    # AUDIO
    if audio_path and os.path.exists(audio_path):
        load_whisper()

        if whisper_model:
            try:
                result = whisper_model.transcribe(audio_path)
                text = result.get("text", "")
                if text.strip():
                    return text.strip()
            except Exception as e:
                print(f"Whisper error: {e}")

    return ""