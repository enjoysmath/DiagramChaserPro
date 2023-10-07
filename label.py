from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QColor

class Label(QGraphicsTextItem):
   default_color = QColor(0, 0, 0)
   
   def __init__(self, text: str):
      super().__init__(text)
      self.setDefaultTextColor(self.default_color)
      