import nltk
from nltk.corpus import stopwords
from num2words import num2words
import re
import emoji
import spacy
import stanza

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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

def manejar_contradicciones(text):
    patron = r'\b(?:' + '|'.join(map(re.escape, conectores_contradiccion)) + r')\b'
    partes = re.split(patron, text, flags=re.IGNORECASE)
    if len(partes) > 1:
        ultima_parte = partes[-1].strip()
        return ultima_parte
    else:
        return text
    

def manejar_negaciones(tokens):
    negaciones = {"no", "nunca", "jamás", "sin"}
    resultado = []
    tokens = [token for token in tokens if token.strip() != '']

    negando = False
    for token in tokens:
        if token in negaciones:
            negando = True
            resultado.append(token)
        elif negando:
            resultado.append("NOT_" + token)
            negando = False
        else:
            resultado.append(token)
    return resultado


def normalize(text):
    text = manejar_contradicciones(text)
    text = remove_urls(text)
    text = remove_mentions(text)
    text = convert_emojis_to_words(text)
    text = tokenize(text)
    text = to_lowercase(text)
    text = remove_stopwords(text)
    text = replace_number(text)
    text = remove_punctuation(text)
    text = lemmatize_verbs(text)
    text = manejar_negaciones(text)
    return ' '.join(text)

