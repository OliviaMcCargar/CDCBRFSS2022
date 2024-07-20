import os
import pandas as pd
import xml.etree.ElementTree as ET
import html5lib

project_dir = os.path.join(os.path.dirname( __file__ ), os.path.pardir)
raw_data_2022_dir = os.path.join(project_dir, 'data', 'raw', '2022')

def load_data_dictionary_descriptors(filepath):
    """
    Takes a string representing the path to an html data dictionary and converts it into a dictionary object

    Parameters
    ----------
    filepath : str
        a string representing the desired path to the data dictionary

    Returns
    -------
    variable_descriptions : dataframe
        The data dictionary for the CDCBRFSS file with the header, description, value, and value conversion in a long table
    """
    with open(filepath, "rb") as f:
        document = html5lib.parse(f)
        return create_descriptions_table(document)

def create_descriptions_table(tree):
    """
    Takes an xml etree element representing html data dictionary and converts it into a pandas dataframe with a variable name and description

    Parameters
    ----------
    tree : etree
        an xml etree element representing the full html document for the source data dictionary

    Returns
    -------
    variable_descriptions : dataframe
        The data dictionary for the CDCBRFSS file with the header, description, value, and value conversion in a long table
    """
    dict = {'Variable':[],
        'Description':[],
        'Label':[],
        'Type':[],
        'Section':[],
        'Prologue':[]
       }

    variable_descriptions = pd.DataFrame(dict)
    for table in tree.findall('.//{http://www.w3.org/1999/xhtml}table'):
        variable = ""
        description = ""
        label = ""
        variable_type = ""
        section_name = ""
        prologue = ""

        for td in table.findall('./{http://www.w3.org/1999/xhtml}thead/{http://www.w3.org/1999/xhtml}tr/{http://www.w3.org/1999/xhtml}td'):
            for child in td.itertext():
                text = child.strip()
                text_list = text.split(":")
                for index, text in enumerate(text_list):
                    text_list[index] = text_list[index].replace('\xa0', ' ').strip()

                if (text_list[0] == "SAS Variable Name"):
                    variable = text_list[1]
                if (text_list[0] == "Question"):
                    description = text_list[1]
                if (text_list[0] == "Label"):
                    label = text_list[1]
                if (text_list[0] == "Type of Variable"):
                    variable_type = text_list[1]
                if (text_list[0] == "Section Name"):
                    section_name = text_list[1]
                if (text_list[0] == "Question Prologue"):
                    prologue = text_list[1]

        if (variable != ""):
            dict = {'Variable': variable, 'Description': description, 'Label':label, 'Type':variable_type, 'Section':section_name, 'Prologue':prologue}
            variable_descriptions = variable_descriptions.append(dict, ignore_index = True)
        
        if(variable == "_STATE"):
            print("State table found!")
            for tr in table.findall('./{http://www.w3.org/1999/xhtml}tbody/{http://www.w3.org/1999/xhtml}tr'):
                print("\nNew Row Starts")
                for index,td in enumerate(tr.findall('./{http://www.w3.org/1999/xhtml}td')):
                    print("Variable: ", variable, "Line:", index, "Text: ", td.text)
    
    return(variable_descriptions)

filepath = os.path.join(raw_data_2022_dir, 'USCODE22_LLCP_102523.HTML')
variable_descriptions = load_data_dictionary_descriptors(filepath)

# filepath = os.path.join(raw_data_2022_dir, 'LLCP2022.XPT')
# raw_data_2022 = pd.read_sas(filepath, format='xport', encoding='utf-8')

def main():
    print("End Process")

if __name__ == "__main__":
    main()