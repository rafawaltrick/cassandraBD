from usuario.select import buscar_usuarios

from produto.select import buscar_produtos

from datetime import date
import uuid

def inserir_compra(session):
    dataAtual = date.today()
    execucao = True

    buscar_usuarios(session)
    id_cliente = input(str("Digite o id do cliente que irá realizar a compra: "))
    resultado_busca_cliente = session.execute(f"select * from usuarios where id ='{id_cliente}'")

    if resultado_busca_cliente:

        while execucao:

            buscar_produtos(session)
            id_produto = input(str("Digite o id do produto que deseja comprar: "))
            resultado_busca_produto = session.execute(f"select * from produtos where id = '{id_produto}'")
            data_compra = dataAtual.strftime('%d/%m/%Y')

            if resultado_busca_produto:

                for cliente in resultado_busca_cliente:
                    dict_cliente = {'id':cliente.id, 'nome':cliente.nome, 'cpf':cliente.cpf, 'email':cliente.email}

                for produto in resultado_busca_produto:
                    dict_produto = {'id':produto.id, 'nome':produto.nome, 'preco':produto.preco}
                    dict_vendedor = produto.vendedor

                session.execute("""
                        insert into compras
                            (id, data_compra, total, cliente, produto, vendedor)
                        values
                            (%s,%s,%s,%s,%s,%s)
                """,
                (str(uuid.uuid1()),data_compra, dict_produto['preco'], str(dict_cliente), str(dict_produto), dict_vendedor))

                opcao = input(str("Deseja cadastrar outro produto ? [SIM/NAO] "))

                if opcao.upper() != "SIM":
                    execucao = False

            else:
                print("Produto não encontrado")

    else:

        print("Cliente não encontrado...")