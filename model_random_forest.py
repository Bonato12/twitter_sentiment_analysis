from sklearn.ensemble import RandomForestClassifier
from util import show_data_evaluation
from features_tf_idf import vectorizer
from sklearn.model_selection import GridSearchCV
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf

def random_forest():
    print("<------RANDOM FOREST------->")
    model = RandomForestClassifier()
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction) 
    return model

def random_forest_adjs():
    print("<------RANDOM FOREST AJD------->")
    model = RandomForestClassifier()
    param_grid = {
        'n_estimators': [100, 200, 2000],
        'max_depth': [10, 20, 300],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=2)
    grid_search.fit(X_train_tfidf, y_train_tfidf)
    best_model = grid_search.best_estimator_
    
    yprediction = best_model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction)
    return best_model

def evaluate_tweets_sentiment(tweets):
    model = random_forest()
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
