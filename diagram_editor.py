from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt
from diagram_scene import DiagramScene



class DiagramEditor(QGraphicsView):
   default_zoom_factor = 1.2
   
   def __init__(self):
      super().__init__(DiagramScene())
      self._zoomFactor = self.default_zoom_factor
      self.setDragMode(self.RubberBandDrag)
      
   @property
   def zoom_factor(self) -> float:
      return self._zoomFactor
   
   def set_zoom_factor(self, factor: float):
      if self._zoomFactor != factor:         
         self._zoomFactor = factor
      
   def wheelEvent(self, event):      
      if event.modifiers() & Qt.ControlModifier:
         factor = self.zoom_factor
         
         if event.angleDelta().y() > 0:
            self.scale(factor, factor)            
         else:
            self.scale(1.0 / factor, 1.0 / factor)
            
      else:
         super().wheelEvent(event)
   
   def keyPressEvent(self, event):
      factor = self.zoom_factor
      if event.modifiers() & Qt.ControlModifier:
         if event.key() == Qt.Key_Equal:
            self.scale(factor, factor)      
         elif event.key() == Qt.Key_Minus:
            self.scale(1.0 / factor, 1.0 / factor)
         else:
            super().keyPressEvent(event)
      else:
         super().keyPressEvent(event)
         
            
            
            
# Mouse wheel zooms in / out only if control is pressed
      
# Also ctrl +/- should zoom in / out