from data_base import lista_de_produtos


def boasVindas():
    print("Bem vindo à Loja!")
    print()

def limparTela():
    print(30 * "\n")


def mostrarCarrinho(carrinho, total_carrinho):
    limparTela()
    print("----------------------------------")
    print("             CARRINHO             ")
    print("----------------------------------")
    for _ in carrinho:
        print(f'{_["Produto"]}: R${_["Preço"]}')
    print()
    print(f"Valor total: R${total_carrinho}")
    print("----------------------------------")


def addItem(produto_escolhido, carrinho):
    carrinho.append(
        {
            "Produto": lista_de_produtos.loc[int(produto_escolhido), "Produto"],
            "Preço": lista_de_produtos.loc[int(produto_escolhido), "R$"],
        }
    )


def calcularCarrinho(carrinho):
    soma_total_carrinho = 0

    for _ in carrinho:
        soma_total_carrinho += _["Preço"]

    return soma_total_carrinho


def mostrarMenu():
    limparTela()
    print("----------------------------------")
    print("              MENU                ")
    print("----------------------------------")
    print("[1] Adicionar Item.")
    print("[2] Ver Carrinho.")
    print("[3] Finalizar Compra.")
    print("[0] Sair.")
    print()
    print("----------------------------------")


def mostrarListaDeProdutos(limite_do_cartao, total_carrinho):
    limparTela()
    print("----------------------------------")
    print("             PRODUTOS             ")
    print("----------------------------------")
    print(f"Limite do Cartão: R${limite_do_cartao}")
    print(f"Compras feitas: R${total_carrinho}")
    print()
    print(lista_de_produtos)
    print()
    print("----------------------------------")

def mostrarCompraFinalizada(limite_do_cartao, carrinho):
    resultado_compra = finalizarCompra(limite_do_cartao, carrinho)
    total_carrinho = calcularCarrinho(carrinho)

    limparTela()

    print("----------------------------------")
    print("         EXTRATO DE COMPRA        ")
    print("----------------------------------")
    for _ in carrinho:
        print(f'{_["Produto"]}: R${_["Preço"]}')
    print("----------------------------------")
    print(f"Limite do cartão: R${limite_do_cartao}")
    print(f"Valor total da compra: R${total_carrinho}")
    print("----------------------------------")

    if resultado_compra == 1:
        print("Compra negada, limite excedido!")
    else:
        print("Compra efetuada com sucesso!")
    print("----------------------------------")


def finalizarCompra(limite_do_cartao, carrinho):
    valor_total_carrinho = calcularCarrinho(carrinho)
    return 1 if valor_total_carrinho > limite_do_cartao else 0  # Operador ternário # Retornando 1 e 0


# def testeFinalizarCompra():
#     resultado_compra = finalizarCompra(100, [{"Produto": "Banana", "Preço": 200}])
#     if resultado_compra == 1: print("Teste passou!")
#     else: print("Teste reprovou!")
#
# def testeFinalizarCompraLimiteAprovado():
#     resultado_compra = finalizarCompra(100, [{"Produto": "Banana", "Preço": 100}])
#     if resultado_compra == 0: print("Teste passou!")
#     else: print("Teste reprovou!")

boasVindas()

def main():
    limite_do_cartao = float(input("Digite o limite do cartão: R$ "))
    carrinho = []

    mostrarListaDeProdutos(limite_do_cartao, 0)

    produto_escolhido = input("Digite o número do produto: ")

    addItem(produto_escolhido, carrinho)

    sair = False

    while not sair:

        mostrarMenu()

        opcao_menu = input("Digite a opção desejada: ")

        if opcao_menu == '1':
            total_carrinho = calcularCarrinho(carrinho)
            mostrarListaDeProdutos(limite_do_cartao, total_carrinho)

            produto_escolhido = input("Digite o número do produto: ")

            addItem(produto_escolhido, carrinho)

        elif opcao_menu == '2':
            total_carrinho = calcularCarrinho(carrinho)
            mostrarCarrinho(carrinho, total_carrinho)

            input("Aperte enter para continuar: ")

        elif opcao_menu == '3':
            mostrarCompraFinalizada(limite_do_cartao, carrinho)

            input("Aperte enter para finalizar: ")
            sair = True

        elif opcao_menu == '0':
            sair = True

        else:
            print("Opção inválida!")


main()
