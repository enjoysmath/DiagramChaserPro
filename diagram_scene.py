from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtCore import QPointF

class DiagramScene(QGraphicsScene):
   default_grid_pen = QPen(QColor(0, 0, 0), 1.5)
   default_grid_size = 100
   
   def __init__(self):
      super().__init__()
      
      
      self._gridPen = self.default_grid_pen
      self._gridSize = self.default_grid_size
      
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
         
   @property     
   def grid_size(self):
      return self._gridSize
         
   def set_grid_size(self, size: int):
      if self._gridSize != size:
         self._gridSize = size
         self.update()
         
   @property
   def grid_pen(self):
      return self._gridPen
   
   def set_grid_pen(self, pen):
      if self._gridPen != pen:
         self._gridPen = pen
         self.update()
         
   def drawBackground(self, painter, rect):
      painter.setPen(self.grid_pen)      
      grid_size = self.grid_size
            
      left = int(rect.left()) - (int(rect.left()) % grid_size)
      top =  int(rect.top()) - (int(rect.top()) % grid_size)
      points = []
      
      x = left
      
      while x < rect.right():
         y = top
         while y < rect.bottom():
            points.append(QPointF(x, y))            
            y += grid_size
         x += grid_size
         
      painter.drawPoints(points)