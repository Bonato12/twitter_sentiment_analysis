from util import export_dataset
from preprocessing_text import normalize
import config as cfg
from generate_dataset import get_dataset_muestra


def preprocessing_dataset():
    dataset  = get_dataset_muestra() 
    dataset['clean_tweet'] = dataset['tweet'].apply(normalize)
    dataset = dataset[dataset['clean_tweet'].notnull()]  # Elimina valores nulos
    dataset = dataset[dataset['clean_tweet'].str.strip() != '']  # Elimina cadenas vacías
    export_dataset(dataset,cfg.DATASET_ES_MUESTRA_PREPROCESSED_PATH)
    print("Fin")


preprocessing_dataset()