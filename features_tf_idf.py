from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split
from generate_dataset import get_dataset_preprocessed

train_dataset = get_dataset_preprocessed()

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(train_dataset['clean_tweet'].values.astype('U'))
x = tfidf_vectorizer.transform(train_dataset['clean_tweet'].values.astype('U'))
y = train_dataset['label']

X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf = train_test_split(x , y, test_size=0.20, random_state=42)

print('Training Data :', X_train_tfidf.shape)
print('Testing Data : ', X_test_tfidf.shape)

def vectorizer(max_features=5000):
    df = get_dataset_preprocessed()
    vectorizer = TfidfVectorizer(max_features=5000, max_df=0.85)
    vectorizer.fit(df['clean_tweet'].values.astype('U'))
    return vectorizer
