import sys
import pandas as pd
from src.exception import CustomException

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

class PredictPipeline:
    
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
class CustomData: #this function map all inputs that we gave in HTML to the backend
    def __init__(self,USMER:int,MEDICAL_UNIT:int,SEX:str,HOSPITALIZED:int,
                 PNEUMONIA:int,AGE:int,PREGNANT:int,DIABETES:int,COPD:int,              
                 ASTHMA:int,INMSUPR:int,HIPERTENSION:int,OTHER_DISEASE:int,
                 CARDIOVASCULAR:int,OBESITY:int,RENAL_CHRONIC:int,TOBACCO :int,
                 ANTIGEN_TEST:int, AGE_GROUP:str
                 ):
        self.USMER = USMER #So whatever user type in field USMER for example it become self.USMER variable
        self.MEDICAL_UNIT = MEDICAL_UNIT
        self.SEX = SEX
        self.HOSPITALIZED = HOSPITALIZED
        self.PNEUMONIA=PNEUMONIA
        self.AGE = AGE 
        self.PREGNANT = PREGNANT 
        self.DIABETES = DIABETES 
        self.COPD = COPD 
        self.ASTHMA = ASTHMA 
        self.INMSUPR = INMSUPR
        self.HIPERTENSION = HIPERTENSION 
        self.OTHER_DISEASE = OTHER_DISEASE
        self.CARDIOVASCULAR = CARDIOVASCULAR 
        self.OBESITY = OBESITY
        self.RENAL_CHRONIC = RENAL_CHRONIC 
        self.TOBACCO = TOBACCO 
        self.ANTIGEN_TEST = ANTIGEN_TEST 
        self.AGE_GROUP = AGE_GROUP      
        
    def get_data_as_data_frame(self): #this function should create a date frame from user input on home page, becuase we trained our model with a dataframe
        
        try:
        
            custom_data_input_dict = {
                "USMER": [self.USMER],#HERE what ever user typed and we save in __init__ method now we use to create values for dictionary
                "MEDICAL_UNIT": [self.MEDICAL_UNIT],
                "SEX": [self.SEX],
                "HOSPITALIZED": [self.HOSPITALIZED],
                "PNEUMONIA": [self.PNEUMONIA],
                "AGE": [self.AGE],
                "PREGNANT": [self.PREGNANT],
                "DIABETES": [self.DIABETES],
                "COPD": [self.COPD],
                "ASTHMA": [self.ASTHMA],
                "INMSUPR": [self.INMSUPR],
                "HIPERTENSION": [self.HIPERTENSION],
                "OTHER_DISEASE": [self.OTHER_DISEASE],
                "CARDIOVASCULAR": [self.CARDIOVASCULAR],
                "OBESITY": [self.OBESITY],
                "RENAL_CHRONIC": [self.RENAL_CHRONIC],
                "TOBACCO": [self.TOBACCO],
                "ANTIGEN_TEST": [self.ANTIGEN_TEST],
                "AGE_GROUP": [self.AGE_GROUP]    
            }
            
            return pd.DataFrame(custom_data_input_dict) #Now we turn dictionary into a dataframe that our model.pkl can use for prediction
        except Exception as e:
            raise CustomException(e,sys)
    
