from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from util import show_data_evaluation
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf,vectorizer

def logistic_regression():
    print("<------LOGISTIC REGRESSION------->")
    model = LogisticRegression(max_iter=1000) 
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction) 
    return model

def logistic_regression_adjustment():
    model = LogisticRegression(solver='lbfgs', max_iter=1000)

    param_grid = {
        'C': [0.001, 0.01, 0.1, 1, 10],
        'penalty': ['l2', 'l1'],
        'solver': ['liblinear', 'lbfgs', 'saga'],
        'max_iter': [1000]
    }

    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)
    grid_search.fit(X_train_tfidf, y_train_tfidf)
    print("Mejores parámetros:", grid_search.best_params_)
    yprediction = grid_search.best_estimator_.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction)
    return grid_search.best_estimator_

def evaluate_tweets_sentiment(tweets):
    model = logistic_regression()
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
