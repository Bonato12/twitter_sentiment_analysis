from util import import_dataset
from wordcloud import WordCloud
import seaborn as sns
from collections import Counter
from util import import_dataset
import matplotlib.pyplot as plt
import config as cfg
import pandas as pd
from  generate_dataset import get_dataset_muestra

dataset  = get_dataset_muestra()

def get_info():
    print("Cantidad Originales de Tweets: ")
    print(len(dataset))

    print("Cantidad de Tweets Positivos")
    print((dataset['label'] == 1).sum())

    print("Cantidad Originales de Tweets: ")
    print(len(dataset))

    print("Cantidad de Tweets Positivos")
    print((dataset['label'] == 1).sum())

    print("Cantidad de Tweets Negativos")
    print((dataset['label'] == 0).sum())

    print("Cantidad de Tweets Neutrales")
    print((dataset['label'] == 2).sum())
    show_label_tweet()
    show_count_words_frequency()

def show_label_tweet():
    plt.figure(figsize=(8, 6))
    sns.countplot(data=dataset, x='label', palette='viridis')
    plt.title('Polaridad de los tweets')
    plt.xlabel('Polaridad')
    plt.ylabel('Número de tweets')
    plt.show()

def show_count_words_frequency():
    all_text = ' '.join(dataset['clean_tweet']).lower()
    words = all_text.split()
    word_counts = Counter(words)
    top_words = dict(word_counts.most_common(100))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('100 Palabras Más Frecuentes')
    plt.show()

def show_count_words_frequency(dataset):
    positive_tweets = dataset[dataset['label'] == 1]['clean_tweet']
    negative_tweets = dataset[dataset['label'] == 0]['clean_tweet']
    positive_text = ' '.join(positive_tweets).lower()
    negative_text = ' '.join(negative_tweets).lower()
    positive_words = positive_text.split()
    negative_words = negative_text.split()
    positive_word_counts = Counter(positive_words)
    negative_word_counts = Counter(negative_words)
    top_positive_words = dict(positive_word_counts.most_common(100))
    top_negative_words = dict(negative_word_counts.most_common(100))
    positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_positive_words)
    negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_negative_words)
    # Mostrar las nubes de palabras
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(positive_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('100 Palabras Más Frecuentes en Tweets Positivos')
    plt.subplot(1, 2, 2)
    plt.imshow(negative_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('100 Palabras Más Frecuentes en Tweets Negativos')
    plt.tight_layout()
    plt.show()

def results():

    data = {
    "Model": ["NAIVE BAYES", "LOGISTIC REGRESSION", "RANDOM FOREST", "SVM", "VADER"],
    "f1-Score": [0.763, 0.784, 0.754, 0.779, 0.645],
    "Accuracy": [0.761, 0.782, 0.759, 0.778, 0.655],
    "Recall": [0.776, 0.795, 0.743, 0.789, 0.628],
    "Precision": [0.751, 0.772, 0.764, 0.769, 0.664]
    }

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Establecer la figura para el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graficar los valores de cada métrica
    df.set_index("Model")[["f1-Score", "Accuracy", "Recall", "Precision"]].plot(kind='bar', ax=ax)

    # Personalizar el gráfico
    plt.title("Comparison of Model Metrics")
    plt.ylabel("Scores")
    plt.xlabel("Models")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Añadir los valores encima de las barras
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.3f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    xytext=(0, 5),  # distancia para evitar que el texto se superponga con la barra
                    textcoords='offset points', 
                    ha='center', va='bottom')

    # Mostrar el gráfico
    plt.show()


results()    