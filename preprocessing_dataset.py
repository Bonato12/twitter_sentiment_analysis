from util import import_dataset,export_dataset
from preprocessing_text import normalize
import config as cfg

def preprocessing_dataset():
    input = cfg.DATASET_TRAIN_MUESTRA_PATH
    dataset  = import_dataset(input) 
    dataset['clean_tweet'] = dataset['tweet'].apply(normalize)
    dataset = dataset[dataset['clean_tweet'].notnull()]  # Elimina valores nulos
    dataset = dataset[dataset['clean_tweet'].str.strip() != '']  # Elimina cadenas vacías
    export_dataset(dataset,cfg.DATASET_TRAIN_MUESTRA_PREPROCESSED_PATH)
    print("Fin")
