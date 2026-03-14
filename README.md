# Clasificador de Pingüinos

## Descripción
Este repositorio contiene un script en Python que clasifica especies de pingüinos a partir de sus características físicas usando un modelo de Machine Learning previamente entrenado.

## Requisitos

Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

## Formato del archivo de entrada

El archivo CSV debe contener las siguientes columnas:

- bill_length_mm
- bill_depth_mm
- flipper_length_mm
- body_mass_g

Ejemplo de entrada:

```csv
bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g
39.1,18.7,181,3750
39.5,17.4,186,3800
40.3,18.0,195,3250
```

## Ejecución

```bash
python clasificador_pinguinos.py datos_entrada.csv
```

## Salida

El programa genera un nuevo archivo CSV con la predicción de la especie.

Ejemplo:

```csv
Humano,Maquina
Adelie,Adelie
Chinstrap,Chinstrap
Gentoo,Gentoo
```
