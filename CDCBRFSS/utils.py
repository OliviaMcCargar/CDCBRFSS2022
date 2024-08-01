import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
 
from CDCBRFSS.config import *

def main():
    pass

if __name__ == "__main__":
    main()