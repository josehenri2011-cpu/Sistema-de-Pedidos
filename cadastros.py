import persistencia
import validaçoes


def cliente_cadastro(Cadastro_Clientes,cadastro_produtos):
    nome=validaçoes.cliente(Cadastro_Clientes)
    produto=validaçoes.ler_produto(cadastro_produtos)
    quantidade=validaçoes.ler_quantidade()
    
    registros={
        "produto": produto,
        "quantidade": quantidade

    }
    registros[nome]=registros
    persistencia.salvar_json(cadastro_produtos,Cadastro_Clientes)



def produto_cadastro(cadastro_produtos,Cadastro_Clientes):
    print("Cadastro de Produtos")
    produto=validaçoes.ler_produto(cadastro_produtos)
    preco=validaçoes.ler_preço() 
    quantidade =validaçoes.ler_quantidade()
    
    dados = {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade
    }
    cadastro_produtos[produto]=dados
    persistencia.salvar_json(cadastro_produtos,Cadastro_Clientes)
    return dados