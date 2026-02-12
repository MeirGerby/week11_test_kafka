from mongo_connection import DBConnection 

class DBCrud:
    _collection = DBConnection.get_collection()

    @staticmethod
    def get_all_data():
        data = DBCrud._collection.find({},{"_id":0})
        return data 
    
