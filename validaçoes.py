
def cliente(Cadastro_Clientes):
    while True:
         print("informe o cliente")
         cliente=input()
         cliente=cliente.strip()
         if cliente=="":
            print("o cliente deve conter um nome!")
            continue
         if cliente not in Cadastro_Clientes:
            return cliente
         else:
            print(f"{cliente} já esta cadastrado")

def ler_produto(cadastro_produtos):
    while True:
            print("informe o produto")
            produto=input()
            produto=produto.strip()
            if produto=="":
               print("o produto deve conter um nome!")
               continue
            if produto not in cadastro_produtos:
               return produto
            else:
                print(f"{produto} já esta cadastrado")


def ler_quantidade():
      while True:
              try:
                 print("coloque a quantidade")
                 quantidade=int(input())
                 if quantidade>0:
                    return quantidade
                                   
                 else:
                     print("A quantidade deve ser um numero inteiro e positivo")
              except ValueError:
                    print("A quantidade deve conter um valor inteiro")




def consultar_estoque(produto,quantidade,cadastro_produtos):
   flag=True
   while flag:
        if produto in cadastro_produtos:
            if cadastro_produtos[produto]["quantidade"] >= quantidade:
               flag=False
            else:
                print("quantidade insuficiente em estoque")
                return False
        else:
            print("produto nao encontrado no estoque")
            return False

        if flag==False:
           break
   return True 

def ler_preço():
    while True:   
          try:
              print("informe o preço")
              preço=float(input())
              
              if preço>0:
                 return preço
                                
               
              else:
                  print("o valor do preço deve ser maior que zero")
                  continue
               
          except ValueError:
                 print("o preço deve conter um valor numerico, sua anta")



def buscar_cliente(cliente,Cadastro_Clientes):
    if cliente in Cadastro_Clientes:
       return Cadastro_Clientes[cliente]
    else:
        return False



def buscar_produto(produto,cadastro_produtos):
    if produto in cadastro_produtos:
       return cadastro_produtos[produto]
    else:
        return False


