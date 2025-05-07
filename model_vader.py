

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from util import show_data_evaluation
from util import import_dataset
import config as cfg
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


#Para hacer VADER
#https://hex.tech/templates/sentiment-analysis/vader-sentiment-analysis/
#https://www.kaggle.com/code/infinator/sentiment-analysis-vader-twitter-data
# Create an instance of SentimentIntensityAnalyzer
#https://www.kaggle.com/code/keitazoumana/social-media-sentiment-analysis-with-vader

model = SentimentIntensityAnalyzer()

def format_output(score):
    compound = score['compound']
    if compound >= 0.5:
        return 1  # Positivo
    else:
        return 0  # Negativo

def predict_sentiment(text):
    score =  model.polarity_scores(str(text))
    return format_output(score)

def vader():
    print("<------VADER------->")
    data = import_dataset(cfg.DATASET_ES_MUESTRA_PATH)
    data["vader_prediction"] = data["tweet"].apply(predict_sentiment)
    f1 = f1_score(data['label'], data["vader_prediction"], average='macro')  # Puedes probar 'micro' o 'weighted' dependiendo de tus necesidades
    print(f"F1 Score: {f1}")
    accuracy = accuracy_score(data['label'], data["vader_prediction"])
    print(f"Accuracy: {accuracy}")


vader()