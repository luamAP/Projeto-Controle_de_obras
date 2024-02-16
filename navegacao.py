from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import datetime as dt
from tkinter import Tk, messagebox
# import pyautogui

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
def aguarde_documento_baixar(nome_documento, tempo_espera=60):
    t0 = contar()
    while not os.path.exists(os.path.join(os.path.expanduser("~"+os.sep+"Downloads"), nome_documento)): 
        tf = contar()
        if (tf-t0)>=tempo_espera: break
    else: print('Documento baixado!')


class Navegacao():

    def retry_on_error(max_attempts=3, delay=1.5):
        """
        Decorador que tenta novamente uma função em caso de erro até um número máximo de tentativas.
        
        Args:
            max_attempts (int): O número máximo de tentativas.
            delay (int): O atraso em segundos entre as tentativas.
        
        Retorna:
            função: A função decorada.
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < max_attempts:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"Ocorreu um erro: {e}")
                        print(f"Tentativa {attempts + 1}/{max_attempts}. Tentando novamente após {delay} segundos...")
                        para(delay)
                        attempts += 1
                raise Exception(f"A função {func.__name__} falhou após {max_attempts} tentativas.")
            return wrapper
        return decorator

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
            self.navegador.find_element(By.NAME, 'password').send_keys(self._vars['senha'])
            self.navegador.find_element(By.NAME, 'enviar').click()
        elif site=='pmm':
            self.navegador.find_element(By.CSS_SELECTOR, '#email').send_keys('LUAN_PINTO')
            self.navegador.find_element(By.CSS_SELECTOR, '#senha').send_keys('123456')
            self.navegador.find_element(By.CSS_SELECTOR, '#entrar').click()
        
        para(2)

    def __init__(self, modo_escondido=False):
        # if not modo_escondido: 
        #     janela = Tk()
        #     modo_escondido = messagebox.askokcancel('Headless Mode', 'Deseja ativar o modo headless?')
        #     janela.destroy()
        # else: modo_escondido = True
        try:
            servico = Service(ChromeDriverManager().install())
            if modo_escondido:
                # Configurar o Chrome em modo headless
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                self.navegador = webdriver.Chrome(service=servico, options=chrome_options)
            else: self.navegador = webdriver.Chrome(service=servico)

        except: 
            if modo_escondido:
                # Configurar o Firefox em modo headless
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.add_argument('--headless')

                # Criar uma instância do driver do Firefox com as opções
                self.navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

            else: self.navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        # Cria uma instância de ActionChains
        self.action_chains = ActionChains(self.navegador)

        self._vars = {'ignored_exceptions': (NoSuchElementException,StaleElementReferenceException), 
                    'ultimo dia mes anterior': dt.date.today().replace(day=1) - dt.timedelta(days=1),
                    'path': os.getcwd().split('Desktop')[0] + r'Downloads',
                    'senha': f'Jaspekde27.{dt.date.today().month}',
                    'abas': 0,
                    'lista_obs': []}
        
    # def ():
    def esperar_pagina_carregar(self, timeout=10):
        t0=contar()
        print(f"Esperando a página carregar por {timeout} segundos... ")
        
        def is_page_loading(driver):
            script = "return document.readyState"
            return driver.execute_script(script) != "complete"
        
        try: WebDriverWait(self.navegador, timeout).until(lambda x: not is_page_loading(x))
        except Exception as e: print(f"O tempo limite de {timeout} segundos foi atingido. A página pode não estar completamente carregada.")

        print(f"Pagina carregada em {round(contar()-t0,3)} segundos!")
        
    @retry_on_error()
    def trocar_abas(self, termo=''):
        """
        Alterna entre as abas do navegador e verifica se um determinado termo está presente na URL de qualquer aba.

        Args:
            termo (str): O termo a ser buscado nas URLs das abas. Pode ser também um número que representa o índice da aba.

        Returns:
            int: O índice da aba onde o termo foi encontrado, ou 0 se o termo não foi encontrado em nenhuma aba.

        Prints:
            str: Uma mensagem indicando que o termo não foi encontrado em nenhuma página.
        """
        self.esperar_pagina_carregar()
        self._vars['abas'] = len(self.navegador.window_handles)
        
        if type(termo) is int: 
            aba=termo
            if aba<0: return self.navegador.switch_to.window(self.navegador.window_handles[aba])
        else: aba=''

        for i,win in enumerate(self.navegador.window_handles): 
            self.navegador.switch_to.window(win)
            if (not termo=='') and (termo in self.navegador.current_url): 
                print(i, self.navegador.current_url)
                return self.navegador.switch_to.window(win)
            elif (not aba=='') and (aba==i): 
                print(i, self.navegador.current_url)
                return self.navegador.switch_to.window(win)
            
        print(f'O termo "{termo}" não foi encontrado em nenhuma página!')
        return 0

    def name_credor(self, palavra):
        self.trocar_abas('credor')
        self.navegador.find_element(By.NAME, 'input.entrada_dados').send_keys(palavra)

    @retry_on_error()
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
        while True :
            try: alerta = self.navegador.switch_to.alert
            except: break
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
            print(f'>>> Elementos "{nome_elemento}" encontrados em {round(tempo_final - tempo_inicial, 3)}s! (len({len(elementos)}))')
            return elementos
        else:
            elemento = WebDriverWait(self.navegador, tempo_maximo_espera, ignored_exceptions=self._vars['ignored_exceptions'])\
                            .until(expected_conditions.presence_of_element_located((tipo_elemento, nome_elemento)))
            tempo_final = contar()
            if len(elemento.text) > 20: elemento_texto_resumido = elemento.text[:20]
            else: elemento_texto_resumido = elemento.text
                
            print(f'>>> Elemento "{elemento_texto_resumido}" encontrado em {round(tempo_final - tempo_inicial, 3)}s!')
            return elemento

    @retry_on_error()
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
            self._vars['link'] = f'http://afim3.manaus.am.gov.br/AfimPRD{afim}/'
            self.navegador.get(self._vars['link'])
            self._espera_login('afim')
            self.trocar_abas('AfimPRD')

        #AFIM DE 2019
        if afim >= 2023:
            self._vars['link'] = f'https://afim1.manaus.am.gov.br/AfimPRD{afim}/'
            self.navegador.get(self._vars['link'])
            self._espera_login('afim')
            self.trocar_abas('AfimPRD')

        if afim >= 2020 and afim < 2023:
            self._vars['link'] = f'https://afim2.manaus.am.gov.br/AfimPRD{afim}/'
            self.navegador.get(self._vars['link'])
            
            self._espera_login('afim')
            
            if afim == 2019:
                for w in self.navegador.window_handles:
                    self.navegador.switch_to.window(w)
                    if 'mensagem' in self.navegador.current_url: self.navegador.close()
                    elif str(afim) in self.navegador.current_url: pass
                    else: self.navegador.close()

            self.trocar_abas('AfimPRD')


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

        para(1)
        self.navegador.find_element(By.ID, 'IconImg_CrystalReportViewer_toptoolbar_export').click()
        para(1)
        self.navegador.find_element(By.ID, 'IconImg_Txt_iconMenu_icon_CrystalReportViewer_exportUI_dialog_combo').click()
        para(1)
        self.navegador.find_element(By.ID, 'iconMenu_menu_CrystalReportViewer_exportUI_dialog_combo_span_text_CrystalReportViewer_exportUI_dialog_combo_it_3').click()
        para(1)
        # self.navegador.find_element(By.ID, 'iconMenu_menu_CrystalReportViewer_exportUI_dialog_combo_paraan_text_CrystalReportViewer_exportUI_dialog_combo_it_8').click()
        self.navegador.find_element(By.ID, 'theBttnCrystalReportViewer_exportUI_dialog_submitBtn').click()

        para(2)
        aguarde_documento_baixar('RELEXTRATOEMPENHO.xls')

        print('=============== Finalizando exportar_excel! ===============')
        self.navegador.close()
        self._vars['abas'] = len(self.navegador.window_handles)
        self.trocar_abas(-1)

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
        # for i in range(8): pyautogui.typewrite('\t')
        para(1)
        for i in range(2): 
            para(1)
            # pyautogui.typewrite('\n')

    @retry_on_error()
    def RELSALEMP(self, NE):
        if type(NE) is str and 'NE' in NE: NE = NE.split("NE")[1]
        if self.trocar_abas('Relsalemp.do')==0:
            lisne_link = self._vars['link'] + 'Relsalemp.do'
            self.navegador.get(lisne_link)

        para(2)
        self.trocar_abas('Relsalemp')

        self.navegador.find_element(By.CSS_SELECTOR, 'option[value="270101"]').click()
        self.navegador.find_element(By.CSS_SELECTOR, '[name="numeroNE"]').send_keys(NE)
        self.navegador.find_element(By.CSS_SELECTOR, '#IMGimprimir').click()

        # Espere até que a aba/janela fechada seja considerada obsoleta
        # WebDriverWait(self.navegador, 10).until(expected_conditions.staleness_of(self.navegador.find_element(By.XPATH, "//body")))

        # while os.path.isfile(r"C:\Users\luan.pinto\Downloads\SomeReport.pdf") or os.path.isfile(r"C:\Users\luan.pinto\Downloads\RELEXTRATOEMPENHO.pdf"):
        #     self._mensagem('Apague, renomeie ou mova os arquivos', 'Entre na pasta de Downloads e apague ou renomeie os arquivos "doc.pdf" e "RelBalanceteMensal.xls", para que o programa possa executar sem erros!')

    @retry_on_error()
    def detalhando_ne(self, ne):
        para(1)
        self.action_chains.move_to_element(ne).perform() # Rola para o elemento de destino
        ne.click() # Clica na Nota de Empenho
        para(1.25)

        fechar = self.esperar_elementos_carregarem(By.CSS_SELECTOR, '[ng-click="closeModal_Empenho()"]')
        para(1.25)

        dt_emissao = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtDataEmissao"]').get_attribute('value').rstrip()
        dt_lancamento = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtDataLancamento"]').get_attribute('value').rstrip()
        n_empenho = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strPndNumero"]').get_attribute('value').rstrip()
        credor = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtCredor"]').get_attribute('value').rstrip()
        evento = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtEvento"]').get_attribute('value').rstrip()
        uo = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtUnidadeOrcamentaria"]').get_attribute('value').rstrip()
        fonte_de_recurso = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtFonte"]').get_attribute('value').rstrip()
        natureza_despesa = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtNaturezaDespesa"]').get_attribute('value').rstrip()
        empenho_original = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtNEOriginal"]').get_attribute('value').rstrip()
        processo = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtProcesso"]').get_attribute('value').rstrip()
        valor = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.strTxtValor"]').get_attribute('value').rstrip()
        descricao = self.navegador.find_element(By.CSS_SELECTOR, '[ng-model="notaDeEmpenho.txtDescricao"]').get_attribute('value').rstrip()

        fechar.click() # Fechar a ne aberta 

        linha_tabela = [dt_emissao, dt_lancamento, n_empenho, credor, evento, uo, fonte_de_recurso, natureza_despesa, empenho_original, processo, valor, descricao]
        return linha_tabela

    @retry_on_error()
    def LISNE(self, NE='', favorecido='', detalhar_ne=False):

        print('\n=============== Executando LISNE! ===============')
        self._vars['NEs'] = []
        if 'NE' in NE: NE = NE.split("NE")[1]
        lisne_link = self._vars['link'] + 'Lisne.do'
        self.navegador.get(lisne_link)
        self._vars['linha_lisne'] = []

        self.trocar_abas('Lisne')
        para(2)

        # titulo = ['UG', 'Gestão', 'Data', 'Número', 'Valor', 'Favorecido', 'Evento', 'Fonte', 'Natureza', 'Modalidade', 'Licitação', 'Tipo_Empenho', 'Ipo']

        if favorecido!='': 
            tab,nTab = '-tab1',1
            """# A partir daqui a pagina será executada na aba 
            "Natureza / Favorecido / Modalidade / Licitacao / Tipo" """

            # Seleciona a aba "Natureza / Favorecido / Modalidade / Licitacao / Tipo"
            self.navegador.find_element(By.CSS_SELECTOR, '#nav-profile-tab').click()
            para(1)

            self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#unidade-gestora{tab}').send_keys('270101 - Secretaria Municipal de Infraestrutura')

            self.navegador.find_element(By.CSS_SELECTOR, '#txtCredor').clear()
            self.navegador.find_element(By.CSS_SELECTOR, '#txtCredor').send_keys(favorecido)
            para(0.5)
            # self.navegador.find_element(By.CSS_SELECTOR, 'div.ui-menu-item-wrapper').click()
            self.navegador.find_element(By.CSS_SELECTOR, '#txtCredor').send_keys(Keys.ENTER)
            

            try: self.navegador.find_element(By.CSS_SELECTOR, f'form#needs-validation{tab} button[class*="btnProcurar"]').click()
            except: self.navegador.find_element(By.CSS_SELECTOR, '#IMGprocurar').click()
            para(2)

            self.navegador.find_element(By.CSS_SELECTOR, f'select[name="tableNotasTab{nTab}_length"] option[value="-1"]').click()
            para(1)

            # Seleciona todas as Notas de Empenho
            try:
                if self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#tableNotasTab{nTab} td.dataTables_empty').text == 'Nenhum registro encontrado': return 'Nenhum registro encontrado' 

            except:
                nes_tabela = self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#tableNotasTab{nTab} > tbody > tr td.sorting_1 button', True)

            # # Cria uma matriz onde cada linha contém os dados de uma Nota de Empenho
            # linha_tabela = self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#tableNotasTab{nTab} > tbody > tr td.ng-binding', True)
            # matriz_empenhos = [[item.text for item in linha_tabela[i:i+13]] for i in range(0, len(linha_tabela), 13)]

            # Loop para cada Nota de Empenho encontrada no ano pelo credor
            for ne in nes_tabela: 
                if detalhar_ne: self._vars['linha_lisne'].append(self.detalhando_ne(ne))
                ## NÃO ESTA FUNCIONAL AINDA
                else: self._vars['linha_lisne'].append([i.text for i in self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#tableNotasTab{nTab} > tbody > tr td.ng-binding', True)])
        else: 
            tab,nTab = '',0
            self.navegador.find_element(By.NAME, 'cboUnidadeGestora').send_keys('270101 - Secretaria Municipal de Infraestrutura')
            self.navegador.find_element(By.ID, 'mkdNumeroNE').clear()
            self.navegador.find_element(By.ID, 'mkdNumeroNE').send_keys(NE)
            try: self.navegador.find_element(By.ID, 'btnProcurar').click()
            except: self.navegador.find_element(By.CSS_SELECTOR, '#IMGprocurar').click()

            para(2)
            if detalhar_ne: self._vars['linha_lisne'].append(self.detalhando_ne(self.esperar_elementos_carregarem(By.CSS_SELECTOR, f'#tableNotasTab{nTab} > tbody > tr td.sorting_1 button')))
            else: self._vars['linha_lisne'].append([i.text for i in self.esperar_elementos_carregarem(By.CSS_SELECTOR, '#tableNotasTab0 > tbody > tr td', True)])

        return self._vars['linha_lisne']
        
    def procurar_credor(self, credor_cnpj, credor_nome):
        self.trocar_abas(aba=self._vars['abas'])
        self.navegador.find_element(By.CSS_SELECTOR, '#txtProcura').clear()
        for i,palavra in enumerate(credor_nome):
            self.navegador.find_element(By.CSS_SELECTOR, '#txtProcura').send_keys(palavra)
            if i%5==0: 
                para(1)

                try: 
                    self.navegador.find_element(By.CSS_SELECTOR, f'option[value="{credor_cnpj}"]').click()
                    self.navegador.find_element(By.CSS_SELECTOR, '#btnSelecionar').click()
                    break
                except: pass
  
    @retry_on_error()
    def LISOB(self, credor):
        credor_cnpj = credor.split(' - ')[0]
        print(f'\n=============== Executando LISOB! ({credor_cnpj}) ===============')
        lisne_link = self._vars['link'] + 'Lisob.do'
        self.navegador.get(lisne_link)
        self.trocar_abas('Lisob.do')

        self.navegador.find_element(By.CSS_SELECTOR, '#cboUnidadeGestoraDestino').send_keys('270101 - Secretaria Municipal de Infraestrutura')

        credor = self.navegador.find_element(By.CSS_SELECTOR, '#txtCredor')
        credor.clear()
        credor.send_keys(credor_cnpj)
        credor.send_keys(Keys.ENTER)
        
        para(2)

        checkbox = self.esperar_elementos_carregarem(By.CSS_SELECTOR, '#credorComTributos')
        if not checkbox.is_selected(): checkbox.click()
        try: self.navegador.find_element(By.ID, 'btnProcurar').click()
        except: self.navegador.find_element(By.CSS_SELECTOR, '#IMGprocurar').click()

        print('\n=============== Finalizando LISOB! ===============')

    @retry_on_error()
    def LISOBGrid_v1(self):
        def extrair_informacoes_obs(texto):
            import re
            # Tenta encontrar o padrão no texto fornecido
            correspondencia = {'ug_financeira': re.search(r'(\d+)', texto).group(),
                                'ug_favorecida': re.search(r'UG: (\d+)', texto).group(1),
                                'ob': re.search(r'\d+OB\d+', texto).group(),
                                'valor': re.search(r'[\d+\.]+,\d+', texto).group(),
                                'data': re.search(r'(\d{2}/\d{2}/\d{4})', texto).group()}
            return list(correspondencia.values())

        print('\n=============== Executando LisObGrid! ===============')

        self.trocar_abas('LisObGrid')
        obs = []
        pags = self.navegador.find_elements(By.CSS_SELECTOR, 'a[title]') # Numero de Paginas

        for i in range(len(pags)+1):
            linhas = self.esperar_elementos_carregarem(By.CSS_SELECTOR, 'tr[class^="linha"]',True)
            obs.extend([linha.text for linha in linhas if not 'Total' in linha.text])
            if len(pags)>0: self.navegador.find_element(By.CSS_SELECTOR, 'img[src$="proximo.gif"]').click() # Proxima pagina

        obs = [extrair_informacoes_obs(ob) for ob in obs]
        for ob in obs: ob.append(self._vars['credor'])
        self.navegador.close()
        self.trocar_abas(-1)

        print('\n=============== Finalizando LisObGrid! ===============')
        return obs

    @retry_on_error()
    def LISOBGrid_detalha_ob(self):
        def extrair_NE_controlada(ob):
            import re
            para(1)
            return re.search(r'<br>NE controlada: (\d*NE\d*)<br>', ob).group(1)


        self.trocar_abas('LisObGrid')
        para(1)
        pags = self.navegador.find_elements(By.CSS_SELECTOR, 'a[title]') # Numero de Paginas

        for pag_atual in range(1,len(pags)+2):
            detalhe_ob = [i for i in self.navegador.find_elements(By.CSS_SELECTOR,'tr[class*="linha"] td div[style]') if not 'Total' in i.get_attribute('ondblclick')]

            for ob in detalhe_ob:     
                self.action_chains.double_click(ob).perform()
                para(1)
                self.trocar_abas('SubDetaOB')

                dt_emissao = self.esperar_elementos_carregarem(By.CSS_SELECTOR, '[name="txtDataEmissao"]').get_attribute('value').strip()
                dt_lancamento = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtDataLancamento"]').get_attribute('value').strip()
                nOB = self.navegador.find_element(By.CSS_SELECTOR, '[name="pndNumero"]').get_attribute('value').strip()
                UG_fin = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtUnidadeGestora"]').get_attribute('value').strip()
                UG_fav = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtUnidadeGestora2"]').get_attribute('value').strip()
                credor = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtCredor"]').get_attribute('value').strip()
                processo = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtProcesso"]').get_attribute('value').strip()
                valor = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtValor"]').get_attribute('value').strip()
                finalidade = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtFinalidade"]').get_attribute('value').strip()
                NL_controlada = self.navegador.find_element(By.CSS_SELECTOR, '[name="txtNLProgramacao"]').get_attribute('value').strip()
                
                self.navegador.switch_to.frame(self.navegador.find_element(By.CSS_SELECTOR, 'iframe'))
                NE_controlada = self.navegador.find_elements(By.CSS_SELECTOR, 'td.defaulttdcell')[1].text.strip()

                self._vars['lista_obs'].append([dt_emissao, dt_lancamento, nOB, UG_fin, UG_fav, credor, processo, valor, finalidade, NE_controlada, NL_controlada])

                self.navegador.close()
                self.trocar_abas('LisObGrid')
            
            if not (len(pags)+1)==pag_atual: self.navegador.find_element(By.CSS_SELECTOR, 'img[src$="proximo.gif"]').click() # Proxima pagina
            para(0.5)

        self.navegador.close()
        self.trocar_abas(-1)


    




