import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    BASE_URL =  os.environ['BD_REST_HOST']
    USER = os.environ['BD_USER']
    PASSWORD = os.environ['BD_PASS']
    DEPLOYMENT_ID = os.environ['DEPLOYMENT_ID']
    
