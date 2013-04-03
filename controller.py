
from post import Post

class Controller(object):

    def __init__(self, db=None, view=None):
        if not db:
            raise ValueError("Controller must have a db and a view")

        self.db = db
        self.view = view

        self.view.setController(self)

    def start(self):
        self.view.displayList(Post.findAll(self.db))

    def showPost(self, key):
        try:
            self.view.displayPost(Post.find(self.db, key))
        except KeyError:
            self.view.showError("Post not found.")
            self.view.displayList(Post.findAll(self.db))

    def backToList(self):
        self.view.displayList(Post.findAll(self.db))

    def newPost(self):
        self.view.displayForm()

    def createPost(self, title, body):
        if not title or not body:
            self.view.showError("Invalid input.")
            self.view.displayForm()
            return

        try:
            post = Post(title=title, body=body)

            post.save(self.db)

            self.backToList()
        except ValueError:
            self.view.showError("Invalid post.")
            self.backToList()
        except Exception as e:
            self.view.showError("An error occured: %s" % e)
            self.backToList()

    def exit(self):
        return

