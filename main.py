from generate_dataset import generate_dataset_muestra
from preprocessing_dataset import preprocessing_dataset
from model_logistic_regression import logistic_regression
from model_random_forest import random_forest
from model_naive_bayes import naive_bayes
from model_svm import svm_,evaluate_tweets_sentiment
from preprocessing_text import normalize

#from model_vader import vader

def main():
    generate_dataset_muestra()
    preprocessing_dataset()
    naive_bayes()
    logistic_regression()
    random_forest()
    svm_()


def execute_sentinemt_analysis():
    tweets = []
    clean_tweets = [normalize(tweet) for tweet in tweets]
    resultado = evaluate_tweets_sentiment(clean_tweets)
    print(f"Porcentaje de tweets positivos: {resultado['Positivos']}%")
    print(f"Porcentaje de tweets negativos: {resultado['Negativos']}%")
    


if __name__ == "__main__":
    main()    
    execute_sentinemt_analysis()
