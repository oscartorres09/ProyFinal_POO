import streamlit as st
import pandas as pd
import time

# Cargar datos
df = pd.read_csv("locationPoints.csv", encoding="ISO-8859-1")

df["Coordx"] = pd.to_numeric(df["Coordx"], errors="coerce")
df["Coordy"] = pd.to_numeric(df["Coordy"], errors="coerce")

df = df.dropna(subset=["Coordx", "Coordy"])

# Crear contenedor para el mapa
map_placeholder = st.empty()

# Mostrar los datos de 100 en 100
batch_size = 100

st.button("reinicia")

for i in range(0, len(df), batch_size):
    # Selecciona 100 registros
    batch = df.iloc[i:i + batch_size]
    
    # Actualiza el mapa dentro del contenedor
    map_placeholder.map(batch, latitude="Coordy", longitude="Coordx", zoom=10)
    
    # Espera 1 segundo antes de la siguiente actualización
    time.sleep(1)


