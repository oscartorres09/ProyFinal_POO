import pandas as pd

def analizar_colores(ruta_archivo):
    print(f"🔍 Analizando los colores en: {ruta_archivo}...")
    
    try:
        # Optimizacion: 'usecols' hace que solo cargue esa columna, 
        # haciendo el proceso instantáneo aunque sean millones de datos.
        df = pd.read_csv(ruta_archivo, usecols=['predominant_color'])
        
        # Obtener los valores únicos y contarlos
        conteo = df['predominant_color'].value_counts()
        
        print("\n📊 REPORTE DE COLORES ENCONTRADOS:")
        print("-----------------------------------")
        print(conteo)
        print("-----------------------------------")
        
        print("\n📝 Lista simple para copiar:")
        print(df['predominant_color'].unique().tolist())
        
    except FileNotFoundError:
        print("❌ Error: No encontré el archivo. Verifica el nombre.")
    except ValueError:
        print("❌ Error: La columna 'predominant_color' no existe en este archivo.")

# --- EJECUCIÓN ---
# Asegúrate de usar el nombre de tu archivo LIMPIO
ARCHIVO = 'locationPointsLimpioFinal.csv' 

if __name__ == "__main__":
    analizar_colores(ARCHIVO)