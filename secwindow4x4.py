# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Victus/PycharmProjects/Gme/secwindow4x4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secwindow4x4(object):
    def setupUi(self, secwindow4x4):
        secwindow4x4.setObjectName("secwindow4x4")
        secwindow4x4.resize(830, 880)
        secwindow4x4.setMinimumSize(QtCore.QSize(830, 880))
        secwindow4x4.setMaximumSize(QtCore.QSize(830, 880))
        secwindow4x4.setBaseSize(QtCore.QSize(2, 0))
        secwindow4x4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        secwindow4x4.setMouseTracking(False)
        secwindow4x4.setAccessibleName("")
        secwindow4x4.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(secwindow4x4)
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
        self.gridLayout_2.setContentsMargins(25, 30, 25, 609)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(150)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(50, 50))
        self.back.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.music.setFont(font)
        self.music.setIconSize(QtCore.QSize(16, 16))
        self.music.setObjectName("music")
        self.gridLayout_2.addWidget(self.music, 0, 2, 1, 1)
        self.countlevel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countlevel.sizePolicy().hasHeightForWidth())
        self.countlevel.setSizePolicy(sizePolicy)
        self.countlevel.setMinimumSize(QtCore.QSize(50, 50))
        self.countlevel.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.countlevel.setFont(font)
        self.countlevel.setTabletTracking(True)
        self.countlevel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.countlevel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.countlevel.setAutoFillBackground(False)
        self.countlevel.setAlignment(QtCore.Qt.AlignCenter)
        self.countlevel.setObjectName("countlevel")
        self.gridLayout_2.addWidget(self.countlevel, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(530, 530))
        self.tableWidget.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(132)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        secwindow4x4.setCentralWidget(self.centralwidget)

        self.retranslateUi(secwindow4x4)
        QtCore.QMetaObject.connectSlotsByName(secwindow4x4)

    def retranslateUi(self, secwindow4x4):
        _translate = QtCore.QCoreApplication.translate
        secwindow4x4.setWindowTitle(_translate("secwindow4x4", "Филворды"))
        self.back.setText(_translate("secwindow4x4", "НАЗАД"))
        self.music.setText(_translate("secwindow4x4", "ВКЛ/ВЫКЛ МУЗЫКУ"))
        self.countlevel.setText(_translate("secwindow4x4", "ОТ 3 ДО 7 БУКВ"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


