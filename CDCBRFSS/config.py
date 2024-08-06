import os
import sys
import psycopg2

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

global PROJ_DIR
global DATA_DIRECTORY_2022
global DATABASE
global DB_CONN_INTERNAL
global DB_CONN_EXTERNAL
global DB_USER
global DB_PASSWORD
global DB_PORT
global VARIABLE_DATA_2022_URL
global RAW_SURVEY_DATA_2022_URL
global DEFAULT_VARIABLE_DATA_2022_FILE_NAME
global DEFAULT_RAW_SURVEY_DATA_2022_FILE_NAME

PROJ_DIR = parent
DATA_DIRECTORY_2022 = os.path.join(parent, 'data', 'raw', '2022')
DATABASE = 'brfss_database'
DB_CONN_INTERNAL = 'db'
DB_CONN_EXTERNAL = '0.0.0.0'
DB_USER = 'brfss_user'
DB_PASSWORD = 'CDCBRFSS'
DB_PORT = 5432
VARIABLE_DATA_2022_URL = 'https://www.cdc.gov/brfss/annual_data/2022/zip/codebook22_llcp-v2-508.zip'
RAW_SURVEY_DATA_2022_URL = 'https://www.cdc.gov/brfss/annual_data/2022/files/LLCP2022XPT.zip'
DEFAULT_VARIABLE_DATA_2022_FILE_NAME = 'USCODE22_LLCP_102523.HTML'
DEFAULT_RAW_SURVEY_DATA_2022_FILE_NAME = 'LLCP2022.XPT'

try:
    connection = psycopg2.connect(database = DATABASE,
                              user = DB_USER,
                              host = DB_CONN_EXTERNAL,
                              password = DB_PASSWORD,
                              port = DB_PORT)
except psycopg2.OperationalError:
    try:
        connection = psycopg2.connect(database = DATABASE,
                              user = DB_USER,
                              host = DB_CONN_INTERNAL,
                              password = DB_PASSWORD,
                              port = DB_PORT)
    except psycopg2.OperationalError:
        print("Problem connecting to database")

def main():
    pass

if __name__ == "__main__":
    main()