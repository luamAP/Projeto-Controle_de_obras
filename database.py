import sqlite3


class Database():
    def __init__(self, name='users.db') -> None:
        self.name = name

    def conection(self):
        self.connection = sqlite3.connect(self.name)

    def close_conection(self):
        try: self.connection.close()
        except AttributeError: print('Erro ao fechar conexão!')

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor TEXT NOT NULL,
                senha TEXT NOT NULL,
                acesso TEXT NOT NULL
            );""")
        except AttributeError: print('Erro ao criar tabela!')

    def insert_user(self, nome, setor, senha, acesso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""INSERT INTO users(nome, setor, senha, acesso) VALUES(?, ?, ?, ?);""", (nome, setor, senha, acesso))
            self.connection.commit()
        except AttributeError: print('Erro ao inserir dados!')

    def check_user(self, nome, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM users;""")
        
            # print(cursor.fetchall())
            for l in cursor.fetchall():
                # print(l)
                if l[1].upper()==nome.upper() and l[3]==senha: return l[4]
            return 'Sem acesso'

        except AttributeError: print('Erro ao verificar dados!')
    
        
if __name__=="__main__":
    db = Database()
    db.conection()
    db.create_table_users()
    db.close_conection()

