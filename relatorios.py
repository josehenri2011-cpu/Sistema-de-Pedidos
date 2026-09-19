def calculo_faturamento(cadastro_produtos,pedidos):
     if cadastro_produtos=={}:
            print("nenhum produto cadastrado")
            return
     if pedidos==[]:
            print("nenhum pedido cadastrado")
            return      


     faturamento={}
     for chave in cadastro_produtos:
        produto_atual=chave
        for dicionario in pedidos:
           if produto_atual==dicionario["produto"]:
              if produto_atual not in faturamento:
                  faturamento[produto_atual]={
                      "faturamento":0,
                  }
           

              faturamento[produto_atual]["faturamento"]+=cadastro_produtos[produto_atual]["preco"]*dicionario["quantidade"]
    
    
     return faturamento


def Relatorio_faturamento(cadastro_produtos,pedidos):
    resultado=calculo_faturamento(cadastro_produtos,pedidos)
    if resultado==None:
        print("Nenhum faturamento a ser relatado.")
    else:
        print("Faturamento por produto:")
        for produto, dados in resultado.items():
            print(f"Produto: {produto}, Faturamento: {dados['faturamento']}")

def produto_mais_vendido(pedidos):
    dados_pedidos=pedidos
    
    auditor={}
    mais_vendido={
        "mais_vendido":None,
         "unidades":0
    }
    for dicionario in dados_pedidos:
        produto_atual=dicionario["produto"]
        if produto_atual not in auditor:
               auditor[produto_atual]={
                     "unidades":0
                      }
            
        
        auditor[produto_atual]["unidades"]+=dicionario["quantidade"]
    

    for chave,valor in auditor.items():
        if valor["unidades"]>mais_vendido["unidades"]:
            mais_vendido["mais_vendido"]=chave
            mais_vendido["unidades"]=valor["unidades"]
    print(mais_vendido)
