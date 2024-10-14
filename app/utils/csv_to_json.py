import pandas as pd
import json

def csv_a_json(archivo_csv, archivo_json):
    # Lee el archivo CSV
    df = pd.read_csv(archivo_csv, encoding='utf-8')

    # Convierte el DataFrame a un diccionario
    datos_json = df.to_dict(orient='records')

    # Guarda el diccionario como un archivo JSON en UTF-8
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(datos_json, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    archivo_csv = 'PSU_DATA.csv'  # Cambia esto al nombre de tu archivo CSV
    archivo_json = 'PSU_DATA.json'  # Nombre del archivo JSON de salida

    csv_a_json(archivo_csv, archivo_json)
    print(f'Archivo {archivo_json} creado exitosamente.')
