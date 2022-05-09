# Questão 2:
# Calcular o rendimento da poupança de acordo com os seguintes requisitos:

# 1. As entradas são: valor, quantidade de meses, Taxa SELIC e Taxa Referencial
# 2. Se a SELIC estiver abaixo de 8.5, a poupança rende 70% da SELIC + Taxa Referencial (ao mês)
# 3. Se a SELIC estiver acima, a poupança rende 0.5% + Taxa Referencial (ao mês)
# 4. A saída deve ser o resultado do investimento (inicial + rendimento).

valor_investido = int(input("Digite o valor do seu investimento: R$ "))  # valor
qntd_meses = int(input("Digite a quantidade de meses que este valor vai ficar investido: "))  # meses
taxa_selic = float(input("Digite a Taxa SELIC atual: "))
taxa_referencial = float(input("Digite a Taxa Referencial: "))
print("-------------------------------------------------------------------")

if taxa_selic < 8.5:
    rendimento_poupanca = ((taxa_selic * 70) / 100) + taxa_referencial  # por mês
    rendimento_valor_investido = valor_investido + (rendimento_poupanca * qntd_meses)
    print(f"Valor investido: R${valor_investido}")
    print(f"Em {qntd_meses} meses você terá o retorno de: R${rendimento_valor_investido}")
else:
    rendimento = (((taxa_selic * 75) / 100) + taxa_referencial) * qntd_meses
