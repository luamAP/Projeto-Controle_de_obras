# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(412, 348)
        login.setCursor(QCursor(Qt.PointingHandCursor))
        login.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(29, 98, 351, 241))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.7);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(120, 160, 111, 31))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.txt_login_senha = QLineEdit(self.frame)
        self.txt_login_senha.setObjectName(u"txt_login_senha")
        self.txt_login_senha.setGeometry(QRect(70, 110, 221, 20))
        self.txt_login_senha.setEchoMode(QLineEdit.Password)
        self.txt_login_senha.setAlignment(Qt.AlignCenter)
        self.txt_login_matricula = QLineEdit(self.frame)
        self.txt_login_matricula.setObjectName(u"txt_login_matricula")
        self.txt_login_matricula.setGeometry(QRect(70, 60, 221, 20))
        self.txt_login_matricula.setAlignment(Qt.AlignCenter)
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 241, 101))
        self.label.setPixmap(QPixmap(u"IMAGE/logo-secretaria-seminf-header.png"))
        self.label.setScaledContents(True)
        QWidget.setTabOrder(self.txt_login_matricula, self.txt_login_senha)
        QWidget.setTabOrder(self.txt_login_senha, self.btn_login)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.txt_login_senha.setPlaceholderText(QCoreApplication.translate("login", u"Senha", None))
        self.txt_login_matricula.setPlaceholderText(QCoreApplication.translate("login", u"Matr\u00edcula", None))
        self.label.setText("")
    # retranslateUi

