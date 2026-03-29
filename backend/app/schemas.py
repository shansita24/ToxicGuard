from pydantic import BaseModel
from typing import List


class TextRequest(BaseModel):
    text: str


class BatchRequest(BaseModel):
    texts: List[str]

# ENGLISH + HINGLISH ABUSE WORDS (for rule-based first pass)
BLACKLIST = [
    # English Abusive / Bullying Words
    "asshole", "arsehole", "bastard", "bitch", "cunt", "dick", "dickhead", "prick",
    "fucker", "motherfucker", "shit", "piece of shit", "wanker", "idiot", "dumbass",
    "moron", "retard", "loser", "faggot", "whore", "slut", "pussy", "cock", "bollocks",
    "jerk", "fool", "ugly", "fatty", "stupid", "kill yourself", "go die", "go fuck yourself",

    # Common Hinglish / Hindi Gaaliyan (Roman Script)
    "madarchod", "maaderchod", "maderchod", "madarchood", "mc",
    "behenchod", "bhenchod", "bahenchod", "bc", "bkl",
    "betichod", "betichood",
    "bhosadike", "bhosdiwala", "bhosdi ke", "bhosdi",
    "chutiya", "chootiya", "chutiye", "chutia",
    "gaandu", "gandu", "gaand", "gand",
    "lund", "lauda", "aand", "aandu",
    "chut", "choot",
    "randi", "randi ka", "randika",
    "kuttiya", "kutiya", "kutta", "kutte",
    "harami", "haramzada", "kamina", "kamini",
    "chodu", "bhadwa", "bhadve", "bhadwaa",
    "hijra", "bakchod", "bakchodi",
    "tatti", "paad", "gadha", "gadhi",
    "bewakoof", "ullu ka pattha", "saala", "saale",
    "saala kutta", "saali kutti",

    # Short forms & Common Variations (very frequent on Instagram)
    "bkl", "mkl", "bc", "mc", "mdrchod", "bhnchod", "chutiye",
    "gandu", "lund", "laude", "chut", "randi", "bhosdi",

    # Mixed Hinglish Phrases (common in comments)
    "chut",
    "madarchod saale", "bhenchod idiot", "chutiya saala",
    "gaandu", "randi ka bachcha", "harami kutte", "bhosdi ke",
    "fuck you madarchod", "stupid chutiya", "madarchod", "behenchod",
    "tera baap", "teri ma", "bhen ke lode", "lund ke", "chut ke",

    # Milder Bullying Insults (still often flagged as toxic)
    "pagal", "bewakuf", "idiot", "stupid", "loser", "fool", "donkey",
    "ullu", "gadha", "kutta", "kuttiya", "harami", "kamina"
]
