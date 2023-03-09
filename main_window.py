# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowjRrAOj.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QAction ,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 538)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSolve_Table = QAction(MainWindow)
        self.actionSolve_Table.setObjectName(u"actionSolve_Table")
        self.actionAbout_Game = QAction(MainWindow)
        self.actionAbout_Game.setObjectName(u"actionAbout_Game")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 30, 411, 371))
        self.grid_Layout = QGridLayout(self.gridLayoutWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(60, 430, 411, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(80, 71, 80);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 531, 26))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_openfile)
        self.menuGame.addAction(self.actionSolve_Table)
        self.menuGame.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Game)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SODOKU", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSolve_Table.setText(QCoreApplication.translate("MainWindow", u"Solve Table ", None))
        self.actionAbout_Game.setText(QCoreApplication.translate("MainWindow", u"About Game...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help !", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dark Mode 🌚", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Light Mode 💡", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

