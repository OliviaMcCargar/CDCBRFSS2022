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

df = raw_data_2022

tuples = [tuple(x) for x in df.to_numpy()] 
  
cols = ','.join(list(df.columns)) 


print(cols)

def main():
    pass

if __name__ == "__main__":
    main()