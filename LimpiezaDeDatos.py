import pandas as pd
import numpy as np

def limpiar_y_formatear_datos(ruta_entrada, ruta_salida):
    """
    Carga el CSV ordenado, estandariza los formatos de las columnas
    clave (Coordx, Coordy, timestamp) y elimina filas con datos faltantes.
    """
    try:
        print(f"Cargando archivo ordenado desde: {ruta_entrada}...")
        
        
        df = pd.read_csv(ruta_entrada, encoding='utf-8', sep=',') 
        print(f"Total de filas a limpiar: {len(df)}")
        
        
        df.columns = df.columns.str.strip()
        print("Nombres de columnas limpiados de espacios en blanco.")
        
        # 1. Limpiar y Convertir Coordenadas
        print("\n1. Limpiando y convirtiendo coordenadas (Coordx, Coordy)...")
        df['Coordx'] = pd.to_numeric(df['Coordx'], errors='coerce') 
        df['Coordy'] = pd.to_numeric(df['Coordy'], errors='coerce')

        # 2. Limpiar y Formatear Timestamp
        print("2. Formateando la columna 'timestamp'...")
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        
        # 3. Manejo de Datos Faltantes (Limpieza)
        print("3. Eliminando filas con datos cruciales faltantes...")
        
        filas_antes = len(df)
        df.dropna(subset=['Coordx', 'Coordy', 'timestamp', 'predominant_color'], inplace=True)
        filas_despues = len(df)
        
        filas_eliminadas = filas_antes - filas_despues
        if filas_eliminadas > 0:
            print(f"   Se eliminaron {filas_eliminadas} filas con datos incompletos o erróneos.")
        else:
            print("   No se encontraron filas con valores cruciales faltantes para eliminar.")

        # 4. Guardar el archivo limpio
        print(f"\nGuardando el archivo limpio en: {ruta_salida}...")
        df.to_csv(ruta_salida, index=False, encoding='utf-8', sep=',') 
        print(f"✅ Proceso de limpieza y formateo terminado con éxito. Filas finales: {len(df)}")

    except FileNotFoundError:
        print(f" ERROR: El archivo de entrada no se encontró en la ruta: {ruta_entrada}")
    except KeyError as e:
        print(f" ERROR: Una de las columnas especificadas NO EXISTE. Esto no debería ocurrir. Por favor, verifica el archivo: {e}")
    except Exception as e:
        print(f" Ocurrió un error inesperado durante la limpieza: {e}")


# --- CONFIGURACIÓN PRINCIPAL ---

ARCHIVO_ENTRADA = 'locationPointsOrdenado.csv'
ARCHIVO_SALIDA = 'locationPointsLimpioFinal.csv'


if __name__ == "__main__":
    limpiar_y_formatear_datos(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)