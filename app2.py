import streamlit as st
import pandas as pd
import pydeck as pdk
import time

# Cargar datos
df = pd.read_csv("locationPoints.csv", encoding="ISO-8859-1")

df["Coordx"] = pd.to_numeric(df["Coordx"], errors="coerce")
df["Coordy"] = pd.to_numeric(df["Coordy"], errors="coerce")

df = df.dropna(subset=["Coordx", "Coordy"])

# Definir centro fijo (por ejemplo, el promedio de todas las coordenadas)
center_lat = df["Coordy"].mean()
center_lon = df["Coordx"].mean()

# Crear contenedor del mapa
map_placeholder = st.empty()



# Crear capa de puntos
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["Coordx", "Coordy"],
    get_radius=50,
    get_color=[255, 0, 0],  # rojo
    pickable=True,
)

# Definir vista del mapa (fija)
view_state = pdk.ViewState(
    zoom=11, #zoom 
    pitch=0, #inclinacion de la camara
    latitude=center_lat,
    longitude=center_lon,
)

# Renderizar mapa
map_placeholder.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
time.sleep(1)


    