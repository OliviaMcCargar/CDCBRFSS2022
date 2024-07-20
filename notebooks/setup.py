import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from CDCBRFSS.utils import project_dir
from CDCBRFSS.data import variable_descriptions, raw_data_2022, translation_table

def main():
    pass

if __name__ == "__main__":
    main()