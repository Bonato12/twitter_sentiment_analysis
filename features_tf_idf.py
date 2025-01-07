from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split
from util import import_dataset
import config as cfg

#TF-IDF Features
def preprocess_tfidf(max_features=5000, test_size=0.2):
    train_dataset = import_dataset(cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH) 
    tfidf_vectorizer = vectorizer()
    
    tweet = tfidf_vectorizer.fit_transform(train_dataset['clean_tweet'].values.astype('U')).toarray()
    label = train_dataset['label']
    
    X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf = train_test_split(tweet, label, test_size=test_size, random_state=42)

    print('Training Data :', X_train_tfidf.shape)
    print('Testing Data : ', X_test_tfidf.shape)

    return X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf


def vectorizer(max_features=5000):
    df = import_dataset(cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH) 
    vectorizer = TfidfVectorizer(max_features=max_features)
    vectorizer.fit(df['clean_tweet'].values.astype('U'))
    return vectorizer
