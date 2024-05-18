# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designNNNnxG.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(679, 399)
        MainWindow.setWindowTitle(u"T2S")
        MainWindow.setStyleSheet(u"background-color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_container = QWidget(self.centralwidget)
        self.title_container.setObjectName(u"title_container")
        self.title_container.setGeometry(QRect(-11, -31, 691, 121))
        self.title_container.setStyleSheet(u"background-color: #ccc")
        self.appTitle = QLabel(self.title_container)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(80, 65, 47, 30))
        self.appTitle.setStyleSheet(u"font-family: cursive;\n"
"font-size: 26px;\n"
"color: royalblue;")
        self.appDesc = QLabel(self.title_container)
        self.appDesc.setObjectName(u"appDesc")
        self.appDesc.setGeometry(QRect(370, 70, 237, 22))
        self.appDesc.setStyleSheet(u"font-size: 20px;\n"
"font-family: Arial, helvetica, sans-serif;\n"
"font-style: italic;\n"
"color: seagreen;")
        self.speech = QTextEdit(self.centralwidget)
        self.speech.setObjectName(u"speech")
        self.speech.setGeometry(QRect(40, 130, 251, 181))
        self.speech.setStyleSheet(u"color: yellow;")
        self.speak_now = QPushButton(self.centralwidget)
        self.speak_now.setObjectName(u"speak_now")
        self.speak_now.setGeometry(QRect(350, 290, 121, 51))
        self.speak_now.setStyleSheet(u"background-color: firebrick;\n"
"color: yellow;\n"
"\n"
"border: none;\n"
"outline:none;\n"
"border-radius: 15px;")
        self.speak_down = QPushButton(self.centralwidget)
        self.speak_down.setObjectName(u"speak_down")
        self.speak_down.setGeometry(QRect(530, 290, 121, 51))
        self.speak_down.setStyleSheet(u"background-color: firebrick;\n"
"color: yellow;\n"
"\n"
"border: none;\n"
"outline: none;\n"
"border-radius: 15px;")
        self.gender_choose = QComboBox(self.centralwidget)
        self.gender_choose.addItem(u"Male")
        self.gender_choose.addItem(u"Female")
        self.gender_choose.setObjectName(u"gender_choose")
        self.gender_choose.setGeometry(QRect(390, 140, 81, 31))
        self.gender_choose.setStyleSheet(u"background-color: firebrick;\n"
"color: yellow;\n"
"border-radius: 15px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"T2S", None))
        self.appDesc.setText(QCoreApplication.translate("MainWindow", u"A text-to-speech converter.", None))
        self.speak_now.setText(QCoreApplication.translate("MainWindow", u"Speak", None))
        self.speak_down.setText(QCoreApplication.translate("MainWindow", u"Download Speech", None))

        pass
    # retranslateUi

