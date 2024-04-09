import sys
import re
import random
import string
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainmenu import Ui_Dialog
from secwindow3x3 import Ui_secwindow3x3
from secwindow4x4 import Ui_secwindow4x4
from secwindow5x5 import Ui_secwindow5x5
from gamelevels import Ui_gamelevels
from rules import Ui_rules

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.open_gamelevels)
        self.ui.rules.clicked.connect(self.open_rules)
        self.ui.exit.clicked.connect(self.close)

    def open_gamelevels(self):
        self.game_levels = GameLevels()
        self.game_levels.show()
        self.hide()

    def open_rules(self):
        self.rules_window = RulesWindow()
        self.rules_window.show()

class RulesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_rules()
        self.ui.setupUi(self)

class GameLevels(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_gamelevels()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_mainmenu)
        self.ui.play3x3.clicked.connect(self.open_secwindow3x3)
        self.ui.play4x4.clicked.connect(self.open_secwindow4x4)
        self.ui.play5x5.clicked.connect(self.open_secwindow5x5)

    def open_secwindow3x3(self):
        self.sec_window3x3 = SecWindow3x3()
        self.sec_window3x3.show()
        self.hide()

    def open_secwindow4x4(self):
        self.sec_window4x4 = SecWindow4x4()
        self.sec_window4x4.show()
        self.hide()
    def open_secwindow5x5(self):
        self.sec_window5x5 = SecWindow5x5()
        self.sec_window5x5.show()
        self.hide()

    def back_to_mainmenu(self):
        self.close()
        main_menu.show()

class SecWindow3x3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_secwindow3x3()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_gamelevels)
        self.letters3x3 = []
        self.positions3x3 = []
        self.variants3x3 = [
            [(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0), (1, 1), (0, 1), (0, 2), (2, 1), (2, 2), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        ]
        self.searchThreeLetterWords()
#------------------------------------------------------------------------------------------------3 слова по 3 буквы в каждом
    def searchThreeLetterWords(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_words = re.findall(r'\b\w{3}\b', text)
            random_words = self.selectRandomWords(three_letter_words)
            self.delenie3po3(random_words)
            self.zapolnenie3po3()

    def selectRandomWords(self, words):
        # Проверяем, что в списке есть хотя бы 3 слова
        if len(words) < 3:
            return ["Не хватает слов"]
        # Выбираем 3 случайные слова
        return random.sample(words, 3)

    def delenie3po3(self, words):
        # Проверяем, что в списке есть ровно 3 слова
        if len(words) != 3:
            print("Ошибка, не 3 слова")
            return

        # Выбираем случайный вариант расстановки
        self.positions3x3 = random.choice(self.variants3x3)

        # Разделяем слова на буквы и добавляем их в список букв
        for word in words:
            self.letters3x3.extend(list(word))

    def zapolnenie3po3(self):
        if len(self.letters3x3) != len(self.positions3x3):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3x3)):
            row, col = self.positions3x3[i]
            item = QTableWidgetItem(self.letters3x3[i].upper())
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-------------------------------------------------------------------------------------------------------------------





    def back_to_gamelevels(self):
        self.close()
        game_levels.show()

class SecWindow4x4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_secwindow4x4()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_gamelevels)

    def game4x4(self):
        pass

    def back_to_gamelevels(self):
        self.close()
        game_levels.show()
class SecWindow5x5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_secwindow5x5()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_gamelevels)

    def game5x5(self):
        pass

    def back_to_gamelevels(self):
        self.close()
        game_levels.show()

app = QApplication(sys.argv)
main_menu = MainMenu()
game_levels = GameLevels()
main_menu.show()
sys.exit(app.exec_())