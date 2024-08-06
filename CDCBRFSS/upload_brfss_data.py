import sys
import os
import psycopg2
import psycopg2.extras as extras 
import pandas as pd 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
 
from CDCBRFSS.config import *
from CDCBRFSS.data import *

def write_sql_to_script_folder(script_text, file_name):
    '''
    Takes a string representing the sql script text and a file name and writes the text to the file name in the scripts folder of this project.

    Parameters
    ----------
    script_text : str
        a string representing the sql script being written
    file_name : str
        a string representing the path to the file
    """
    '''
    sql_file = os.path.join(PROJ_DIR, 'scripts', file_name)

    with open(sql_file, 'w') as file:
        file.write(script_text)


def write_table_creation_sql(table_name, primary_key_name, table):
    """
    Takes string representing the desired table name and name for the primary key of that table, and a pandas dataframe and writes out the sql needed to create a table with the same columns as the dataframe

    Parameters
    ----------
    table_name : string
        a string representing the desired table name
    primary_key_name : string
        a string representing the desired primary key name

    Returns
    -------
    sql_output : string
        The string representing the sql code needed to create the postgres table from that dataframe.
    """
    sql_output = 'DROP TABLE IF EXISTS ' + table_name + ';\n\nCREATE TABLE ' + table_name + ' (\n     ' + primary_key_name + ' SERIAL PRIMARY KEY,\n'

    for column in table.columns:
        sql_output += '     ' + column.upper() + ' TEXT,\n'

    sql_output += ');'

    return(sql_output)



# Create Table Scripts

# Raw Data
sql_output = write_table_creation_sql('raw_data_2022', 'RESPONSE_ID', raw_data_2022)

write_sql_to_script_folder(sql_output, 'raw_data_2022_table_create.sql')

# Description Table
sql_output = write_table_creation_sql('variable_descriptions', 'VARIABLE_ID', variable_descriptions)

write_sql_to_script_folder(sql_output, 'variable_descriptions_table_create.sql')

# Translation Table
sql_output = write_table_creation_sql('variable_translations', 'TRANSLATION_ID', translation_table)

write_sql_to_script_folder(sql_output, 'variable_translations_table_create.sql')

def main():
    pass

if __name__ == "__main__":
    main()