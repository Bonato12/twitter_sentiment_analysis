from sklearn import svm
from util import show_data_evaluation
from features_tf_idf import preprocess_tfidf

def svm_():
    print("<------SVM------->")
    X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf = preprocess_tfidf()
    model = svm.SVC(kernel='linear')
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf) 
    show_data_evaluation(y_test_tfidf, yprediction)    
    return model
