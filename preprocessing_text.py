import nltk
from nltk.corpus import stopwords
from num2words import num2words
import re
from textblob import TextBlob
import emoji
import spacy
from spacy.tokens import Doc
import stanza

nlp = spacy.load("es_core_news_sm")

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

#stanza.download('es')
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

# Lista de stopwords importantes que queremos conservar
stopwords_importantes = {
    "no", "muy", "realmente", "bastante", "también", "si", "como", "tan", "porque", "cuando", "quiero",
    "me", "te", "estoy", "estaba", "esto", "este", "ese", "aquí", "allí", "más", "lo", "quién", "algo",
    "todo", "poco", "nada", "tal"
}

# Diccionario de antónimos básicos para invertir polaridad
antonimos = {
    "enojado": "tranquilo",
    "feliz": "triste",
    "triste": "alegre",
    "bueno": "malo",
    "fuerte": "débil",
    "rápido": "lento",
    "fácil": "difícil",
    "alto": "bajo",
    "largo": "corto",
    "hermoso": "feo",
    "brillante": "opaco",
    "rico": "pobre",
    "caro": "barato",
    "limpio": "sucio",
    "caliente": "frío",
    "joven": "viejo",
    "suave": "áspero",
    "inteligente": "tonto",
    "amable": "grosero",
    "generoso": "egoísta",
    "honesto": "falso",
    "trabajador": "perezoso",
    "valiente": "cobarde",
    "optimista": "pesimista",
    "simpático": "antipático",
    "sano": "enfermo",
    "ordenado": "desordenado",
    "seguro": "inseguro",
    "positivo": "negativo",
    "sabio": "ignorante",
    "útil": "inútil",
    "abierto": "cerrado",
    "tranquilo": "nervioso",
    "amable": "hostil"
}
# Conectores de contradicción
conectores_contradiccion = {"pero", "aunque", "sin embargo", "no obstante"}

def remove_mentions(text):
    return re.sub(r'@\w+', '', text).strip()

# Función para reemplazar emojis por descripciones
def convert_emojis_to_words(text):
    return emoji.demojize(text, language='es')

# Función para reemplazar URLs en el texto
def remove_urls(texto):
    return re.sub(r'http[s]?://\S+|www\.\S+', '', texto)

# Tokenización de texto
def tokenize(words):  
    return nltk.word_tokenize(words)

# Conversión a minúsculas
def to_lowercase(words):
    return [word.lower() for word in words]

# Eliminación de stopwords pero conservando las importantes
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('spanish'))
    return [token for token in tokens if token not in stop_words or token in stopwords_importantes]

# Eliminación de URLs en tokens
def eliminar_urls(tokens):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return [token for token in tokens if not url_pattern.match(token)]

# Lematización de verbos
def lemmatize_verbs(tokens):
    tokens = [token for token in tokens if token.strip() != '']
    text = " ".join(tokens)
    doc = nlp(text)
    lemmatized_tokens = []
    for sent in doc.sentences:
        for word in sent.words:
            if word.upos in ["VERB", "AUX"]:
                lemmatized_tokens.append(word.lemma if word.lemma else word.text)
            else:
                lemmatized_tokens.append(word.text)
    return lemmatized_tokens

# Reemplazo de números por palabras
def replace_number(words):
    return [num2words(word, lang='es') if word.isdigit() else word for word in words]

# Eliminación de puntuación
def remove_punctuation(words):
    return [re.sub(r'[^\w\s]', '', word) for word in words if word.strip()]

# Manejo de negaciones con opción de invertir polaridad
def manejar_negaciones(palabras, invertir_polaridad=False):
    palabras_procesadas = []
    negar = False  # Marcamos si estamos en una sección negativa
    for i, palabra in enumerate(palabras):
        # Detectamos si hay una negación como "no", "nunca", "jamás", etc.ç
        if palabra.lower() in {"no", "nunca", "jamás", "sin"}:
            negar = True  # Marcamos que encontramos una negació
        elif negar and palabra.isalpha():  # Si viene una palabra después de la negación
            if invertir_polaridad and palabra in antonimos:
                palabras_procesadas.append(antonimos[palabra])  # Reemplazamos por su antónimo
            else:
                palabras_procesadas.append(palabra)  # Si no invertimos, dejamos la palabra tal cual
        else:
            palabras_procesadas.append(palabra)  # Agregamos palabras no afectadas

    if invertir_polaridad:
        palabras_procesadas = [palabra for palabra in palabras_procesadas if palabra.lower() != "no"]

    return palabras_procesadas

# Manejo de contradicciones
def manejar_contradicciones(text):
    for conector in conectores_contradiccion:
        if conector in text:
            partes = text.split(conector, 1)
            if len(partes) == 2:
                primera_parte, segunda_parte = partes
                pol_primera = TextBlob(primera_parte).sentiment.polarity
                pol_segunda = TextBlob(segunda_parte).sentiment.polarity
                
                # Si hay contradicción, priorizar la parte más fuerte en sentimiento
                if abs(pol_primera) > abs(pol_segunda):
                    return primera_parte.strip()
                else:
                    return segunda_parte.strip()
    return text

def normalize(text):
    text = remove_urls(text)
    text = remove_mentions(text)
    text = convert_emojis_to_words(text)
    text = tokenize(text)
    text = to_lowercase(text)
    text = remove_stopwords(text)
    text = replace_number(text)
    text = remove_punctuation(text)
    text = lemmatize_verbs(text)
    return ' '.join(text)

