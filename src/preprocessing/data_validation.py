import pandas as pd
import numpy as np
from src.utils.logger import logger
from pathlib import Path

def validate_data(df:pd.DataFrame, expected_dtypes):
    """
        This function will validate the data and logs the issues
    """
    try:
        #check the target column
        target = "fraud"
        logger.info(f"Checking if {target} column exist")
        if target not in df.columns:
            logger.error(f"{target} column missing")
            raise ValueError(f"{target} columns missing")
        else:
            logger.info(f"Target column exist : {target}")

        #check for duplicates
        logger.info("Checking for duplicates")
        duplicate_count = df[df.duplicated()].shape[0]
        logger.info(f"Found {duplicate_count} duplicates")

        #check for null values
        logger.info("checking for null values")
        null_count = df[df.isnull().any(axis=1)].shape[0]
        logger.info(f"Found {null_count} missing values")

        #check if dataset is empty
        logger.info("checking if dataset is empty")
        if df.empty:
            logger.info("dataset is  empty")
        else:
            logger.info("dataset is not empty")

        #check the shape of the dataset
        logger.info(f"Dataset Shape : {df.shape}")

        # Validate the data types
        for column, expected_dtype in expected_dtypes.items():
            actual_dtype = str(df[column].dtype)

            if actual_dtype == expected_dtype:
                logger.info(f"{column} : True")
            else:
                logger.info(f"{column} : False")

        # Calculate target variable distribution

        target_distribution = (df[target].value_counts() / df.shape[0])
        logger.info(f"{target} distribution : {target_distribution.loc[1.0]}")
        logger.info(f"Not_{target} distribution : {target_distribution.loc[0.0]}")
    
    except Exception as e:
        logger.info(f"Error : {e}")



