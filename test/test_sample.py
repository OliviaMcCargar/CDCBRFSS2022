import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from CDCBRFSS.download_brfss_data import download_external_file, unzip_file, delete_file


def test_download_1():
    variable_data_url = 'https://www.cdc.gov/brfss/annual_data/2022/zip/codebook22_llcp-v2-508.zip'
    variable_data_filename = 'codebook22_llcp-v2-508.zip'
    data_directory = os.path.join(parent, 'data', 'raw', '2022')
    file_path = os.path.join(data_directory, variable_data_filename)
    assert download_external_file(variable_data_url, data_directory) == file_path

def test_extract_1():
    variable_data_url = 'https://www.cdc.gov/brfss/annual_data/2022/zip/codebook22_llcp-v2-508.zip'
    variable_data_filename = 'codebook22_llcp-v2-508.zip'
    data_directory = os.path.join(parent, 'data', 'raw', '2022')
    file_path = os.path.join(data_directory, variable_data_filename)
    if not os.path.isfile(file_path):
        file_path = download_external_file(variable_data_url, data_directory)
    assert unzip_file(file_path, data_directory) == os.path.join(data_directory, 'USCODE22_LLCP_102523.HTML')

def test_delete_1():
    variable_data_url = 'https://www.cdc.gov/brfss/annual_data/2022/zip/codebook22_llcp-v2-508.zip'
    variable_data_filename = 'codebook22_llcp-v2-508.zip'
    data_directory = os.path.join(parent, 'data', 'raw', '2022')
    file_path = os.path.join(data_directory, variable_data_filename)
    if not os.path.isfile(file_path):
        file_path = download_external_file(variable_data_url, data_directory)
    delete_file(file_path)
    assert os.path.isfile(file_path) == False