from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize, QFile, Qt, QEvent, QPoint, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QBrush, QColor, QPainter, QPixmap, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QTreeWidgetItem, QLabel, QSizePolicy
from PyQt5 import QtCore
import sys
import qtawesome
import threading
import random
import time
print(random.randint(0, 9))
from UI_main import Ui_MainWindow


num=15

colors=[QColor(255, 0 ,0),QColor(	255 ,165 ,0),QColor(255 ,255, 0),QColor(0, 255, 0),QColor(127 ,255 ,212),QColor(0 ,0, 255),QColor(155,48,255)]

class MainUi(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.init_UI()
        self.show_thread = threading.Thread(target=self.flamboyant_show)
        self.show_thread.start()

    def init_UI(self):
        self.chessboard=[]
        for i in range(num):
            for j in range(num):
                label=QtWidgets.QLabel("")
                background_color = QColor(0,0,0)

                # 初始化标签控件
                label.setAutoFillBackground(True)
                palette = QPalette()
                palette.setColor(QPalette.Window, background_color)
                label.setPalette(palette)

                self.chessboard.append(label)
                self.gridLayout.addWidget(label,i,j)
                self.gridLayout.setSpacing(0)

    def flamboyant_show(self):
        while True:
            for i in range(num):
                for j in range(num):
                    index = i * num + j

                    palette = QPalette()
                    palette.setColor(QPalette.Window, colors[random.randint(0,len(colors)-1)])
                    self.chessboard[index].setPalette(palette)
                    time.sleep(0.0001)



def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()