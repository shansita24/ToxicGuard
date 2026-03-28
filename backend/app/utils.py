def validate_text(text: str):
    if not text or len(text.strip()) == 0:
        return False
    if len(text) > 500:
        return False
    return True