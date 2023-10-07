from PyQt5.QtWidgets import QGraphicsView
from diagram_scene import DiagramScene


class DiagramEditor(QGraphicsView):
   def __init__(self):
      super().__init__(DiagramScene())
      
      self.setDragMode(self.RubberBandDrag)