from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd

from data_ingestion.data_transform import data_converter

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE

class ingest_data:

    def __init__(self):
        print("Data ingestion class has initialized")
        self.embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
        self.data_converter = data_converter()

    def data_ingestion(self, status):
        vstore = AstraDBVectorStore(
                embedding=self.embeddings,
                collection_name="ecommchatbot",
                api_endpoint=ASTRA_DB_API_ENDPOINT,
                token=ASTRA_DB_APPLICATION_TOKEN,
                namespace=ASTRA_DB_KEYSPACE, 
        )
        storage = status
        
        if storage == None:
            docs = self.data_converter.data_transformation()
            inserted_ids = vstore.add_documents(docs)
            print(inserted_ids)
        else:
            return vstore
        
        return vstore, inserted_ids

if __name__ == '__main__':
    ingest_data = ingest_data()
    vstore = ingest_data.data_ingestion("Not none")
    # print(f"\Inserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell the low budget headphone")
    for result in results:
        print(f"{result.page_content} [{result.metadata}]")