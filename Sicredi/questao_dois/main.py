# Questão 2:
# Calcular o rendimento da poupança de acordo com os seguintes requisitos:

# 1. As entradas são: valor, quantidade de meses, Taxa SELIC e Taxa Referencial
# 2. Se a SELIC estiver abaixo de 8.5, a poupança rende 70% da SELIC + Taxa Referencial (ao mês)
# 3. Se a SELIC estiver acima, a poupança rende 0.5% + Taxa Referencial (ao mês)
# 4. A saída deve ser o resultado do investimento (inicial + rendimento).

import re


def truncate(num):
    return re.sub(r'^(\d+\.\d{,2})\d*$', r'\1', str(num))


def boasVindas():
    print("------------------------------------------------------------")
    print("           Bem vindo ao Programa de Investimento!           ")
    print("------------------------------------------------------------")


def limparTela():
    print(30 * "\n")


def calculaRendimento(valor_investido, qntd_meses, taxa_selic, taxa_referencial):
    taxa_rendimento_mes = (((taxa_selic * 70) / 100) / 12) if taxa_selic <= 8.5 else 0.5  # Operador ternário
    rendimento_valor_investido = valor_investido

    for _ in range(qntd_meses):
        rendimento_mes = (rendimento_valor_investido * ((taxa_rendimento_mes + taxa_referencial) / 100))
        rendimento_valor_investido += rendimento_mes

    return rendimento_valor_investido


def finalizarInvestimento(valor_final, valor_investido):
    print("------------------------------------------------------------")
    print("                  EXTRATO DE INVESTIMENTO                   ")
    print("------------------------------------------------------------")
    print(f"            Investimento inicial: R${truncate(valor_investido)}")
    print(f"              Rendimento final: R${truncate(valor_final)}")
    print("------------------------------------------------------------")


boasVindas()


def main():
    valor_investido = float(input("Digite o valor do seu investimento: R$ "))  # valor
    qntd_meses = int(input("Meses de investimento: "))  # meses
    taxa_selic = float(input("Digite a Taxa SELIC atual: "))  # selic
    taxa_referencial = float(input("Digite a Taxa Referencial: "))  # taxa referencial

    rendimento_valor_investido = calculaRendimento(valor_investido, qntd_meses, taxa_selic, taxa_referencial)

    finalizarInvestimento(rendimento_valor_investido, valor_investido)


main()

# Assunto do email:
# Pesquisa na internet do calculo: De acordo com o enunciado foi considerado ABAIXO de 8.5 ou seja < 8.5,
# mas na realidade seria <= 8.5

# Fazer dois, um de acordo com o enunciado e um de acordo com o calculo selic
