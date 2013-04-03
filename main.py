
from controller import Controller
from commandlineview import CommandLineView
from memdb import MemDB

db = MemDB()
view = CommandLineView()
controller = Controller(db=db, view=view)

controller.start()
