from util import import_dataset
from util import import_dataset,export_dataset
import config as cfg
import numpy as np

def generate_dataset_muestra():
    input = cfg.DATASET_ES_PATH
    dataset  = import_dataset(input) 
    dataset = dataset[['label', 'tweet']]
    dataset = dataset[dataset['label'].notnull()]  # Elimina valores nulos
    dataset['id'] = np.random.randint(10000000, 20000000, size=len(dataset))  # Genera números aleatorios entre 1 y 100
    dataset = dataset[['id','label', 'tweet']]
    dataset['label'] = dataset['label'].apply(lambda x: int(x))  # Convertir todo explícitamente a entero
    print(dataset['label'].dtype)
    export_dataset(dataset,cfg.DATASET_ES_MUESTRA_PATH)
    print("Fin")

def get_dataset():
    train_dataset  = import_dataset(cfg.DATASET_ES_PATH) 
    return train_dataset

def get_dataset_preprocessed():
    train_dataset  = import_dataset(cfg.DATASET_ES_MUESTRA_PREPROCESSED_PATH) 
    return train_dataset
    

