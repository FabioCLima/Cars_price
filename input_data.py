# Data Wrangling
# Setup of scripts folder and datafiles 
#
import os
import pandas as pd 

def fetch_cars_data():
    
    """[Summary]
       This function setup up the scripts directory and data file
       in order to run in any system or machine.
    """    
    DATA_INPUT = "cars_input.csv"
    SRC_DIR = os.path.abspath(__file__)
    SRC_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(SRC_DIR)
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    csv_file = os.path.join(DATA_DIR, DATA_INPUT)
    return csv_file

def load_cars_data():
    
    csv_file =  fetch_cars_data() 
    return csv_file
data = load_cars_data()
# df = pd.read_csv(data)


