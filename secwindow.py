# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Victus\PycharmProjects\Gme\secwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secwindow(object):
    def setupUi(self, secwindow):
        secwindow.setObjectName("secwindow")
        secwindow.resize(830, 880)
        secwindow.setMinimumSize(QtCore.QSize(830, 880))
        secwindow.setMaximumSize(QtCore.QSize(830, 880))
        secwindow.setBaseSize(QtCore.QSize(2, 0))
        secwindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        secwindow.setMouseTracking(False)
        secwindow.setAccessibleName("")
        secwindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(secwindow)
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
"QLabel{\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border: 1px solid #b1b1b1\n"
"}\n"
"\n"
"QTableView{\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border: 1px solid #b1b1b1;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(50, 20, 50, 10)
        self.gridLayout_2.setHorizontalSpacing(40)
        self.gridLayout_2.setVerticalSpacing(56)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setIconSize(QtCore.QSize(40, 50))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(91)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(73)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 3)
        self.countlevel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countlevel.sizePolicy().hasHeightForWidth())
        self.countlevel.setSizePolicy(sizePolicy)
        self.countlevel.setMinimumSize(QtCore.QSize(50, 50))
        self.countlevel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.countlevel.setTabletTracking(True)
        self.countlevel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.countlevel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.countlevel.setAutoFillBackground(False)
        self.countlevel.setText("")
        self.countlevel.setAlignment(QtCore.Qt.AlignCenter)
        self.countlevel.setObjectName("countlevel")
        self.gridLayout_2.addWidget(self.countlevel, 0, 1, 1, 1)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(50, 50))
        self.back.setMaximumSize(QtCore.QSize(16777215, 14))
        self.back.setObjectName("back")
        self.gridLayout_2.addWidget(self.back, 0, 0, 1, 1)
        self.music = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music.sizePolicy().hasHeightForWidth())
        self.music.setSizePolicy(sizePolicy)
        self.music.setMinimumSize(QtCore.QSize(50, 50))
        self.music.setMaximumSize(QtCore.QSize(16777215, 14))
        self.music.setBaseSize(QtCore.QSize(0, 1))
        self.music.setIconSize(QtCore.QSize(16, 16))
        self.music.setObjectName("music")
        self.gridLayout_2.addWidget(self.music, 0, 2, 1, 1)
        self.wordBankBox = QtWidgets.QTextEdit(self.centralwidget)
        self.wordBankBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.wordBankBox.setObjectName("wordBankBox")
        self.gridLayout_2.addWidget(self.wordBankBox, 3, 0, 1, 3)
        secwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(secwindow)
        QtCore.QMetaObject.connectSlotsByName(secwindow)

    def retranslateUi(self, secwindow):
        _translate = QtCore.QCoreApplication.translate
        secwindow.setWindowTitle(_translate("secwindow", "Филворды"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.back.setText(_translate("secwindow", "В ГЛАВНОЕ МЕНЮ"))
        self.music.setText(_translate("secwindow", "ВКЛ/ВЫКЛ МУЗЫКУ"))


