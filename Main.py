import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import MainWindow

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 500)
    window.move(300, 300)
    window.setWindowTitle('Books Unpacker')
    window.show()
    
    sys.exit(app.exec_())
