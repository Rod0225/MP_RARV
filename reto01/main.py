import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from collections import Counter
import random

import pickle
from sklearn.tree import DecisionTreeClassifier


def clasificador_humano_v2(bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g):

    votos = []

    x1, y1 = 37.5, 15
    x2, y2 = 47.5, 20
    m1 = (y2 - y1) / (x2 - x1)

    x3, y3 = 35, 13
    x4, y4 = 55, 18.5
    m2 = (y4 - y3) / (x4 - x3)

    y_recta1 = m1 * (bill_length_mm - x1) + y1
    y_recta2 = m2 * (bill_length_mm - x3) + y3

    if bill_depth_mm > y_recta1:
        votos.append("Adelie")
    elif bill_depth_mm < y_recta2:
        votos.append("Gentoo")
    else:
        votos.append("Chinstrap")

    if flipper_length_mm > 205:
        votos.append("Gentoo")
    elif bill_depth_mm > 0.5 * bill_length_mm - 4:
        votos.append("Adelie")
    else:
        votos.append("Chinstrap")

    if flipper_length_mm > 210:
        votos.append("Gentoo")
    elif bill_length_mm > 45:
        votos.append("Chinstrap")
    else:
        votos.append("Adelie")

    conteo = Counter(votos)
    max_votos = max(conteo.values())

    candidatos = [k for k, v in conteo.items() if v == max_votos]

    if len(candidatos) > 1:
        return votos[0]

    return candidatos[0]


def main():

    if len(sys.argv) < 2:
        print("Uso: python clasificar_penguins.py datos.csv")
        sys.exit()

    archivo_csv = sys.argv[1]

    df = pd.read_csv(archivo_csv)

    # cargar modelo entrenado
    with open("modelo_penguins.pkl", "rb") as f:
        modelo_ml = pickle.load(f)

    # características
    X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

    # predicción máquina
    pred_maquina = modelo_ml.predict(X)

    # predicción humano
    pred_humano = []

    for _, row in df.iterrows():
        pred = clasificador_humano_v2(
            row['bill_length_mm'],
            row['bill_depth_mm'],
            row['flipper_length_mm'],
            row['body_mass_g']
        )
        pred_humano.append(pred)

    resultado = pd.DataFrame({
        "Humano": pred_humano,
        "Maquina": pred_maquina
    })

    resultado.to_csv("clasificaciones.csv", index=False)

    print("Clasificación completada")
    print("Archivo generado: clasificaciones.csv")


if __name__ == "__main__":
    main()