import cadastros
import persistencia
cadastro_produtos=persistencia.carregar_json()
Cadastro_Clientes={}

print(Cadastro_Clientes)

print("Menu Inicial")
print("1 - Cadastro de Produtos:")
print("2 - Cadastro de Clientes:")

opçao=input("Escolha uma opção: ")

if opçao == "1":
   cadastros.produto_cadastro(cadastro_produtos,Cadastro_Clientes)
if opçao == "2":
   cadastros.cliente_cadastro(Cadastro_Clientes,cadastro_produtos)




