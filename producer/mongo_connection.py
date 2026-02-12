import os
from pymongo import MongoClient


MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "data")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "suspicious_customers_orders")


class DBConnection:
    @staticmethod
    def get_collection():
        client = MongoClient(MONGODB_URL)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        return collection







