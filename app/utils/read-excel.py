import pandas as pd

# Ruta del archivo .xlsx
archivo = '/Users/raysalgado/CE/Projects/Oxxo/DB2 Simplex Operativo - Inteligente - Correlación con evaluaciones  v2 proveedor (2).xlsx'

# Leer el archivo .xlsx
df = pd.read_excel(archivo)

# Iterar sobre cada fila en el DataFrame
for index, row in df.iterrows():
    print(f"Fila {index + 1}:")
    with open('inserts.sql','a') as file:
        query = f"INSERT INTO AMEF_GPT (seccion, responsabilidad_operativa, problematica, efecto_de_falla, severidad, ocurrencia, deteccion, riesgo_potencial, acciones_preventivas) VALUES ('{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}, {row[6]}, {row[7]}, {row[8]}, '{row[9]}');"
        file.write(query)
        file.write('\n')
