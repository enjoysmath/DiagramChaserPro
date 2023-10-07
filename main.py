from PyQt5.QtWidgets import QApplication
import sys
from main_window import MainWindow
from PyQt5.QtGui import QFont

if __name__ == '__main__':
   app = QApplication([])
   app.setFont(QFont('Times New Roman', 16))
   window = MainWindow()
   window.show()
   
   sys.exit(app.exec_())