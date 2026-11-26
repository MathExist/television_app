from gui import Ui_MainWindow
from PyQt6.QtWidgets import *
from gui import *
from television import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tv = Television()