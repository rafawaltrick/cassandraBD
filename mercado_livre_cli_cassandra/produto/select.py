import json

def buscar_produtos(session):

    produtos = session.execute("select * from produtos")

    if produtos:

        print("Listagem dos produtos...\n")

        for produto in produtos:
            vendedor = json.loads(produto.vendedor.replace("\'", "\""))
            print("|")
            print(f'| id: {produto.id}')
            print(f'| Nome: {produto.nome}')
            print(f'| Descricao: {produto.descricao}')
            print(f'| Preço: {produto.preco}')
            print(f'| Quantidade de produtos em estoque: {produto.quantidade}')
            print(f'| Data de postagem do produto: {produto.data_postagem}')
            print("| Informações do vendedor: {nome}, email: {email}, cnpj: {cnpj}".format(
                nome = vendedor['nome'], email = vendedor['email'], cnpj = vendedor['cnpj']
            ))

    else:

        print("Nenhum produto encontrado...")