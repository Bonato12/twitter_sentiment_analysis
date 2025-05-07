import re
import string

# Emojis comúnmente usados en sarcasmo
SARCASTIC_EMOJIS = {
    "🙃", "🙄", "😒", "😑", "😬", "😏", "😐", "😶",
    "😂", "🤣", "😅", "😆", "😌"  # A veces se usan en ironía tipo "me muero"
}

# Frases comunes irónicas
SARCASTIC_PHRASES = {
    "sí claro", "claro que sí", "obvio", "gracias por nada",
    "impresionante", "qué emoción", "excelente servicio",
    "el mejor día de mi vida", "ni se notó", "como no",
    "no me lo esperaba", "qué sorpresa", "espectacular",
    "wow increíble", "todo bien", "gracias por tanto", "re emocionante",
    "todo mal", "ni se notó", "felicidad total", "aguante todo"
}

# Preprocesamiento simple
def _clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(rf"[{re.escape(string.punctuation)}]", "", text)
    return text.strip()

# Función principal
def has_sarcasm_features(text: str) -> dict:
    clean = _clean_text(text)

    # Emojis
    emojis_found = [e for e in SARCASTIC_EMOJIS if e in text]
    has_emoji = len(emojis_found) > 0

    # Frases
    phrases_found = [p for p in SARCASTIC_PHRASES if p in clean]
    has_phrase = len(phrases_found) > 0

    return {
        "has_sarcastic_emoji": has_emoji,
        "has_sarcastic_phrase": has_phrase,
        "is_potentially_sarcastic": has_emoji or has_phrase,
        "emoji_count": len(emojis_found),
        "sarcastic_phrase_count": len(phrases_found),
        "emojis_detected": emojis_found,
        "phrases_detected": phrases_found
    }



data = {
    'Tweet': [
"@TinoCLeclerc Totalmente de acuerdo !!",
"@TinoCLeclerc Laa viste ? Yo en el medio me quede dormido me desperté me quede dormido me desperté gano Max me volví a dormir",
"@TinoCLeclerc @TinoCLeclerc Pero cualquier cosa es más emocionante que lo que fue el gp de japon... dioooss jajaja me dormía...",
"@TinoCLeclerc Confirmo",
"@TinoCLeclerc Sin duda.. Elijo creer",
"@TinoCLeclerc Coincido 100%!!! 53 vueltas de las cuales sobraron unas 50 (estoy siendo generosa)"
    ]
}



#response  = import_dataset(cfg.DATASET_RESPONSE_FINAL) 

#evaluate_tweets_sentiment(response)

for tweet in data["Tweet"]:
    print(has_sarcasm_features(tweet))
