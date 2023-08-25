import os
import time
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from tkinter import Tk, messagebox
import pyautogui

def para(segundos): 
    """
    Pausa a execução do programa por um número específico de segundos.

    Parâmetros:
        segundos (int): O número de segundos para pausar o programa.

    Retorna:
        None
    """
    time.sleep(segundos)
def contar():
    """
    Retorna o tempo atual em segundos desde a época Unix.

    Retorna:
        float: O tempo atual em segundos.
    """
    return time.time()

class Navegacao():

    @staticmethod
    def _mensagem(titulo, mensagem):
        """
        Exibe uma mensagem de alerta.     
        
        Parâmetros:
            titulo (str): O título da caixa de mensagem.
            mensagem (str): A mensagem a ser exibida na caixa de mensagem.
    
        Retorna:
            Nenhum
        """
        janela = Tk()
        messagebox.showinfo(titulo, mensagem)
        janela.destroy()

    def _espera_login(self, site=''):
        """
+       Aguarda o login ocorrer e realiza ações específicas com base no valor do parâmetro `site`.
+
+       Parâmetros:
+            site (str): O site de destino para o login. Os valores possíveis são uma string vazia ('') para um login manual, 'afim' ou 'pmm' para outro login específico.
+
+       Retorna:
+            Nenhum
        """  
        if site=='':
            self._mensagem('Esperando fazer login', 'Faça login para prosseguir a automação!',)
            pag_atual = self.navegador.current_url
            print('Página atual: {}'.format(self.navegador.current_url))
            while pag_atual==self.navegador.current_url: continue        
            print('Página atual: {}'.format(self.navegador.current_url))
        elif site=='afim':
            self.navegador.find_element(By.NAME, 'user').send_keys('034.410.422-20')
            self.navegador.find_element(By.NAME, 'password').send_keys('Jaspekde27.24')
            self.navegador.find_element(By.NAME, 'enviar').click()
        elif site=='pmm':
            self.navegador.find_element(By.CSS_SELECTOR, '#email').send_keys('LUAN_PINTO')
            self.navegador.find_element(By.CSS_SELECTOR, '#senha').send_keys('123456')
            self.navegador.find_element(By.CSS_SELECTOR, '#entrar').click()
        
        para(2)

    def __init__(self):
        try:
            servico = Service(ChromeDriverManager().install())
            self.navegador = webdriver.Chrome(service=servico)
        except: self.navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        self._vars = {'ignored_exceptions': (NoSuchElementException,StaleElementReferenceException), 
                    'ultimo dia mes anterior': dt.date.today().replace(day=1) - dt.timedelta(days=1),
                    'path': os.getcwd().split('Desktop')[0] + r'Downloads'}
        
    def trocar_abas(self, termo):
        """
        Alterna entre as abas do navegador e verifica se um determinado termo está presente na URL de qualquer aba.

        Args:
            termo (str): O termo a ser buscado nas URLs das abas.

        Returns:
            int: O índice da aba onde o termo foi encontrado, ou 0 se o termo não foi encontrado em nenhuma aba.

        Prints:
            str: Uma mensagem indicando que o termo não foi encontrado em nenhuma página.
        """

        for i,win in enumerate(self.navegador.window_handles): 
            self.navegador.switch_to.window(win)
            if termo in self.navegador.current_url: 
                print(i, self.navegador.current_url)
                return 0
            
        print(f'O termo "{termo}" não foi encontrado em nenhuma página!')

    def espera_alerta(self):
        """
        Espera até que um alerta seja exibido no navegador.

        Retorna:
            None
        """
        print('Esperando o alerta!')
        # esperar até que o alerta apareça      
        while True: 
            try:
                alerta = WebDriverWait(self.navegador, 10).until(expected_conditions.alert_is_present())
                print('O alerta apareceu')
                break
            except TimeoutException: continue

        # pegar o objeto do alerta
        mensagem = alerta.text

        # esperar até que o alerta seja fechado pelo usuário
        while True:
            try: alerta = self.navegador.switch_to.alert
            except NoAlertPresentException: break
        print('O alerta foi fechado')

        return mensagem

    def last_day(self):
        """
        Retorna o último dia do mês para uma data específica.

        Parâmetros:
            data (datetime): A data para a qual se deseja obter o último dia do mês.

        Retorna:
            int: O último dia do mês para a data especificada.
        """
        first_day = self._vars['primeiro dia do mes']
        while first_day.weekday() >= 5: first_day -= dt.timedelta(days=1)
        return first_day
    
    def esperar_elementos_carregarem(self, tipo_elemento: str, nome_elemento: str, varios_elementos: bool = False, tempo_maximo_espera: int = 30):
        """Espera um ou vários elementos carregarem na página

        Args:
            tipo_elemento (str): tipo do elemento
            nome_elemento (str): nome do elemento
            varios_elementos (bool): procurar mais de um elemento
            tempo_maximo_espera (int): tempo determinado para executar a espera, em segundos. Padrão 30 (0,5 min).
        """    
        tempo_inicial = contar() 
        
        if varios_elementos:
            elementos = WebDriverWait(self.navegador, tempo_maximo_espera, ignored_exceptions=self._vars['ignored_exceptions'])\
                            .until(expected_conditions.presence_of_all_elements_located((tipo_elemento, nome_elemento)))
            tempo_final = contar()
            print(f'>>> Elementos "{nome_elemento}" encontrados em {round(tempo_final - tempo_inicial, 2)}s! (len({len(elementos)}))')
            return elementos
        else:
            elemento = WebDriverWait(self.navegador, tempo_maximo_espera, ignored_exceptions=self._vars['ignored_exceptions'])\
                            .until(expected_conditions.presence_of_element_located((tipo_elemento, nome_elemento)))
            tempo_final = contar()
            if len(elemento.text) > 20: elemento_texto_resumido = elemento.text[:20]
            else: elemento_texto_resumido = elemento.text
                
            print(f'>>> Elemento "{elemento_texto_resumido}" encontrado em {round(tempo_final - tempo_inicial, 2)}s!')
            return elemento

    def entra_AFIM(self, afim):
        """
        Uma função que navega até um link AFIM específico com base no ano (afim) fornecido.

        Parâmetros:
        - afim (int): O ano do link AFIM para navegar.

        Retorna:
        Nenhum
        """
        print(f'\n=============== Executando entra_AFIM {afim}! ===============')
        
        if afim <= 2018:
            self._vars['link'] = f'http://afim2.manaus.am.gov.br/AfimPRD{afim}/'
            self.navegador.get(self._vars['link'])
            self._espera_login('afim')
            para(1)
            self.trocar_abas('AfimPRD')

        #AFIM DE 2019
        if afim == 2019:
            self._vars = 'https://afim1.manaus.am.gov.br/AfimPRD2019/'
            self.navegador.get(self._vars['link'])
            self._espera_login('afim')
            para(2)
            for w in self.navegador.window_handles:
                self.navegador.switch_to.window(w)
                if 'mensagem' in self.navegador.current_url: self.navegador.close()
                elif str(afim) in self.navegador.current_url: pass
                else: self.navegador.close()
                
            self.trocar_abas('AfimPRD')

        if afim >= 2020:
            self._vars['link'] = f'https://afim1.manaus.am.gov.br/AfimPRD{afim}/'
            self.navegador.get(self._vars['link'])
            
            self._espera_login('afim')
            para(1)
            self.trocar_abas('AfimPRD')

        para(2)
        print(f'=============== Finalizando entra_AFIM {afim}! ===============\n')
    
    def exportar_excel(self):
        """
        Exporta os dados para um arquivo Excel.

        Essa função exporta os dados da página atual para um arquivo Excel. Ela executa as seguintes etapas:

        1. Imprime uma mensagem indicando que a função "exportar_excel" está sendo executada.
        2. Chama a função "para" com um valor de parâmetro igual a 1.
        3. Chama a função "trocar_abas", passando a string 'mocatu' como parâmetro.
        4. Chama a função "para" com um valor de parâmetro igual a 2.
        5. Alterna o foco para o primeiro frame da página web.
        6. Aguarda o carregamento do elemento com o ID 'IconImg_CrystalReportViewer_toptoolbar_export'.
        7. Clica no elemento com o ID 'IconImg_CrystalReportViewer_toptoolbar_export'.
        8. Clica no elemento com o ID 'IconImg_Txt_iconMenu_icon_CrystalReportViewer_exportUI_dialog_combo'.
        9. Clica no elemento com o ID 'iconMenu_menu_CrystalReportViewer_exportUI_dialog_combo_span_text_CrystalReportViewer_exportUI_dialog_combo_it_3'.
        10. Clica no elemento com o ID 'theBttnCrystalReportViewer_exportUI_dialog_submitBtn'.
        11. Chama a função "para" com um valor de parâmetro igual a 2.
        12. Imprime uma mensagem indicando que a função "exportar_excel" foi concluída.
        13. Encerra o navegador web.

        Parâmetros:
            self: A instância atual da classe.

        Retorna:
            Nenhum
        """
        print('\n=============== Executando exportar_excel! ===============')

        para(1)
        self.trocar_abas('mocatu')
        para(2)

        self.navegador.switch_to.frame(0)

        para(1)
        self.esperar_elementos_carregarem( By.ID, 'IconImg_CrystalReportViewer_toptoolbar_export')

        para(2)
        self.navegador.find_element(By.ID, 'IconImg_CrystalReportViewer_toptoolbar_export').click()
        self.navegador.find_element(By.ID, 'IconImg_Txt_iconMenu_icon_CrystalReportViewer_exportUI_dialog_combo').click()
        self.navegador.find_element(By.ID, 'iconMenu_menu_CrystalReportViewer_exportUI_dialog_combo_span_text_CrystalReportViewer_exportUI_dialog_combo_it_3').click()
        # self.navegador.find_element(By.ID, 'iconMenu_menu_CrystalReportViewer_exportUI_dialog_combo_paraan_text_CrystalReportViewer_exportUI_dialog_combo_it_8').click()
        self.navegador.find_element(By.ID, 'theBttnCrystalReportViewer_exportUI_dialog_submitBtn').click()

        para(2)

        print('=============== Finalizando exportar_excel! ===============')
        self.navegador.quit

    def entra_ESTOQUE_PMM_entrada_de_ITENS(self):
        """
        Entrada do estoque de ITENS.
        """
        print(f'=============== Inicializando entra_ESTOQUE_PMM_entrada_de_ITENS! ===============\n')

        if os.path.exists(self._vars['path'] + r"\doc.pdf"):
            print("O arquivo já existe.") 

            arquivo = pyf.PdfReader(self._vars['path'] + r"\doc.pdf")

            # percorrendo todas as páginas
            for pagina in arquivo.pages:
                # pega o que está escrito na página
                if ('QUANTIDADE DE ENTRADA DE ITENS DO ESTOQUE' in pagina.extract_text()): return 0

        self.navegador.get("https://estoque.manaus.am.gov.br/src/autenticacao/index.php")

        self._espera_login('pmm')
        self._mensagem('ALERTA!', 'Não mexa no mouse ou teclado.')

        self.navegador.implicitly_wait(120)
        
        self.navegador.get('https://estoque.manaus.am.gov.br/src/relatorios/entrada/')

        # Calcula o último dia do mês anterior
        self._vars['ultimo dia mes anterior'] = dt.date.today().replace(day=1) - dt.timedelta(days=1)

        # Calcula o primeiro dia do mês anterior
        primeiro_dia_mes_anterior = self._vars['ultimo dia mes anterior'].replace(day=1)

        self.navegador.find_element(By.ID, "TX_UNIDADE_ORG").send_keys('UE - SEMINF - OBRAS E INVESTIMENTOS')
        self.navegador.find_element(By.ID, "ITENS").click()
        self.navegador.find_element(By.CSS_SELECTOR, "#TIPO_ITENS option[value='2']").click()
        self.navegador.find_element(By.ID, "DT_INICIAL").send_keys(primeiro_dia_mes_anterior.strftime('%d/%m/%Y'))
        self.navegador.find_element(By.ID, "DT_FINAL").send_keys(self._vars['ultimo dia mes anterior'].strftime('%d/%m/%Y'))

        self.navegador.find_element(By.ID, "gerarRelatorio").click()

        self.esperar_elementos_carregarem(By.TAG_NAME, 'body', tempo_maximo_espera=90)
        self.download_PMM()

        self.navegador.close()
        self.navegador.switch_to.window(self.navegador.window_handles[0])
        self._mensagem('ALERTA!', 'Agora pode movimentar o teclado ou o mouse!')

        print(f'=============== Finalizando entra_ESTOQUE_PMM_entrada_de_ITENS! ===============\n')

    def preenche_NL(self, lancar_baixas): 
        """
        Preenche os campos da página NL com as informações necessárias.

        Args:
            lancar_baixas (DataFrame): O DataFrame contendo os dados a serem preenchidos nos campos.

        Returns:
            None
        """
        self.navegador.get(self._vars['link'] + '/Nl.do')

        para(2)
        self.trocar_abas('Nl.do')

        self.esperar_elementos_carregarem(By.CSS_SELECTOR, '[name="mkdDataEmissao"]').send_keys(self._vars['ultimo dia mes anterior'].strftime('%d/%m/%Y'))
        self.navegador.find_element(By.CSS_SELECTOR, '[name="unidadeGestora"]').send_keys('270101 - Secretaria Municipal de Infraestrutura')
        self.esperar_elementos_carregarem(By.CSS_SELECTOR, '[name="gestao"]').send_keys('00001 - Administração Direta')
        self.esperar_elementos_carregarem(By.CSS_SELECTOR, '[name="txtCredor"]').send_keys('270101-00001')

        print('Começando a interação!')
        self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'body').click()
        self.navegador.switch_to.frame(0)

        for row, linha in enumerate(lancar_baixas.iterrows()):
            linha = linha[1].tolist()
            inscricao = linha[0][-2:]
            conta = linha[0]
            valor = str(linha[1])
            if len(valor.split('.')[1]) != 2: valor += '0'
            valor = valor.split('.')[0] + valor.split('.')[1]
            print(row,':', inscricao, conta, valor)
            if row%7==0 and row!=0:
                self.navegador.switch_to.default_content()
                self.navegador.switch_to.frame(0)
                self.navegador.find_element(By.CSS_SELECTOR, "td:nth-child(4) font").click()
                self.navegador.find_element(By.CSS_SELECTOR, "td:nth-child(4) font").click()

            # Numero do evento
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{0}"]').click()
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{0}"]').send_keys('540456')
            # Numero de inscrição
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{1}"]').click()
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{1}"]').send_keys(inscricao)
            # Numero da classificação(conta)
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{2}"]').click()
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{2}"]').send_keys(conta)
            # Número da Fonte
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{3}"]').click()
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{3}"]').send_keys('15000000')
            # Valor
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{4}"]').click()
            self.navegador.find_element(By.CSS_SELECTOR, f'[id="g_{row}_{4}"]').send_keys(valor)
            
        # Preenche o campo observação
        self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'body').click()
        self.navegador.switch_to.default_content()

        self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'textarea[name="txtObservacao"]').click()
        self.navegador.find_element(By.CSS_SELECTOR, f'textarea[name="txtObservacao"]').send_keys(f'Baixa de material de consumo no mês de {self._vars["ultimo dia mes anterior"].replace(day=1).strftime("%B")} para regularização do saldo contábil.')
        self._mensagem('Conferência da NL', r'Cheque se há divêrgencia nas informações da NL com a planilha \\soturno\CONTABILIDADE\11 - MATERIAL DE CONSUMO\2023\relatorio geral.xlsx')

    def download_PMM(self): 
        """
        Alterna entre as abas do navegador e verifica se um determinado termo está presente na URL de qualquer aba.

        Args:
            termo (str): O termo a ser buscado nas URLs das abas.

        Returns:
            int: O índice da aba onde o termo foi encontrado, ou 0 se o termo não foi encontrado em nenhuma aba.

        Prints:
            str: Uma mensagem indicando que o termo não foi encontrado em nenhuma página.
        """
        para(10)
        for i in range(8): pyautogui.typewrite('\t')
        para(1)
        for i in range(2): 
            para(1)
            pyautogui.typewrite('\n')
