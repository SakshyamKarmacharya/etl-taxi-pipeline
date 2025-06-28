import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI")
DATA_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

