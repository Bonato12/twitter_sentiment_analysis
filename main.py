from generate_dataset import export_dataset_drive,generate_dataset_muestra
from preprocessing_dataset import preprocessing_dataset
from model_logistic_regression import logistic_regression
from model_random_forest import random_forest
from model_naive_bayes import naive_bayes
from model_svm import svm_
from model_vader import vader

def main():
    export_dataset_drive()
    generate_dataset_muestra()
    #get_info()
    preprocessing_dataset()
    naive_bayes()
    logistic_regression()
    random_forest()
    svm_()
    vader()

if __name__ == "__main__":
    main()    

