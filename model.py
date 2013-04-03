

class Model(object):

    def save(self, db):
        db.put(self.getKey(), self.toData())
        return self

    @classmethod
    def find(cls, db, key):
        return cls.fromData(db.get(key))

    @classmethod
    def findAll(cls, db):
        return [ cls.fromData(data) for data in db.getAll() ]

    def toData(self):
        raise NotImplementedError()

    @classmethod
    def fromData(cls, data):
        raise NotImplementedError()

    def getKey(self):
        raise NotImplementedError()
