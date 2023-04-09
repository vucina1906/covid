# In utils we put common functionalities that whole project can use (imorting in different modules)
import os
import sys
import numpy as np
import pandas as pd
import dill
import dill
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

from exception import CustomException

def save_object(file_path,obj):#create function to save Python object(obj) to a file specified by file path
    try:
        dir_path = os.path.dirname(file_path)#Extract directory path from file_path
        os.makedirs(dir_path,exist_ok=True)#Create directory in extracted path and avoid error if already exist
        
        with open(file_path,"wb") as file_obj:#Open file from file_path in write and binary mode as file_obj that can be used to accept new data
            dill.dump(obj,file_obj)#Dump function serilize object and write it to file_obj 
        
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        
        report = {}

        for i, model_name in enumerate(models.keys()):
            model = models[model_name]
            para = param[model_name]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = accuracy_score(y_train, y_train_pred)

            test_model_score = accuracy_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)        
                   
        