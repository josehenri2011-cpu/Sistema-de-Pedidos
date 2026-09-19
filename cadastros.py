import persistencia
import validaçoes
import estoque

def consultar_pedidos(pedidos):
    cliente=input("informe o cliente\n")
    flag=True
    for dicionario in pedidos:
        print()
        if cliente==dicionario["cliente"]:
            for chave,valor in dicionario.items():
                print(chave,":",valor)
                flag=False

    if flag:
        print("cliente não encontrado")

def cadastro_pedidos(Cadastro_Clientes,cadastro_produtos,pedidos):
    flag=True
    while flag:
        cliente=input("informe o cliente\n")
        dados_cliente=validaçoes.buscar_cliente(cliente,Cadastro_Clientes)
        if dados_cliente==False:
           print("cliente não encontrado")
        else:
            flag=False
        
        if flag==False:
           break
               
    flag=True
    while flag:
        produto=input("informe o produto\n")
        dados_produto=validaçoes.buscar_produto(produto,cadastro_produtos)
        if dados_produto==False:
          print("produto não cadastrado")
        else:
            flag=False

        if flag==False:
           break    

    while True:
        quantidade=validaçoes.ler_quantidade()
        confere_estoque=validaçoes.consultar_estoque(produto,quantidade,cadastro_produtos)
        

        if confere_estoque:
            estoque.reduzir_estoque(produto,cadastro_produtos,quantidade)

            registros={
            
            "cliente": cliente,
            "produto": produto,
            "quantidade": quantidade
                                
            }
            pedidos.append(registros)
            persistencia.salvar_json(cadastro_produtos,Cadastro_Clientes,pedidos)
            break
        else:
            print("tente novamente")   

    


def cliente_cadastro(Cadastro_Clientes,cadastro_produtos,pedidos):
    nome=validaçoes.cliente(Cadastro_Clientes)

    registros={}
    Cadastro_Clientes[nome]=registros
    persistencia.salvar_json(cadastro_produtos,Cadastro_Clientes,pedidos)



def produto_cadastro(cadastro_produtos,Cadastro_Clientes,pedidos):
    print("Cadastro de Produtos")
    produto=validaçoes.ler_produto(cadastro_produtos)
    preco=validaçoes.ler_preço() 
    quantidade =validaçoes.ler_quantidade()
    
    dados = {
        "preco": preco,
        "quantidade": quantidade
    }
    cadastro_produtos[produto]=dados
    persistencia.salvar_json(cadastro_produtos,Cadastro_Clientes,pedidos)
    return dados