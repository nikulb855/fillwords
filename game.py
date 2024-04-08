import sys
import random
import string
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainmenu import Ui_Dialog
from secwindow import Ui_secwindow
from rules import Ui_rules

rowBoxChecked = False
columnBoxChecked = False
generateAll = True

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.open_secwindow)
        self.ui.rules.clicked.connect(self.open_rules)
        self.ui.exit.clicked.connect(self.close)

    def open_secwindow(self):
        self.sec_window = SecWindow()
        self.sec_window.show()
        self.hide()

    def open_rules(self):
        self.rules_window = RulesWindow()
        self.rules_window.show()

class RulesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_rules()
        self.ui.setupUi(self)


class SecWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_secwindow()
        self.ui.setupUi(self)
        self.words = []
        self.selected_letters = []
        self.ui.back.clicked.connect(self.back_to_mainmenu)
        self.createTable()
        self.xVisited = []
        self.yVisited = []



    def Game(self):


    def back_to_mainmenu(self):
        self.close()
        main_menu.show()

app = QApplication(sys.argv)
main_menu = MainMenu()
main_menu.show()
sys.exit(app.exec_())