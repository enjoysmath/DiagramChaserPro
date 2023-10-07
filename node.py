from PyQt5.QtCore import pyqtSignal, QRectF, Qt, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen, QPainter
from PyQt5.QtWidgets import QGraphicsObject, QApplication
from label import Label

class Node(QGraphicsObject):
   default_rect = QRectF(-50, -50, 100, 100)
   default_brush = QBrush(QColor(255, 255, 0))
   default_pen = QPen(Qt.NoPen)
   default_corner_radius = 15
   default_selection_pen = QPen(QColor(10, 110, 255), 4)
   default_padding = 10

   def __init__(self, label: str = None):
      super().__init__()
      self._rect = self.default_rect
      self._brush = self.default_brush
      self._pen = self.default_pen
      self._cornerRadius = self.default_corner_radius
      self._selectionPen = self.default_selection_pen
      self._rectPadding = self.default_padding

      if label:
         self.add_label(label)

      self.setFlags(self.ItemIsMovable | self.ItemIsFocusable | self.ItemIsSelectable | self.ItemSendsGeometryChanges)



   def boundingRect(self) -> QRectF:
      return self._rect

   @property
   def brush(self):
      return self._brush

   def set_brush(self, brush: QBrush):
      if self._brush != brush:
         self._brush = brush
         self.update()

   @property
   def pen(self) -> QPen:
      return self._pen

   def set_pen(self, pen: QPen):
      if self._pen != pen:
         self._pen = pen
         self.update()

   @property
   def selection_pen(self) -> QPen:
      return self._selectionPen

   def paint(self, painter: QPainter, option, widget):
      painter.setRenderHints(QPainter.Antialiasing)
      if self.isSelected():
         pen = self.selection_pen
      else:
         pen = self.pen
      painter.setBrush(self.brush)
      painter.setPen(pen)
      radius = self._cornerRadius
      painter.drawRoundedRect(self._rect, radius, radius)

   def add_label(self, label):
      label = Label(label)
      label.setParentItem(self)
      p = self._rectPadding
      self._rect = self.childrenBoundingRect().adjusted(-p, -p, p, p)




   def itemChange(self, change, value):
      scene = self.scene()
      
      if change == self.ItemPositionChange and scene:
         new_pos = value
         
         if QApplication.mouseButtons() == Qt.LeftButton:
            grid_size = scene.grid_size
            
            x = int(new_pos.x()/grid_size)*grid_size
            y = int(new_pos.y()/grid_size)*grid_size
            
            return QPointF(x, y)
         
         else:
            return new_pos
      else:
         return super().itemChange(change, value)
