import json

def buscar_compras(session):

    compras = session.execute("select * from compras")

    if compras:

        print("Listagem das compras...\n")

        for compra in compras:
            cliente = json.loads(compra.cliente.replace("\'", "\""))
            produto = json.loads(compra.produto.replace("\'","\""))
            vendedor = json.loads(compra.vendedor.replace("\'","\""))
            print("|")
            print("| informações da compra")
            print(f"| id: {compra.id}")
            print("| produto:{nome}, preco: {preco}".format(
                nome = produto['nome'], preco = produto['preco']
            ))
            print(f"| data da compra: {compra.data_compra}")
            print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']))
            print("| Informações do cliente: {nome}, email: {email}".format(nome = cliente['nome'], email = cliente['email']))
            print("|")

    else:

        print("Nenhuma compra encontrada...")