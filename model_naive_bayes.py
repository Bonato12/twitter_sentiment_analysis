from sklearn.naive_bayes import BernoulliNB
from util import show_data_evaluation
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def naive_bayes():
    print("<------NAIVE BAYES------->")
    model = BernoulliNB() 
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf)
    show_data_evaluation(y_test_tfidf, yprediction) 
    return model
