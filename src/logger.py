import logging
import os
from datetime import datetime

#Create a name of future log files(it will consist of current date time and present as month,date,year,hour,minute and second with log extension)
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Create a directory path so get curent workind directory and put a folder called 'logs' with log file in it
dir_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

#Create a directory in directory path and also avoid error if folder already exist with exist=ok
os.makedirs(dir_path,exist_ok=True)

#Create a full path for a log file (put a file in a directory)
LOG_FILE_PATH = os.path.join(dir_path,LOG_FILE)

#Set up logging configuration,what should login file be consist ofmwhat it should present.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)