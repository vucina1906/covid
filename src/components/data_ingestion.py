import os 
import sys
from logger import logging
from exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#By using dataclass decorator this class automaticaly generate special methods such as __init__ , __repr__
#We use this decorator when we only define variables in class
@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts',"train.csv")#Create path so later we can use it to save train data(in new folder artifacts under name test data)
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str= os.path.join('artifacts',"raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#We create a variable that is consist of all free variables (that represent paths) from decorated DataIngestionConfig class
    

    def initiate_data_ingestion(self):#Create a function that do ingestion,splitting and saving data
        logging.info("Entered data ingestion method")
        try:
            df = pd.read_csv('notebook\data\CovidData.csv')
            logging.info('Dataset read as a dataframe')
            
            #Create a artifacts directory using os.makedirs method and avoid error if folder already exist with exist_ok = True argument
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            #Now when we created folder we should save raw data using raw data path save in self.ingestion_config class variable
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)#Split data 80% of data to train set and 20% of data to test set
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#Save train data in artifacts folder
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#Save test data in artifacts folder 
            
            logging.info("Ingestion of data is completed")
            return(
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    
    
 