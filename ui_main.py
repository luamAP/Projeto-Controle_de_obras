# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from IMAGE import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_btns_pgs = QFrame(self.centralwidget)
        self.frame_btns_pgs.setObjectName(u"frame_btns_pgs")
        self.frame_btns_pgs.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_pgs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btns_pgs)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame_btns_pgs)
        self.btn_home.setObjectName(u"btn_home")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_obras = QPushButton(self.frame_btns_pgs)
        self.btn_obras.setObjectName(u"btn_obras")

        self.horizontalLayout.addWidget(self.btn_obras)

        self.btn_sobre = QPushButton(self.frame_btns_pgs)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame_btns_pgs)
        self.btn_contato.setObjectName(u"btn_contato")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_config = QPushButton(self.frame_btns_pgs)
        self.btn_config.setObjectName(u"btn_config")

        self.horizontalLayout.addWidget(self.btn_config)


        self.verticalLayout.addWidget(self.frame_btns_pgs)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pg_obras = QWidget()
        self.pg_obras.setObjectName(u"pg_obras")
        self.verticalLayout_3 = QVBoxLayout(self.pg_obras)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.pg_obras)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.treeWidget = QTreeWidget(self.tables)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 60, 641, 192))
        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_obras)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.pages.addWidget(self.pg_contato)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.pg_cadastro)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.pg_cadastro)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_2.addWidget(self.txt_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_setor = QLineEdit(self.pg_cadastro)
        self.txt_setor.setObjectName(u"txt_setor")

        self.horizontalLayout_8.addWidget(self.txt_setor)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.txt_matricula = QLineEdit(self.pg_cadastro)
        self.txt_matricula.setObjectName(u"txt_matricula")

        self.horizontalLayout_3.addWidget(self.txt_matricula)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.txt_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_7.addWidget(self.cb_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.btn_cadastro_usuario = QPushButton(self.pg_cadastro)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")

        self.horizontalLayout_6.addWidget(self.btn_cadastro_usuario)

        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pages.addWidget(self.pg_sobre)
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.verticalLayout_5 = QVBoxLayout(self.pg_config)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.pg_config)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.btn_cadastrar_user = QPushButton(self.pg_config)
        self.btn_cadastrar_user.setObjectName(u"btn_cadastrar_user")

        self.horizontalLayout_9.addWidget(self.btn_cadastrar_user)

        self.label_12 = QLabel(self.pg_config)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.pages.addWidget(self.pg_config)

        self.verticalLayout.addWidget(self.pages)

        self.rodape = QLabel(self.centralwidget)
        self.rodape.setObjectName(u"rodape")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rodape.sizePolicy().hasHeightForWidth())
        self.rodape.setSizePolicy(sizePolicy1)
        self.rodape.setStyleSheet(u"background-image: url(:/img/rodape.png);\n"
"background-size: cover;\n"
"")
        self.rodape.setTextFormat(Qt.RichText)

        self.verticalLayout.addWidget(self.rodape)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_obras.setText(QCoreApplication.translate("MainWindow", u"OBRAS", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Portaria de Nomea\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Eng. Fiscal", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Empresa/Credor", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Objeto", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"N\u00b0 Contrato", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">CONTROLE DE OBRAS INTEGRADO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Setor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_senha.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_senha_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador do Setor", None))
        self.cb_perfil.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrador Geral", None))

        self.label_8.setText("")
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_9.setText("")
        self.label_11.setText("")
        self.btn_cadastrar_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_12.setText("")
        self.rodape.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">.</span></p></body></html>", None))
    # retranslateUi

