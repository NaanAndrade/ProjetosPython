import unicodedata
import sys
import pandas as pd

bolsistas = pd.read_csv("dell.csv")


def bolsista_zero(ano):
    """Retorna o primeiro bolsista do ano X."""
    bolsistas_do_ano = bolsistas.loc[bolsistas['AN_REFERENCIA'] == ano]

    try:
        print(
            f"Nome: {bolsistas_do_ano.iloc[0, 0]} \n"
            f"CPF: {bolsistas_do_ano.iloc[0, 1]} \n"
            f"Entidade de Ensino: {bolsistas_do_ano.iloc[0, 2]} \n"
            f"Valor da Bolsa: {bolsistas_do_ano.iloc[0, 9]} {bolsistas_do_ano.iloc[0, 10]}"
        )
    except:
        print(f"Não existem bolsistas no ano {ano}.")


def codificar_nome(nome):
    """Tira acentuações do nome e codifica ele em César +1."""
    # Variaveis
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    nome_decodificado = []
    nome_codificado = ''
    quanto_pular = 1

    # Tratamento do nome
    # 1. Tirando acentuação
    processamento = unicodedata.normalize("NFD", nome)
    processamento = processamento.encode("ascii", "ignore")
    processamento = processamento.decode("utf-8")

    # 2. Tirando caracteres que não sejam letras, mas permitindo espaços
    for letra in processamento:
        if letra.isalpha() or letra == ' ':
            if letra.isalpha():
                nome_decodificado += letra.upper()
            else:
                nome_decodificado += ' '

    # Codificando o Nome
    # 1. Armazenando a PRIMEIRA e ÚLTIMA letra
    parte_um = [nome_decodificado[0], nome_decodificado[-1]]

    # 2. Inverter o MEIO
    parte_dois = nome_decodificado[1: -1]
    parte_dois.reverse()

    # 3. Organizando as letras de acordo
    parte_tres = [parte_um[0]]
    for _ in parte_dois:
        parte_tres.append(_)
    parte_tres.append(parte_um[-1])

    # 4. Código César
    for letra in nome_decodificado:
        if letra.isalpha():
            posicao = alfabeto.index(letra)
            nova_posicao = posicao + quanto_pular
            nova_letra = alfabeto[nova_posicao]
            nome_codificado += nova_letra
        else:
            nome_codificado += letra

    # Retornando o nome codificado
    return nome_codificado


def pesquisar_bolsista(nome_bolsista, ano):
    """Retorna os dados do aluno X do ano Y."""
    encontrando_nome = bolsistas.loc[bolsistas['NM_BOLSISTA'] == nome_bolsista.upper()]
    separando_por_ano = encontrando_nome.loc[encontrando_nome['AN_REFERENCIA'] == ano]

    print("____________________________________________________________")
    print("                    PESQUISAR BOLSISTA                      ")
    print("____________________________________________________________")

    try:
        print(f"Nome: {codificar_nome(separando_por_ano.iloc[0, 0])}")
        print(f"Ano: {separando_por_ano.iloc[0, 4]}")
        print(f"Entidade de Ensino: {separando_por_ano.iloc[0, 2]}")
        print(f"Valor da Bolsa: {separando_por_ano.iloc[0, 9]} {separando_por_ano.iloc[0, 10]}")
    except:
        print(f"Não encontramos este bolsista no ano de {ano}.")


def media_de_bolsas(ano):
    """Retorna a Média de valores dos pagamentos das bolsas do ano X."""
    bolsistas_do_ano = bolsistas.loc[bolsistas['AN_REFERENCIA'] == ano]
    valores_para_media = 0
    divisao_da_media = 0

    try:
        for indice, linha in bolsistas_do_ano.iterrows():
            valores_para_media += linha['VL_BOLSISTA_PAGAMENTO']
            divisao_da_media += 12

        media = round(valores_para_media / divisao_da_media, 2)

        print(f"R$ {media}")
    except:
        print(f"Não existem bolsistas no ano {ano}.")


def ranking_de_bolsas(ano):
    """Retorna uma lista com os representantes das 3 maiores bolsas e das 3 menores bolsas de determinado ano."""
    bolsistas_do_ano = bolsistas.loc[bolsistas['AN_REFERENCIA'] == ano]
    hierarquia_de_pagamentos = bolsistas_do_ano.sort_values(['VL_BOLSISTA_PAGAMENTO'], ascending=False)

    try:
        print(f"MAIORES BOLSAS: \n"
              f"____________________________________________________________\n"
              f"1. {hierarquia_de_pagamentos.iloc[0, 0]}: R$ {hierarquia_de_pagamentos.iloc[0, 10]}")
        print(f"2. {hierarquia_de_pagamentos.iloc[1, 0]}: R$ {hierarquia_de_pagamentos.iloc[0, 10]}")
        print(f"3. {hierarquia_de_pagamentos.iloc[2, 0]}: R$ {hierarquia_de_pagamentos.iloc[0, 10]}")
        print("____________________________________________________________")
        print(f"MENORES BOLSAS:")
        print(f"1. {hierarquia_de_pagamentos.iloc[-1, 0]}: R$ {hierarquia_de_pagamentos.iloc[-1, 10]}")
        print(f"2. {hierarquia_de_pagamentos.iloc[-2, 0]}: R$ {hierarquia_de_pagamentos.iloc[-2, 10]}")
        print(f"3. {hierarquia_de_pagamentos.iloc[-3, 0]}: R$ {hierarquia_de_pagamentos.iloc[-3, 10]}")
    except:
        print(f"Não existem bolsistas no ano {ano}.")


def finalizar_programa():
    """Chama o método sys.exit()"""
    limpar_tela()
    print("____________________[SISTEMA DESLIGADO]___________________")
    sys.exit()


def continuar():
    """Retorna inicio() ou finalizar_programa() de acordo com a escolha"""
    print("____________________________________________________________")
    resposta = input("Deseja resposta? [S]im ou [N]ão: ").upper()
    if resposta == 'S':
        inicio()
        print("____________________________________________________________")
    if resposta == 'N':
        finalizar_programa()
    while not resposta == 'S' or resposta == 'N':
        resposta = input("Deseja continuar? [S]im ou [N]ão: ").upper()
        if resposta == 'S':
            inicio()
            print("____________________________________________________________")
        if resposta == 'N':
            finalizar_programa()


def limpar_tela():
    """Printa diversas vezes para tirar o conteúdo do console"""
    print(35 * "\n")


def inicio():
    """Inicia o programa"""
    limpar_tela()

    print("____________________________________________________________")
    print("                          SISTEMA                           ")
    print("____________________________________________________________")

    ano = input("DIGITE O ANO: ")
    if not ano.isnumeric():
        while not ano.isnumeric():
            ano = input("Digite um ano válido: ")

    print("____________________________________________________________")
    print("                 SISTEMA DE BOLSAS E ALUNOS                 ")
    print("____________________________________________________________")
    print("[1]. Bolsista Zero.")
    print("[2]. Pesquisar Bolsista.")
    print("[3]. Media de Bolsas.")
    print("[4]. Ranking de Bolsas.")
    print("[5]. Finalizar Programa.")
    print("____________________________________________________________")
    opcao = input("DIGITE A FUNÇÃO: ")
    limpar_tela()

    if opcao == '1':
        print("____________________________________________________________")
        print(f"                PRIMEIRO BOLSISTA DE {ano}                 ")
        print("____________________________________________________________")
        print()

        bolsista_zero(int(ano))
        continuar()

    if opcao == '2':
        print("____________________________________________________________")
        print("                    PESQUISAR BOLSISTA                      ")
        print("____________________________________________________________")
        nome = input("Digite o nome: ")
        limpar_tela()

        pesquisar_bolsista(nome, int(ano))
        continuar()

    if opcao == '3':
        print("____________________________________________________________")
        print(f"             MÉDIA DE BOLSAS DO ANO DE {ano}               ")
        print("____________________________________________________________")
        media_de_bolsas(int(ano))
        continuar()

    if opcao == '4':
        print("____________________________________________________________")
        print(f"                    RANKING DE BOLSAS                      ")
        print("____________________________________________________________")
        ranking_de_bolsas(int(ano))
        continuar()

    if opcao == '5':
        finalizar_programa()
        continuar()

    else:
        inicio()  # Programa em funcionamento


inicio()
