from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
from util import import_dataset
import config as cfg


#https://myscale.com/blog/text-analysis-tf-idf-vs-bag-of-words/

#Bag-of-Words Features
def preprocess_bow(max_features=5000, test_size=0.2, random_state=42):
    train_dataset  = import_dataset(cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH) 

    bow_vectorizer = CountVectorizer(max_features=max_features)    
    bow = bow_vectorizer.fit_transform(train_dataset['clean_tweet'].values.astype('U'))  # Asegúrate de que 'clean_tweet' esté presente en el dataset
    train_bow = bow
    
    # Dividir los datos en entrenamiento y validación
    xtrain_bow, xvalid_bow, ytrain, yvalid = train_test_split(train_bow, train_dataset['label'], random_state=random_state, test_size=test_size)

    print('Training Data :', xtrain_bow.shape)
    print('Testing Data : ', xvalid_bow.shape)
    
    return xtrain_bow, xvalid_bow, ytrain, yvalid


