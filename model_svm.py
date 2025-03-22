from sklearn import svm
from util import show_data_evaluation
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf
from features_tf_idf import vectorizer
from sklearn.model_selection import GridSearchCV
from preprocessing_text import normalize

def svm_():
    print("<------SVM------->")
    model = svm.SVC(kernel='linear')
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf) 
    show_data_evaluation(y_test_tfidf, yprediction)    
    return model

def svm_regression_adjustment():
    model = svm.SVC(kernel='linear')

    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
        'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
        'degree': [3, 4, 5],
        'coef0': [0.0, 0.1, 0.5, 1.0],
        'decision_function_shape': ['ovr', 'ovo']
    }

    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)
    grid_search.fit(X_train_tfidf, y_train_tfidf)
    print("Mejores parámetros:", grid_search.best_params_)
    yprediction = grid_search.best_estimator_.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction)
    return grid_search.best_estimator_

def evaluate_tweets_sentiment(tweets):
    model = svm_()
    positive_count = 0
    negative_count = 0
    
    for tweet in tweets:
        tweet_normalize = normalize(tweet,True,True)
        tweet_transformed = vectorizer().transform([tweet_normalize]).toarray()
        prediction = model.predict(tweet_transformed)
        
        if prediction == 1:
            print(tweet+"-->Positivo")
            positive_count += 1
        else:
            print(tweet +"--->Negativo")
            negative_count += 1
    print("Cantidad de Tweets Positivos: ")
    print(positive_count)     
    print("Cantidad de Tweets Negativos: ")
    print(negative_count)    
    


tweets = [
    "Falta perder contra el River este que es igual de malo que nosotros",
    "Falta que reviva al muerto de Gallardo (si es que llega)",
    "Ruso Zielinski y Costas.",
    "También perdió contra Chiqui Bouzat y casi pierde de local contra el Ogro Fabbiani",
    "Gago es el fracaso hecho persona, en todos los partidos importantes pierde, hasta como jugador",
    "Gago es un hijo de puta",
    "Y no le pudo hacer un gol al Cali Izquierdoz y al Káiser Zambrano."
]


evaluate_tweets_sentiment(tweets)