from sklearn.naive_bayes import BernoulliNB
from util import show_data_evaluation
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf,vectorizer

def naive_bayes():
    print("<------NAIVE BAYES------->")
    model = BernoulliNB() 
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction) 
    return model

def evaluate_tweets_sentiment(tweets):
    model = naive_bayes()
    positive_count = 0
    negative_count = 0
    for tweet in tweets:
        print(tweet)
        tweet_transformed = vectorizer().transform([tweet]).toarray()
        prediction = model.predict(tweet_transformed)
        
        if prediction == 1:
            print("Positivo")
            positive_count += 1
        else:
            print("Negativo")
            negative_count += 1
    
    total_tweets = len(tweets)
    positive_percentage = (positive_count / total_tweets) * 100
    negative_percentage = (negative_count / total_tweets) * 100
    
    return {
        "Positivos": positive_percentage,
        "Negativos": negative_percentage
    }