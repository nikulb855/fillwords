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
        self.open_zanovo()

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

    def open_zanovo(self):
        self.zanovo = Zanovo(self.nickname, self.selected_level)
        self.zanovo.show()
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
        if self.place == '333':
            variants_positions = self.positions['333']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:6] or \
                    selected_positions == variants_positions[6:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        #Для расстановки 2 слов по 3 и 6 букв
        elif self.place == '36':
            variants_positions = self.positions['36']
            if selected_positions == variants_positions[:3] or selected_positions == variants_positions[3:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        #Для расстановки 2 слов по 4 и 5 букв
        elif self.place == '45':
            variants_positions = self.positions['45']
            if selected_positions == variants_positions[:4] or selected_positions == variants_positions[4:]:
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
        self.letters = {}
        self.positions = {}

# -----------------------------------------------------------------------------------------------------------------------
                                     # Позиции на поле
        self.variants = {
            '3346': [
                [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (1, 0), (1, 1),
                 (1, 2), (2, 2), (3, 3), (3, 2), (3, 1), (2, 1), (2, 0), (3, 0)],
                [(3, 2), (3, 1), (3, 0), (1, 1), (0, 1), (0, 2), (0, 0), (1, 0),
                 (2, 0), (2, 1), (0, 3), (1, 3), (1, 2), (2, 2), (2, 3), (3, 3)]
            ],
            '3445': [
                [(1, 0), (2, 0), (3, 0), (0, 2), (0, 3), (1, 3), (1, 2), (3, 2),
                 (2, 2), (2, 3), (3, 3), (0, 0), (0, 1), (1, 1), (2, 1), (3, 1)],
                [(2, 3), (2, 2), (2, 1), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1),
                 (1, 2), (1, 3), (0, 3), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
            ],
            '457': [
                [(3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (0, 1), (0, 2),
                 (0, 3), (2, 2), (2, 1), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)],
                [(2, 0), (2, 1), (2, 2), (1, 2), (2, 3), (3, 3), (3, 2), (3, 1),
                 (3, 0), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)]
            ],
            '3355': [
                [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (2, 3), (3, 3),
                 (3, 2), (3, 1), (2, 1), (2, 2), (1, 2), (1, 3), (0, 3), (0, 2)],
                [(0, 2), (0, 3), (1, 3), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1),
                 (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3)]
            ],
            '367': [
                [(3, 2), (3, 3), (2, 3), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2),
                 (2, 2), (1, 1), (2, 1), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)],
                [(1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1),
                 (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3)]
            ],
            '3337': [
                [(0, 0), (0, 1), (0, 2), (2, 3), (3, 3), (3, 2), (2, 0), (3, 0),
                 (3, 1), (0, 3), (1, 3), (1, 2), (2, 2), (2, 1), (1, 1), (1, 0)],
                [(0, 2), (0, 1), (0, 0), (1, 1), (1, 2), (2, 2), (0, 1), (0, 2),
                 (0, 3), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3)]
            ],
            '4444': [
                [(0, 0), (0, 1), (0, 2), (0, 3), (3, 2), (3, 3), (2, 3), (1, 3),
                 (2, 1), (2, 2), (1, 2), (1, 1), (3, 1), (3, 0), (2, 0), (1, 0)],
                [(1, 1), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1),
                 (2, 0), (3, 0), (3, 1), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
            ]
        }
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
        self.open_zanovo()

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

    def open_zanovo(self):
        self.zanovo = Zanovo(self.nickname, self.selected_level)
        self.zanovo.show()
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

        # 4 слова по 3 3 4 6 букв

        if self.place == '3346':
            variants_positions = self.positions['3346']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:6] or \
                    selected_positions == variants_positions[6:10] or \
                    selected_positions == variants_positions[10:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 4 слова по 3 4 4 5 букв

        elif self.place == '3445':
            variants_positions = self.positions['3445']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:7] or \
                    selected_positions == variants_positions[7:11] or \
                    selected_positions == variants_positions[11:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 3 слова по 4 5 7 букв

        elif self.place == '457':
            variants_positions = self.positions['457']
            if selected_positions == variants_positions[:4] or \
                    selected_positions == variants_positions[4:9] or \
                    selected_positions == variants_positions[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 4 слова по 3 3 5 5 букв

        elif self.place == '3355':
            variants_positions = self.positions['3355']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:6] or \
                    selected_positions == variants_positions[6:11] or \
                    selected_positions == variants_positions[11:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 3 слова по 3 6 7 букв

        elif self.place == '367':
            variants_positions = self.positions['367']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:9] or \
                    selected_positions == variants_positions[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 4 слова по 3 3 3 7 букв

        elif self.place == '3337':
            variants_positions = self.positions['3337']
            if selected_positions == variants_positions[:3] or \
                    selected_positions == variants_positions[3:6] or \
                    selected_positions == variants_positions[6:9] or \
                    selected_positions == variants_positions[9:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

                # 4 слова по 4 буквы каждое

        elif self.place == '4444':
            variants_positions = self.positions['4444']
            if selected_positions == variants_positions[:4] or \
                    selected_positions == variants_positions[4:8] or \
                    selected_positions == variants_positions[8:12] or \
                    selected_positions == variants_positions[12:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
    def randomWordsPlace(self):
        choice = random.choice(list(self.variants.keys()))
        word_lengths = {
            '3346': [3, 3, 4, 6],
            '3445': [3, 4, 4, 5],
            '457': [4, 5, 7],
            '3355': [3, 3, 5, 5],
            '367': [3, 6, 7],
            '3337': [3, 3, 3, 7],
            '4444': [4, 4, 4, 4]
        }
        self.place = choice
        self.searchWords(word_lengths[choice], choice)

    # -----------------------------------------------------------------------------------------------------------------------

    def searchWords(self, word_lengths, variant_key):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            words = {length: re.findall(r'\b\w{' + str(length) + r'}\b', text) for length in word_lengths}
            selected_words = self.selectRandomWords(words, variant_key)
            if isinstance(selected_words, dict):
                self.delenie(selected_words, variant_key)
                self.zapolnenie(variant_key)
            else:
                # Handle the error message returned by selectRandomWords
                print(selected_words)

    def selectRandomWords(self, words, variant_key):
        selected_words = {}
        if variant_key == '3346':
            if len(words[3]) < 2 or len(words[4]) < 1 or len(words[6]) < 1:
                return {"Не хватает слов1"}
            selected_words[3] = random.sample(words[3], 2)
            selected_words[4] = random.choice(words[4])
            selected_words[6] = random.choice(words[6])
        elif variant_key == '3445':
            if len(words[3]) < 1 or len(words[4]) < 2 or len(words[5]) < 1:
                return {'Не хватает слов2'}
            selected_words[3] = random.choice(words[3])
            selected_words[4] = random.sample(words[4], 2)
            selected_words[5] = random.choice(words[5])
        elif variant_key == '457':
            if len(words[4]) < 1 or len(words[5]) < 1 or len(words[7]) < 1:
                return {'Не хватает слов3'}
            selected_words[4] = random.choice(words[4])
            selected_words[5] = random.choice(words[5])
            selected_words[7] = random.choice(words[7])
        elif variant_key == '3355':
            if len(words[3]) < 2 or len(words[5]) < 2:
                return {"Не хватает слов4"}
            selected_words[3] = random.sample(words[3], 2)
            selected_words[5] = random.sample(words[5], 2)
        elif variant_key == '367':
            if len(words[3]) < 1 or len(words[6]) < 1 or len(words[7]) < 1:
                return {"Не хватает слов5"}
            selected_words[3] = random.choice(words[3])
            selected_words[6] = random.choice(words[6])
            selected_words[7] = random.choice(words[7])
        elif variant_key == '3337':
            if len(words[3]) < 3 or len(words[7]) < 1:
                return {"Не хватает слов6"}
            selected_words[3] = random.sample(words[3], 3)
            selected_words[7] = random.choice(words[7])
        elif variant_key == '4444':
            if len(words[4]) < 4:
                return {"Не хватает слов7"}
            selected_words[4] = random.sample(words[4], 4)
        else:
            return {"Неизвестный вариант"}
        return selected_words

    def delenie(self, selected_words, variant_key):
        if variant_key == '3346':
            random_variants = random.choice(self.variants['3346'])
        elif variant_key == '3445':
            random_variants = random.choice(self.variants['3445'])
        elif variant_key == '457':
            random_variants = random.choice(self.variants['457'])
        elif variant_key == '3355':
            random_variants = random.choice(self.variants['3355'])
        elif variant_key == '367':
            random_variants = random.choice(self.variants['367'])
        elif variant_key == '3337':
            random_variants = random.choice(self.variants['3337'])
        elif variant_key == '4444':
            random_variants = random.choice(self.variants['4444'])
        self.positions[variant_key] = random_variants
        self.letters[variant_key] = []

        for word_list in selected_words.values():
            if isinstance(word_list, list):
                for word in word_list:
                    self.letters[variant_key].extend(list(word))
            else:
                self.letters[variant_key].extend(list(word_list))

    def zapolnenie(self, variant_key):
        if len(self.letters[variant_key]) != len(self.positions[variant_key]):
            print("Количество букв и позиций должно быть одинаковым.")
            print(self.positions, self.letters)
            return

        for i, (row, col) in enumerate(self.positions[variant_key]):
            if i < len(self.letters[variant_key]):
                letter = self.letters[variant_key][i]
                item = QTableWidgetItem(letter)
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
        self.letters = {}
        self.positions = {}
        self.variants = {
            '55555': [
                [(1, 1), (1, 0), (0, 0), (0, 1), (0, 2),
                 (0, 3), (0, 4), (1, 4), (1, 3), (1, 2),
                 (3, 3), (2, 3), (2, 2), (2, 1), (2, 0),
                 (4, 2), (4, 3), (4, 4), (3, 4), (2, 4),
                 (3, 2), (3, 1), (4, 1), (4, 0), (3, 0)],

                [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                 (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                 (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                 (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                 (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
                ],
            '4777': [(1, 1), (1, 2), (2, 2), (2, 1), (3, 0),
                     (2, 0), (1, 0), (0, 0), (0, 1), (0, 2),
                     (0, 3), (1, 3), (2, 3), (3, 3), (3, 4),
                     (2, 4), (1, 4), (0, 4), (4, 0), (4, 1),
                     (3, 1), (3, 2), (4, 2), (4, 3), (4, 4)],

            '6667': [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1),
                     (1, 0), (2, 1), (2, 0), (3, 0), (4, 0),
                     (4, 1), (4, 2), (3, 1), (3, 2), (2, 2),
                     (2, 3), (3, 3), (4, 3), (1, 3), (0, 3),
                     (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],

            '5677': [(1, 1), (2, 1), (2, 2), (1, 2), (1, 3),
                     (3, 4), (4, 4), (4, 3), (3, 3), (2, 3),
                     (2, 4), (1, 0), (0, 0), (0, 1), (0, 2),
                     (0, 3), (0, 4), (1, 4), (4, 0), (4, 1),
                     (4, 2), (3, 2), (3, 1), (3, 0), (2, 0)],

            '5578': [(3, 3), (2, 3), (1, 3), (1, 2), (1, 1),
                     (1, 0), (2, 0), (2, 1), (2, 2), (3, 2),
                     (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                     (1, 4), (2, 4), (3, 1), (3, 0), (4, 0),
                     (4, 1), (4, 2), (4, 3), (4, 4), (3, 4)],

            '4588': [(0, 3), (1, 3), (2, 3), (3, 3), (1, 1),
                     (0, 1), (0, 2), (1, 2), (2, 2), (0, 0),
                     (1, 0), (2, 0), (3, 0), (4, 0), (4, 1),
                     (3, 1), (2, 1), (0, 4), (1, 4), (2, 4),
                     (3, 4), (4, 4), (4, 3), (4, 2), (3, 2)]
        }
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
        self.open_zanovo()


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

    def open_zanovo(self):
        self.zanovo = Zanovo(self.nickname, self.selected_level)
        self.zanovo.show()
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
        if self.place == '55555':
            variant_positions = self.positions['55555']
            if selected_positions == variant_positions[:5] or \
                    selected_positions == variant_positions[5:10] or \
                    selected_positions == variant_positions[10:15] or \
                    selected_positions == variant_positions[15:20] or \
                    selected_positions == variant_positions[25:]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == '4777':
            variant_positions = self.positions['4777']
            if selected_positions == variant_positions[:4] or \
                    selected_positions == variant_positions[4:11] or \
                    selected_positions == variant_positions[11:18] or \
                    selected_positions == variant_positions[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == '6667':
            variant_positions = self.positions['6667']
            if selected_positions == variant_positions[:6] or \
                    selected_positions == variant_positions[6:12] or \
                    selected_positions == variant_positions[12:18] or \
                    selected_positions == variant_positions[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == '5677':
            variant_positions = self.positions['5677']
            if selected_positions == variant_positions[:5] or \
                    selected_positions == variant_positions[5:11] or \
                    selected_positions == variant_positions[11:18] or \
                    selected_positions == variant_positions[18:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == '5578':
            variant_positions = self.positions['5578']
            if selected_positions == variant_positions[:5] or \
                    selected_positions == variant_positions[5:10] or \
                    selected_positions == variant_positions[10:17] or \
                    selected_positions == variant_positions[17:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()

        elif self.place == '4588':
            variant_positions = self.positions['4588']
            if selected_positions == variant_positions[:4] or \
                    selected_positions == variant_positions[4:9] or \
                    selected_positions == variant_positions[9:17] or \
                    selected_positions == variant_positions[17:25]:
                for item in self.highlighted_items:
                    item.setBackground(QColor(0, 255, 0))
            else:
                self.reset_colors()
        self.highlighted_items.clear()
#-----------------------------------------------------------------------------------------------------------------------
    def randomWordsPlace(self):
        choice = random.choice(list(self.variants.keys()))
        word_lengths = {
            '55555': [5, 5, 5, 5, 5],
            '4777': [4, 7, 7, 7],
            '6667': [6, 6, 6, 7],
            '5677': [5, 6, 7, 7],
            '5578': [5, 5, 7, 8],
            '4588': [4, 5, 8, 8]
        }
        self.place = choice
        self.searchWords(word_lengths[choice], choice)
#-----------------------------------------------------------------------------------------------------------------------

    def searchWords(self, word_lengths, variant_key):
        with open("words.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            words = {length: re.findall(r'\b\w{' + str(length) + r'}\b', text) for length in word_lengths}
            selected_words = self.selectRandomWords(words, variant_key)
            if isinstance(selected_words, dict):
                self.delenie(selected_words, variant_key)
                self.zapolnenie(variant_key)
            else:
                # Handle the error message returned by selectRandomWords
                print(selected_words)

    def selectRandomWords(self, words, variant_key):
        selected_words = {}
        if variant_key == '4777':
            if len(words[4]) < 1 or len(words[7]) < 3:
                return {"Не хватает слов1"}
            selected_words[4] = random.choice(words[4])
            selected_words[7] = random.sample(words[7], 3)
        elif variant_key == '55555':
            if len(words[5]) < 5:
                return {'Не хватает слов2'}
            selected_words[5] = random.sample(words[5], 5)
        elif variant_key == '6667':
            if len(words[6]) < 3 or len(words[7]) < 1:
                return {'Не хватает слов3'}
            selected_words[6] = random.sample(words[6], 3)
            selected_words[7] = random.choice(words[7])
        elif variant_key == '5677':
            if len(words[5]) < 1 or len (words[6]) < 1 or len(words[7]) < 2:
                return {"Не хватает слов4"}
            selected_words[5] = random.choice(words[5])
            selected_words[6] = random.choice(words[6])
            selected_words[7] = random.sample(words[7], 2)
        elif variant_key == '5578':
            if len(words[5]) < 2 or len(words[7]) < 1 or len(words[8]) < 1:
                return {"Не хватает слов5"}
            selected_words[5] = random.sample(words[5], 2)
            selected_words[7] = random.choice(words[7])
            selected_words[8] = random.choice(words[8])
        elif variant_key == '4588':
            if len(words[4]) < 1 or len(words[5]) < 1 or len(words[8]) < 2:
                return {"Не хватает слов6"}
            selected_words[4] = random.choice(words[4])
            selected_words[5] = random.choice(words[5])
            selected_words[8] = random.sample(words[8], 2)
        else:
            return {"Неизвестный вариант"}
        return selected_words

    def delenie(self, selected_words, variant_key):
        self.positions[variant_key] = self.variants[variant_key]
        self.letters[variant_key] = []
       # if variant_key == '55555':
       #     random_variants = random.choice(self.variants['55555'])
       # elif variant_key == '4777':
       #     random_variants = random.choice(self.variants['4777'])
       # elif variant_key == '6667':
       #    random_variants = random.choice(self.variants['6667'])
       # elif variant_key == '5677':
       #     random_variants = random.choice(self.variants['5677'])
       # elif variant_key == '5578':
       #     random_variants = random.choice(self.variants['5578'])
       # elif variant_key == '4588':
       #     random_variants = random.choice(self.variants['4588'])
       # self.positions[variant_key] = random_variants
       # self.letters[variant_key] = []


        for word_list in selected_words.values():
            if isinstance(word_list, list):
                for word in word_list:
                    self.letters[variant_key].extend(list(word))
            else:
                self.letters[variant_key].extend(list(word_list))

    def zapolnenie(self, variant_key):
        if len(self.letters[variant_key]) != len(self.positions[variant_key]):
            print("Количество букв и позиций должно быть одинаковым.")
            print(self.positions, self.letters)
            return

        # Ensure that each letter is placed at the corresponding position
        for i, (row, col) in enumerate(self.positions[variant_key]):
            if i < len(self.letters[variant_key]):
                letter = self.letters[variant_key][i]
                item = QTableWidgetItem(letter)
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