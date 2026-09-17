def reduzir_estoque(produto,cadastro_produtos,quantidade):
    if produto in cadastro_produtos:
        cadastro_produtos[produto]["quantidade"] -= quantidade
        
