import sys
import os
import requests
import zipfile
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

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
        extracted_file_name = os.path.join(file_directory, zip.namelist()[0]).strip()
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall(file_directory) 
        print('Done!')
        return(extracted_file_name)

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

data_directory = os.path.join(parent, 'data', 'raw', '2022')
variable_data_url = 'https://www.cdc.gov/brfss/annual_data/2022/zip/codebook22_llcp-v2-508.zip'
raw_survey_data_url = 'https://www.cdc.gov/brfss/annual_data/2022/files/LLCP2022XPT.zip'

variable_data_file_path = os.path.join(data_directory, 'USCODE22_LLCP_102523.HTML')
raw_survey_data_file_path = os.path.join(data_directory, 'LLCP2022.XPT')

if not os.path.isfile(variable_data_file_path):
    variable_data_file_path = download_and_extract_file(variable_data_url, data_directory)

if not os.path.isfile(raw_survey_data_file_path):
    raw_survey_data_file_path = download_and_extract_file(raw_survey_data_url, data_directory)

def main():
    pass

if __name__ == "__main__":
    main()