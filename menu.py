from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
from ui_login import Ui_login
from database import Database
import sys


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.trys = 0
        self.setupUi(self)
        self.setWindowTitle("Login")

        self.btn_login.clicked.connect(self.check_login)
    
    def check_login(self):
        print('check_login')
        self.users = Database()
        self.users.conection()
        autentication = self.users.check_user(self.txt_login_nome.text(), self.txt_login_senha.text())
        print(f'autentication: {autentication} ({self.txt_login_nome.text()}, {self.txt_login_senha.text()})')

        if autentication == "Usuário" or autentication == "Administrador do Setor" or autentication == "Administrador Geral":
            self.window = MainWindow()
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
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Obras")

        #Páginas do menu
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_obras.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_obras))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_config.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_config))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_cadastrar_user.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastro_usuario.clicked.connect(self.subscribe_user)

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




if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
