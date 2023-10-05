from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table, TableStyle, Frame, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pandas as pd
from datetime import datetime
import os
import shutil

## CODIGO que cancela as Warnings do pandas
import warnings
from pandas.errors import SettingWithCopyWarning
warnings.filterwarnings("ignore", category=SettingWithCopyWarning)


# Função para criar uma tabela a partir do DataFrame
def create_table_from_dataframe(dataframe):
    """
	Cria uma tabela a partir de um DataFrame.

	Parâmetros:
		dataframe (pandas.DataFrame): O DataFrame a ser convertido em tabela.

	Retorno:
		list: Uma lista contendo os dados da tabela.
	"""

     # # Verificar se coluna1 está vazia e obter valores de coluna2
    valores_coluna1 = []
    valores_coluna2 = []
    for index, row in dataframe.iterrows():
        if pd.isna(row['VALOR ANULADO (R$)']) or row['VALOR ANULADO (R$)'] == '':
            valores_coluna2.append('EMPENHO')
            valores_coluna1.append(row['VALOR EMPENHADO (R$)'])
        else:
            valores_coluna2.append(row['VALOR TOTAL (R$)'])  # Se coluna1 não estiver vazia, insira None
            valores_coluna1.append(row['VALOR ANULADO (R$)']*-1)

    # Adicionar a lista de valores de coluna2 como uma nova coluna no DataFrame
    dataframe['TIPO'] = valores_coluna2
    dataframe['VALOR'] = valores_coluna1
    dataframe = dataframe[['TIPO', 'EMPENHO', 'UNIDADE ORÇAMENTARIA', 'PROGRAMA DE TRABALHO', 'FONTE DE RECURSO', 'NATUREZA DESPESA', 'CONTA CONTÁBIL', 'VALOR']]
    dataframe = dataframe.fillna('')

    table_data = dataframe.values.tolist()
    for l,linha in enumerate(table_data): 
        for c,coluna in enumerate(linha): 
            # if coluna=='nan' or coluna==None or coluna=='': table_data[l][c] = ''
            if type(coluna)==str and ' - 'in coluna: 
                table_data[l][c] = coluna.split(' - ')[0]
            if type(coluna)==float:
                # Formate o número para o formato desejado
                table_data[l][c] = '{:,.2f}'.format(coluna).replace(',', '_').replace('.', ',').replace('_', '.')
    
    # for i in table_data: 
    table_data.insert(0, ['TIPO', 'EMPENHO', 'U.O.',
       'PT', 'FONTE', 'NATUREZA', 'C. CONTÁBIL', 'VALOR'])  # Cabeçalho da tabela
    # table_data.extend(dataframe.values.tolist())  # Dados do DataFrame
    return table_data

def nova_pagina(c:canvas.Canvas, y, atualiza=0):
    largura, altura=landscape(A4)
    y -= atualiza
    if y < 30: 
        c.showPage()
        frame=Frame(x1=15,y1=15,width=largura-30,height=altura-30,showBoundary=1)
        frame.addFromList([],c)
        return cabecalho(c,altura,largura) - atualiza
    else: return y


def centralizar_texto(pdf: canvas.Canvas, y_titulo, titulo, fontName, fontSize, espacamento=20):         
    # Calcular a posição X para centralizar o título
    largura, altura = landscape(A4)
    x_titulo = (largura) / 2

    # Configurar o título do relatório
    pdf.setFont(fontName, fontSize)

    # Desenhar o título centralizado
    pdf.drawCentredString(x_titulo, y_titulo, titulo)

    altura_pagina = y_titulo - espacamento  # Iniciar logo abaixo do título
    return altura_pagina

def converter_proporcao(largura_atual, altura_atual, nova_largura=None, nova_altura=None):
    '''
        Converter as dimensões de uma imagem
        
        return: (nova_largura, nova_altura)
    '''
    if nova_largura is not None:
        proporcao = nova_largura / largura_atual
        nova_altura = int(altura_atual * proporcao)
    elif nova_altura is not None:
        proporcao = nova_altura / altura_atual
        nova_largura = int(largura_atual * proporcao)

    return (nova_largura, nova_altura)

def definir_linhas(pdf,row,column):
    largura, altura = landscape(A4)
    # Height (Largura) da linha
    pdf.drawString(x=column/2, y=row, text=str(int(row)))
    pdf.line(x1=0, y1=row, x2=largura, y2=row)
    # Width (Altura) da linha
    pdf.drawString(x=column, y=row/2, text=str(int(column)))
    pdf.line(x1=column, y1=0, x2=column, y2=altura)

def inserir_imagem(pdf:canvas.Canvas,nome_imagem: str, x: int, y: int, largura=None, altura=None, centered='XY', showBoundary=0):
    '''
        Inserir uma imagem
        
        return: (nova_largura, nova_altura)
    '''
    path=r'C:\Users\luan.pinto\Desktop\Códigos\Projeto - Controle de obras\IMAGE'+'\\'+nome_imagem
    image = Image(path,0,0)
    altura_imagem, largura_imagem = image.imageHeight, image.imageWidth

    proporcao = converter_proporcao(image.imageWidth, image.imageHeight, largura, altura)
    largura_imagem, altura_imagem = proporcao

    if centered == 'XY': y = y-altura_imagem
    if centered == 'CENTER':
        x = (x-largura_imagem)/2
        y = y-altura_imagem+(altura_imagem/2)

    pdf.drawImage(image=path, x=x, y=y, width=largura_imagem, height=altura_imagem, preserveAspectRatio=True, mask='auto', showBoundary=showBoundary)

    return proporcao

def cabecalho(pdf: canvas.Canvas, altura_pag, largura_pag):
    margens = 15 # Definindo as margens
    # Margens do relatorio
    frame0=Frame(margens,margens,largura_pag-margens*2,altura_pag-margens*2, showBoundary=1)
    frame0.addFromList([], pdf)
    
    # Imagem Pref, 1 parte do cabecalho
    cabecalho1 = inserir_imagem(pdf,'cabeçalho esq.png', margens+5, altura_pag - (margens+5), 180)

    # Calculo para alinhar à Imagem Pref, 1* parte do cabecalho
    metade_cabecalho1 = altura_pag - (margens+5) - cabecalho1[1] + cabecalho1[1]/2
   
    # Imagem SEMINF, 2 parte do cabecalho
    inserir_imagem(pdf,'logo-secretaria-seminf-header.png', largura_pag, metade_cabecalho1, 120,centered='CENTER')

    # Criar um estilo personalizado com a fonte desejada
    estilo_personalizado = ParagraphStyle(
        "estilo_personalizado",
        parent=getSampleStyleSheet()["Heading4"],  # Copie as configurações de estilo padrão
        fontName="Courier-Bold",  # Substitua pelo nome da fonte desejada
        fontSize=12
    )

    # Endereço, 3 parte do cabecalho
    p = Paragraph('Rua: Gabriel Gonçalves nº 351 – Aleixo - CEP 69060–010\nTel.: 3642-3064 - Manaus-AM\nwww.manaus.am.gov.br', estilo_personalizado)
    p.wrapOn(pdf, 200, 48)
    p.drawOn(pdf, x=largura_pag-(margens+5)-p.width, y=metade_cabecalho1-p.height+(p.height/2))

    altura_pag = altura_pag - (margens + 5) - cabecalho1[1]

    return centralizar_texto(pdf, altura_pag-14-5, "INVENTÁRIO DE BENS IMÓVEIS", 'Helvetica-Bold', 14, 15)

def rodape(pdf:canvas.Canvas):
        # Defina o estilo do texto do rodapé
        estilo_rodape = ParagraphStyle(
            'rodape',
            parent=getSampleStyleSheet()['Normal'],
            fontSize=10,
            alignment=1
        )

        # Obtenha a data atual
        data_atual = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')

        # Obtenha o número da página atual
        numero_pagina = pdf.getPageNumber()

        # Defina o texto do rodapé
        texto_rodape = f'{data_atual}  |  Página {numero_pagina}'

        # Crie um objeto Paragraph com o texto do rodapé e o estilo definido
        paragrafo_rodape = Paragraph(texto_rodape, estilo_rodape)

        # Desenhe o parágrafo do rodapé no pdf
        alt = paragrafo_rodape.wrap(landscape(A4)[0], 0)[1]
        paragrafo_rodape.drawOn(pdf, 0, 15+2)

def caminho(file_name="file.pdf", dir=None):
    print(dir, type(dir))
    # Obtenha o diretório de downloads do sistema
    if dir==None: dir = os.path.expanduser('~' + os.sep + 'Downloads')
    else: dir = os.path.normpath(dir)

    # Crie o caminho completo para o destino (pasta de downloads + nome do arquivo)
    return os.path.join(dir, file_name)

    # Copie ou mova o arquivo para a pasta de downloads
    # Use shutil.copy() para copiar ou shutil.move() para mover
    shutil.copy(caminho_arquivo_origem, caminho_destino)

    print(f'Arquivo salvo em: {caminho_destino}')


def gerar(path):
    # Lê o DataFrame do arquivo Excel
    df = pd.read_excel(r'C:\Users\luan.pinto\Desktop\Códigos\Projeto - Controle de obras\ARQUIVOS\obras_2021.xlsx')

    # Cria um arquivo PDF
    pdf_file = caminho("relatorio_de_obras.pdf", path)
    c = canvas.Canvas(pdf_file, pagesize=landscape(A4))
    largura, altura = landscape(A4)
    # largura x altura
    # 595.276 x 841.89

    # Estilos para parágrafos
    style_normal = getSampleStyleSheet()['Normal']


    frame=Frame(x1=15,y1=15,width=largura-30,height=altura-30,showBoundary=1)
    frame.addFromList([],c)

    x, y = int(largura/2), cabecalho(c,altura,largura)


    # Lista de contratos processados não repetidos
    contratos_processados = set()
    for n_contrato in df["CONTRATO N°"]:
        if n_contrato not in contratos_processados:
            corte_df = df[df['CONTRATO N°'] == n_contrato]
            t_corte_df = corte_df[['VALOR EMPENHADO (R$)', 'VALOR ANULADO (R$)', 'VALOR TOTAL (R$)', 'EMPENHO', 'UNIDADE ORÇAMENTARIA', 'PROGRAMA DE TRABALHO', 'FONTE DE RECURSO', 'NATUREZA DESPESA', 'CONTA CONTÁBIL']]


            # Cria um parágrafo com informações
            paragraph1 = Paragraph(f"<b>Objeto:</b> {corte_df['OBJETO'].values[0]}", style_normal)
            paragraph1_largura, paragraph1_altura = paragraph1.wrapOn(c, 700, 50)  # Define o tamanho do parágrafo
            y = nova_pagina(c,y,paragraph1_altura+20)
            paragraph1.drawOn(c, x-paragraph1_largura/2, y)


            vlr_contrato = corte_df['VALOR DO CONTRATO (R$)'].values[0]

            # Cria uma tabela com informações para o paragrafo
            data = [[Paragraph(f"<b>N° do Contrato:</b> {corte_df['CONTRATO N°'].values[0]}"), Paragraph(f"<b>Situação da Obra:</b> {corte_df['SITUAÇÃO DA OBRA'].values[0]}"), Paragraph(f"<b>Vlr. do Contrato:</b> {'{:,.2f}'.format(vlr_contrato).replace(',', '_').replace('.', ',').replace('_', '.')}")]]
            paragraph2 = Table(data, colWidths=[((700)/3)])
            paragraph2_largura, paragraph2_altura = paragraph2.wrapOn(c, 700, 400)
            y = nova_pagina(c,y,paragraph2_altura)
            paragraph2.drawOn(c, x-paragraph2_largura/2, y)  # Ajuste o valor de Y conforme necessário
            

            # Cria uma tabela com informações
            table_data = create_table_from_dataframe(t_corte_df)
            table = Table(table_data, colWidths=[120, 90, 50, 120, 70, 70, 90], rowHeights=22.5)
            style = TableStyle([
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Cor do texto do cabeçalho
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento no centro
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alinhamento vertical no meio das células
                ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),  # Alinhe à direita
                ('ALIGN', (0,0), (0,-1), 'LEFT'),  # Alinhe à direita
                ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),  # Linha inferior do cabeçalho
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),  # Linha superior da última linha
                ('LINEBELOW', (0, -1), (-1, -1), 2, colors.black),  # Linha superior da última linha
            ])
            for i in range(1, len(table_data), 2): style.add('BACKGROUND', (0, i), (-1, i), colors.lightgrey)
            table.setStyle(style)
            # Define a posição da tabela e desenha-a no canvas
            table_largura, table_altura = table.wrapOn(c, 700, 400)
            y = nova_pagina(c,y,table_altura+5)
            table.drawOn(c, x-table_largura/2, y)  # Ajuste o valor de Y conforme necessário
            

            # Soma dos empenhos 
            for v in table_data:
                if ',' in v[-1]: vlr_contrato -= int(v[-1].replace('.','').replace(',',''))/100

            
            # Estilo de paragrafo
            styles = getSampleStyleSheet()["Normal"]
            styles.alignment = 2

            # Cria uma tabela com informações para o paragrafo
            data1 = [[Paragraph(f"<b>Depreciação :</b> {'nan'}"),  Paragraph(f"<b>Saldo do Contrato:</b> {'{:,.2f}'.format(vlr_contrato).replace(',', '_').replace('.', ',').replace('_', '.')}", styles)]]
            paragraph3_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), (0.9,0.9,0.9)),  # Cor de fundo das células de dados
                ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),  # Linha inferior do cabeçalho
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),  # Linha superior da última linha
            ])
            paragraph3 = Table(data1, colWidths=[((700)/2)], style=paragraph3_style)
            paragraph3_largura, paragraph3_altura = paragraph3.wrapOn(c, 700, 400)
            y = nova_pagina(c,y,paragraph3_altura)
            paragraph3.drawOn(c, x-paragraph3_largura/2, y)  # Ajuste o valor de Y conforme necessário

            rodape(c)

            contratos_processados.add(n_contrato)


    # Fecha o arquivo PDF
    c.save()
    return f'O arquivo relatorio_de_obras.pdf foi criado com sucesso!'
