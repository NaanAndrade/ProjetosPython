import pandas as pd

produto_0 = pd.Series({'Nome': 'Chinelo', 'Preço': 14.90})
produto_1 = pd.Series({'Nome': 'Sapato', 'Preço': 70.55})
produto_2 = pd.Series({'Nome': 'Camisa Social', 'Preço': 65.99})
produto_3 = pd.Series({'Nome': 'Camisa Polo', 'Preço': 85.25})
produto_4 = pd.Series({'Nome': 'Calça Sarja', 'Preço': 120.90})
produto_5 = pd.Series({'Nome': 'Calça Jeans', 'Preço': 89.99})

lista_de_produtos = pd.DataFrame([produto_0, produto_1, produto_2, produto_3, produto_4, produto_5])
lista_de_produtos.columns = "Produto", "R$"
