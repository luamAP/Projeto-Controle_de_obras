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
        MainWindow.resize(903, 609)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_btns_pgs = QFrame(self.centralwidget)
        self.frame_btns_pgs.setObjectName(u"frame_btns_pgs")
        self.frame_btns_pgs.setStyleSheet(u"\n"
"background-color: rgb(255, 222, 155);")
        self.frame_btns_pgs.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_pgs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btns_pgs)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame_btns_pgs)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_obras = QPushButton(self.frame_btns_pgs)
        self.btn_obras.setObjectName(u"btn_obras")
        self.btn_obras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_obras.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_obras)

        self.btn_sobre = QPushButton(self.frame_btns_pgs)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame_btns_pgs)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_config = QPushButton(self.frame_btns_pgs)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_config.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_config)


        self.verticalLayout.addWidget(self.frame_btns_pgs)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(200, 80))
        font = QFont()
        font.setPointSize(16)
        self.pages.setFont(font)
        self.pages.setStyleSheet(u"background-color: rgb(255, 222, 155);")
        self.pg_obras = QWidget()
        self.pg_obras.setObjectName(u"pg_obras")
        self.verticalLayout_3 = QVBoxLayout(self.pg_obras)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.pg_obras)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 222, 155);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setMovable(False)
        self.tab_obras = QWidget()
        self.tab_obras.setObjectName(u"tab_obras")
        self.verticalLayout_10 = QVBoxLayout(self.tab_obras)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.tab_obras)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(300, 80))
        font2 = QFont()
        font2.setPointSize(23)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_17.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.txt_path = QLineEdit(self.tab_obras)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_path.setFont(font3)
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.txt_path)

        self.btn_open_dir = QPushButton(self.tab_obras)
        self.btn_open_dir.setObjectName(u"btn_open_dir")
        self.btn_open_dir.setMinimumSize(QSize(120, 35))
        self.btn_open_dir.setFont(font3)
        self.btn_open_dir.setStyleSheet(u"QPushButton {\n"
"                 background-color: #FFFFFF;  /* Cor de fundo branca */\n"
"                color: #000000;            /* Cor do texto preto */ \n"
"				border:1px solid ;\n"
"                border-radius: 5px;        /* Borda arredondada */\n"
"				border-top-right-radius:20px;\n"
"                padding: 5px 10px;          /* Espa\u00e7amento interno */\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: #000000;  /* Altera a cor de fundo ao passar o mouse */\n"
"                color: #FFFFFF;            /* Altera a cor do texto ao passar o mouse */\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_open_dir)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.radio_pdf = QRadioButton(self.tab_obras)
        self.radio_pdf.setObjectName(u"radio_pdf")

        self.horizontalLayout_16.addWidget(self.radio_pdf)

        self.radio_exce = QRadioButton(self.tab_obras)
        self.radio_exce.setObjectName(u"radio_exce")

        self.horizontalLayout_16.addWidget(self.radio_exce)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.tab_obras)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.btn_importar = QPushButton(self.tab_obras)
        self.btn_importar.setObjectName(u"btn_importar")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_importar.setFont(font4)
        self.btn_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;	\n"
"	background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"	border:1px solid;\n"
"	gridline-color: rgb(0, 0, 0);\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    \n"
"	\n"
"	background-color: rgb(195, 195, 195);\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btn_importar)

        self.label_16 = QLabel(self.tab_obras)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.tabWidget.addTab(self.tab_obras, "")
        self.tab_contratos = QWidget()
        self.tab_contratos.setObjectName(u"tab_contratos")
        self.verticalLayout_6 = QVBoxLayout(self.tab_contratos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_procurar_contratos = QPushButton(self.tab_contratos)
        self.btn_procurar_contratos.setObjectName(u"btn_procurar_contratos")
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setBold(True)
        font5.setItalic(True)
        font5.setWeight(75)
        self.btn_procurar_contratos.setFont(font5)
        self.btn_procurar_contratos.setTabletTracking(False)
        self.btn_procurar_contratos.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"	font-size: 16px;\n"
"	background-color: rgb(230, 230, 230);\n"
"    padding: 10px 10px;\n"
"	border-color: rgb(40, 40, 40);\n"
"	color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        icon = QIcon()
        iconThemeName = u"search"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btn_procurar_contratos.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.btn_procurar_contratos)

        self.txt_procurar_contratos = QLineEdit(self.tab_contratos)
        self.txt_procurar_contratos.setObjectName(u"txt_procurar_contratos")

        self.horizontalLayout_10.addWidget(self.txt_procurar_contratos)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.tw_contratos = QTreeWidget(self.tab_contratos)
        self.tw_contratos.setObjectName(u"tw_contratos")
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.tw_contratos.setFont(font6)
        self.tw_contratos.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.tw_contratos.setAutoScrollMargin(16)

        self.verticalLayout_6.addWidget(self.tw_contratos)

        self.tabWidget.addTab(self.tab_contratos, "")
        self.tab_financeiro = QWidget()
        self.tab_financeiro.setObjectName(u"tab_financeiro")
        self.verticalLayout_7 = QVBoxLayout(self.tab_financeiro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_procurar_financeiro = QPushButton(self.tab_financeiro)
        self.btn_procurar_financeiro.setObjectName(u"btn_procurar_financeiro")
        self.btn_procurar_financeiro.setFont(font5)
        self.btn_procurar_financeiro.setTabletTracking(False)
        self.btn_procurar_financeiro.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"	font-size: 16px;\n"
"	background-color: rgb(230, 230, 230);\n"
"    padding: 10px 10px;\n"
"	border-color: rgb(40, 40, 40);\n"
"	color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.btn_procurar_financeiro.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.btn_procurar_financeiro)

        self.txt_procurar_financeiro = QLineEdit(self.tab_financeiro)
        self.txt_procurar_financeiro.setObjectName(u"txt_procurar_financeiro")

        self.horizontalLayout_11.addWidget(self.txt_procurar_financeiro)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.tw_financeiro = QTreeWidget(self.tab_financeiro)
        self.tw_financeiro.setObjectName(u"tw_financeiro")
        self.tw_financeiro.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.tw_financeiro)

        self.tabWidget.addTab(self.tab_financeiro, "")
        self.tab_contabil = QWidget()
        self.tab_contabil.setObjectName(u"tab_contabil")
        self.verticalLayout_8 = QVBoxLayout(self.tab_contabil)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_procurar_contabil = QPushButton(self.tab_contabil)
        self.btn_procurar_contabil.setObjectName(u"btn_procurar_contabil")
        self.btn_procurar_contabil.setFont(font5)
        self.btn_procurar_contabil.setTabletTracking(False)
        self.btn_procurar_contabil.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"	font-size: 16px;\n"
"	background-color: rgb(230, 230, 230);\n"
"    padding: 10px 10px;\n"
"	border-color: rgb(40, 40, 40);\n"
"	color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.btn_procurar_contabil.setIcon(icon)

        self.horizontalLayout_12.addWidget(self.btn_procurar_contabil)

        self.txt_procurar_contabil = QLineEdit(self.tab_contabil)
        self.txt_procurar_contabil.setObjectName(u"txt_procurar_contabil")

        self.horizontalLayout_12.addWidget(self.txt_procurar_contabil)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.tw_contabil = QTreeWidget(self.tab_contabil)
        self.tw_contabil.setObjectName(u"tw_contabil")
        self.tw_contabil.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.tw_contabil)

        self.tabWidget.addTab(self.tab_contabil, "")
        self.tab_engenharia = QWidget()
        self.tab_engenharia.setObjectName(u"tab_engenharia")
        self.verticalLayout_9 = QVBoxLayout(self.tab_engenharia)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_procurar_engenharia = QPushButton(self.tab_engenharia)
        self.btn_procurar_engenharia.setObjectName(u"btn_procurar_engenharia")
        self.btn_procurar_engenharia.setFont(font5)
        self.btn_procurar_engenharia.setTabletTracking(False)
        self.btn_procurar_engenharia.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"	font-size: 16px;\n"
"	background-color: rgb(230, 230, 230);\n"
"    padding: 10px 10px;\n"
"	border-color: rgb(40, 40, 40);\n"
"	color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.btn_procurar_engenharia.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.btn_procurar_engenharia)

        self.txt_procurar_engenharia = QLineEdit(self.tab_engenharia)
        self.txt_procurar_engenharia.setObjectName(u"txt_procurar_engenharia")

        self.horizontalLayout_13.addWidget(self.txt_procurar_engenharia)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.tw_engenharia = QTreeWidget(self.tab_engenharia)
        self.tw_engenharia.setObjectName(u"tw_engenharia")
        self.tw_engenharia.setFont(font6)
        self.tw_engenharia.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_9.addWidget(self.tw_engenharia)

        self.tabWidget.addTab(self.tab_engenharia, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_obras)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.label_13 = QLabel(self.pg_contato)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 40, 131, 31))
        font7 = QFont()
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_13.setFont(font7)
        self.pages.addWidget(self.pg_contato)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 222, 155);")

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.pg_cadastro.setStyleSheet(u"background-color: rgb(255, 222, 155, 0.5);")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.pg_cadastro)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(40, -1, 20, -1)
        self.label_3 = QLabel(self.pg_cadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")

        self.horizontalLayout_2.addWidget(self.txt_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(40, -1, 20, -1)
        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.txt_matricula = QLineEdit(self.pg_cadastro)
        self.txt_matricula.setObjectName(u"txt_matricula")
        self.txt_matricula.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")

        self.horizontalLayout_3.addWidget(self.txt_matricula)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(40, -1, 20, -1)
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.txt_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(40, -1, 20, -1)
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(40, -1, 20, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.cb_setor = QComboBox(self.pg_cadastro)
        self.cb_setor.addItem("")
        self.cb_setor.addItem("")
        self.cb_setor.addItem("")
        self.cb_setor.addItem("")
        self.cb_setor.setObjectName(u"cb_setor")
        self.cb_setor.setMinimumSize(QSize(330, 0))
        self.cb_setor.setFont(font3)
        self.cb_setor.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")

        self.horizontalLayout_7.addWidget(self.cb_setor)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setMinimumSize(QSize(300, 0))
        self.cb_perfil.setFont(font3)
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255, 0.75);")

        self.horizontalLayout_8.addWidget(self.cb_perfil)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.btn_cadastro_usuario = QPushButton(self.pg_cadastro)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
        self.btn_cadastro_usuario.setFont(font4)
        self.btn_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_usuario.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_cadastro_usuario)

        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(255, 222, 155, 0);")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.label_14 = QLabel(self.pg_sobre)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(400, 20, 101, 71))
        self.label_14.setFont(font7)
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
        self.btn_cadastrar_user.setStyleSheet(u"/* Estilos padr\u00e3o do bot\u00e3o */\n"
"QPushButton {\n"
"    display: inline-block;\n"
"	font-size: 16px;\n"
"    padding: 12px 20px;	\n"
"	background-color: rgb(255, 255, 255);\n"
"    \n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"	border:1px solid;\n"
"	gridline-color: rgb(0, 0, 0);\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* Estilos do bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    \n"
"	\n"
"	background-color: rgb(195, 195, 195);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_cadastrar_user)

        self.label_12 = QLabel(self.pg_config)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.pages.addWidget(self.pg_config)

        self.verticalLayout.addWidget(self.pages)

        self.rodape = QLabel(self.centralwidget)
        self.rodape.setObjectName(u"rodape")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rodape.sizePolicy().hasHeightForWidth())
        self.rodape.setSizePolicy(sizePolicy2)
        self.rodape.setStyleSheet(u"background-image: url(:/img/rodape.png);\n"
"background-size: cover;\n"
"")
        self.rodape.setTextFormat(Qt.RichText)

        self.verticalLayout.addWidget(self.rodape)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_home, self.btn_obras)
        QWidget.setTabOrder(self.btn_obras, self.btn_sobre)
        QWidget.setTabOrder(self.btn_sobre, self.btn_contato)
        QWidget.setTabOrder(self.btn_contato, self.btn_config)
        QWidget.setTabOrder(self.btn_config, self.txt_nome)
        QWidget.setTabOrder(self.txt_nome, self.txt_matricula)
        QWidget.setTabOrder(self.txt_matricula, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.txt_senha_2)
        QWidget.setTabOrder(self.txt_senha_2, self.cb_setor)
        QWidget.setTabOrder(self.cb_setor, self.cb_perfil)
        QWidget.setTabOrder(self.cb_perfil, self.btn_cadastro_usuario)
        QWidget.setTabOrder(self.btn_cadastro_usuario, self.txt_procurar_contratos)
        QWidget.setTabOrder(self.txt_procurar_contratos, self.tw_contratos)
        QWidget.setTabOrder(self.tw_contratos, self.btn_procurar_financeiro)
        QWidget.setTabOrder(self.btn_procurar_financeiro, self.txt_procurar_financeiro)
        QWidget.setTabOrder(self.txt_procurar_financeiro, self.tw_financeiro)
        QWidget.setTabOrder(self.tw_financeiro, self.btn_procurar_contabil)
        QWidget.setTabOrder(self.btn_procurar_contabil, self.txt_procurar_contabil)
        QWidget.setTabOrder(self.txt_procurar_contabil, self.tw_contabil)
        QWidget.setTabOrder(self.tw_contabil, self.btn_procurar_engenharia)
        QWidget.setTabOrder(self.btn_procurar_engenharia, self.txt_procurar_engenharia)
        QWidget.setTabOrder(self.txt_procurar_engenharia, self.tw_engenharia)
        QWidget.setTabOrder(self.tw_engenharia, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.btn_open_dir)
        QWidget.setTabOrder(self.btn_open_dir, self.radio_pdf)
        QWidget.setTabOrder(self.radio_pdf, self.radio_exce)
        QWidget.setTabOrder(self.radio_exce, self.btn_importar)
        QWidget.setTabOrder(self.btn_importar, self.btn_procurar_contratos)
        QWidget.setTabOrder(self.btn_procurar_contratos, self.btn_cadastrar_user)
        QWidget.setTabOrder(self.btn_cadastrar_user, self.txt_path)

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
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">IMPORTAR OBRAS</p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta de destino", None))
        self.btn_open_dir.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.radio_pdf.setText(QCoreApplication.translate("MainWindow", u"Gerar em PDF", None))
        self.radio_exce.setText(QCoreApplication.translate("MainWindow", u"Gerar em Excel", None))
        self.label_15.setText("")
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_16.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_obras), QCoreApplication.translate("MainWindow", u"Obras", None))
        self.btn_procurar_contratos.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        ___qtreewidgetitem = self.tw_contratos.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Processo", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Portaria de Nomea\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Eng. Fiscal", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Empresa/Credor", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Origem", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Objeto", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"N\u00b0 Contrato", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contratos), QCoreApplication.translate("MainWindow", u"Contratos", None))
        self.btn_procurar_financeiro.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        ___qtreewidgetitem1 = self.tw_financeiro.headerItem()
        ___qtreewidgetitem1.setText(11, QCoreApplication.translate("MainWindow", u"Saldo a Faturar (R$)", None));
        ___qtreewidgetitem1.setText(10, QCoreApplication.translate("MainWindow", u"Valor Faturado (R$)", None));
        ___qtreewidgetitem1.setText(9, QCoreApplication.translate("MainWindow", u"Nota Fiscal", None));
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("MainWindow", u"Medi\u00e7\u00f5es", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"Valor Total (R$)", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"Valor Anulado (R$)", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"Valor Empenhado (R$)", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Valor de Aditivo (R$)", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Redu\u00e7\u00e3o do Valor do Contrato (R$)", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Valor do Contrato (R$)", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Indeniza\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"N\u00b0 Contrato", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_financeiro), QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.btn_procurar_contabil.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        ___qtreewidgetitem2 = self.tw_contabil.headerItem()
        ___qtreewidgetitem2.setText(8, QCoreApplication.translate("MainWindow", u"Deprecia\u00e7\u00e3o", None));
        ___qtreewidgetitem2.setText(7, QCoreApplication.translate("MainWindow", u"Conta Cont\u00e1bil", None));
        ___qtreewidgetitem2.setText(6, QCoreApplication.translate("MainWindow", u"Natureza da Despesa", None));
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"Fonte de Recurso", None));
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Programa de Trabalho", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Unidade Or\u00e7amet\u00e1ria", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Empenho", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Data do empenho", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"N\u00b0 Contrato", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contabil), QCoreApplication.translate("MainWindow", u"Cont\u00e1bil", None))
        self.btn_procurar_engenharia.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        ___qtreewidgetitem3 = self.tw_engenharia.headerItem()
        ___qtreewidgetitem3.setText(8, QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtreewidgetitem3.setText(7, QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da Obra", None));
        ___qtreewidgetitem3.setText(6, QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None));
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("MainWindow", u"T\u00e9rmino", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"In\u00edcio", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"Prazo Total (DIAS)", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"Aditivo de Prazo (DIAS)", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Prazo do Contrato (DIAS)", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"N\u00b0 Contrato", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_engenharia), QCoreApplication.translate("MainWindow", u"Engenharia", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">CONTROLE DE OBRAS INTEGRADO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_senha.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_senha_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Setor", None))
        self.cb_setor.setItemText(0, QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.cb_setor.setItemText(1, QCoreApplication.translate("MainWindow", u"Contrato", None))
        self.cb_setor.setItemText(2, QCoreApplication.translate("MainWindow", u"Engenharia", None))
        self.cb_setor.setItemText(3, QCoreApplication.translate("MainWindow", u"Cont\u00e1bil", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador do Setor", None))
        self.cb_perfil.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrador Geral", None))

        self.label_8.setText("")
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_9.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_11.setText("")
        self.btn_cadastrar_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_12.setText("")
        self.rodape.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">.</span></p></body></html>", None))
    # retranslateUi

