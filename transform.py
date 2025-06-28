def transform_data(df):
    print("Transforming data...")
    df = df[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'fare_amount']]
    df = df[df['passenger_count'] > 0]
    df = df[df['trip_distance'] > 0]    
    return df

