from util import import_dataset
from wordcloud import WordCloud
import seaborn as sns
from collections import Counter
from util import import_dataset
import matplotlib.pyplot as plt
import config as cfg

dataset  = import_dataset(cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH) 

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
