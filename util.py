from sklearn.metrics import classification_report, accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import pandas as pd 

def show_data_evaluation(yvalid,yprediction):
    f1 = f1_score(yvalid, yprediction)
    accuracy = accuracy_score(yvalid, yprediction)
    recall = recall_score(yvalid, yprediction)
    precision = precision_score(yvalid, yprediction)
    print("f1-Score: {}\n".format(round(f1,3)))
    print("Accuracy: {}\n".format(round(accuracy,3)))
    print("Recall  {}\n".format(round(recall,3)))
    print("Presicion  {}\n".format(round(precision,3)))
    print("Confusion Matrix : ")
    print(confusion_matrix(yvalid,yprediction))
    print(classification_report(yvalid, yprediction))

def import_dataset(path):
    return pd.read_csv(path,encoding='ISO-8859-1')

def export_dataset(dataset,path):
    dataset.to_csv(path,index=False)