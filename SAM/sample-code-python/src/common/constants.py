import os

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

MAIN_DB = os.environ.get('MAIN_DB')
MAIN_DB_HOST = os.environ.get('MAIN_DB_HOST')
MAIN_DB_PASSWORD = os.environ.get('MAIN_DB_PASSWORD')
MAIN_DB_PORT = os.environ.get('MAIN_DB_PORT')
MAIN_DB_USER = os.environ.get('MAIN_DB_USER')

BLUECHIP_CNS_HISTORY_DB = os.environ.get('BLUECHIP_CNS_HISTORY_DB')
CELL_POSITION_DB = os.environ.get('CELL_POSITION_DB')

OUTER_MOVE_EVENT_CHECK_REQUEST_DB = os.environ.get('OUTER_MOVE_EVENT_CHECK_REQUEST_DB')
EVENT_DIAGNOSIS_DB = os.environ.get('EVENT_DIAGNOSIS_DB')

ERROR_DB = os.environ.get('ERROR_DB')