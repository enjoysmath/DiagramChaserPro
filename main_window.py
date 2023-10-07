from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from identity_is_unique import IdentityIsUnique
from game import Game
from diagram_editor import DiagramEditor

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self._baseTitle = "Arrow Theory Games"      
      self.setWindowTitle(self._baseTitle)
      self._pages = QStackedWidget()
      #self.setCentralWidget(self._pages)
      #self.add_game(IdentityIsUnique())
      self.diagram_editor = DiagramEditor()
      
      self.setCentralWidget(self.diagram_editor)
      
   def add_game(self, game: Game):
      self._pages.addWidget(game)
      
      
      