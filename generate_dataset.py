from util import import_dataset
import pandas as pd
from util import import_dataset,export_dataset
import gdown
import config as cfg
import numpy as np

def export_dataset_drive():
    gdown.download(cfg.URL_DRIVE, cfg.DATASET_TRAIN_PATH, quiet=False)
    print("Archivo descargado exitosamente.")

def generate_dataset_muestra():
    df = import_dataset(cfg.DATASET_TRAIN_PATH) 
    df = procesar_columnas(df)
    df = obtener_muestra_balanceada(df,5000)
    df['label'] = df['label'].map({0: 0, 4: 1})
    export_dataset(df,cfg.DATASET_TRAIN_MUESTRA_PATH)
    print("Fin de la generacion de la muestra") 

def procesar_columnas(df):
    df.columns = ["label", "id", "date", "flag", "user", "tweet"]
    columnas_a_eliminar = ['flag', 'date', 'user']
    df = df.drop(columns=columnas_a_eliminar)
    return df

def obtener_muestra_balanceada(df, muestra_por_clase):
    tweets_positivos = df[df['label'] == 4]
    tweets_negativos = df[df['label'] == 0]
    muestra_positivos = tweets_positivos.sample(n=muestra_por_clase, random_state=42)
    muestra_negativos = tweets_negativos.sample(n=muestra_por_clase, random_state=42)
    muestra_final = pd.concat([muestra_positivos, muestra_negativos])
    muestra_final = muestra_final.sample(frac=1, random_state=42).reset_index(drop=True)
    return muestra_final

def generate_dataset_es_muestra():
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
    

generate_dataset_es_muestra()

