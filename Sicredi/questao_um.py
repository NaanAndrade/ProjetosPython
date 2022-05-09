# Questão 3:
# Implementar um gerenciador de limites de cartão de Crédito

# 1. As entradas são: limite e lista de compras;
# 2. A saída deve ser 1 se o limite foi excedido e 0 se o limite não foi;
# 3. O limite é excedido quando a soma das compras é maior que o limite


limite_do_cartao = int(input("Digite o limite do seu cartão: R$ "))

# Criar uma lista de compras?

end = False
while not end:
    valor_da_compra = int(input("Digite o valor de suas compras: R$ "))

    if limite_do_cartao - valor_da_compra >= 0:
        limite_do_cartao -= valor_da_compra
        print(f"Seu limite atual é de R${limite_do_cartao}.")  # 0
    else:
        print("Infelizmente seu limite do cartão foi ultrapassado, esta compra não poderá ser efetuada!")  # 1
        end = True

    continuar = input("Desejar continuar suas compras? [S]im [N]ão: ").upper()

    if continuar == 'N':
        end = True