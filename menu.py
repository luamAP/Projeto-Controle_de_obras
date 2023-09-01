from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QTreeWidgetItem
from PySide2 import QtCore
from UI.ui_main import Ui_MainWindow
from UI.ui_login import Ui_login
from database import Database
import sys
import re
import sqlite3
import pandas as pd
import numpy as np


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.trys = 0
        self.setupUi(self)
        self.setWindowTitle("Login")

        self.btn_login.clicked.connect(self.check_login)
    
    def check_login(self):
        # print('check_login')
        self.users = Database()
        self.users.conection()
        autentication = self.users.check_user(self.txt_login_nome.text(), self.txt_login_senha.text())
        # print(f'autentication: {autentication} ({self.txt_login_nome.text()}, {self.txt_login_senha.text()})')

        if autentication in ["Usuário", "Administrador do Setor", "Administrador Geral"]:
            # print(autentication)
            self.window = MainWindow(autentication)
            self.window.show()
            self.close()
        else:
            if self.trys < 3:
                self.trys += 1
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Senha Incorreta")
                msg.setText(f"Login ou Senha incorretas!\n\nTentativas: {self.trys} de 3")
                msg.exec_()
            if self.trys == 3:
                #bloquear usuario
                self.users.close_conection()
                sys.exit(0)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Obras")
        self.pages.setCurrentWidget(self.pg_home)

        print(user)
        if user =="Usuário": self.btn_cadastrar_user.setVisible(False)

        #Páginas do menu
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_obras.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_obras))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_config.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_config))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_cadastrar_user.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastro_usuario.clicked.connect(self.subscribe_user)

        self.reset_tables()

    def subscribe_user(self):
        if self.txt_senha_2.text() != self.txt_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Divergentes")
            msg.setText("As senhas devem ser iguais!")
            msg.exec_()
            return None

        nome = self.txt_nome.text()
        setor = self.txt_setor.text()
        senha = self.txt_senha.text()
        acesso = self.cb_perfil.currentText()

        if nome == "" or setor == "" or senha == "" or acesso == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campos Vazios")
            msg.setText("Todos os campos devem ser preenchidos!")
            msg.exec_()
            return None

        db=Database()
        db.conection()
        db.insert_user(nome, setor, senha, acesso)
        db.close_conection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadasto de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_setor.setText("")
        self.txt_matricula.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")
        self.txt_nome.setText("")

    def table_contratos(self):
        self.tw_contratos.setStyleSheet(u' QHeaderView{ color:black}; color: rgb(0, 0, 0); font-size: 15px;')

        # cn = sqlite3.connect('contratos.db')
        # resultado = pd.read_sql_query("SELECT * FROM ", cn)

        resultado = pd.read_excel('contratos.xlsx')
        resultado = resultado.astype(str)
        resultado.fillna(np.nan, inplace=True)
        resultado.replace('nan', '', inplace=True)

        resultado = resultado.values.tolist()   

        self.x=''
        for i in resultado:
            if i[0]==self.x: 
                QTreeWidgetItem(self.campo, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
            else:
                self.campo = QTreeWidgetItem(self.tw_contratos, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
                # Adiciona um CheckBox na tabela
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_contratos.setSortingEnabled(True)
    
    def table_contabil(self):
        self.tw_contabil.setStyleSheet(u' QHeaderView{ color:black}; color: rgb(0, 0, 0); font-size: 15px;')

        resultado = pd.read_excel('contabil.xlsx')

        resultado.fillna('', inplace=True)
        resultado.replace(np.nan, '', inplace=True)
        resultado['DATA DO EMPENHO'] = resultado['DATA DO EMPENHO'].astype(str).replace('NaT', '')

        # cn = sqlite3.connect('contratos.db')
        # resultado = pd.read_sql_query("SELECT * FROM ", cn)
        resultado = resultado.values.tolist()   

        self.x=''
        for i in resultado:
            if i[0]==self.x: 
                QTreeWidgetItem(self.campo, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
            else:
                self.campo = QTreeWidgetItem(self.tw_contabil, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
                # Adiciona um CheckBox na tabela
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_contabil.setSortingEnabled(True)

        # for i in range(1,8): self.tw_contratos.resizeColumnToContents(i)

    def table_obras(self):
        return 0
        self.tw_contratos.setStyleSheet(u' QHeaderView{ color:black}; color: rgb(0, 0, 0); font-size: 15px;')

        resultado = pd.read_excel('contratos.xlsx')

        # cn = sqlite3.connect('contratos.db')
        # resultado = pd.read_sql_query("SELECT * FROM ", cn)
        resultado = resultado.values.tolist()   

        self.x=''
        for i in resultado:
            if i[0]==self.x: 
                QTreeWidgetItem(self.campo, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
            else:
                self.campo = QTreeWidgetItem(self.tw_contratos, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
                # Adiciona um CheckBox na tabela
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_contratos.setSortingEnabled(True)

        # for i in range(1,8): self.tw_contratos.resizeColumnToContents(i)

    def table_engenharia(self):
        self.tw_engenharia.setStyleSheet(u' QHeaderView{ color:black}; color: rgb(0, 0, 0); font-size: 15px;')

        # cn = sqlite3.connect('contratos.db')
        # resultado = pd.read_sql_query("SELECT * FROM ", cn)

        resultado = pd.read_excel('engenharia.xlsx')
                
        for coluna in resultado.columns: 
            # print(coluna)
            if 'DIAS' in coluna or 'VALIDADE' in coluna: 
                resultado[coluna].fillna(0, inplace=True)
                resultado[coluna] = resultado[coluna].replace([np.inf, -np.inf], 0).astype(int)
                resultado[coluna] = resultado[coluna].astype(int)
            elif 'TÉRMINO' in coluna or 'INÍCIO' in coluna: 
                resultado[coluna] = pd.to_datetime(resultado[coluna], errors='coerce')

        # Preencha todas as células vazias e as zeradas com NaN 
        resultado[resultado.columns] = resultado[resultado.columns].astype(str)
        # resultado.fillna(np.nan, inplace=True)
        resultado.replace('0', '', inplace=True)
        resultado.replace('nan', '', inplace=True)

        resultado = resultado.values.tolist()

        self.x=''
        for i in resultado:
            if i[0]==self.x: 
                QTreeWidgetItem(self.campo, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
            else:
                self.campo = QTreeWidgetItem(self.tw_engenharia, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
                # Adiciona um CheckBox na tabela
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_engenharia.setSortingEnabled(True)

        # for i in range(1,8): self.tw_contratos.resizeColumnToContents(i)
    
    def table_financeiro(self):
        self.tw_financeiro.setStyleSheet(u' QHeaderView{ color:black}; color: rgb(0, 0, 0); font-size: 15px;')

        resultado = pd.read_excel('financeiro.xlsx')
        include = ['CONTRATO N°', 'MEDIÇÕES', 'NOTA FISCAL']
        resultado[include] = resultado[include].astype(str)

        for coluna in resultado.columns: 
            tp_coluna = resultado[coluna].dtype
            # print(coluna, tp_coluna)
            resultado[coluna] = resultado[coluna].replace({'-//-': ''})
            if tp_coluna!="object": 
                resultado[coluna] = resultado[coluna].astype(float)
                # Formata os valores para formato de moeda real
                resultado[coluna] = resultado[coluna].apply(lambda x: '{:,.2f}'.format(x).replace('.', ' ').replace(',', '.').replace(' ', ','))

        # Preencha todas as células vazias com NaN
        resultado.replace(np.nan, '', inplace=True)
        resultado.replace('nan', '', inplace=True)

        # cn = sqlite3.connect('contratos.db')
        # resultado = pd.read_sql_query("SELECT * FROM ", cn)
        resultado = resultado.values.tolist()   

        self.x=''
        for i in resultado:
            if i[0]==self.x: 
                QTreeWidgetItem(self.campo, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
            else:
                self.campo = QTreeWidgetItem(self.tw_financeiro, i) # item = QWidget.QTreeWidgetItem(self.tab_contratos, i) 
                # Adiciona um CheckBox na tabela
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_financeiro.setSortingEnabled(True)

        # for i in range(1,8): self.tw_contratos.resizeColumnToContents(i)

    def reset_tables(self):
        # self.tw_obras.clear()
        self.tw_contratos.clear()
        self.tw_contabil.clear()
        self.tw_engenharia.clear()
        self.tw_financeiro.clear()

        self.table_contratos()
        self.table_contabil()
        self.table_engenharia()
        self.table_financeiro()
        # self.table_obras()


if __name__=="__main__":
    app = QApplication(sys.argv)
    # window = Login()
    window = MainWindow('Administrador do Setor')
    window.show()
    app.exec_()
