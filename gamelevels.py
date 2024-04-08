

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gamelevels(object):
    def setupUi(self, gamelevels):
        gamelevels.setObjectName("gamelevels")
        gamelevels.resize(370, 468)
        gamelevels.setMinimumSize(QtCore.QSize(370, 468))
        gamelevels.setMaximumSize(QtCore.QSize(16777215, 16777215))
        gamelevels.setBaseSize(QtCore.QSize(2, 0))
        gamelevels.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        gamelevels.setMouseTracking(False)
        gamelevels.setAccessibleName("")
        gamelevels.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(gamelevels)
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
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.play3x3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play3x3.sizePolicy().hasHeightForWidth())
        self.play3x3.setSizePolicy(sizePolicy)
        self.play3x3.setMinimumSize(QtCore.QSize(0, 0))
        self.play3x3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.play3x3.setFont(font)
        self.play3x3.setStyleSheet("")
        self.play3x3.setObjectName("play3x3")
        self.verticalLayout.addWidget(self.play3x3)
        self.play4x4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play4x4.sizePolicy().hasHeightForWidth())
        self.play4x4.setSizePolicy(sizePolicy)
        self.play4x4.setMinimumSize(QtCore.QSize(0, 0))
        self.play4x4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.play4x4.setFont(font)
        self.play4x4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.play4x4.setStyleSheet("")
        self.play4x4.setObjectName("play4x4")
        self.verticalLayout.addWidget(self.play4x4)
        self.play5x5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play5x5.sizePolicy().hasHeightForWidth())
        self.play5x5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.play5x5.setFont(font)
        self.play5x5.setObjectName("play5x5")
        self.verticalLayout.addWidget(self.play5x5)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(0, 0))
        self.back.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back.setStyleSheet("")
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(3, 10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        gamelevels.setCentralWidget(self.centralwidget)

        self.retranslateUi(gamelevels)
        QtCore.QMetaObject.connectSlotsByName(gamelevels)

    def retranslateUi(self, gamelevels):
        _translate = QtCore.QCoreApplication.translate
        gamelevels.setWindowTitle(_translate("gamelevels", "Филворды"))
        self.play3x3.setText(_translate("gamelevels", "3x3"))
        self.play4x4.setText(_translate("gamelevels", "4x4"))
        self.play5x5.setText(_translate("gamelevels", "5x5"))
        self.back.setText(_translate("gamelevels", "НАЗАД"))

