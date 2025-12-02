import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Tráfico en la ZMG",
    layout="wide"
)

def ObtenerColor(color_texto):
    """
    Convierte el nombre del color del tráfico a una lista RGB [R, G, B].
    """
    if color_texto == 'red':
        # Rojo (Congestión)
        return [240, 0, 0]
    elif color_texto == 'green':
        # Verde (Flujo libre)
        return [20, 217, 4]
    elif color_texto == 'orange':
        # Amarillo (Tráfico lento)
        return [245, 230, 11]
    elif color_texto == 'red_wine':
         return [163, 11, 8]
    else:
        # Gris (Para datos no definidos o nulos)
        return [150, 150, 150]

@st.cache_data
def CargarDatos(ruta):
    df = pd.read_csv(ruta)
    df['timestamp'] = pd.to_datetime(['timestamp'])
    df['color'] = df['predominant_color'].apply(ObtenerColor)
    return df

HorasUnicas =  sorted(DatosTrafico['timestamp'].dt.floor('H').unique())

ArchivoDatosLimpios = 'locationPointsLimpioFinal.csv'

try:
        datos_trafico = CargarDatos(ArchivoDatosLimpios)
except FileNotFoundError:
      st.error(f"Error: No se encontró el archivo {ArchivoDatosLimpios}.")
      st.stop()

st.title("Trafico con el tiempo en la ZMG")

MapPlaceholder = st.empty()
TimeTextPlaceholder = st.empty()

