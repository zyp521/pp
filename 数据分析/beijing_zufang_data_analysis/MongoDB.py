import pymongo

HOST = "127.0.0.1"
PORT = 27017


class MongoDB:

    def __init__(self):
        self.client = pymongo.MongoClient(host=HOST, port=PORT)
        self.db = self.client['anjuke']
        self.collection = self.db['ajk_collection']

    def find(self):
        return [i for i in self.collection.find()]


if __name__ == '__main__':
    mongo = MongoDB()
    print(mongo.find())
