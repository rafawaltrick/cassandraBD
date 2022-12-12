from produto.select import buscar_produtos

def atualiazr_produto(session):

    print('''Opções de edição:
    [1] editar todas as informações
    [2] escolher o que deseja editar
    [0] Voltar
    ''')

    opcao_edicao = input(str("Escolha a opção desejada: "))

    match int(opcao_edicao):

        case 1:

            buscar_produtos(session)
            id_produto = input(str("Digite o id do produto que deseja atualizar: "))
            resultado_busca_produto = session.execute(f"select * from produtos where id = '{id_produto}'")

            if resultado_busca_produto:

                nome = input(str("Digite o novo nome do produto: "))
                descricao = input(str("Digite a nova descricao do produto: "))
                preco = input(str("Digite o novo preço do produto: "))
                quantidade = input(str("Digite a nova quantidade de produtos em estoque: "))
                session.execute(f"update produtos set nome='{nome}', descricao='{descricao}', preco='{preco}', quantidade='{quantidade}' where id='{id_produto}'")
                print("\nAlterações realizadas com sucesso...\n")
                return

            else:
                print("\nProduto não encontrado...\n")
                return

        case 2:
            
            buscar_produtos(session)
            id_produto = input(str("Digite o id do produto que deseja atualizar: "))
            resultado_busca_produto = session.execute(f"select * from produtos where id = '{id_produto}'")

            if resultado_busca_produto:
                execucao = True

                while execucao:
                    print('''
    [1] Nome
    [2] Descricao
    [3] Preço
    [4] Quantidade
    [0] Finalizar alterações
                    ''')

                    opcao = input(str("Digite o numero do que deseja atualizar: "))

                    match int(opcao):
                        case 1:
                            nome = input(str("Digite o novo nome do produto: "))
                            session.execute(f"update produtos set nome='{nome}' where id='{id_produto}'")
                        case 2:
                            descricao = input(str("Digite a nova descricao do produto: "))
                            session.execute(f"update produtos set descricao='{descricao}' where id='{id_produto}'")
                        case 3:
                            preco = input(str("Digite o novo preço do produto: "))
                            session.execute(f"update produtos set preco='{preco}' where id='{id_produto}'")
                        case 4:
                            quantidade = input(str("Digite a nova quantidade de produtos em estoque: "))
                            session.execute(f"update produtos set quantidade='{quantidade}' where id='{id_produto}'")
                        case 0:
                            print("\nAlterações realizadas com sucesso...\n")
                            execucao = False
                            return
                        case _:
                            print("Operação não entendida...")

            else:
                print("\nProduto não encontrado...\n")
                return

        case 0:
            return

        case _:
            print("Operação não entendida...")