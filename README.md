This project is a Python-based ETL (Extract, Transform, Load) pipeline that processes real-world Yellow Taxi trip data from New York City. It demonstrates how raw CSV data from a public source can be cleaned and loaded into a PostgreSQL database for further analysis or reporting.

The pipeline is built with modular scripts:

extract.py downloads compressed CSV data from a GitHub release.

transform.py filters the dataset to include only valid trips (positive passengers and distance).

load.py connects to a PostgreSQL database using SQLAlchemy and stores the cleaned data in a trips table.

Technologies used include Python, Pandas, PostgreSQL, SQLAlchemy, and dotenv for configuration. The project showcases core data engineering practices: data ingestion, cleaning, validation, and storage in a structured, queryable format.
