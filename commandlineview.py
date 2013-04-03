
from view import View

class CommandLineView(View):

    def __init__(self):
        pass

    def setController(self, controller):
        self.controller = controller

    def showError(self, message):
        print "Error: %s" % message

    def displayPost(self, post):
        print """
title: %s
body: %s

[enter]: Continue
""" % (post.title, post.body)

        raw_input()
        self.controller.backToList()

    def displayList(self, posts):
        for idx, post in enumerate(posts):
            print "%d: %s" % (idx, post.title)

        print "Choose a number, 'new' to create a new post, 'exit' to exit"

        option = raw_input()

        if not option:
            self.controller.backToList()
        elif option == "new":
            self.controller.newPost()
        elif option == "exit":
            self.controller.exit()
        else:
            try:
                self.controller.showPost(posts[int(option)].getKey())
            except ValueError:
                print "Invalid number."
                self.controller.backToList()

    def displayForm(self):
        title = raw_input("Enter the title:")
        body = raw_input("Enter the body:")

        self.controller.createPost(title, body)

