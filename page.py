from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QFont

class Page(QWidget):
   def __init__(self, title: str):
      super().__init__()
      self._title = QLabel(title)
      self._title.setFont(QFont(self._title.font().family(), 30))
      self.setLayout(QGridLayout())
      self.layout().addWidget(self._title)