import pandas as pd
from config import DATA_URL

def extract_data():
    print("Extracting data...")
    df = pd.read_csv(DATA_URL, compression='gzip')
    return df
