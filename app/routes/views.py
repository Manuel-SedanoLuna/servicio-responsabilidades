from flask import Blueprint
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
