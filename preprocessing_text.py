import nltk
from nltk.corpus import stopwords
from num2words import num2words
import re
import emoji
import spacy
import stanza

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#nlp = spacy.load("es_core_news_sm")

#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('punkt_tab')

#stanza.download('es')
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

# Lista de stopwords importantes que queremos conservar
stopwords_importantes = {
    "no", "muy", "realmente", "bastante", "también", "si", "como", "tan", "porque", "cuando", "quiero",
    "me", "te", "estoy", "estaba", "esto", "este", "ese", "aquí", "allí", "más", "lo", "quién", "algo",
    "todo", "poco", "nada", "tal","sin"
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
            if word.upos in ["VERB", "AUX", "NOUN", "ADJ", "ADV"]:
                lemmatized_tokens.append(word.lemma if word.lemma else word.text)
            else:
                lemmatized_tokens.append(word.text)
    return lemmatized_tokens

def tokenize_and_lemmatize(text):
    doc = nlp(text)
    tokens = []
    for sentence in doc.sentences:
        for word in sentence.words:
            lemma = word.lemma if word.lemma else word.text
            tokens.append(lemma.lower())
    return tokens

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

def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticonos
                           u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas
                           u"\U0001F680-\U0001F6FF"  # transporte y mapas
                           u"\U0001F1E0-\U0001F1FF"  # banderas
                           u"\U00002500-\U00002BEF"  # símbolos chinos
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # marcas de variación
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def manage_negations(tokens, window=2):
    negations = {"no", "nunca", "jamás", "sin"}
    result = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in negations:
            result.append(token)
            for j in range(1, window + 1):
                if i + j < len(tokens):
                    result.append("NOT_" + tokens[i + j])
            i += window + 1
        else:
            result.append(token)
            i += 1
    return result

def normalize(text):
    text = manejar_contradicciones(text)
    text = remove_urls(text)
    text = remove_mentions(text)
    text = convert_emojis_to_words(text)
    #text = replace_number(text)

    tokens  = tokenize_and_lemmatize(text)
    tokens  = remove_stopwords(tokens )
    tokens  = replace_number(tokens )
    tokens  = remove_punctuation(tokens )
    tokens  = manage_negations(tokens )
    return ' '.join(tokens )