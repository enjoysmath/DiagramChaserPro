from PyQt5.QtWidgets import * 
from page import Page

class Game(QWidget):
   def __init__(self, title: str):
      super().__init__()
      self.setLayout(QGridLayout())
      self._pages = QStackedWidget()
      self.layout().addWidget(self._pages)
      self.add_page(Page(title))
            
   def add_page(self, page: Page):
      self._pages.addWidget(page)
      return page
   
   def nth_page(self, n: int) -> Page:
      """
      Returns the nth page in a 1-based index, so the first page
      is actually n = 1 and not n = 0.
      """
      return self._pages.widget(n - 1)
   
   def get_paragraph(self, text: str) -> QLabel:
      label = QLabel(text)
      font = label.font()
      font.setPointSize(15)
      label.setFont(font)
      return label
   
   