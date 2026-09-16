import json

def salvar_json(cadastro_produtos,Cadastro_Clientes,pedidos):
 with open("produtos.json", "w") as arquivo:
     json.dump(cadastro_produtos, arquivo,ensure_ascii=False, indent=4)   
 with open("clientes.json", "w") as arquivo:
     json.dump(Cadastro_Clientes, arquivo,ensure_ascii=False, indent=4)   
 with open("pedidos.json", "w") as arquivo:
     json.dump(pedidos, arquivo,ensure_ascii=False, indent=4)

def carregar_json_produtos():
    try:
        with open("produtos.json","r") as arquivo:
            produtos=json.load(arquivo)
            return produtos
        
    except FileNotFoundError:
        return {}

def carregar_json_clientes():
    try:
        with open("clientes.json", "r") as arquivo:
            clientes=json.load(arquivo)
            return clientes
    except FileNotFoundError:
        return {}

def carregar_json_pedidos():
    try:
        with open("pedidos.json", "r") as arquivo:
            pedidos=json.load(arquivo)
            return pedidos
    except FileNotFoundError:
        return []