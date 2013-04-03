
from db import DB

class MemDB(DB):

    def __init__(self):
        self.storage = {}

    def get(self, key):
        return self.storage[key]

    def put(self, key, data):
        self.storage[key] = data
        return self

    def getAll(self):
        return self.storage.values()

