from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd

from data_ingestion.data_transform import data_convert


class ingest_data:

    def __init__(self):
        print("Data ingestion class has initialized")

    def data_ingestion(self):
        pass

if __name__ == '__main__':
    data_ingestion = ingest_data()