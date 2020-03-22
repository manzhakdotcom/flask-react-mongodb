import pymongo

DATABASE = 'testdb'


class DBHelper:
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]

    def get_city(self, state):
        return list(self.db.testcol.find({"state": state}).limit(3))

