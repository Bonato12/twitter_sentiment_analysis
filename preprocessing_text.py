import nltk
from nltk.corpus import stopwords
from num2words import num2words
from nltk.stem import WordNetLemmatizer
import re

# Diccionario de contracciones en inglés
contractions_dict = {
    "ain't": "am not", "aren't": "are not", "can't": "cannot", "could've": "could have", 
    "couldn't": "could not", "didn't": "did not", "doesn't": "does not", "don't": "do not", 
    "hadn't": "had not", "haven't": "have not", "he'd": "he would", "he'll": "he will", 
    "he's": "he is", "how'd": "how did", "how'll": "how will", "how's": "how is", 
    "I'd": "I would", "I'll": "I will", "I'm": "I am", "I've": "I have", "isn't": "is not", 
    "it'd": "it would", "it'll": "it will", "it's": "it is", "let's": "let us", "ma'am": "madam", 
    "might've": "might have", "mightn't": "might not", "must've": "must have", 
    "mustn't": "must not", "needn't": "need not", "she'd": "she would", "she'll": "she will", 
    "she's": "she is", "should've": "should have", "shouldn't": "should not", "that'd": "that would", 
    "that's": "that is", "there'd": "there would", "there's": "there is", "they'd": "they would", 
    "they'll": "they will", "they're": "they are", "they've": "they have", "wasn't": "was not", 
    "weren't": "were not", "what'd": "what did", "what'll": "what will", "what's": "what is", 
    "what've": "what have", "where'd": "where did", "where'll": "where will", "where's": "where is", 
    "who'd": "who would", "who'll": "who will", "who's": "who is", "who've": "who have", 
    "why'd": "why did", "why'll": "why will", "why's": "why is", "won't": "will not", 
    "would've": "would have", "wouldn't": "would not"
}

# Función para expandir contracciones
def expand_contractions(text):
    expanded_text = []
    words = text.split()
    for word in words:
        if word.lower() in contractions_dict:
            expanded_text.append(contractions_dict[word.lower()])
        else:
            expanded_text.append(word)
    return ' '.join(expanded_text)

# Función para tokenizar
def tokenize(words):  
    return nltk.word_tokenize(words)

# Función para convertir a minúsculas
def to_lowercase(words):
    return [word.lower() for word in words]

# Función para eliminar stopwords
def remove_stopwords(words):
    stop_words = stopwords.words('english')
    return [word for word in words if word not in stop_words]

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
    text = expand_contractions(text)  # Expande contracciones primero
    words = tokenize(text)            # Tokeniza el texto
    words = to_lowercase(words)       # Convierte todo a minúsculas
    words = replace_number(words)     # Convierte los números a palabras
    #words = remove_stopwords(words)   # Elimina stopwords
    words = remove_punctuation(words) # Elimina puntuación
    #words = lemmatize_verbs(words)    # Lematiza las palabras
    return ' '.join(words)            # Devuelve el texto limpio

