import sys
import re
import random
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
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
        self.letters3and6 = []
        self.positions3and6 = []
        self.letters4and5 = []
        self.positions4and5 = []
#-----------------------------------------------------------------------------------------------------------------------
                                                #Позиции на поле
        self.variants3x3 = [
            [(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (2, 0), (2, 1), (2, 2)],
            #[(0, 0), (1, 0), (2, 0), (1, 1), (0, 1), (0, 2), (2, 1), (2, 2), (1, 2)],
            #[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
        ]
        self.variants3and6 = [
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)]
           # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
           # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)]
        ]
        self.variants4and5 = [
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (1, 1), (1, 0), (2, 0)]
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)],
            #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1), (2, 0)]
        ]
        self.randomWordsPlace()
#-----------------------------------------------------------------------------------------------------------------------
                                          #Выделение ячеек

        self.ui.tableWidget.itemEntered.connect(self.on_item_entered)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectItems)
        self.mouse_pressed = False
        self.ui.tableWidget.viewport().installEventFilter(self)
        self.highlighted_items = []
        self.chosen_words = []
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

    def on_item_entered(self, item):
        if self.mouse_pressed:
            self.highlight_item(item)

    def highlight_item(self, item):
        if item not in self.highlighted_items:
            item.setBackground(QColor(255, 0, 0))
            self.highlighted_items.append(item)

    def reset_colors(self):
        for item in self.highlighted_items:
            if item.background().color() != QColor(0, 255, 0): #если зелёный, значит правильно иначе в белый
                item.setBackground(QColor(255, 255, 255))

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mouse_pressed = True
            self.ui.tableWidget.viewport().setCursor(Qt.ClosedHandCursor)
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouse_pressed = False
            self.ui.tableWidget.viewport().setCursor(Qt.ArrowCursor)
            self.check_word()
        return super().eventFilter(source, event)

    # если выбранные ячейки соответсвуют позициям расстановки слова то она окрашивается в зелёный и закрепляется
    def check_word(self):
        selected_positions = [(item.row(), item.column()) for item in self.highlighted_items]
        if self.place == self.searchWords3and6:
            if selected_positions == self.positions3and6[:3] or selected_positions == self.positions3and6[3:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()
        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
                                        # Случайный выбор количества слов
    def randomWordsPlace(self):
        choice = random.choice(['3and6', '4and5', '3x3'])
        if choice == '3and6':
            self.place = self.searchWords3and6
        elif choice == '4and5':
            self.place = self.searchWords4and5
        elif choice == '3x3':
            self.place = self.searchThreeLetterWords

        self.place()

#-----------------------------------------------------------------------------------------------------------------------
                                            #3 слова по 3 буквы в каждом
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
#-----------------------------------------------------------------------------------------------------------------------
                                        #2 слова, 1-ое 3 буквы 2-ое 6 букв
    def searchWords3and6(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_words = re.findall(r'\b\w{3}\b', text)
            six_letter_words = re.findall(r'\b\w{6}\b', text)
            random_three_word = self.selectRandomWords(three_letter_words)
            random_six_word = self.selectRandomWords(six_letter_words)
            self.delenie3and6(random_three_word, random_six_word)
            self.zapolnenie3and6()
    def selectRandomWords3and6(self, three_letter_words, six_letter_words):
        if len(three_letter_words) < 1 or len(six_letter_words) < 1:
            return ["Не хватает слов"]
        return random.choice(three_letter_words), random.choice(six_letter_words)


    def delenie3and6(self, three_word, six_word):
        if len(three_word) < 1 or len(six_word) < 1:
            print("Ошибка delenie3and6")
            return
        self.positions3and6 = random.choice(self.variants3and6)

        self.letters3and6.extend(list(three_word[0]))
        self.letters3and6.extend(list(six_word[0]))

    def zapolnenie3and6(self):
        if len(self.letters3and6) != len(self.positions3and6):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3and6)):
            row, col = self.positions3and6[i]
            item = QTableWidgetItem(self.letters3and6[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)

#-----------------------------------------------------------------------------------------------------------------------
                                            #2 слова, 1-ое 4 буквы 2-ое 5 букв
    def searchWords4and5(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            four_letter_words = re.findall(r'\b\w{4}\b', text)
            five_letter_words = re.findall(r'\b\w{5}\b', text)
            random_four_word = self.selectRandomWords(four_letter_words)
            random_five_word = self.selectRandomWords(five_letter_words)
            self.delenie4and5(random_four_word, random_five_word)
            self.zapolnenie4and5()

    def selectRandomWords4and5(self, four_letter_words, five_letter_words):
        if len(four_letter_words) < 1 or len(five_letter_words) < 1:
            return ["Не хватает слов"]
        return random.choice(four_letter_words), random.choice(five_letter_words)


    def delenie4and5(self, four_word, five_word):
        if len(four_word) < 1 or len(five_word) < 1:
            print("Ошибка delenie4and5")
            return

        self.positions4and5 = random.choice(self.variants4and5)

        self.letters4and5.extend(list(four_word[0]))
        self.letters4and5.extend(list(five_word[0]))

    def zapolnenie4and5(self):
        if len(self.letters4and5) != len(self.positions4and5):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters4and5)):
            row, col = self.positions4and5[i]
            item = QTableWidgetItem(self.letters4and5[i].upper())
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
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