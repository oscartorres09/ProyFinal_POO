import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
import chardet

with open("locationPoints.csv", "rb") as f:
    result = chardet.detect(f.read(100000))
print(result)

# Ejemplo de salida: {'encoding': 'ISO-8859-1', 'confidence': 0.99}

df = pd.read_csv("locationPoints.csv", encoding=result['encoding'])

df["Coordx"] = pd.to_numeric(df["Coordx"], errors="coerce")
df["Coordy"] = pd.to_numeric(df["Coordy"], errors="coerce")
df = df.dropna(subset=["Coordx", "Coordy"])  # opcional, por seguridad

print(df.dtypes)

st.map(df, latitude="Coordy", longitude="Coordx", zoom=10)