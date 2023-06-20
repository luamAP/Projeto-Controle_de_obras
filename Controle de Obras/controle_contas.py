from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep as para
from time import time as contar
import datetime as dt

import pandas as pd

# from openpyxl import load_workbook, Workbook

class Navegacao():
    def __init__(self):
        # options=webdriver.ChromeOptions()
        # if input('Deseja esconder o navegador? y/n\n')=='y': 
        #     options.add_argument("--headless")
        #     self.navegador = webdriver.Chrome(chrome_options=options)
        # else: 
        self.navegador = webdriver.Chrome()
        self.vars = {'conta_contabil': [],
                    'ignored_exceptions': (NoSuchElementException,StaleElementReferenceException), 
                    'senha': f'Jaspekde27.{dt.date.today().month*3}'}
        self.pl = {}

    def esperar_elemento(self, param1, param2, elementos=False, tempo_parar=30):
        """Espera um elemento carregar na página

        Args:
            param1 (): tipo do elemento
            param2 (str): nome do elemento
            elementos(bool): procurar mais de um elemento
            tempo0 (int, optional): tempo determinado para executar a espera. Padrão 30 (0,5 min).
        """    
        tempo0 = contar() 
        
        if elementos:
            try:
                elemento =self.navegador.find_elements(param1, param2)
                while ((tempo-tempo0)>=tempo_parar) and (len(elemento)==0):
                    para(1)
                    tempo = contar() 
                else: print(f'Tempo excedido!')

            except:
                elemento = WebDriverWait(self.navegador, tempo_parar,ignored_exceptions=self.vars['ignored_exceptions'])\
                            .until(expected_conditions.presence_of_all_elements_located((param1, param2)))
                tempo = contar()

            finally:
                try: print(f'>>> Elementos "{param2}" encontrados em {round(tempo-tempo0,2)}s! (len({len(elemento)}))')
                except: print(f'>>> Elementos "{param2}" encontrados! (len({len(elemento)}))') 
                return elemento
        else:
            try:
                elemento =self.navegador.find_elements(param1, param2)
                while ((tempo-tempo0)>=tempo_parar) and (len(elemento)==0):
                    para(1)
                    tempo = contar() 
                else: print(f'Tempo excedido!')
                    
            except:
                elemento = WebDriverWait(self.navegador, tempo_parar, ignored_exceptions=self.vars['ignored_exceptions'])\
                                .until(expected_conditions.presence_of_element_located((param1, param2)))
                tempo = contar()
            
            finally:
                if len(elemento.text) > 20: elemento_print_text = elemento.text[:20]
                try: print(f'>>> Elemento "{elemento_print_text}" encontrado em {round(tempo-tempo0,2)}s!')
                except: print(f'>>> Elemento "{elemento}" encontrado em {round(tempo-tempo0,2)}s!')
                return elemento

    ### Esperar uma página carregar -> *_esperar_aba(param)_*
    def navegar_aba(self):
        print('Esperando aba/página abrir!')
        paginas = len(self.navegador.window_handles)
        while paginas <= len(self.navegador.window_handles): para(1)
        para(1)
        
        print('Página carregada!')

    def entra_AFIM(self, afim):
        """Abre o AFIM e direciona para a função LISNE

        Args:
            afim (_type_): Ano no qual o FIM irá abrir
        """
        print(f'\n=============== Executando entra_AFIM {afim}! ===============')
        
        if afim in ['2014','2015','2016','2017','2018']:
            #AFIM DE 2018
            if afim=='2018': self.navegador.get('http://afim2.manaus.am.gov.br/AfimPRD2018/')
            #AFIM DE 2017
            elif afim=='2017': self.navegador.get('http://afim2.manaus.am.gov.br/AfimPRD2017/')
            #AFIM DE 2016
            elif afim=='2016': self.navegador.get('http://afim2.manaus.am.gov.br/AfimPRD2016/')
            #AFIM DE 2015
            elif afim=='2015': self.navegador.get('http://afim2.manaus.am.gov.br/AfimPRD2015/')
            #AFIM DE 2014
            elif afim=='2014': self.navegador.get('http://afim2.manaus.am.gov.br/AfimPRD2014/')
        
            self.navegador.find_element(By.NAME, 'user').send_keys('03441042220')
            self.navegador.find_element(By.NAME, 'password').send_keys(self.vars['senha'])
            self.navegador.find_element(By.NAME, 'enviar').click()
            para(1)
            self.navegador.switch_to.window(self.navegador.window_handles[-1])
            self.navegador.switch_to.frame(1)

        #AFIM DE 2019
        if afim =='2019':
            self.navegador.get('https://afim1.manaus.am.gov.br/AfimPRD2019/')
            self.navegador.find_element(By.ID, 'user').send_keys('034.410.422-20')
            # Mudar as senhas periodocamente
            self.navegador.find_element(By.ID, 'password').send_keys(self.vars['senha'])
            self.navegador.find_element(By.ID, 'password').send_keys(Keys.ENTER)

            para(2)
            for w in self.navegador.window_handles:
                self.navegador.switch_to.window(w)
                if 'mensagem' in self.navegador.current_url: self.navegador.close()
                elif afim in self.navegador.current_url: pass
                else: self.navegador.close()
                
            self.navegador.switch_to.window(self.navegador.window_handles[-1])
            self.navegador.switch_to.frame(1)

        if afim in ['2020', '2021', '2022']:
            #AFIM DE 2022
            if afim=='2022': self.navegador.get('https://afim1.manaus.am.gov.br/AfimPRD2022/')
            #AFIM DE 2021
            elif afim=='2021': self.navegador.get('https://afim1.manaus.am.gov.br/AfimPRD2021/')
            #AFIM DE 2020
            elif afim=='2020': self.navegador.get('https://afim1.manaus.am.gov.br/AfimPRD2020/')
            
            self.navegador.find_element(By.ID, 'user').send_keys('034.410.422-20')
            # Mudar as senhas periodocamente
            self.navegador.find_element(By.ID, 'password').send_keys(self.vars['senha'])
            self.navegador.find_element(By.ID, 'password').send_keys(Keys.ENTER)
            self.navegador.switch_to.window(self.navegador.window_handles[-1])
            self.navegador.switch_to.frame(0)

        try: self.navegador.find_element(By.CSS_SELECTOR, "body").click()
        except: self.navegador.esperar_elemento(By.CSS_SELECTOR, "body").click()

        print(f'=============== Finalizando entra_AFIM {afim}! ===============\n')
        ## Mudando de janela,
        para(2)

    def NL_detalhada(self, obj_NL):
        """Pesquisa a Nota de Lançamento desejada para retirar as informações

        Args:
            obj_NL (_type_): Objeto Selenium da Nota de Lançamento

        Returns:
            _type_: Tupla com as informações extraidas
        """
        if not 'NL' in obj_NL.text: 
            print(f'\n=============== Impossível executar! Não é uma NL ({obj_NL.text}) ===============')
            return ('', '', '', '', '', '','')
        
        
        print(f'\n=============== Executando a NL ({obj_NL.text}) ===============')
        para(2)
        self.navegador.switch_to.window(self.navegador.window_handles[-1])

        elemento = obj_NL
        ActionChains(self.navegador)\
        .double_click(elemento)\
        .perform()

        para(1)
        self.navegador.switch_to.window(self.navegador.window_handles[-1])
        
        credor_empresa = self.esperar_elemento(By.CSS_SELECTOR, 'tr td input[name="txtCredor"]').get_attribute('value')
        obs = self.esperar_elemento(By.CSS_SELECTOR, 'textarea[name="txtObservacao"]').text
        NE = self.esperar_elemento(By.CSS_SELECTOR, 'input[name="txtNuNe"').get_attribute('value')
        natureza_despesa = self.esperar_elemento(By.CSS_SELECTOR, 'input[name="txtRdNaturezaDespesa"]').get_attribute('value')
        doc = self.esperar_elemento(By.CSS_SELECTOR, 'input[name="txtRdNuDocmento"').get_attribute('value')
        processo = self.esperar_elemento(By.CSS_SELECTOR, 'input[name="txtRdNuProcesso"').get_attribute('value')
        
        self.navegador.close()
        self.navegador.switch_to.window(self.navegador.window_handles[-1])
        
        return (obj_NL.text, credor_empresa, obs, NE, natureza_despesa, doc, processo)

    def RAZAO(self, ano):
        print(f'\n=============== Executando RAZAO {ano}! ===============')
        # Ano anterior a 2020
        if ano >= 2020:
            self.navegador.find_element(By.ID, 'dados').send_keys('RAZAO')
            self.navegador.find_element(By.ID, 'dados').send_keys(Keys.ENTER)
        else:
            self.navegador.find_element(By.CSS_SELECTOR, "body").click()
            self.navegador.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/ul/li[7]').click()
            self.navegador.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/ul/ul[7]/li[1]').click()
            self.navegador.find_element(By.LINK_TEXT, "RAZAO").click()

        para(1)
        self.navegador.switch_to.window(self.navegador.window_handles[-1])
        self.vars['conta_contabil'] = [cbo.get_attribute('Value') for cbo in self.esperar_elemento(By.CSS_SELECTOR, "select[name='cboConta'] option[value^='1232105']", True, 20)]
        para(1)

    def RAZAO_detalhada(self, ano, conta):          
        print(f'\n=============== Executando RAZAO_detalhada em {ano}! ===============')

        ano = str(ano)
        N = self
        # Ano anterior a 2020
        if int(ano) >= 2020:
            print(f'Selecionando a Data Inicial: 01/01/{ano}')
            if self.esperar_elemento(By.ID, 'mkdDataInicio').get_attribute('value')!=f'01/01/{ano}':
                self.esperar_elemento(By.ID, 'mkdDataInicio').click()
                self.esperar_elemento(By.CSS_SELECTOR, "li[data-view='month current']").click()
                self.esperar_elemento(By.CSS_SELECTOR, "ul li[data-view='month']", True, 30)[0].click()
            else: print('Data Inicial já selecionada')
                
            print(f'Selecionando a Data Final: 31/12/{ano}')
            if self.esperar_elemento(By.ID, 'mkdDataFim').get_attribute('value')!=f'31/12/{ano}':
                self.esperar_elemento(By.ID, 'mkdDataFim').click()
                self.esperar_elemento(By.CSS_SELECTOR, "div[class*='datepicker-top-right'] li[data-view='month current']").click()
                self.esperar_elemento(By.CSS_SELECTOR, "div[class*='datepicker-top-right'] ul[data-view='months'] li[data-view='month']", True, 30)[-1]
            else: print('Data Final já selecionada')

        # Ano 2020 em diante
        else:
            print(f'Selecionando a Data Inicial: 01/01/{ano}')
            if self.esperar_elemento(By.ID, 'mkdDataInicio').get_attribute('value')!=f'01/01/{ano}':
                self.esperar_elemento(By.ID, 'img0').click()
                while not (ano in self.navegador.find_elements(By.CSS_SELECTOR, "font[size='1']")[0].text): self.navegador.find_element(By.ID, "toLeft").click()
                if self.navegador.find_element(By.CSS_SELECTOR, "#month [selected]").text!='Janeiro': self.esperar_elemento(By.CSS_SELECTOR, "#month").send_keys('Janeiro')
                self.esperar_elemento(By.CSS_SELECTOR, "td[class='calReg']", True, 30)[0].click()
            else: print('Data Inicial já selecionada')

            print(f'Selecionando a Data Final: 31/12/{ano}')
            if self.esperar_elemento(By.ID, 'mkdDataFim').get_attribute('value')!=f'31/12/{ano}':
                self.esperar_elemento(By.ID, 'img1').click()
                while not (ano in self.navegador.find_elements(By.CSS_SELECTOR, "font[size='1']")[0].text): self.navegador.find_element(By.ID, "toLeft").click()
                if self.navegador.find_element(By.CSS_SELECTOR, "#month [selected]").text!='Dezembro': self.esperar_elemento(By.CSS_SELECTOR, "#month").send_keys('Dezembro')
                self.esperar_elemento(By.CSS_SELECTOR, "td[class='calReg']", True, 30)[-1].click()
            else: print('Data Final já selecionada')

        self.navegador.switch_to.window(self.navegador.window_handles[-1])

        self.esperar_elemento( By.CSS_SELECTOR, 'select[name="cboUnidadeGestora"]').send_keys("270101 - Secretaria Municipal de Infraestrutura")
        self.navegador.find_element(By.CSS_SELECTOR, 'select[name="cboUnidadeGestora"]').click()

        self.esperar_elemento(By.NAME, 'cboConta').send_keys(conta)

        N.esperar_elemento(By.CSS_SELECTOR, 'input[name="..."]').click()
        try:
            alerta = N.navegador.switch_to.alert
            alerta.accept()
            ccs = []
        except:
            ccs = [i.text for i in N.esperar_elemento(By.CSS_SELECTOR, 'select[id="lstHelp"] option', True)]


        for c in ccs:
            N.esperar_elemento(By.CSS_SELECTOR, 'input[name="..."]').click()
            element = N.esperar_elemento(By.CSS_SELECTOR, f'select[id="lstHelp"] option[value="{c}"]')
            ActionChains(N.navegador)\
                .double_click(element)\
                .perform()

            conta_nominada = N.navegador.find_element(By.CSS_SELECTOR, f"select[name='cboConta'] option[value='{conta}']").text + f' ({c})'

            para(1)
            try: N.esperar_elemento(By.ID, 'IMGprocurar').click()
            except: N.esperar_elemento(By.ID, 'btnProcurar').click()

            if '\\' in conta_nominada: conta_nominada = conta_nominada.replace('\\','/')

            lista_no_razao = []
            # Tabela
            for n in N.navegador.find_elements(By.CSS_SELECTOR, '#dbGrid tr'): lista_no_razao.append(n.text.split('  '))

            detalhes_da_NL = [['NOTA DE LANÇAMENTO','CREDOR','OBSERVAÇÃO','NOTA DE EMPENHO',
            'NATUREZA DE DESPESA','N° DO DOCUMENTO', 'PROCESSO']]

            for i in N.navegador.find_elements(By.CSS_SELECTOR, '#dbGrid tr td[onclick="selectCell(this,3)"]'): detalhes_da_NL.append(N.NL_detalhada(i))

            temp = []
            for indice,linha in enumerate(lista_no_razao):
                print(f'{indice}: {linha} + {detalhes_da_NL[indice-1]}') 
                linha.extend(detalhes_da_NL[indice])
                temp.append(linha)
                self.pl[conta_nominada] = lista_no_razao

            # pl.save(f'123210500\\123210500-BENS DE USO COMUM DO POVO - {ano}.xlsx')
            
            self.pl[conta_nominada][1][0] = f'01/01/{ano}'
            self.pl[conta_nominada][1][6] = 'Saldo Anterior'
            self.pl[conta_nominada][1][5] = ''
            self.pl[conta_nominada][-1][0] = f'31/12/{ano}'
            self.pl[conta_nominada][-1][6] = 'Saldo Atual'
            self.pl[conta_nominada][-1][5] = ''

            cabecalho = self.pl[conta_nominada][0]
            self.pl[conta_nominada] = pd.DataFrame(self.pl[conta_nominada][1:], columns=cabecalho)
            # self.pl[conta_nominada].columns = cabecalho

        print('=============== Finalizando RAZAO! ===============')
        # return f'123210500\\123210500-BENS DE USO COMUM DO POVO - {ano}.xlsx'
        
    def contas_unidas(self, ano):
        for pl in self.pl:
            self.pl[pl].insert(0, "Conta Contábil", [pl for i in range(len(self.pl[pl]))],True)
            display(self.pl[pl][:1])
            
        result = pd.concat([self.pl[pl] for pl in self.pl])
        path = f"123210500\\123210500-BENS DE USO COMUM DO POVO - {ano}.xlsx"

        print(f'Salvando as contas em uma planilha excel em "{path}"')
        result.to_excel(path, index=False)


for ano in range(2019, 2023):
    N = Navegacao()
    N.entra_AFIM(str(ano))
    N.RAZAO(ano)
    for conta in N.vars['conta_contabil']: N.RAZAO_detalhada(ano, conta)
    N.navegador.close()
    N.contas_unidas(ano)

