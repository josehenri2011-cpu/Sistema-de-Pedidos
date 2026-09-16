import cadastros
import persistencia

cadastro_produtos=persistencia.carregar_json_produtos()
Cadastro_Clientes=persistencia.carregar_json_clientes()
pedidos=persistencia.carregar_json_pedidos()

print(Cadastro_Clientes)
print(cadastro_produtos)
print("Pedidos cadastrados: ",pedidos)

def Menu_Inicial():
    while True:
         print("Menu_Inicial")
         print("1 - Cadastro de Produtos:")
         print("2 - Cadastro de Clientes:")
         print("3 - Registro de Pedidos:")
         print("4 - Sair")
         opçao=int(input("Escolha uma opção: "))

         if opçao<5 and opçao>0:
            return opçao


while True:
   opçao = Menu_Inicial()
   if opçao == 1:
      cadastros.produto_cadastro(cadastro_produtos,Cadastro_Clientes,pedidos)
   elif opçao == 2:
      cadastros.cliente_cadastro(Cadastro_Clientes,cadastro_produtos,pedidos)
   elif opçao == 3:
      print("teste")
      resultado=cadastros.cadastro_pedidos(Cadastro_Clientes,cadastro_produtos,pedidos)
   elif opçao== 4:
         while True:
            print("Tem certeza que deseja finalizar ?") 
            resposta=input()
            if resposta =="sim":
                  encerrar=True
                  break

            elif resposta=="nao":
                  print("voltando ao menu")
                  break
            
            else:
                  print("resposta invalida")

         if encerrar==True:
            print("programa finalizado")
            break

