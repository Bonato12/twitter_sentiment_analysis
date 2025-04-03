from util import import_dataset
from util import import_dataset,export_dataset
import config as cfg
import numpy as np

def generate_dataset_muestra():
    input = cfg.DATASET_ES_PATH
    dataset  = import_dataset(input) 
    dataset = dataset[['label', 'tweet']]
    dataset = dataset[dataset['label'].notnull()] 
    dataset['id'] = np.random.randint(10000000, 20000000, size=len(dataset))
    dataset = dataset[['id','label', 'tweet']]
    dataset['label'] = dataset['label'].apply(lambda x: int(x)) 
    print(dataset['label'].dtype)
    export_dataset(dataset,cfg.DATASET_ES_MUESTRA_PATH)
    print("Fin")

def get_dataset():
    train_dataset  = import_dataset(cfg.DATASET_ES_PATH) 
    return train_dataset

def get_dataset_muestra():
    train_dataset  = import_dataset(cfg.DATASET_ES_MUESTRA_PATH) 
    return train_dataset

def get_dataset_preprocessed():
    train_dataset  = import_dataset(cfg.DATASET_ES_MUESTRA_PREPROCESSED_PATH) 
    return train_dataset

def get_dataset_response():
    response  = import_dataset(cfg.DATASET_RESPONSE) 
    return response

def get_dataset_response_preprocessed():
    response  = import_dataset(cfg.DATASET_RESPONSE_PREPROCESSED_PATH) 
    return response
    
generate_dataset_muestra()