from src.ingestion.data_ingestion import load_raw_data, save_the_data
from pathlib import Path
from src.preprocessing.data_validation import validate_data
from src.preprocessing.clean_data import clean
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "card_transdata.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "processed_data.csv"

expected_dtypes = {
    "distance_from_home": "float64",
    "ratio_to_median_purchase_price": "float64",
    "repeat_retailer": "float64",
    "used_chip": "float64",
    "used_pin_number": "float64",
    "online_order": "float64",
    "fraud": "float64"
}

# load the raw data
df = load_raw_data(RAW_DATA_PATH)

# validate the loaded data and log the information
validate_data(df, expected_dtypes = expected_dtypes)

# save the loaded data
save_the_data(df=df, file_path=PROCESSED_DATA_PATH)

# load the processed data
df = pd.read_csv(PROCESSED_DATA_PATH)

# clean the data
df_clean = clean(df=df)

print(df_clean)