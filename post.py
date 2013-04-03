
from model import Model

class Post(Model):

    def __init__(self, title=None, body=None):
        if not title or not body:
            raise ValueError("Post must have both title and body.")
        self.title = title
        self.body = body

    def toData(self):
        return { "title": self.title, "body": self.body }

    @classmethod
    def fromData(cls, data):
        if data['title'] and data['body']:
            return Post(title=data['title'], body=data['body'])
        else:
            raise ValueError("Unable to construct Post from %r" % data)

    def getKey(self):
        return self.title
