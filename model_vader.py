from nltk.sentiment.vader import SentimentIntensityAnalyzer
from util import show_data_evaluation
from util import import_dataset
import config as cfg

#Para hacer VADER
#https://hex.tech/templates/sentiment-analysis/vader-sentiment-analysis/
#https://www.kaggle.com/code/infinator/sentiment-analysis-vader-twitter-data
# Create an instance of SentimentIntensityAnalyzer
#https://www.kaggle.com/code/keitazoumana/social-media-sentiment-analysis-with-vader

model = SentimentIntensityAnalyzer()

def format_output(score):
    polarity = 0
    if(score['compound']>= 0.05):
        polarity = 1
    elif(score['compound']<= -0.05):
        polarity = 0
    return polarity

def predict_sentiment(text):
    score =  model.polarity_scores(str(text))
    return format_output(score)

def vader():
    data = import_dataset(cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH)
    data["vader_prediction"] = data["clean_tweet"].apply(predict_sentiment)
    show_data_evaluation(data['label'], data["vader_prediction"])
