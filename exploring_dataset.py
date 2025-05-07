# --- IMPORTACIONES ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import emoji
import re
import matplotlib.pyplot as plt
import numpy as np

from util import import_dataset
from generate_dataset import get_dataset_muestra, get_dataset_preprocessed
import config as cfg

# --- DESCARGA DE RECURSOS NLTK ---
nltk.download('stopwords')
nltk.download('punkt')
dataset = get_dataset_muestra()
stop_words = set(stopwords.words('spanish'))


def get_info():
    print("Cantidad Originales de Tweets:", len(dataset))
    print("Cantidad de Tweets Positivos:", (dataset['label'] == 1).sum())
    print("Cantidad de Tweets Negativos:", (dataset['label'] == 0).sum())
    print("Cantidad de Tweets Neutrales:", (dataset['label'] == 2).sum())

    show_label_tweet()
    show_count_words_frequency()
    show_positive_wordcloud()
    show_negative_wordcloud()
    show_positive_wordcloud_no_stopword()
    show_negative_wordcloud_no_stopword()
    analizar_elementos_tweet()

def show_label_tweet():
    plt.figure(figsize=(8, 6))
    sns.countplot(data=dataset, x='label', palette='viridis')
    plt.title('Polaridad de los tweets')
    plt.xlabel('Polaridad')
    plt.ylabel('Número de tweets')
    plt.show()

def show_count_words_frequency():
    all_text = ' '.join(dataset['tweet']).lower()
    words = all_text.split()
    word_counts = Counter(words)
    top_words = dict(word_counts.most_common(100))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('100 Palabras Más Frecuentes')
    plt.show()

def generate_wordcloud_from_label(label_value, title, remove_stopwords=False):
    tweets = dataset[dataset['label'] == label_value]['tweet']
    text = ' '.join(tweets).lower()
    words = text.split()

    if remove_stopwords:
        words = [word for word in words if word not in stop_words]

    word_counts = Counter(words)
    top_words = dict(word_counts.most_common(100))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words)

    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def show_positive_wordcloud():
    generate_wordcloud_from_label(1, '100 Palabras Más Frecuentes en Tweets Positivos')

def show_negative_wordcloud():
    generate_wordcloud_from_label(0, '100 Palabras Más Frecuentes en Tweets Negativos')

def show_positive_wordcloud_no_stopword():
    generate_wordcloud_from_label(1, '100 Palabras Más Frecuentes en Tweets Positivos', remove_stopwords=True)

def show_negative_wordcloud_no_stopword():
    generate_wordcloud_from_label(0, '100 Palabras Más Frecuentes en Tweets Negativos', remove_stopwords=True)

# --- MÉTRICAS DE MODELOS ---

def results():
    data = {
        "Model": ["NAIVE BAYES", "LOGISTIC REGRESSION", "RANDOM FOREST", "SVM"],
        "f1-Score": [0.763, 0.784, 0.754, 0.779],
        "Accuracy": [0.761, 0.782, 0.759, 0.778],
        "Recall": [0.776, 0.795, 0.743, 0.789],
        "Precision": [0.751, 0.772, 0.764, 0.769]
    }

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    df.set_index("Model")[["f1-Score", "Accuracy", "Recall", "Precision"]].plot(kind='bar', ax=ax)

    plt.title("Comparison of Model Metrics")
    plt.ylabel("Scores")
    plt.xlabel("Models")
    plt.xticks(rotation=45)
    plt.tight_layout()

    for p in ax.patches:
        ax.annotate(f'{p.get_height():.3f}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    xytext=(0, 5),
                    textcoords='offset points',
                    ha='center', va='bottom')

    plt.show()

# --- FUNCIONES DE CONTEO LÉXICO Y SÍMBOLOS ---

def contar_stopwords(texto):
    palabras = word_tokenize(str(texto).lower())
    return sum(1 for palabra in palabras if palabra in stop_words)

def contar_emojis(texto):
    return len([c for c in str(texto) if c in emoji.EMOJI_DATA])

def contar_numeros(texto):
    return len(re.findall(r'\b\d+\b', str(texto)))

def contar_menciones(texto):
    return len(re.findall(r'@\w+', str(texto)))

def contar_urls(texto):
    return len(re.findall(r'(https?://\S+|www\.\S+)', str(texto)))

def contar_palabras_limpias(texto):
    texto = re.sub(r'@\w+|#\w+|https?://\S+|www\.\S+|\b\d+\b', '', str(texto))
    palabras = re.findall(r'\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', texto)
    return len(palabras)

# --- FUNCIONES PARA MAYÚSCULAS / MINÚSCULAS / MIXTAS ---

def limpiar_texto(texto):
    return re.sub(r'@\w+|#\w+|https?://\S+|www\.\S+', '', str(texto))

def contar_mayusculas(texto):
    texto = limpiar_texto(texto)
    return len(re.findall(r'\b[A-ZÁÉÍÓÚÜÑ]{2,}\b', texto))

def contar_minusculas(texto):
    texto = limpiar_texto(texto)
    return len(re.findall(r'\b[a-záéíóúüñ]{2,}\b', texto))

def contar_mixtas(texto):
    texto = limpiar_texto(texto)
    palabras = re.findall(r'\b\w+\b', texto)
    return len([p for p in palabras if not p.islower() and not p.isupper()])

# --- APLICACIÓN AL DATASET ---

def analizar_elementos_tweet():
    # Aplicación de funciones de conteo al dataset
    dataset['stopwords'] = dataset['tweet'].apply(contar_stopwords)
    dataset['emoji_count'] = dataset['tweet'].apply(contar_emojis)
    dataset['menciones_count'] = dataset['tweet'].apply(contar_menciones)
    dataset['url_count'] = dataset['tweet'].apply(contar_urls)
    dataset['numeros_count'] = dataset['tweet'].apply(contar_numeros)
    dataset['hashtag_count'] = dataset['tweet'].astype(str).str.count(r'#')
    dataset['word_count'] = dataset['tweet'].apply(contar_palabras_limpias)
    dataset['mayusculas_count'] = dataset['tweet'].apply(contar_mayusculas)
    dataset['minusculas_count'] = dataset['tweet'].apply(contar_minusculas)
    dataset['mixtas_count'] = dataset['tweet'].apply(contar_mixtas)

    # Cálculo de totales
    elementos_especiales_total = (
        dataset['menciones_count'].sum() +
        dataset['hashtag_count'].sum() +
        dataset['url_count'].sum()
    )

    totales = {
        'Emojis': dataset['emoji_count'].sum(),
        'Números': dataset['numeros_count'].sum(),
        'Elementos Especiales': elementos_especiales_total,
        'Stopwords': dataset['stopwords'].sum(),
        #'Palabras mixtas': dataset['mixtas_count'].sum(),
        #'Palabras en minúsculas': dataset['minusculas_count'].sum(),
        #'Palabras en mayúsculas': dataset['mayusculas_count'].sum(),
        'Palabras': dataset['word_count'].sum()
    }

    # Visualización
    plt.figure(figsize=(6, 3))
    bars = plt.barh(list(totales.keys()), list(totales.values()), color='skyblue')
    plt.xlabel('')
    plt.title('')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 5, bar.get_y() + bar.get_height() / 2, str(int(width)), va='center')

    plt.tight_layout()
    plt.show()


def graficar_accuracy():
    # Nombres de los modelos
    modelos = ['Naive Bayes', 'Logistic Regression', 'Random Forest', 'SVM']
    
    # Métricas
    accuracy = [0.917, 0.903, 0.88, 0.932]
    f1_score = [0.925, 0.917, 0.885, 0.939]

    # Posiciones
    x = np.arange(len(modelos))
    width = 0.35

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, accuracy, width, label='Accuracy', color='skyblue')
    ax.bar(x + width/2, f1_score, width, label='F1-Score', color='salmon')

    # Etiquetas y formato
    ax.set_ylabel('Puntaje')
    ax.set_title('Comparación de Accuracy y F1-Score por Modelo')
    ax.set_xticks(x)
    ax.set_xticklabels(modelos)
    ax.set_ylim([0.85, 1.0])
    ax.legend()

    # Mostrar valores encima de las barras
    for valores, offset in zip([accuracy, f1_score], [-width/2, width/2]):
        for i in range(len(modelos)):
            yval = valores[i]
            ax.text(x[i] + offset, yval + 0.005, f'{yval:.3f}', 
                    ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()

def graficar_accuracy_svm():
    # Nombre del modelo
    modelos = ['SVM']
    
    # Métricas de SVM
    accuracy = [0.932]
    f1_score = [0.939]

    # Posición
    x = np.arange(len(modelos))
    width = 0.35

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.bar(x - width/2, accuracy, width, label='Accuracy', color='skyblue')
    ax.bar(x + width/2, f1_score, width, label='F1-Score', color='salmon')

    # Etiquetas y formato
    ax.set_ylabel('Puntaje')
    ax.set_title('Métricas del Modelo SVM')
    ax.set_xticks(x)
    ax.set_xticklabels(modelos)
    ax.set_ylim([0.9, 1.0])
    ax.legend()

    # Mostrar valores encima de las barras
    for valores, offset in zip([accuracy, f1_score], [-width/2, width/2]):
        for i in range(len(modelos)):
            yval = valores[i]
            ax.text(x[i] + offset, yval + 0.003, f'{yval:.3f}', 
                    ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()


def show_count_words_frequency_sin_stopwords():
    stop_words = set(stopwords.words('spanish'))
    all_text = ' '.join(dataset['tweet']).lower()
    words = all_text.split()
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    word_counts = Counter(filtered_words)
    top_words = dict(word_counts.most_common(100))
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('100 Palabras Más Frecuentes')
    plt.show()






show_count_words_frequency_sin_stopwords()
show_positive_wordcloud_no_stopword()
show_negative_wordcloud_no_stopword()