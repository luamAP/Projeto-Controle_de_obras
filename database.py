import sqlite3

import pandas as pd

from tkinter import Tk, filedialog, messagebox, simpledialog

import os


class Database():
    def __init__(self, name='DATABASE/USERS.db') -> None:
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
                matricula TEXT NOT NULL,
                setor TEXT NOT NULL,
                senha TEXT NOT NULL,
                acesso TEXT NOT NULL
            );""")
        except AttributeError: print('Erro ao criar tabela!')

    def insert_user(self, nome, matricula, setor, senha, acesso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""INSERT INTO users(nome, matricula, setor, senha, acesso) VALUES(?, ?, ?, ?, ?);""", (nome, matricula, setor, senha, acesso))
            self.connection.commit()
        except AttributeError: print('Erro ao inserir dados!')
        except sqlite3.OperationalError: 
            self.create_table_users()
            cursor = self.connection.cursor()
            cursor.execute("""INSERT INTO users(nome, matricula, setor, senha, acesso) VALUES(?, ?, ?, ?, ?);""", (nome, matricula, setor, senha, acesso))
            self.connection.commit()

    def check_user(self, nome, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM users;""")
        
            # print(cursor.fetchall())
            for l in cursor.fetchall():
                # print(l)
                if l[2].upper()==nome.upper() and l[4]==senha: return l[5]
            return 'Sem acesso'

        except AttributeError: print('Erro ao verificar dados!')
    
    def adicionar_informacoes_ao_banco_de_dados(self, dataframe:pd.DataFrame, nome_banco_de_dados:str, nome_tabela:str):
        """
        Adds information from a dataframe to a specified database table.

        Args:
            dataframe (pandas.DataFrame): The dataframe containing the information to be added.
            nome_banco_de_dados (str): The name of the database to connect to.
            nome_tabela (str): The name of the table in the database to add the information to.

        Returns:
            str: A message indicating that the information has been added to the database.
        """
        colunas = dataframe.columns

        # Exclui linhas duplicadas no dataframe, usando o metodo 'duplicated' e negando os verdadeiros com '~'.
        dataframe = dataframe[~dataframe.duplicated()]

        # Dicionário de mapeamento para renomear as colunas tirando espaços para '_'
        novo_nome_colunas = dict(zip(colunas, [c.replace(' ', '_') for c in colunas]))

        # Use o método rename
        dataframe.rename(columns=novo_nome_colunas, inplace=True)

        # if messagebox.askyesno("Confirmação", "Você deseja adicionar informações ao banco de dados?"):
        
        # Adiciona as informações do DataFrame à tabela no banco de dados
        dataframe.to_sql(nome_tabela, self.conection(), if_exists='replace', index=False)

        self.verificar_e_tratar_duplicatas(nome_tabela, self.conection())
        
        # Fecha a conexão
        self.close_conection()

        return "Informações adicionadas ao banco de dados!"
            # messagebox.showinfo("Sucesso", "Informações adicionadas ao banco de dados!")

    def get_year():
        """
        Retrieves the year from the user.
        
        Returns:
            int: The year inputted by the user.
        """
        janela = Tk()
        year = simpledialog.askinteger("Informe o ano", "Digite o ano:")
        # if year is not None:  # Verifica se o usuário forneceu um valor válido
        janela.destroy()
        return year

    def verificar_e_tratar_duplicatas(table_name, conn):
        """
        Verifies and treats duplicates in a given table.

        Args:
            table_name (str): The name of the table to verify and treat duplicates.
            conn (Connection): The connection object to the database.

        Returns:
            None
        """
        # Conectar ao banco de dados
        cursor = conn.cursor()

        # Obter informações sobre as colunas da tabela
        cursor.execute(f"PRAGMA table_info({table_name})")
        column_info = cursor.fetchall()

        # Construir uma lista de nomes de colunas
        column_names = [info[1] for info in column_info]

        # Construir uma consulta SQL dinâmica para verificar duplicatas
        sql_check_duplicates = f'''
            SELECT *, COUNT(*) as qtd_duplicadas
            FROM {table_name}
            GROUP BY {', '.join(column_names)}
            HAVING COUNT(*) > 1
        '''

        # Executar a consulta para verificar duplicatas
        cursor.execute(sql_check_duplicates)
        duplicates = cursor.fetchall()

        if duplicates:
            print("Linhas duplicadas encontradas:")
            for duplicate in duplicates:
                print(f"Quantidade de duplicatas: {duplicate[-1]}")

            # Construir uma consulta SQL dinâmica para tratar duplicatas
            # (remover todas, exceto a primeira ocorrência)
            sql_remove_duplicates = f'''
                DELETE FROM {table_name}
                WHERE ROWID NOT IN (
                    SELECT MIN(ROWID)
                    FROM {table_name}
                    GROUP BY {', '.join(column_names)}
                    HAVING COUNT(*) > 1
                )
            '''

            # Executar a consulta para tratar duplicatas
            cursor.execute(sql_remove_duplicates)
            print("Linhas duplicadas tratadas.")

            # Confirmar e fechar a conexão
            conn.commit()
        else: print("Nenhuma linha duplicada encontrada.")

    def incluir_coluna_no_banco_de_dados(nome_banco_de_dados, nome_tabela, nome_coluna, valores_coluna=None):
        """
        Adds a new column to a specified table in a given database.

        Parameters:
            nome_banco_de_dados (str): The name of the database.
            nome_tabela (str): The name of the table.
            nome_coluna (str): The name of the new column.
            valores_coluna (list, optional): A list of values to populate the new column. Default is None.

        Returns:
            None

        Raises:
            None
        """
        # if messagebox.askyesno("Confirmação", "Você deseja incluir uma nova coluna no banco de dados?"):
            # Conecta-se ao banco de dados
        conn = sqlite3.connect(nome_banco_de_dados)
        
        # Cria uma consulta SQL para adicionar uma nova coluna
        consulta = f'ALTER TABLE {nome_tabela} ADD COLUMN "{nome_coluna}"'
        
        # Executa a consulta para adicionar a nova coluna
        conn.execute(consulta)
        
        if valores_coluna:
            # Atualiza a tabela com os valores da nova coluna
            for valor in valores_coluna:
                consulta = f'UPDATE {nome_tabela} SET "{nome_coluna}" = ?'
                conn.execute(consulta, (valor,))
        
        # Commit para salvar as alterações
        conn.commit()
        
        # Fecha a conexão
        conn.close()
        # messagebox.showinfo("Sucesso", "Nova coluna incluída no banco de dados!")

    def carregar_arquivos():
        """
        Prompt the user to select a file to load and return the selected file path.

        Returns:
            str: The selected file path.
        """
        janela = Tk()
        file = filedialog.askopenfilename(title="Selecione o arquivo para carregar")
        janela.destroy()

        return file

    def salvar_arquivos():
        """
        Saves files to a selected destination and returns the path of the saved file.

        Returns:
            str: The path of the saved file.
        """
        janela = Tk()
        file = filedialog.asksaveasfilename(title="Selecione o destino para salvar o arquivo")
        janela.destroy()

        return file

    def alerta_existe(self, termo, tempo=5):
        """
        Check if an alert exists and accept it if a specific term is present in the alert text.

        Parameters:
            self (object): The instance of the class.
            termo (str): The term to search for in the alert text.
            tempo (int, optional): The time to wait before checking for the alert. Defaults to 5.

        Returns:
            bool: True if the alert exists and the term is present, False otherwise.
        """
        from selenium.webdriver.remote.errorhandler import NoAlertPresentException
        from navegacao import para
        para(tempo)
        try: 
            a = self.navegador.switch_to.alert
            if termo in a.text: a.accept()
            return True
        except NoAlertPresentException: return False

    def ler_extrato(ne):
        """
        Reads an Excel file containing an extract of commitments and returns a filtered DataFrame.

        :param ne: A string representing the commitment number.
        :return: A pandas DataFrame containing the filtered extract of commitments.
        """
        downloads = os.path.expanduser("~"+os.sep+"Downloads")
        caminho = os.path.join(downloads, 'RELEXTRATOEMPENHO.xls')
        # "C:\Users\luan.pinto\Downloads\RELEXTRATOEMPENHO.xls"

        df = pd.read_excel(caminho)[['Evento', 'Documento', 'Data', 'Valor']][:-2]
        df['EMPENHO'] = ne

        os.remove(caminho)
        return df

    def clonar_banco(db_origem, db_destino, origem_table):
        """
        Clones a database table from one database to another.

        Parameters:
            db_origem (str): The path to the source database.
            db_destino (str): The path to the destination database.
            origem_table (str): The name of the table to be cloned.

        Returns:
            None
        """
        # Conectar ao banco de dados de origem
        conn_origem = sqlite3.connect(db_origem)
        dataframe = pd.read_sql_query(f"SELECT * FROM {origem_table}", conn_origem)
        conn_origem.close()

        adicionar_informacoes_ao_banco_de_dados(dataframe, db_destino, origem_table)

    def excluir_tabela(tabela, conn):
        """
        Delete a table from the database.

        Parameters:
            tabela (str): The name of the table to be deleted.
            conn (Connection): The connection to the database.

        Returns:
            None
        """
        # Crie um objeto cursor
        cursor = conn.cursor()
        # Execute o comando SQL para excluir a tabela
        cursor.execute(f'DROP TABLE IF EXISTS {tabela}')
        # Confirme a operação
        conn.commit()
        # Feche a conexão com o banco de dados
        conn.close()

    def atualiza_dados(nome_banco_de_dados, sua_tabela, atualizar_coluna, coluna_criterio, novo_valor, critério):
        """
        Updates data in a specified database table based on a given criteria.

        Args:
            nome_banco_de_dados (str): The name of the database to connect to.
            sua_tabela (str): The name of the table to update.
            atualizar_coluna (str): The name of the column to update.
            coluna_criterio (str): The name of the column to use as the criteria for updating.
            novo_valor (str): The new value to set in the updated column.
            critério (str): The criteria to use for updating the data.

        Returns:
            None
        """
        # Conectar ao banco de dados
        conn = sqlite3.connect(nome_banco_de_dados)
        cursor = conn.cursor()

        # Atualizar dados na tabela
        cursor.execute(f'UPDATE {sua_tabela} SET {atualizar_coluna} = ? WHERE {coluna_criterio} = ?', (novo_valor, critério))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão
        conn.close()


if __name__=="__main__":
    db = Database()
    db.conection()
    db.create_table_users()
    db.close_conection()

