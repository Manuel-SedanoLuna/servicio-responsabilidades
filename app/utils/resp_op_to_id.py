import pandas as pd
import json

# Ruta del archivo JSON y CSV
archivo_json = './app/utils/resp_ops.json'
archivo_csv = 'data_PSU_v1_0_0.csv'
archivo_salida = 'new.csv'

# Leer el archivo JSON
with open(archivo_json, 'r') as f:
    datos_json = json.load(f)

# Crear un diccionario para mapear RESPONSABILIDAD_OPERATIVA a ID
mapa_responsabilidad_id = {
    item['Responsabilidad Operativa'].strip().lower(): str(item['ID']) for item in datos_json
}

print("Mapa de Responsabilidad Operativa a ID:", mapa_responsabilidad_id)

# Leer el archivo CSV
df_csv = pd.read_csv(archivo_csv)

# Normalizar los valores de Responsabilidad Operativa en el CSV
df_csv['Responsabilidad Operativa'] = df_csv['Responsabilidad Operativa'].str.strip().str.lower()

# Reemplazar la columna Responsabilidad Operativa por el ID correspondiente
df_csv['Responsabilidad Operativa'] = df_csv['Responsabilidad Operativa'].map(mapa_responsabilidad_id)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df_csv.to_csv(archivo_salida, index=False)

print(f"Archivo modificado guardado como: {archivo_salida}")
