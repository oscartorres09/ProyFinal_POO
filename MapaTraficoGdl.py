import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title = "Mapa de Trafico en la ZMG",
    layout = "wide"
)

st.title("Trafico por hora en la ZMG")

st.sidebar.markdown("Proyecto Final POO")
st.sidebar.markdown("Oscar Torres")

# Musica
try:
    st.audio("POOsong.mp3", format = "audio/mp3")
except:
    st.sidebar.warning("No se encontro el archivo de musica")

# Definicion de colores

def ColorPuntos(color_texto):
    if color_texto == 'red_wine':
        return [130,0,180]
    elif color_texto == 'red':
        return [230,11,6]
    elif color_texto == 'orange':
        return [230,120,20]
    elif color_texto == 'green':
        return [24,217,30]
    else:
        return [150,150,150]

# Hacer mas fluida la animacion
@st.cache_data

# Lectura de datos
def CargarDatos(ruta):
    try:
        # Leer archivo
        df = pd.read_csv(ruta)

        # Convertir la columna de texto a tiempo real
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Aplicar colores
        df['color'] = df['predominant_color'].apply(ColorPuntos)
        return df

    except FileNotFoundError:
        return None

ARCHIVO = 'locationPointsLimpioFinal.csv'
datos_trafico = CargarDatos(ARCHIVO)

if datos_trafico is None:
    st.error(f"No se encontro el archivo: {ARCHIVO}")
    st.stop()

# Cambiar texto a fecha y redondear
horas_unicas = sorted(datos_trafico['timestamp'].dt.floor('h').unique())

# Sobre escribir sobre lo que hay
TextoHora = st.empty()
MapaContenedor = st.empty()

# Elegir velocidad
OpcionVelocidad = st.select_slider(
    "Selecciona la velocidad deseada:",
    options = ["Lento", "Normal", "Rapido", "Muy Rapido"],
    value = "Normal"
)
if OpcionVelocidad == "Lento":
    tiempo_espera = 0.8
elif OpcionVelocidad == "Normal":
    tiempo_espera = 0.5
elif OpcionVelocidad == "Rapido":
    tiempo_espera = 0.2
elif OpcionVelocidad == "Muy Rapido":
    tiempo_espera = 0.05

# Boton de comenzar
if st.button ('Ver trafico'):
    BarraProgreso = st.progress(0)
    TotalPasos = len(horas_unicas)

    for i, hora_actual in enumerate(horas_unicas):
        TextoHora.subheader(f"Fecha y hora: {hora_actual}")

        DatosHora = datos_trafico[datos_trafico['timestamp'].dt.floor('h') == hora_actual]

        if not DatosHora.empty:
            MapaContenedor.map(
                DatosHora,
                latitude='Coordy',
                longitude='Coordx',
                color='color',
                size=20,
                zoom=11
            )

        BarraProgreso.progress((i + 1)/ TotalPasos)

        # Segundos por hora
        time.sleep(tiempo_espera)
    
    st.success("Animacon mostrada con exito")