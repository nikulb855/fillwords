import sys
import re
import random
from PyQt5.QtCore import Qt, QEvent, QMimeData
from PyQt5.QtGui import QColor, QDrag
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from mainmenu import Ui_Dialog
from secwindow3x3 import Ui_secwindow3x3
from secwindow4x4 import Ui_secwindow4x4
from secwindow5x5 import Ui_secwindow5x5
from gamelevels import Ui_gamelevels
from rules import Ui_rules
from zanovo import Ui_zanovo_2
from rating import Ui_Rating
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.open_gamelevels)
        self.ui.rules.clicked.connect(self.open_rules)
        self.ui.exit.clicked.connect(self.close)
        self.ui.rating.clicked.connect(self.open_ratingmenu)
        self.ui.nickname.textChanged.connect(self.on_text_edited)
        self.nickname = ""
        self.max_length = 12
    def on_text_edited(self, text):
        #фильтрация ввода
        filtered_text = re.sub(r'[^\w_]', '', text)

        if len(filtered_text) > self.max_length:
            QMessageBox.warning(self, "Ошибка", f"Превышен лимит символов. Максимум {self.max_length}.")
            filtered_text = filtered_text[:self.max_length]

        if text != filtered_text:
            self.ui.nickname.setText(filtered_text)
            self.ui.nickname.setCursorPosition(len(filtered_text))
    def open_ratingmenu(self):
        self.rating = RatingMenu()
        self.rating.show()
        self.hide()

    def save_nickname(self):
    #получение никнейма из поля для ввода никнейма
        self.nickname = self.ui.nickname.text().strip()

    #если поле пустое то происходит выход из функции без изменений
        if not self.nickname:
            return
    #проверка существующих никнеймов
        with open('nicknames.txt', 'r', encoding='utf8') as file:
            nicknames = set(line.strip() for line in file)

    #если никнейм уже существует то повторной записи никнейма не будет
        if self.nickname in nicknames:
            return
    #добавление никнейма в текстовый файл
        with open('nicknames.txt', 'a', encoding='utf8') as file:
            file.write(self.nickname + '\n')

    def open_gamelevels(self):
        self.save_nickname()
        self.game_levels = GameLevels(self.nickname)
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

class RatingMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Rating()
        self.ui.setupUi(self)
        self.nicknamesfromtxt()
        self.ui.back.clicked.connect(self.back_to_mainmenu)
        
    def back_to_mainmenu(self):
        self.menu = MainMenu()
        self.menu.show()
        self.hide()
    def nicknamesfromtxt(self):
        with open('rating.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
        ratings = []
        for line in lines:
            nickname, score = line.strip().split(':')
            ratings.append((nickname, int(score)))

        ratings.sort(key=lambda x: x[1], reverse=True)

        nicknames = ["Лидирует {} с {} {}".format(ratings[0][0], ratings[0][1], self.sklonenielider(ratings[0][1]))]
        nicknames += ["{}: {} {}".format(nickname, score, self.sklonenie(score)) for nickname, score in
                      ratings[1:]]
        self.ui.label.setText('\n'.join(nicknames))

    def sklonenielider(self, score):
        if score % 10 == 1 and score % 100 != 11:
            return "баллом"
        else:
            return "баллами"

    def sklonenie(self, score):
        if score % 10 == 1 and score % 100 != 11:
            return "балл"
        elif 2 <= score % 10 <= 4 and (score % 100 < 10 or score % 100 > 20):
            return "балла"
        else:
            return "баллов"

class GameLevels(QMainWindow):
    def __init__(self, nickname):
        super().__init__()
        self.ui = Ui_gamelevels()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_mainmenu)
        self.ui.play3x3.clicked.connect(lambda: self.open_secwindow(1))
        self.ui.play4x4.clicked.connect(lambda: self.open_secwindow(2))
        self.ui.play5x5.clicked.connect(lambda: self.open_secwindow(3))
        self.nickname = nickname
        self.selected_level = None

    def open_secwindow(self, level):
        if level == 1:
            self.sec_window = SecWindow3x3(self.nickname)
        elif level == 2:
            self.sec_window = SecWindow4x4(self.nickname)
        elif level == 3:
            self.sec_window = SecWindow5x5(self.nickname)

        self.sec_window.show()
        self.hide()

        self.selected_level = level
    def back_to_mainmenu(self):
        self.hide()
        main_menu.show()

class Zanovo(QMainWindow):
    def __init__(self, nickname, selected_level):
        super().__init__()
        self.ui = Ui_zanovo_2()
        self.ui.setupUi(self)
        self.ui.glmenu.clicked.connect(self.back_to_mainmenu)
        self.ui.zanovo.clicked.connect(self.open_secwindow)
        self.ui.exit.clicked.connect(self.close)
        self.nickname = nickname
        self.level = selected_level
        self.update_rating_label()


    def update_rating_label(self):
        word = ''
        with open('rating.txt', 'r', encoding='utf8') as file:
            for line in file:
                nickname, score = line.strip().split(':')
                if nickname == self.nickname:
                    score = int(score)
                    #определяю как использовать слово балл :)
                    if score % 10 == 1 and score % 100 != 11:
                        word = 'балл'
                    elif 2 <= score % 10 <= 4 and (score % 100 < 10 or score % 100 > 20):
                        word = 'балла'
                    else:
                        word = 'баллов'
                    break
        if word:
            self.ui.label_2.setText(f"Сейчас у вас уже {score} {word}!")
    def back_to_mainmenu(self):
        self.gamelevels = GameLevels(self.nickname)
        self.gamelevels.show()
        self.hide()

    def open_secwindow(self):
        if self.level == 1:
            self.sec_window = SecWindow3x3(self.nickname)
        elif self.level == 2:
            self.sec_window = SecWindow4x4(self.nickname)
        elif self.level == 3:
            self.sec_window = SecWindow5x5(self.nickname)
        self.sec_window.show()
        self.hide()
class SecWindow3x3(QMainWindow):
    def __init__(self, nickname):
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
            [(0, 0), (1, 0), (2, 0), (1, 1), (0, 1), (0, 2), (2, 1), (2, 2), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
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
        self.score = 0
        self.nickname = nickname
        self.selected_level = 1
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

    def on_item_entered(self, item):
        if item.background().color() != QColor(0, 255, 0):
            item.setBackground(QColor(255, 0, 0))
            self.highlighted_items.append(item)


    def check_all_cells_green(self):
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item.background().color() != QColor(0, 255, 0):
                    return
        self.score += 1
        self.update_rating()
        self.open_zanovo3x3()

    def update_rating(self):
        if not self.nickname:
            return

        with open('rating.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()

        updated_lines = []
        found = False
        for line in lines:
            nickname, score = line.strip().split(':')
            if nickname == self.nickname:
                updated_lines.append(f"{nickname}:{int(score) + self.score}\n")
                found = True
            else:
                updated_lines.append(line)

        if not found:
            updated_lines.append(f"{self.nickname}:{self.score}\n")

        with open('rating.txt', 'w', encoding='utf8') as file:
            file.writelines(updated_lines)

    def open_zanovo3x3(self):
        self.zanovo3x3 = Zanovo(self.nickname, self.selected_level)
        self.zanovo3x3.show()
        self.hide()

    def reset_colors(self):
        for item in self.highlighted_items:
            if item.background().color() != QColor(0, 255, 0):
                item.setBackground(QColor(255, 255, 255))
        self.highlighted_items.clear()

                                                #Контроль перемещения мыши по полю
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            item = self.ui.tableWidget.itemAt(event.pos())
            if item is not None and item.background().color() == QColor(0, 255, 0):
                self.mouse_pressed = True
                self.previous_item_pos = event.pos()
                return True
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouse_pressed = False
            self.check_word()
            self.check_all_cells_green()
            return True
        elif event.type() == QEvent.MouseMove and self.mouse_pressed:
            item = self.ui.tableWidget.itemAt(event.pos())
            previous_item = self.ui.tableWidget.itemAt(self.previous_item_pos)
            if item is not None and previous_item is not None:
                if previous_item.background().color() != QColor(0, 255, 0) and \
                        item.background().color() != QColor(0, 255, 0):
                    drag = QDrag(self)
                    mime_data = QMimeData()
                    drag.setMimeData(mime_data)
                    drag.exec_(Qt.MoveAction)
                else:
                    return True
            else:
                return True
        return super().eventFilter(source, event)

    # если выбранные ячейки соответсвуют позициям расстановки слова то она окрашивается в зелёный и закрепляется
    def check_word(self):
        selected_positions = [(item.row(), item.column()) for item in self.highlighted_items]

        #Для расставноки 3 слов по 3 буквы
        if self.place == self.searchThreeLetterWords:
            if selected_positions == self.positions3x3[:3] or \
                    selected_positions == self.positions3x3[3:6] or \
                    selected_positions == self.positions3x3[6:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        #Для расстановки 2 слов по 5 и 6 букв
        elif self.place == self.searchWords3and6:
            if selected_positions == self.positions3and6[:3] or selected_positions == self.positions3and6[3:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        #Для расстановки 2 слов по 4 и 5 букв
        elif self.place == self.searchWords4and5:
            if selected_positions == self.positions4and5[:4] or selected_positions == self.positions4and5[4:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
                                        # Случайный выбор расстановки и количества слов
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
        if len(words) < 3:
            return ["Не хватает слов"]
        return random.sample(words, 3)

    def delenie3po3(self, words):
        if len(words) != 3:
            print("Ошибка, не 3 слова")
            return

        self.positions3x3 = random.choice(self.variants3x3)

        for word in words:
            self.letters3x3.extend(list(word))
    def zapolnenie3po3(self):
        if len(self.letters3x3) != len(self.positions3x3):
            print("Количество букв и позиций должно быть одинаковым333.")
            return

        for i in range(len(self.letters3x3)):
            row, col = self.positions3x3[i]
            item = QTableWidgetItem(self.letters3x3[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                        #2 слова, 1-ое 3 буквы 2-ое 6 букв
    def searchWords3and6(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_words = re.findall(r'\b\w{3}\b', text)
            six_letter_words = re.findall(r'\b\w{6}\b', text)
            random_three_word, random_six_word = self.selectRandomWords3and6(three_letter_words, six_letter_words)
            self.delenie3and6(random_three_word, random_six_word)
            self.zapolnenie3and6()
    def selectRandomWords3and6(self, three_letter_words, six_letter_words):
        if len(three_letter_words) < 1 or len(six_letter_words) < 1:
            return ["Не хватает слов"]
        return random.choice(three_letter_words), random.choice(six_letter_words)


    def delenie3and6(self, three_word, six_word):
        if len(three_word) < 1 or len(six_word) < 1:
            print("Ошибка delenie3and6")

        self.positions3and6 = random.choice(self.variants3and6)

        self.letters3and6.extend(list(three_word))
        self.letters3and6.extend(list(six_word))
    def zapolnenie3and6(self):
        if len(self.letters3and6) != len(self.positions3and6):
            print("Количество букв и позиций должно быть одинаковым1.")
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
            random_four_word, random_five_word = self.selectRandomWords4and5(four_letter_words, five_letter_words)
            self.delenie4and5(random_four_word, random_five_word)
            self.zapolnenie4and5()

    def selectRandomWords4and5(self, four_letter_words, five_letter_words):
        if len(four_letter_words) < 1 or len(five_letter_words) < 1:
            return ["Не хватает слов"]
        return random.choice(four_letter_words), random.choice(five_letter_words)


    def delenie4and5(self, four_word, five_word):
        if len(four_word) < 1 or len(five_word) < 1:
            print("Ошибка delenie4and5")

        self.positions4and5 = random.choice(self.variants4and5)

        self.letters4and5.extend(list(four_word))
        self.letters4and5.extend(list(five_word))
    def zapolnenie4and5(self):
        if len(self.letters4and5) != len(self.positions4and5):
            print("Количество букв и позиций должно быть одинаковым2.")
            return

        for i in range(len(self.letters4and5)):
            row, col = self.positions4and5[i]
            item = QTableWidgetItem(self.letters4and5[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
    def back_to_gamelevels(self):
        self.gamelevels = GameLevels(self.nickname)
        self.gamelevels.show()
        self.close()

class SecWindow4x4(QMainWindow):
    def __init__(self, nickname):
        super().__init__()
        self.ui = Ui_secwindow4x4()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_gamelevels)
        self.letters3346 = []
        self.positions3346 = []
        self.letters3445 = []
        self.positions3445 = []
        self.letters457 = []
        self.positions457 = []
        self.letters3355 = []
        self.positions3355 = []
        self.letters367 = []
        self.positions367 = []
        self.letters3337 = []
        self.positions3337 = []
        self.letters4444 = []
        self.positions4444 = []
# -----------------------------------------------------------------------------------------------------------------------
                                     # Позиции на поле
        self.variants3346 = [
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (1, 0), (1, 1),
             (1, 2), (2, 2), (3, 3), (3, 2), (3, 1), (2, 1), (2, 0), (3, 0)]
        ]
        self.variants3445 = [
            [(1, 0), (2, 0), (3, 0), (0, 2), (0, 3), (1, 3), (1, 2), (3, 2),
             (2, 2), (2, 3), (3, 3), (0, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
        ]
        self.variants457 = [
            [(3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (0, 1), (0, 2),
             (0, 3), (2, 2), (2, 1), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)]
        ]
        self.variants3355 = [
            [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (2, 3), (3, 3),
             (3, 2), (3, 1), (2, 1), (2, 2), (1, 2), (1, 3), (0, 3), (0, 2)]
        ]
        self.variants367 = [
            [(3, 2), (3, 3), (2, 3), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2),
             (2, 2), (1, 1), (2, 1), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)]
        ]
        self.variants3337 = [
            [(0, 0), (0, 1), (0, 2), (2, 3), (3, 3), (3, 2), (2, 0), (3, 0),
             (3, 1), (0, 3), (1, 3), (1, 2), (2, 2), (2, 1), (1, 1), (1, 0)]
        ]
        self.variants4444 = [
            [(0, 0), (0, 1), (0, 2), (0, 3), (3, 2), (3, 3), (2, 3), (1, 3),
             (2, 1), (2, 2), (1, 2), (1, 1), (3, 1), (3, 0), (2, 0), (1, 0)]
        ]
        self.randomWordsPlace()
# -----------------------------------------------------------------------------------------------------------------------
                                        # Выделение ячеек

        self.ui.tableWidget.itemEntered.connect(self.on_item_entered)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectItems)
        self.mouse_pressed = False
        self.ui.tableWidget.viewport().installEventFilter(self)
        self.highlighted_items = []
        self.chosen_words = []
        self.score = 0
        self.nickname = nickname
        self.selected_level = 2
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

    def on_item_entered(self, item):
        if item.background().color() != QColor(0, 255, 0):
            item.setBackground(QColor(255, 0, 0))
            self.highlighted_items.append(item)

    def check_all_cells_green(self):
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item.background().color() != QColor(0, 255, 0):
                    return
        self.score += 2
        self.update_rating()
        self.open_zanovo4x4()

    def update_rating(self):
        if not self.nickname:
            return

        with open('rating.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()

        updated_lines = []
        found = False
        for line in lines:
            nickname, score = line.strip().split(':')
            if nickname == self.nickname:
                updated_lines.append(f"{nickname}:{int(score) + self.score}\n")
                found = True
            else:
                updated_lines.append(line)

        if not found:
            updated_lines.append(f"{self.nickname}:{self.score}\n")

        with open('rating.txt', 'w', encoding='utf8') as file:
            file.writelines(updated_lines)

    def open_zanovo4x4(self):
        self.zanovo4x4 = Zanovo(self.nickname, self.selected_level)
        self.zanovo4x4.show()
        self.hide()

    def reset_colors(self):
        for item in self.highlighted_items:
            if item.background().color() != QColor(0, 255, 0):
                item.setBackground(QColor(255, 255, 255))
        self.highlighted_items.clear()

                            # Контроль перемещения мыши по полю

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            item = self.ui.tableWidget.itemAt(event.pos())
            if item is not None and item.background().color() == QColor(0, 255, 0):
                self.mouse_pressed = True
                self.previous_item_pos = event.pos()
                return True
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouse_pressed = False
            self.check_word()
            self.check_all_cells_green()
            return True
        elif event.type() == QEvent.MouseMove and self.mouse_pressed:
            item = self.ui.tableWidget.itemAt(event.pos())
            previous_item = self.ui.tableWidget.itemAt(self.previous_item_pos)
            if item is not None and previous_item is not None:
                if previous_item.background().color() != QColor(0, 255, 0) and \
                        item.background().color() != QColor(0, 255, 0):
                    drag = QDrag(self)
                    mime_data = QMimeData()
                    drag.setMimeData(mime_data)
                    drag.exec_(Qt.MoveAction)
                else:
                    return True
            else:
                return True
        return super().eventFilter(source, event)

# если выбранные ячейки соответсвуют позициям расстановки слова то она окрашивается в зелёный и закрепляется

    def check_word(self):
        selected_positions = [(item.row(), item.column()) for item in self.highlighted_items]

                        #4 слова по 3 3 4 6 букв

        if self.place == self.searchWords3346:
            if selected_positions == self.positions3346[:3] or \
                    selected_positions == self.positions3346[3:6] or \
                    selected_positions == self.positions3346[6:10] or \
                    selected_positions == self.positions3346[10:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                        #4 слова по 3 4 4 5 букв

        elif self.place == self.searchWords3445:
            if selected_positions == self.positions3445[:3] or \
                    selected_positions == self.positions3445[3:7] or \
                    selected_positions == self.positions3445[7:11] or \
                    selected_positions == self.positions3445[11:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                        #3 слова по 4 5 7 букв

        elif self.place == self.searchWords457:
            if selected_positions == self.positions457[:4] or \
                    selected_positions == self.positions457[4:9] or \
                    selected_positions == self.positions457[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                        #4 слова по 3 3 5 5 букв

        elif self.place == self.searchWords3355:
            if selected_positions == self.positions3355[:3] or \
                    selected_positions == self.positions3355[3:6] or \
                    selected_positions == self.positions3355[6:11] or \
                    selected_positions == self.positions3355[11:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                            #3 слова по 3 6 7 букв

        elif self.place == self.searchWords367:
            if selected_positions == self.positions367[:3] or \
                    selected_positions == self.positions367[3:9] or \
                    selected_positions == self.positions367[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                        #4 слова по 3 3 3 7 букв

        elif self.place == self.searchWords3337:
            if selected_positions == self.positions3337[:3] or \
                    selected_positions == self.positions3337[3:6] or \
                    selected_positions == self.positions3337[6:9] or \
                    selected_positions == self.positions3337[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                        #4 слова по 4 буквы каждое

        elif self.place == self.searchWords4444:
            if selected_positions == self.positions4444[:4] or \
                    selected_positions == self.positions4444[4:8] or \
                    selected_positions == self.positions4444[8:12] or \
                    selected_positions == self.positions4444[12:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
    def randomWordsPlace(self):
        choice = random.choice(['3346', '3445', '457', '3355', '367', '3337', '4444'])
        if choice == '3346':
            self.place = self.searchWords3346
        elif choice == '3445':
            self.place = self.searchWords3445
        elif choice == '457':
            self.place = self.searchWords457
        elif choice == '3355':
            self.place = self.searchWords3355
        elif choice == '367':
            self.place = self.searchWords367
        elif choice == '3337':
            self.place = self.searchWords3337
        elif choice == '4444':
            self.place = self.searchWords4444
        self.place()

#-----------------------------------------------------------------------------------------------------------------------
                                    #4 слова по 3 3 4 6 букв
    def searchWords3346(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_words = re.findall(r'\b\w{3}\b', text)
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            six_letter_word = re.findall(r'\b\w{6}\b', text)
            random_three_words, random_four_word, random_six_word = self.selectRandomWords3346(three_letter_words, four_letter_word, six_letter_word)
            self.delenie3346(random_three_words, random_four_word, random_six_word)
            self.zapolnenie3346()

    def selectRandomWords3346(self, three_letter_words, four_letter_word, six_letter_word):
        if len(four_letter_word) < 1 or len(six_letter_word) < 1 or len(three_letter_words) < 2:
            return ["Не хватает слов"]
        return random.sample(three_letter_words, 2), random.choice(four_letter_word), random.choice(six_letter_word)

    def delenie3346(self, three_words, four_word, six_word):
        if len(four_word) < 1 or len(six_word) < 1 or len(three_words) < 2:
            print("Ошибка delenie3346")
            return

        self.positions3346 = random.choice(self.variants3346)

        for word in three_words:
            self.letters3346.extend(list(word))
        self.letters3346.extend(list(four_word))
        self.letters3346.extend(list(six_word))

    def zapolnenie3346(self):
        if len(self.letters3346) != len(self.positions3346):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3346)):
            row, col = self.positions3346[i]
            item = QTableWidgetItem(self.letters3346[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                     #4 слова по 3 4 4 5 букв
    def searchWords3445(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_word = re.findall(r'\b\w{3}\b', text)
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            random_three_word, random_four_word, random_five_word = self.selectRandomWords3445(three_letter_word, four_letter_word, five_letter_word)
            self.delenie3445(random_three_word, random_four_word, random_five_word)
            self.zapolnenie3445()

    def selectRandomWords3445(self, three_letter_word, four_letter_word, five_letter_word):
        if len(three_letter_word) < 1 or len(four_letter_word) < 2 or len(five_letter_word) < 1:
            return ["Не хватает слов"]
        return random.choice(three_letter_word), random.sample(four_letter_word, 2), random.choice(five_letter_word)

    def delenie3445(self, three_word, four_word, five_word):
        if len(three_word) < 1 or len(four_word) < 2 or len(five_word) < 1:
            print('delenie3445')

        self.positions3445 = random.choice(self.variants3445)

        self.letters3445.extend(list(three_word))
        for word in four_word:
            self.letters3445.extend(list(word))
        self.letters3445.extend(list(five_word))

    def zapolnenie3445(self):
        if len(self.letters3445) != len(self.positions3445):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3445)):
            row, col = self.positions3445[i]
            item = QTableWidgetItem(self.letters3445[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)

#-----------------------------------------------------------------------------------------------------------------------
                                     # 3 слова по 4 5 7 букв
    def searchWords457(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_four_word, random_five_word, random_seven_word = self.selectRandomWords457(four_letter_word, five_letter_word, seven_letter_word)
            self.delenie457(random_four_word, random_five_word, random_seven_word)
            self.zapolnenie457()

    def selectRandomWords457(self, four_letter_word, five_letter_word, seven_letter_word):
        if len(four_letter_word) < 1 or len(five_letter_word) < 1 or len(seven_letter_word) < 1:
            return ["Не хватает слов"]
        return random.choice(four_letter_word), random.choice(five_letter_word), random.choice(seven_letter_word)

    def delenie457(self, four_word, five_word, seven_letter_word):
        if len(four_word) < 1 or len(five_word) < 1 or len(seven_letter_word) < 1:
            print('delenie457')

        self.positions457 = random.choice(self.variants457)

        self.letters457.extend(list(four_word))
        self.letters457.extend(list(five_word))
        self.letters457.extend(list(seven_letter_word))

    def zapolnenie457(self):
        if len(self.letters457) != len(self.positions457):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters457)):
            row, col = self.positions457[i]
            item = QTableWidgetItem(self.letters457[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                     #4 cлова по 3 3 5 5 букв
    def searchWords3355(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_word = re.findall(r'\b\w{3}\b', text)
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            random_three_word, random_five_word = self.selectRandomWords3355(three_letter_word, five_letter_word)
            self.delenie3355(random_three_word, random_five_word)
            self.zapolnenie3355()

    def selectRandomWords3355(self, three_letter_word, five_letter_word):
        if len(three_letter_word) < 2 or len(five_letter_word) < 2:
            return ["Не хватает слов"]
        return random.sample(three_letter_word,  2), random.sample(five_letter_word, 2)

    def delenie3355(self, three_word, five_word,):
        if len(three_word) < 2 or len(five_word) < 2:
            print('delenie3355')

        self.positions3355 = random.choice(self.variants3355)

        for word in three_word:
            self.letters3355.extend(word)
        for word in five_word:
            self.letters3355.extend(word)

    def zapolnenie3355(self):
        if len(self.letters3355) != len(self.positions3355):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3355)):
            row, col = self.positions3355[i]
            item = QTableWidgetItem(self.letters3355[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                      #3 слова по 3 6 7 букв

    def searchWords367(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_word = re.findall(r'\b\w{3}\b', text)
            six_letter_word = re.findall(r'\b\w{6}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_three_word, random_six_word, random_seven_word = self.selectRandomWords367(three_letter_word, six_letter_word, seven_letter_word)
            self.delenie367(random_three_word, random_six_word, random_seven_word)
            self.zapolnenie367()

    def selectRandomWords367(self, three_letter_word, six_letter_word, seven_letter_word):
        if len(three_letter_word) < 1 or len(six_letter_word) < 1 or len(seven_letter_word) < 1:
            return ["Не хватает слов"]
        return random.choice(three_letter_word), random.choice(six_letter_word), random.choice(seven_letter_word)

    def delenie367(self, three_word, six_word, seven_letter_word):
        if len(three_word) < 1 or len(six_word) < 1 or len(seven_letter_word) < 1:
            print('delenie367')

        self.positions367 = random.choice(self.variants367)

        self.letters367.extend(list(three_word))
        self.letters367.extend(list(six_word))
        self.letters367.extend(list(seven_letter_word))

    def zapolnenie367(self):
        if len(self.letters367) != len(self.positions367):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters367)):
            row, col = self.positions367[i]
            item = QTableWidgetItem(self.letters367[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                    #4 слова по 3 3 3 7 букв

    def searchWords3337(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            three_letter_words = re.findall(r'\b\w{3}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_three_words, random_seven_word = self.selectRandomWords3337(three_letter_words, seven_letter_word)
            self.delenie3337(random_three_words, random_seven_word)
            self.zapolnenie3337()

    def selectRandomWords3337(self, three_letter_words, seven_letter_word):
        if len(three_letter_words) < 3 or len(seven_letter_word) < 1:
            return ["Не хватает слов"]
        return random.sample(three_letter_words, 3), random.choice(seven_letter_word)

    def delenie3337(self, three_words, seven_word):
        if len(three_words) < 3 or len(seven_word) < 1:
            print("Ошибка delenie3337")
            return

        self.positions3337 = random.choice(self.variants3337)

        for word in three_words:
            self.letters3337.extend(list(word))
        self.letters3337.extend(list(seven_word))

    def zapolnenie3337(self):
        if len(self.letters3337) != len(self.positions3337):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters3337)):
            row, col = self.positions3337[i]
            item = QTableWidgetItem(self.letters3337[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
                                      #4 слова по 4 буквы каждое

    def searchWords4444(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            random_four_word = self.selectRandomWords4444(four_letter_word)
            self.delenie4444(random_four_word)
            self.zapolnenie4444()

    def selectRandomWords4444(self, four_letter_word):
        if len(four_letter_word) < 4:
            return ["Не хватает слов"]
        return random.sample(four_letter_word, 4)

    def delenie4444(self, four_word):
        if len(four_word) < 4:
            print("Ошибка delenie4444")
            return

        self.positions4444 = random.choice(self.variants4444)

        for word in four_word:
            self.letters4444.extend(list(word))

    def zapolnenie4444(self):
        if len(self.letters4444) != len(self.positions4444):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters4444)):
            row, col = self.positions4444[i]
            item = QTableWidgetItem(self.letters4444[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------
    def back_to_gamelevels(self):
        self.gamelevels = GameLevels(self.nickname)
        self.gamelevels.show()
        self.close()

class SecWindow5x5(QMainWindow):
    def __init__(self, nickname):
        super().__init__()
        self.ui = Ui_secwindow5x5()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back_to_gamelevels)
        self.letters55555 = []
        self.positions55555 = []
        self.letters4777 = []
        self.positions4777 = []
        self.letters6667 = []
        self.positions6667 = []
        self.letters5677 = []
        self.positions5677 = []
        self.letters5578 = []
        self.positions5578 = []
        self.letters4588 = []
        self.positions4588 = []
        self.variants55555 = [
            [(1, 1), (1, 0), (0, 0), (0, 1), (0, 2),
             (0, 3), (0, 4), (1, 4), (1, 3), (1, 2),
             (3, 3), (2, 3), (2, 2), (2, 1), (2, 0),
             (4, 2), (4, 3), (4, 4), (3, 4), (2, 4),
             (3, 2), (3, 1), (4, 1), (4, 0), (3, 0)]
        ]
        self.variants4777 = [
            [(1, 1), (1, 2), (2, 2), (2, 1), (3, 0),
             (2, 0), (1, 0), (0, 0), (0, 1), (0, 2),
             (0, 3), (1, 3), (2, 3), (3, 3), (3, 4),
             (2, 4), (1, 4), (0, 4), (4, 0), (4, 1),
             (3, 1), (3, 2), (4, 2), (4, 3), (4, 4)]
        ]
        self.variants6667 = [
            [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1),
             (1, 0), (2, 1), (2, 0), (3, 0), (4, 0),
             (4, 1), (4, 2), (3, 1), (3, 2), (2, 2),
             (2, 3), (3, 3), (4, 3), (1, 3), (0, 3),
             (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
        ]
        self.variants5677 = [
            [(1, 1), (2, 1), (2, 2), (1, 2), (1, 3),
             (3, 4), (4, 4), (4, 3), (3, 3), (2, 3),
             (2, 4), (1, 0), (0, 0), (0, 1), (0, 2),
             (0, 3), (0, 4), (1, 4), (4, 0), (4, 1),
             (4, 2), (3, 2), (3, 1), (3, 0), (2, 0)],
        ]
        self.variants5578 = [
            [(3, 3), (2, 3), (1, 3), (1, 2), (1, 1),
             (1, 0), (2, 0), (2, 1), (2, 2), (3, 2),
             (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 4), (2, 4), (3, 1), (3, 0), (4, 0),
             (4, 1), (4, 2), (4, 3), (4, 4), (3, 4)]
        ]
        self.variants4588 = [
            [(0, 3), (1, 3), (2, 3), (3, 3), (1, 1),
             (0, 1), (0, 2), (1, 2), (2, 2), (0, 0),
             (1, 0), (2, 0), (3, 0), (4, 0), (4, 1),
             (3, 1), (2, 1), (0, 4), (1, 4), (2, 4),
             (3, 4), (4, 4), (4, 3), (4, 2), (3, 2)]
        ]
        self.randomWordsPlace()
# -----------------------------------------------------------------------------------------------------------------------
        # Выделение ячеек

        self.ui.tableWidget.itemEntered.connect(self.on_item_entered)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectItems)
        self.mouse_pressed = False
        self.ui.tableWidget.viewport().installEventFilter(self)
        self.highlighted_items = []
        self.chosen_words = []
        self.score = 0
        self.nickname = nickname
        self.selected_level = 3
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

    def on_item_entered(self, item):
        if item.background().color() != QColor(0, 255, 0):
            item.setBackground(QColor(255, 0, 0))
            self.highlighted_items.append(item)

    def check_all_cells_green(self):
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item.background().color() != QColor(0, 255, 0):
                    return
        self.score += 3
        self.update_rating()
        self.open_zanovo5x5()


    def update_rating(self):
        if not self.nickname:
            return

        with open('rating.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()

        updated_lines = []
        found = False
        for line in lines:
            nickname, score = line.strip().split(':')
            if nickname == self.nickname:
                updated_lines.append(f"{nickname}:{int(score) + self.score}\n")
                found = True
            else:
                updated_lines.append(line)

        if not found:
            updated_lines.append(f"{self.nickname}:{self.score}\n")

        with open('rating.txt', 'w', encoding='utf8') as file:
            file.writelines(updated_lines)

    def open_zanovo5x5(self):
        self.zanovo5x5 = Zanovo(self.nickname, self.selected_level)
        self.zanovo5x5.show()
        self.hide()

    def reset_colors(self):
        for item in self.highlighted_items:
            if item.background().color() != QColor(0, 255, 0):
                item.setBackground(QColor(255, 255, 255))
        self.highlighted_items.clear()

        # Контроль перемещения мыши по полю

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            item = self.ui.tableWidget.itemAt(event.pos())
            if item is not None and item.background().color() == QColor(0, 255, 0):
                self.mouse_pressed = True
                self.previous_item_pos = event.pos()
                return True
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouse_pressed = False
            self.check_word()
            self.check_all_cells_green()
            return True
        elif event.type() == QEvent.MouseMove and self.mouse_pressed:
            item = self.ui.tableWidget.itemAt(event.pos())
            previous_item = self.ui.tableWidget.itemAt(self.previous_item_pos)
            if item is not None and previous_item is not None:
                if previous_item.background().color() != QColor(0, 255, 0) and \
                        item.background().color() != QColor(0, 255, 0):
                    drag = QDrag(self)
                    mime_data = QMimeData()
                    drag.setMimeData(mime_data)
                    drag.exec_(Qt.MoveAction)
                else:
                    return True
            else:
                return True
        return super().eventFilter(source, event)

        # если выбранные ячейки соответсвуют позициям расстановки слова то она окрашивается в зелёный и закрепляется

    def check_word(self):
        selected_positions = [(item.row(), item.column()) for item in self.highlighted_items]

                            #5 слов по 5 букв в каждом

        if self.place == self.searchWords55555:
            if selected_positions == self.positions55555[:5] or \
                    selected_positions == self.positions55555[5:10] or \
                    selected_positions == self.positions55555[10:15] or \
                    selected_positions == self.positions55555[15:20] or \
                    selected_positions == self.positions55555[25:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == self.searchWords4777:
            if selected_positions == self.positions4777[:4] or \
                    selected_positions == self.positions4777[4:11] or \
                    selected_positions == self.positions4777[11:18] or \
                    selected_positions == self.positions4777[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == self.searchWords6667:
            if selected_positions == self.positions6667[:6] or \
                    selected_positions == self.positions6667[6:12] or \
                    selected_positions == self.positions6667[12:18] or \
                    selected_positions == self.positions6667[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == self.searchWords5677:
            if selected_positions == self.positions5677[:5] or \
                    selected_positions == self.positions5677[5:11] or \
                    selected_positions == self.positions5677[11:18] or \
                    selected_positions == self.positions5677[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == self.searchWords5578:
            if selected_positions == self.positions5578[:5] or \
                    selected_positions == self.positions5578[5:10] or \
                    selected_positions == self.positions5578[10:17] or \
                    selected_positions == self.positions5578[17:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == self.searchWords4588:
            if selected_positions == self.positions4588[:4] or \
                    selected_positions == self.positions4588[4:9] or \
                    selected_positions == self.positions4588[9:17] or \
                    selected_positions == self.positions4588[17:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()
        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
    def randomWordsPlace(self):
        choice = random.choice(['55555', '4777', '6667', '5677', '5578', '4588'])
        if choice == '55555':
            self.place = self.searchWords55555
        elif choice == '4777':
            self.place = self.searchWords4777
        elif choice == '6667':
            self.place = self.searchWords6667
        elif choice == '5677':
            self.place = self.searchWords5677
        elif choice == '5578':
            self.place = self.searchWords5578
        elif choice == '4588':
            self.place = self.searchWords4588
        #elif choice == '4444':
        #    self.place = self.searchWords55555

        self.place()
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords55555(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            random_five_word = self.selectRandomWords55555(five_letter_word)
            self.delenie55555(random_five_word)
            self.zapolnenie55555()

    def selectRandomWords55555(self, five_letter_word):
        if len(five_letter_word) < 5:
            return ["Не хватает слов"]
        return random.sample(five_letter_word, 5)

    def delenie55555(self, five_word):
        if len(five_word) < 5:
            print('delenie55555')

        self.positions55555 = random.choice(self.variants55555)

        for word in five_word:
            self.letters55555.extend(list(word))

    def zapolnenie55555(self):
        if len(self.letters55555) != len(self.positions55555):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters55555)):
            row, col = self.positions55555[i]
            item = QTableWidgetItem(self.letters55555[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords4777(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_four_word, random_seven_word = self.selectRandomWords4777(four_letter_word, seven_letter_word)
            self.delenie4777(random_four_word, random_seven_word)
            self.zapolnenie4777()

    def selectRandomWords4777(self, four_letter_word, seven_letter_word):
        if len(four_letter_word) < 1 or len(seven_letter_word) < 3:
            return ["Не хватает слов"]
        return random.choice(four_letter_word), random.sample(seven_letter_word, 3)

    def delenie4777(self, four_word, seven_word):
        if len(four_word ) < 1 or len(seven_word) < 3:
            print('delenie4777')

        self.positions4777 = random.choice(self.variants4777)

        self.letters4777.extend(list(four_word))
        for word in seven_word:
            self.letters4777.extend(list(word))

    def zapolnenie4777(self):
        if len(self.letters4777) != len(self.positions4777):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters4777)):
            row, col = self.positions4777[i]
            item = QTableWidgetItem(self.letters4777[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords6667(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            six_letter_word = re.findall(r'\b\w{6}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_six_word, random_seven_word = self.selectRandomWords6667(six_letter_word, seven_letter_word)
            self.delenie6667(random_six_word, random_seven_word)
            self.zapolnenie6667()

    def selectRandomWords6667(self, six_letter_word, seven_letter_word):
        if len(six_letter_word) < 3 or len(seven_letter_word) < 1:
            return ["Не хватает слов"]
        return random.sample(six_letter_word, 3), random.choice(seven_letter_word)

    def delenie6667(self, six_word, seven_word):
        if len(six_word) < 3 or len(seven_word) < 1:
            print('delenie6667')

        self.positions6667 = random.choice(self.variants6667)

        for word in six_word:
            self.letters6667.extend(list(word))
        self.letters6667.extend(list(seven_word))

    def zapolnenie6667(self):
        if len(self.letters6667) != len(self.positions6667):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters6667)):
            row, col = self.positions6667[i]
            item = QTableWidgetItem(self.letters6667[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords5677(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            six_letter_word = re.findall(r'\b\w{6}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            random_five_word, random_six_word, random_seven_word = \
                self.selectRandomWords5677(five_letter_word, six_letter_word, seven_letter_word)
            self.delenie5677(random_five_word, random_six_word, random_seven_word)
            self.zapolnenie5677()

    def selectRandomWords5677(self, five_letter_word, six_letter_word, seven_letter_word):
        if len(five_letter_word) < 1 or len(six_letter_word) < 1 or len(seven_letter_word) < 2:
            return ["Не хватает слов"]
        return random.choice(five_letter_word), random.choice(six_letter_word),\
            random.sample(seven_letter_word, 2)

    def delenie5677(self, five_word, six_word, seven_word):
        if len(five_word) < 1 or len(six_word) < 1 or len(seven_word) < 2:
            print('delenie5677')

        self.positions5677 = random.choice(self.variants5677)

        self.letters5677.extend(list(five_word))
        self.letters5677.extend(list(six_word))
        for word in seven_word:
            self.letters5677.extend(list(word))

    def zapolnenie5677(self):
        if len(self.letters5677) != len(self.positions5677):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters5677)):
            row, col = self.positions5677[i]
            item = QTableWidgetItem(self.letters5677[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords5578(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            seven_letter_word = re.findall(r'\b\w{7}\b', text)
            eight_letter_word = re.findall(r'\b\w{8}\b', text)
            random_five_word, random_eight_word, random_seven_word = \
                self.selectRandomWords5578(five_letter_word, eight_letter_word, seven_letter_word)
            self.delenie5578(random_five_word, random_eight_word, random_seven_word)
            self.zapolnenie5578()

    def selectRandomWords5578(self, five_letter_word, eight_letter_word, seven_letter_word):
        if len(five_letter_word) < 2 or len(eight_letter_word) < 1 or len(seven_letter_word) < 1:
            return ["Не хватает слов"]
        return random.sample(five_letter_word, 2), random.choice(eight_letter_word),\
            random.choice(seven_letter_word)

    def delenie5578(self, five_word, eight_word, seven_word):
        if len(five_word) < 2 or len(eight_word) < 1 or len(seven_word) < 1:
            print('delenie5578')

        self.positions5578 = random.choice(self.variants5578)

        for word in five_word:
            self.letters5578.extend(list(word))
        self.letters5578.extend(list(seven_word))
        self.letters5578.extend(list(eight_word))

    def zapolnenie5578(self):
        if len(self.letters5578) != len(self.positions5578):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters5578)):
            row, col = self.positions5578[i]
            item = QTableWidgetItem(self.letters5578[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords4588(self):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            four_letter_word = re.findall(r'\b\w{4}\b', text)
            five_letter_word = re.findall(r'\b\w{5}\b', text)
            eight_letter_word = re.findall(r'\b\w{8}\b', text)
            random_four_word, random_five_word, random_eight_word = \
                self.selectRandomWords4588(four_letter_word, five_letter_word, eight_letter_word)
            self.delenie4588(random_four_word, random_five_word, random_eight_word)
            self.zapolnenie4588()

    def selectRandomWords4588(self, four_letter_word, five_letter_word, eight_letter_word):
        if len(four_letter_word) < 1 or len(five_letter_word) < 1 or len(eight_letter_word) < 2:
            return ["Не хватает слов"]
        return random.choice(four_letter_word), random.choice(five_letter_word),\
            random.sample(eight_letter_word, 2)


    def delenie4588(self, four_word, five_word, eight_word):
        if len(four_word) < 1 or len(five_word) < 1 or len(eight_word) < 2:
            print('delenie4588')

        self.positions4588 = random.choice(self.variants4588)

        self.letters4588.extend(list(four_word))
        self.letters4588.extend(list(five_word))
        for word in eight_word:
            self.letters4588.extend(list(word))

    def zapolnenie4588(self):
        if len(self.letters4588) != len(self.positions4588):
            print("Количество букв и позиций должно быть одинаковым.")
            return

        for i in range(len(self.letters4588)):
            row, col = self.positions4588[i]
            item = QTableWidgetItem(self.letters4588[i])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, col, item)


    def back_to_gamelevels(self):
        self.game_levels = GameLevels(self.nickname)
        self.game_levels.show()
        self.close()

app = QApplication(sys.argv)
main_menu = MainMenu()
main_menu.show()
sys.exit(app.exec_())