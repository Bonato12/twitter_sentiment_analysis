from sklearn.ensemble import RandomForestClassifier
from util import show_data_evaluation
from features_tf_idf import preprocess_tfidf,vectorizer

def random_forest():
    X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf= preprocess_tfidf()
    model = RandomForestClassifier()
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction) 
    return model

def evaluate_tweet_sentiment(tweet):
    rf = random_forest()
    tweet_transformed = vectorizer().transform([tweet]).toarray() 
    prediction = rf.predict(tweet_transformed)
    if prediction == 1:
        return "Positivo"
    else:
        return "Negativo"
    
