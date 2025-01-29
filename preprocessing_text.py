import nltk
from nltk.corpus import stopwords
from num2words import num2words
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd


# Asegurarnos que nltk esté descargado
nltk.download('stopwords')
nltk.download('punkt')


stopwords_importantes = set([
    "no",           # Negaciones
    "muy",          # Intensificadores
    "realmente",    # Intensificadores
    "bastante",     # Intensificadores
    "también",      # Relacionadores
    "si",           # Condiciones
    "como",         # Comparaciones
    "tan",          # Intensificadores
    "porque",       # Causas
    "cuando",       # Tiempo
    "quiero",       # Verbo importante en sentimiento
    "me",           # Pronombres
    "te",           # Pronombres
    "estoy",        # Verbo relacionado con estado emocional
    "estaba",       # Verbo relacionado con estado emocional
    "esto",         # Pronombre demostrativo
    "este",         # Pronombre demostrativo
    "ese",          # Pronombre demostrativo
    "aquí",         # Relación de lugar
    "allí",         # Relación de lugar
    "más",          # Intensificador
    "lo",           # Pronombres
    "muy",          # Intensificadores
    "quién",        # Preguntas que podrían identificar opiniones
    "algo",         # Palabras clave relacionadas con lo desconocido
    "todo",         # Generalización
    "poco",         # Cantidad
    "nada",         # Negaciones fuertes
    "tal",          # Relaciona de manera contextual
    "también",      # Relacionadores
])



def reemplazar_urls(texto):
    texto_limpio = re.sub(r'http[s]?://\S+|www\.\S+', '', texto)
    return texto_limpio

# Función de tokenización
def tokenizar_con_urls(texto):
    texto = reemplazar_urls(texto)
    return texto



# Función para tokenizar
def tokenize(words):  
    return nltk.word_tokenize(words)

# Función para convertir a minúsculas
def to_lowercase(words):
    return [word.lower() for word in words]

def eliminar_stopwords(tokens):
    # Obtener las stopwords en español desde nltk
    stop_words = set(stopwords.words('spanish'))
    # Filtrar los tokens que no sean stopwords, pero manteniendo las palabras importantes
    return [token for token in tokens if token not in stop_words or token in stopwords_importantes]


def eliminar_urls(tokens):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    tokens_sin_urls = [token for token in tokens if not url_pattern.match(token)]
    return tokens_sin_urls

# Función para lematizar verbos
def lemmatize_verbs(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos='v') for word in words]

# Función para reemplazar números por palabras
def replace_number(words):
    return [num2words(word, lang='en') if word.isdigit() else word for word in words]

# Función para eliminar puntuación
def remove_punctuation(words):
    return [re.sub(r'[^\w\s]', '', word) for word in words]

# Función para normalizar texto
def normalize(text):
    text1 =  tokenizar_con_urls(text)
    words = tokenize(text1)            # Tokeniza el texto
    words = to_lowercase(words)       # Convierte todo a minúsculas
    words = eliminar_stopwords(words)  # Elimina stopwords
    words = remove_punctuation(words) # Elimina puntuación
    #words = lemmatize_verbs(words)    # Lematiza las palabras (opcional)
    return ' '.join(words)            # Devuelve el texto limpio

