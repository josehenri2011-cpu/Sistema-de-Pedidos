def Relatorio_faturamento(cadastro_produtos,pedidos):
     if cadastro_produtos=={}:
            print("nenhum produto cadastrado")
            return
     if pedidos==[]:
            print("nenhum pedido cadastrado")
            return      


     dic_temp={}
     for chave in cadastro_produtos:
        produto_atual=chave
        for dicionario in pedidos:
           if produto_atual in dicionario["produto"]:
              if produto_atual not in dic_temp:
                  dic_temp[produto_atual]={
                      "faturamento":0,
                  }
           else:
               print("Nao existe nenhum pedido desse produto")
               return

           dic_temp[produto_atual]["faturamento"]+=cadastro_produtos[produto_atual]["preco"]*dicionario["quantidade"]
    
     print(dic_temp)               