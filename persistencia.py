import json

def salvar_json(cadastro_produtos,Cadastro_Clientes):
 with open("produtos.json", "w") as arquivo:
     json.dump(cadastro_produtos, arquivo,ensure_ascii=False, indent=4)   
 with open("clientes.json", "w") as arquivo:
     json.dump(Cadastro_Clientes, arquivo,ensure_ascii=False, indent=4)   


def carregar_json():
    with open("produtos.json","r") as arquivo:
        dados=json.load(arquivo)
        return dados
    