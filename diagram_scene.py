from PyQt5.QtWidgets import QGraphicsScene

class DiagramScene(QGraphicsScene):
   def __init__(self):
      super().__init__()
      
      from PyQt5.QtWidgets import QGraphicsEllipseItem
      from PyQt5.QtGui import QColor, QBrush
      ellipse =  QGraphicsEllipseItem(0, 0, 100, 200)
      ellipse.setFlag(ellipse.ItemIsMovable, True)
      ellipse.setBrush(QBrush(QColor(0, 255, 0)))
      self.addItem(ellipse)
      
      from node import Node
      
      for k in range(3):            
         node = Node(label =str(k))
         self.addItem(node)