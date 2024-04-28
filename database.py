import pymongo

class Database:
    def __init__(self, database, collection):
        # Initialize your database connection here
        self.database = database 
        self.collection = collection 
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

    def connect(self):
        # Implement the logic to connect to the MongoDB database
        db = self.client[self.database]
        return db 
    
    def close(self):
        self.database.close()
        