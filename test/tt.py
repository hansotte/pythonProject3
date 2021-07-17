# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledgbFOxB.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(284, 171)
        self.actionNous = QAction(MainWindow)
        self.actionNous.setObjectName(u"actionNous")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 284, 22))
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName(u"menuTest")
        self.menuNous = QMenu(self.menubar)
        self.menuNous.setObjectName(u"menuNous")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuNous.menuAction())
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionNous)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNous.setText(QCoreApplication.translate("MainWindow", u"Nous", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.menuNous.setTitle(QCoreApplication.translate("MainWindow", u"Nous", None))
    # retranslateUi

