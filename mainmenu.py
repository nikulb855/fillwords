# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Victus\PycharmProjects\Gme\game.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 468)
        Dialog.setMinimumSize(QtCore.QSize(370, 468))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setBaseSize(QtCore.QSize(2, 0))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(False)
        Dialog.setAccessibleName("")
        Dialog.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("QWidget{\n"
"color: #333;\n"
"background-color: rgb(212, 220, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border: 1px solid #b1b1b1;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border: 1px solid #b1b1b1;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(208, 208, 208); \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #888;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 30, 20, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nickname = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickname.sizePolicy().hasHeightForWidth())
        self.nickname.setSizePolicy(sizePolicy)
        self.nickname.setMinimumSize(QtCore.QSize(0, 0))
        self.nickname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.nickname.setFont(font)
        self.nickname.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nickname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nickname.setStyleSheet("")
        self.nickname.setText("")
        self.nickname.setFrame(False)
        self.nickname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nickname.setAlignment(QtCore.Qt.AlignCenter)
        self.nickname.setClearButtonEnabled(False)
        self.nickname.setObjectName("nickname")
        self.verticalLayout.addWidget(self.nickname)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setMinimumSize(QtCore.QSize(0, 0))
        self.play.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.play.setFont(font)
        self.play.setStyleSheet("")
        self.play.setObjectName("play")
        self.verticalLayout.addWidget(self.play)
        self.rules = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rules.sizePolicy().hasHeightForWidth())
        self.rules.setSizePolicy(sizePolicy)
        self.rules.setMinimumSize(QtCore.QSize(0, 0))
        self.rules.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.rules.setFont(font)
        self.rules.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rules.setStyleSheet("")
        self.rules.setObjectName("rules")
        self.verticalLayout.addWidget(self.rules)
        self.rating = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rating.sizePolicy().hasHeightForWidth())
        self.rating.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rating.setFont(font)
        self.rating.setObjectName("rating")
        self.verticalLayout.addWidget(self.rating)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QtCore.QSize(0, 0))
        self.exit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.exit.setFont(font)
        self.exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exit.setStyleSheet("")
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Филворды"))
        self.nickname.setPlaceholderText(_translate("Dialog", "Введите никнейм"))
        self.play.setText(_translate("Dialog", "ИГРАТЬ"))
        self.rules.setText(_translate("Dialog", "ПРАВИЛА"))
        self.rating.setText(_translate("Dialog", "РЕЙТИНГ"))
        self.exit.setText(_translate("Dialog", "ВЫЙТИ"))
