from vendedor.select import buscar_vendedores

from datetime import date
import uuid

def inserir_produto(session):
    dataAtual = date.today()
    execucao = True

    buscar_vendedores(session)

    id_vendedor = input(str("Digite o nome do vendedor que deseja cadastrar um produto: "))

    resultado_busca = session.execute(f"select * from vendedores where id = '{id_vendedor}'")

    for vendedor in resultado_busca:
        print("vendedor encontrado...")
        dict = { 'id':vendedor.id, 'nome':vendedor.nome, 'cnpj':vendedor.cnpj, 'email':vendedor.email}

    while execucao:

        nome = input(str("Digite o nome do produto: "))
        descricao = input(str("Digite a descrição do produto: "))
        preco = input(str("Digite o preço do produto: "))
        quantidade = input(str("Digite a quantidade de produtos em estoque: "))
        data_postagem = dataAtual.strftime('%d/%m/%Y')

        session.execute("""
                insert into produtos
                    (id, nome, descricao, preco, quantidade, data_postagem, vendedor )
                values
                    (%s,%s,%s,%s,%s,%s,%s)
        """,
        (str(uuid.uuid1()),nome, descricao, preco, quantidade, data_postagem, str(dict)))

        opcao = input(str("Deseja cadastrar outro produto ? [SIM/NAO] "))

        if opcao.upper() != "SIM":
            execucao = False