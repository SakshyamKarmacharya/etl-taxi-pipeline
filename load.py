from sqlalchemy import create_engine
from config import DB_URI

def load_data(df):
    print("Loading data to database...")
    engine = create_engine(DB_URI)
    df.to_sql(name='trips', con=engine, if_exists='replace', index=False)
