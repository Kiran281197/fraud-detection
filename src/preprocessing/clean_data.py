import pandas as pd
import numpy as np
from src.utils.logger import logger

def clean(df:pd.DataFrame)->pd.DataFrame:
    """
        This function will take dataframe and does below things
            1) Remove unwanted columns
            2) Handle outliers
    """
    try:
        # Remove unwanted columns
        df_copy = df.copy()
        unwanted_column = ["Unnamed: 0"]
        for col in unwanted_column:
            if col in df_copy.columns:
                df_copy = df_copy.drop(col, axis=1)
                logger.info(f"Removed {col} column successfully")

        # Handle Outliers
        =============================

        return df_copy
    
    except Exception as e:
        logger.error(f"Error : {e}")
        raise e