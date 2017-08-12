import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QMainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
