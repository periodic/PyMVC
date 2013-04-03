

class DB(object):

    def get(self, key):
        raise NotImplementedError()

    def put(self, key, obj):
        raise NotImplementedError()

    def getAll(self):
        raise NotImplementedError()
