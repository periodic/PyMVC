

class View(object):

    def setController(self, controller):
        raise NotImplementedError()

    def showError(self, message):
        raise NotImplementedError()

    def displayPost(self, post):
        raise NotImplementedError()

    def displayList(self, posts):
        raise NotImplementedError()

    def displayForm(self):
        raise NotImplementedError()



