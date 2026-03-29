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

    # Very Common Vulgar Tamil Abuses (Romanized)
    "punda", "punde", "pundai", "punda ma", "pear punda",
    "koodhi", "kuthi", "koothi", "kuthi mayir", "koothi mayir",
    "thayoli", "thayoli", "thaayoli", "thaiyoli",
    "thevidiya", "thevudiya", "thevidiyaa", "thevudiyaa",
    "thevidiya paiyan", "thevudiyaa paiyan",
    "otha", "ootha", "ommaala", "ommala okka", "ommaala okka",
    "pool", "poolu", "poola oombu", "pool oombi",
    "sunni", "soothu", "shithi",
    "mayiru", "mairandi", "mayiraandi",
    "baadu", "baadu",
    "oombu", "oombuda",

    # Family-based Severe Abuses (similar to Hindi madarchod/behenchod)
    "thangaiyoli", "okkaravoli", "thangai oli",
    "thayoli",  # motherfucker equivalent

    # Other Common Tamil Insults & Slurs
    "losu", "loos u", "paithiyam", "muttaal", "koomuttai",
    "eruma", "yeruma", "yerumamaadu", "erumai",
    "dhandasoru", "dhanda soru",
    "mundhirikottai", "mundam",
    "puramboku", "arivu ketta mundam",
    "moodevi", "kamunaati",
    "kutti sevuru", "karumam", "sori naai",
    "dubakoor", "dubukku",

    # Mixed / Common Phrases used in comments
    "punda mavane", "punda thambi", "thevidiya paiya",
    "poola oombu", "ommaala okka", "thayoli saale",
    "kuthi mayir", "mayiraandi",
    "otha da", "oombu da",

    # Milder Bullying / Insult words (still often toxic)
    "idiot", "stupid", "pagal", "loosu", "muttaal", "paithiyam",
    "gadha", "eruma", "kutta", "naai"
]
