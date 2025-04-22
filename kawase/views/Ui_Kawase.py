# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(335, 275)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(50, 190, 211, 31))
        font = QFont()
        font.setPointSize(12)
        self.button_start.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(51, 24, 31, 16))
        self.label.setFont(font)
        self.currency_list = QComboBox(self.centralwidget)
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.addItem("")
        self.currency_list.setObjectName(u"currency_list")
        self.currency_list.setGeometry(QRect(160, 20, 121, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(20)
        sizePolicy1.setHeightForWidth(self.currency_list.sizePolicy().hasHeightForWidth())
        self.currency_list.setSizePolicy(sizePolicy1)
        self.currency_list.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 101, 16))
        self.label_2.setFont(font)
        self.lineEdit_interval = QLineEdit(self.centralwidget)
        self.lineEdit_interval.setObjectName(u"lineEdit_interval")
        self.lineEdit_interval.setGeometry(QRect(160, 100, 113, 21))
        self.lineEdit_interval.setFont(font)
        self.checkBox_judge = QCheckBox(self.centralwidget)
        self.checkBox_judge.setObjectName(u"checkBox_judge")
        self.checkBox_judge.setGeometry(QRect(50, 140, 111, 20))
        self.checkBox_judge.setFont(font)
        self.checkBox_chart = QCheckBox(self.centralwidget)
        self.checkBox_chart.setObjectName(u"checkBox_chart")
        self.checkBox_chart.setGeometry(QRect(170, 140, 81, 20))
        self.checkBox_chart.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 60, 111, 16))
        self.label_3.setFont(font)
        self.lineEdit_Year = QLineEdit(self.centralwidget)
        self.lineEdit_Year.setObjectName(u"lineEdit_Year")
        self.lineEdit_Year.setGeometry(QRect(160, 60, 113, 21))
        self.lineEdit_Year.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 335, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u70ba\u66ff", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8ca8", None))
        self.currency_list.setItemText(0, QCoreApplication.translate("MainWindow", u"USD/JPY", None))
        self.currency_list.setItemText(1, QCoreApplication.translate("MainWindow", u"EUR/JPY", None))
        self.currency_list.setItemText(2, QCoreApplication.translate("MainWindow", u"EUR/USD", None))
        self.currency_list.setItemText(3, QCoreApplication.translate("MainWindow", u"EUR/GBP", None))
        self.currency_list.setItemText(4, QCoreApplication.translate("MainWindow", u"AUD/JPY", None))
        self.currency_list.setItemText(5, QCoreApplication.translate("MainWindow", u"AUD/USD", None))
        self.currency_list.setItemText(6, QCoreApplication.translate("MainWindow", u"AUD/NZD", None))
        self.currency_list.setItemText(7, QCoreApplication.translate("MainWindow", u"NZD/JPY", None))
        self.currency_list.setItemText(8, QCoreApplication.translate("MainWindow", u"NZD/USD", None))
        self.currency_list.setItemText(9, QCoreApplication.translate("MainWindow", u"CAD/JPY", None))
        self.currency_list.setItemText(10, QCoreApplication.translate("MainWindow", u"USD/CAD", None))
        self.currency_list.setItemText(11, QCoreApplication.translate("MainWindow", u"GBP/JPY", None))
        self.currency_list.setItemText(12, QCoreApplication.translate("MainWindow", u"GBP/USD", None))
        self.currency_list.setItemText(13, QCoreApplication.translate("MainWindow", u"TRY/JPY", None))
        self.currency_list.setItemText(14, QCoreApplication.translate("MainWindow", u"ZAR/JPY", None))
        self.currency_list.setItemText(15, QCoreApplication.translate("MainWindow", u"MXN/JPY", None))

        self.currency_list.setCurrentText(QCoreApplication.translate("MainWindow", u"USD/JPY", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u30c1\u30e3\u30fc\u30c8\u306e\u9593\u9694", None))
        self.lineEdit_interval.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.checkBox_judge.setText(QCoreApplication.translate("MainWindow", u"\u58f2\u8cb7\u30b8\u30e3\u30c3\u30b8", None))
        self.checkBox_chart.setText(QCoreApplication.translate("MainWindow", u"\u30c1\u30e3\u30fc\u30c8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u30c7\u30fc\u30bf\u53d6\u5f97\u5e74\u6570", None))
        self.lineEdit_Year.setText(QCoreApplication.translate("MainWindow", u"2", None))
    # retranslateUi

