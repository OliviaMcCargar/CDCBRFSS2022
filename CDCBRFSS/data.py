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
    
    return(variable_descriptions)

def load_data_dictionary_translations(filepath):
    """
    Takes a string representing the path to an html data dictionary and converts it into an xml etree

    Parameters
    ----------
    filepath : str
        a string representing the desired path to the data dictionary

    Returns
    -------
    vdocument : etree
        An xml.etree object of the data dictionary
    """
    with open(filepath, "rb") as f:
        document = html5lib.parse(f)
        return create_value_translation_table(document)

def create_value_translation_table(tree):
    """
    Takes an xml etree element representing html data dictionary and converts it into a pandas dataframe with a variable name and response value in enlish where appropriate

    Parameters
    ----------
    tree : etree
        an xml etree element representing the full html document for the source data dictionary

    Returns
    -------
    translation_table : dataframe
        The data dictionary for the CDCBRFSS file with the header, value, and value conversion in a long table for most columns
    """
    dict = {'Variable':[],
        'Value':[],
        'Translation':[],
        'Frequency':[],
        'Percent':[],
        'Weighted':[]
       }

    translation_table = pd.DataFrame(dict)
    for table in tree.findall('.//{http://www.w3.org/1999/xhtml}table'):
        variable = ""
        value = ""
        translation = ""
        frequency = ""
        percent = ""
        weighted = ""

        for td in table.findall('./{http://www.w3.org/1999/xhtml}thead/{http://www.w3.org/1999/xhtml}tr/{http://www.w3.org/1999/xhtml}td'):
            for child in td.itertext():
                text = child.strip()
                text_list = text.split(":")
                for index, text in enumerate(text_list):
                    text_list[index] = text_list[index].replace('\xa0', ' ').strip()

                if (text_list[0] == "SAS Variable Name"):
                    variable = text_list[1]

        for tr in table.findall('./{http://www.w3.org/1999/xhtml}tbody/{http://www.w3.org/1999/xhtml}tr'):
            # print("\nNew Row Starts")
            for index,td in enumerate(tr.findall('./{http://www.w3.org/1999/xhtml}td')):
                # print("Variable: ", variable, "Line:", index, "Text: ", td.text)
                if(index == 0):
                    value = str(td.text).strip()
                if(index == 1):
                    translation = str(td.text).strip()
                if(index == 2):
                    frequency = str(td.text).strip()
                if(index == 3):
                    percent = str(td.text).strip()
                if(index == 4):
                    weighted = str(td.text).strip()
                
            if(variable != "" and translation != "" and value != "BLANK"):
                dict = {'Variable': variable, 'Value': value, 'Translation':translation, 'Frequency':frequency, 'Percent':percent, 'Weighted':weighted}
                translation_table = translation_table.append(dict, ignore_index = True)

    
    return(translation_table)

filepath = os.path.join(raw_data_2022_dir, 'USCODE22_LLCP_102523.HTML')
variable_descriptions = load_data_dictionary_descriptors(filepath)
translation_table = load_data_dictionary_translations(filepath)

# filepath = os.path.abspath(os.path.join(project_dir, 'data', 'clean', '2022', 'translation_table_2022.csv'))
# translation_table.to_csv(filepath, index=False)

filepath = os.path.join(raw_data_2022_dir, 'LLCP2022.XPT')
raw_data_2022 = pd.read_sas(filepath, format='xport', encoding='utf-8')

def main():
    print(translation_table)

if __name__ == "__main__":
    main()