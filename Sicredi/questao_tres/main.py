# Questão 3:
# Calcular o rendimento da poupança de acordo com os seguintes requisitos:

# 1. As entradas são: valor, quantidade de meses, Taxa SELIC e Taxa Referencial
# 2. Se a SELIC estiver abaixo de 8.5, a poupança rende 70% da SELIC + Taxa Referencial (ao mês)
# 3. Se a SELIC estiver acima, a poupança rende 0.5% + Taxa Referencial (ao mês)
# 4. A saída deve ser o resultado do questao_tres (inicial + rendimento).

# retornar não apenas o resultado, mas retornar de
# forma estruturada o valor inicial,
# resultado final do questao_tres e o resultado e rendimento mês a mês

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
    rendimento_atualizado = valor_investido
    dados_investimento = {
        "ValorInvestido": valor_investido,
        "RendimentoMensal": [],
        "ValorFinal": valor_investido
    }

    for _ in range(qntd_meses):
        rendimento_mes = (rendimento_atualizado * ((taxa_rendimento_mes + taxa_referencial) / 100))
        rendimento_atualizado += rendimento_mes
        dados_investimento["RendimentoMensal"].append(
            {
                "RendimentoMes": rendimento_mes,
                "SaldoMes": rendimento_atualizado
            }
        )

    dados_investimento["ValorFinal"] = rendimento_atualizado

    return dados_investimento


def mostrarExtrato(dados_investimento):
    print("------------------------------------------------------------")
    print("                  EXTRATO DE INVESTIMENTO                   ")
    print("------------------------------------------------------------")
    print(f"              Investimento inicial: R${truncate(dados_investimento['ValorInvestido'])}")

    mes = 1
    for _ in dados_investimento["RendimentoMensal"]:
        print("------------------------------------------------------------")
        print(
            f"Mês ({mes}): "
            f"Valor atualizado: R${truncate(_['SaldoMes'])} "
            f"(Rendimento: R${truncate(_['RendimentoMes'])})"
        )
        mes += 1

    print("------------------------------------------------------------")
    print(f"                 Rendimento final: R${truncate(dados_investimento['ValorFinal'])}")
    print("------------------------------------------------------------")


boasVindas()


def main():
    valor_investido = float(input("Digite o valor do seu investimento: R$ "))  # valor
    qntd_meses = int(input("Meses de investimento: "))  # meses
    taxa_selic = float(input("Digite a Taxa SELIC atual: "))  # selic
    taxa_referencial = float(input("Digite a Taxa Referencial: "))  # taxa referencial

    dados_investimento = calculaRendimento(valor_investido, qntd_meses, taxa_selic, taxa_referencial)
    mostrarExtrato(dados_investimento)


main()

# Assunto do email:
# Pesquisa na internet do calculo: De acordo com o enunciado foi considerado ABAIXO de 8.5 ou seja < 8.5,
# mas na realidade seria <= 8.5

# Fazer dois, um de acordo com o enunciado e um de acordo com o calclo selic

# Estudar Calculo Selic / Operador Ternário / Explicação do código
