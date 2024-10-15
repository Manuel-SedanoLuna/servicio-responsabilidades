from flask import Blueprint, jsonify, request
from ..controllers.http_controller import HTTPController
from ..config.config import Config
from ..controllers.formatters import process_response
import json

bp = Blueprint('routes', __name__)
connection = HTTPController()

@bp.route('/api/hello', methods=['GET'])
def hello_world():
    return 'Hello world'

@bp.route('/api/connectioninfo', methods=['GET'])
def connection_info():
    deployment_id = Config.DEPLOYMENT_ID
    response = connection.get(path=f'dbapi/v4/connectioninfo/{deployment_id}')
    print(response, type(response))
    return json.dumps(response)

@bp.route('/api/select', methods=['POST'])
def select():
    payload = {
        "commands": "SELECT * FROM PSU;",
        "limit": 10,
        "separator": ";",
        "stop_on_error": "no"
    }
    response = connection.post(path='dbapi/v4/sql_jobs', json=payload)
    response_id = response.get('id')
    
    query_results = connection.get(path=f'dbapi/v4/sql_jobs/{response_id}')
    
    results = process_response(query_results)
        
    return results

# Método para obtener Listado con las responsabilidades operativas con mayor prioridad.
@bp.route('/api/operational_responsibilities', methods=['GET'])
def operational_responsibilities():
    try:
        # Obtener el JSON de la solicitud
        data = request.get_json()
        
        if isinstance(data, list):
            data = data[0]
        else:
            data = data
        # Validar que el campo 'store' exista en el JSON
        if 'store' not in data:
            return jsonify({'mensaje': 'Falta especificar tienda'}), 400
        # convertir a mayus
        store = "'"+data['store'].upper()+"'"
        # Si se proporciona una fecha, usarla; de lo contrario, usar la fecha más reciente
        if 'date' in data:
            date_query = '%s'  # Placeholder para la fecha proporcionada
            date_value = data['date']
        else:
            # Subconsulta para obtener la fecha más reciente
            date_query = '(SELECT MAX(fecha) FROM SCORE_RESULTADOS WHERE tienda = %s)'
            date_value = store  # Solo se necesita la tienda en la subconsulta
        
        attributes ='ag.seccion, responsabilidad_operativa, resp_op_id, ag.problematica, score' 
        # Crear la consulta SQL usando placeholders
        query = f'SELECT {attributes} FROM SCORE_RESULTADOS sr INNER JOIN AMEF_GPT ag ON resp_op_id=ag.id WHERE tienda = %s AND IS_ACTIVO = True AND fecha = {date_query};'
        values = (store, date_value)

        print(f"Query: {query % values}")

        # Crear el payload con la consulta
        payload = {
            "commands": query % values,  # Usar el método correcto para insertar los valores
            "separator": ";",
            "stop_on_error": "no"
        }

        # Hacer la solicitud POST al servicio externo
        response = connection.post(path='dbapi/v4/sql_jobs', json=payload)
        response_id = response.get('id')
        
        # Obtener los resultados de la consulta
        query_results = connection.get(path=f'dbapi/v4/sql_jobs/{response_id}')
        # Procesar la respuesta
        results = process_response(query_results)
        
        if not results:
            return jsonify({'mensaje': 'No se encontraron responsabilidades operativas'}), 404
        
        return results

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'mensaje': 'Error procesando la solicitud'}), 500