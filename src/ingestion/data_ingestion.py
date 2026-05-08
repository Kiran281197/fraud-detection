import pandas as pd
from src.utils.logger import logger

def load_raw_data(file_path:str)->pd.DataFrame:
    """
        This function will read the .csv file from the given file path.
    """
    try:
        logger.info(f"Attempting to load data from {file_path}")
        df = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully with shape {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data : {e}")

def save_the_data(df:pd.DataFrame, file_path:str):
    """
         This function will take the input and save it to destination folder
    """
    try:
        logger.info(f"Attempting to save the processed data into {file_path}")
        df.to_csv(file_path)
        logger.info(f"processed data has been saved successfully in {file_path}")
    except Exception as e:
        logger.error(f"Failed to save data : {e}")



