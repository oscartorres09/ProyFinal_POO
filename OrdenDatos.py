import pandas as pd

# 1. DEFINICIÓN DE LA FUNCIÓN
def ordenar_datos_trafico(ruta_archivo_entrada, ruta_archivo_salida, columnas_orden):
    """
    Lee un archivo CSV, limpia los espacios en los nombres de las columnas, 
    ordena los datos y guarda el resultado.
    """
    try:
        print(f"Cargando datos desde: {ruta_archivo_entrada}...")
        # Cargar con encoding='latin-1' para evitar el error de decodificación
        df = pd.read_csv(ruta_archivo_entrada, encoding='latin-1')
        print(f"¡Carga completada! Total de filas: {len(df)}")
        
        # ----------------------------------------------------------------------
        # PASO 2: LIMPIAR ESPACIOS EN LOS NOMBRES DE LAS COLUMNAS (¡CRÍTICO!)
        # Elimina espacios en blanco al inicio y al final de todos los nombres.
        df.columns = df.columns.str.strip()
        print("Nombres de columnas limpiados de espacios en blanco.")
        # ----------------------------------------------------------------------

        # Opcional, para verificar si el nombre 'timestamp' ahora existe:
        if 'timestamp' not in df.columns:
            print("\n🚨 ERROR: A pesar de la limpieza, 'timestamp' sigue sin encontrarse.")
            print(f"Nombres de columnas disponibles ahora: {df.columns.tolist()}")
            raise KeyError("'timestamp'")


        # Ordenar el DataFrame (Ahora que los nombres están limpios)
        print(f"\nOrdenando el DataFrame por las columnas: {columnas_orden}...")
        df_ordenado = df.sort_values(by=columnas_orden, ascending=True)
        print("¡Ordenación completada!")

        # Guardar el DataFrame ordenado
        print(f"\nGuardando el resultado en: {ruta_archivo_salida}...")
        df_ordenado.to_csv(ruta_archivo_salida, index=False, encoding='utf-8')
        print("✅ Proceso terminado. El archivo ordenado ha sido guardado con éxito.")

    except FileNotFoundError:
        print(f"❌ ERROR: El archivo de entrada no se encontró en la ruta: {ruta_archivo_entrada}")
    except KeyError as e:
        print(f"❌ ERROR: Una de las columnas especificadas para ordenar no existe: {e}. Revisa cuidadosamente las mayúsculas/minúsculas o si el nombre es diferente.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

# --- CONFIGURACIÓN PRINCIPAL ---

# Las variables quedan como las definiste:
ARCHIVO_ENTRADA = 'dataset2024.csv'
ARCHIVO_SALIDA = 'locationPointsOrdenado.csv'
COLUMNAS_PARA_ORDENAR = ['timestamp', 'id'] 

# ************************************************************************************


if __name__ == "__main__":
    ordenar_datos_trafico(ARCHIVO_ENTRADA, ARCHIVO_SALIDA, COLUMNAS_PARA_ORDENAR)