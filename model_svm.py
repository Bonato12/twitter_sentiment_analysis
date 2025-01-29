from sklearn import svm
from util import show_data_evaluation
from features_tf_idf import X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf
from features_tf_idf import vectorizer
from preprocessing_text import normalize

def svm_():
    print("<------SVM------->")
    model = svm.SVC(kernel='linear')
    model.fit(X_train_tfidf, y_train_tfidf) 
    yprediction = model.predict(X_test_tfidf) 
    show_data_evaluation(y_test_tfidf, yprediction)    
    return model


def evaluate_multiple_tweets_sentiment(tweets):
    model = svm_()
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


tweets = [
"Que no nos goleen tiene nombre y apellido: Rodrigo Rey Qué pedazo de hombre hermano...",
"Independiente está en partido exclusivamente por Rodrigo Rey",
"Gracias por jugar para #Independiente, Rodrigo Rey",
"rodrigo rey es el mejor arquero del fútbol argentino hoy por hoy",
"Gracias a dios existe Rodrigo Rey 🙏🏻",
"todos los días me despierto y apenas abro los ojos le agradezco a dios que Rodrigo Rey sea el arquero de este glorioso club.",
"Que pedazo de arquero rodrigo rey",
"TODO DE RODRIGO REY, EL MEJOR ARQUERO DE ARGENTINA",
"TE AMO RODRIGO REY",
"Señor arquero, Rodrigo Rey.",
"Rodrigo Rey es un animal. Es arquero de equipo grande. Gana partidos.",
"rodrigo rey el amor de mi vida",
"rodrigo rey mi único héroe en este lío",
"Si no existieras te inventaría, Rodrigo Rey",
"Rodrigo Rey siempre está.",
"QUE HOMBRE RODRIGO REY",
]

clean_tweets = [normalize(tweet) for tweet in tweets]
resultado = evaluate_multiple_tweets_sentiment(tweets)
print(f"Porcentaje de tweets positivos: {resultado['Positivos']}%")
print(f"Porcentaje de tweets negativos: {resultado['Negativos']}%")
    



