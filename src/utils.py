# In utils we put common functionalities that whole project can use (imorting in different modules)
import os
import sys
import numpy as np
import pandas as pd
import dill

from exception import CustomException

def save_object(file_path,obj):#create function to save Python object(obj) to a file specified by file path
    try:
        dir_path = os.path.dirname(file_path)#Extract directory path from file_path
        os.makedirs(dir_path,exist_ok=True)#Create directory in extracted path and avoid error if already exist
        
        with open(file_path,"wb") as file_obj:#Open file from file_path in write and binary mode as file_obj that can be used to accept new data
            dill.dump(obj,file_obj)#Dump function serilize object and write it to file_obj 
        
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)
        
