import os
import sys
from exception import CustomException
from logger import logging
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from utils import save_object,evaluate_models
from dataclasses import dataclass
from sklearn.metrics import accuracy_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split train and test input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "XGBClasifier": XGBClassifier(),
                "LGBMClasifier":LGBMClassifier(),
                "CatBoosting Classifier":CatBoostClassifier(verbose=False)
            }
            
            params={
                "Decision Tree": {
                    'criterion':['gini', 'entropy'],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },
                "Random Forest":{
                    'n_estimators': [50, 100, 200],
                    'max_depth': [5, 10, 20]
                },
                "XGBClasifier":{
                    'n_estimators': [50, 100, 200],
                    'max_depth': [5, 10, 20],
                    'learning_rate': [0.1, 0.01, 0.001]
                },
                "LGBMClasifier":{
                    'n_estimators': [50, 100, 200],
                    'max_depth': [5, 10, 20],
                    'learning_rate': [0.1, 0.01, 0.001]
                    
                },
                "CatBoosting Classifier":{
                    'n_estimators': [50, 100, 200],
                    'depth': [5, 10],
                    'learning_rate': [0.1, 0.01, 0.001]
                }
            }
            
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test, models=models,param=params)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info("Best model found on both training and test set")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, predicted)
            return accuracy
        
        except Exception as e:
            raise CustomException(e,sys)
    




