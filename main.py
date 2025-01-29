from preprocessing_dataset import preprocessing_dataset_es
from model_logistic_regression import logistic_regression
from model_random_forest import random_forest
from model_naive_bayes import naive_bayes
from model_svm import svm_
#from model_vader import vader

def main():
    #preprocessing_dataset_es()
    naive_bayes()
    logistic_regression()
    random_forest()
    svm_()
    #vader()

if __name__ == "__main__":
    main()    

