from transformers import pipeline
import re
from .schemas import BLACKLIST

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "unitary/toxic-bert"
THRESHOLD = 0.7  # IMPORTANT: tuned for this model

# -----------------------------
# LOAD MODEL (pipeline is CORRECT for this model)
# -----------------------------
classifier = pipeline(
    "text-classification",
    model=MODEL_NAME,
    device=0 if False else -1  # CPU safe; change if GPU needed
)

# -----------------------------
# CLEANING FUNCTION
# -----------------------------
def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()

# -----------------------------
# RULE-BASED DETECTION
# -----------------------------
def rule_based_check(text: str):
    return any(word in text for word in BLACKLIST)

# -----------------------------
# CORE PREDICTION
# -----------------------------
def predict(text: str):
    clean_text = preprocess(text)

    # 1. RULE-BASED (HIGH PRIORITY)
    if rule_based_check(clean_text):
        return {
            "text": text,
            "toxic": True,
            "confidence": 0.95,
            "source": "rule"
        }

    # 2. MODEL PREDICTION
    result = classifier(clean_text)[0]

    label = result["label"].lower()
    score = float(result["score"])

    is_toxic = (label == "toxic") and (score >= THRESHOLD)

    return {
        "text": text,
        "toxic": is_toxic,
        "confidence": round(score, 4),
        "label": label,
        "source": "model"
    }

# -----------------------------
# BATCH PREDICTION
# -----------------------------
def batch_predict(texts: list[str]):
    cleaned_texts = [preprocess(t) for t in texts]
    results = [None] * len(texts)

    # 1. RULE-BASED FIRST PASS
    for i, text in enumerate(cleaned_texts):
        if rule_based_check(text):
            results[i] = {
                "text": texts[i],
                "toxic": True,
                "confidence": 0.95,
                "source": "rule"
            }

    # 2. MODEL FOR REMAINING
    remaining_indices = [i for i, r in enumerate(results) if r is None]
    remaining_texts = [cleaned_texts[i] for i in remaining_indices]

    if remaining_texts:
        model_outputs = classifier(remaining_texts)

        for idx, output in zip(remaining_indices, model_outputs):
            label = output["label"].lower()
            score = float(output["score"])

            results[idx] = {
                "text": texts[idx],
                "toxic": (label == "toxic") and (score >= THRESHOLD),
                "confidence": round(score, 4),
                "label": label,
                "source": "model"
            }

    return results
