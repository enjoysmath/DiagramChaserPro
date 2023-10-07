from game import Game
from PyQt5.QtWidgets import QLabel


class IdentityIsUnique(Game):
   def __init__(self):
      super().__init__(title="Identity arrows are unique!")
      
      first_page = self.nth_page(1)
      self._introText = self.get_paragraph(
         """By definition, for each object X of a category <b>C</b> <br>
         there exists (at least one) identity arrow <b>id</b><sub>X</sub>, <br>
         which means <b>id</b><sub>X</sub>○f = f and g○<b>id</b><sub>X</sub> = g <br>
         any time those compositions are defined. <br>
         In other words, there exists a special arrow <br>
         that is both a left and a right identity with <br>
         respect to composition. """)
      
      self._goalText = self.get_paragraph(
         """
         The goal of this lesson is to teach you that <br>
         there is only one such arrow.  In other words <br>
         <b>id</b><sub>X</sub> is uniquely determined <br>
         for each object X in <b>C</b>.
         """)
      
      first_page.layout().addWidget(self._introText)
      first_page.layout().addWidget(self._goalText)
            