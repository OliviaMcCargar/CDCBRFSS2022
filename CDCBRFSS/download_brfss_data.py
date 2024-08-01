import sys
import os
import requests
import zipfile

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
 
from CDCBRFSS.config import *

def download_external_file(download_file_url, file_directory):
    """
    Takes a string representing the url to a file and a string representing the path to a desired location on hte local machine and downloads the file to that location.

    Parameters
    ----------
    download_file_url : str
        a string representing the url of the file
    file_directory : str
        a string representing the url of the file

    Returns
    -------
    file_path : str
        a string representing the path to the downloaded file.
    """
    variable_data_filename = download_file_url.split("/")[-1]
    response = requests.get(download_file_url)
    file_path = os.path.join(file_directory, variable_data_filename)

    if response.status_code == 200:
	    with open(file_path, 'wb') as file:
              file.write(response.content)
              print("%s downloaded successfully" % (file_path))
    else:
        raise Exception("Failed to establish connection at %s" % (download_file_url))
    
    return(file_path)

def unzip_file(file_path, file_directory):
    """
    Takes a string representing the path to a zip file and a directory it's contents belong in and extracts the zip file to that directory.

    Parameters
    ----------
    file_path : str
        a string representing the path to the zip file
    file_directory : str
        a string representing the path to the directory where the zip file contents will be extracted to.

    Returns
    -------
    extracted_file_name : str
        a string representing the path to the extracted file.
    """
    # opening the zip file in READ mode 
    with zipfile.ZipFile(file_path, 'r') as zip: 
        # read the name of the file
        extracted_file_name = os.path.join(file_directory, zip.namelist()[0])
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall(file_directory)
        print("Renaming File to remove white spaces")
        os.rename(extracted_file_name, extracted_file_name.strip())
        print('Done!')
        return(extracted_file_name.strip())

def delete_file(file_path):
    """
    Takes a string representing the path to a file and deletes it.

    Parameters
    ----------
    file_path : str
        a string representing the path to the file
    """
    try:
        os.remove(file_path)
    except OSError:
        pass

def download_and_extract_file(download_file_url, file_directory):
    """
    Takes a string representing the url to a zipped file, downloads it, extracts it, and deletes the compressed file.

    Parameters
    ----------
    download_file_url : str
        a string representing the url of the file
    file_directory : str
        a string representing the path to the directory where the zip file contents will be downloaded extracted to.
    """
    zip_file_path = download_external_file(download_file_url, file_directory)
    file_path = unzip_file(zip_file_path, file_directory)
    if os.path.isfile(file_path):
        delete_file(zip_file_path)
    return(file_path)

variable_data_file_path = os.path.join(DATA_DIRECTORY_2022, DEFAULT_VARIABLE_DATA_2022_FILE_NAME)
raw_survey_data_file_path = os.path.join(DATA_DIRECTORY_2022, DEFAULT_RAW_SURVEY_DATA_2022_FILE_NAME)

if not os.path.isfile(variable_data_file_path):
    variable_data_file_path = download_and_extract_file(VARIABLE_DATA_2022_URL, DATA_DIRECTORY_2022)

if not os.path.isfile(raw_survey_data_file_path):
    raw_survey_data_file_path = download_and_extract_file(RAW_SURVEY_DATA_2022_URL, DATA_DIRECTORY_2022)

global VARIABLE_DATA_2022_FILE_PATH
global RAW_SURVEY_DATA_2022_FILE_PATH

VARIABLE_DATA_FILE_PATH = variable_data_file_path
RAW_SURVEY_DATA_2022_FILE_PATH = raw_survey_data_file_path

def main():
    pass

if __name__ == "__main__":
    main()