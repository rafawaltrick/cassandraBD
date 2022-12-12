from usuario.select import buscar_usuarios

def atualizar_usuario(session):

    print('''Opções de edição:
    [1] editar todas as informações
    [2] escolher o que deseja editar
    [0] Voltar
    ''')

    opcao_edicao = input(str("Escolha a opção desejada: "))

    match int(opcao_edicao):

        case 1:

            buscar_usuarios(session)
            id_usuario = input(str("Digite o id do usuario que deseja atualizar: "))
            resultado_busca_cliente = session.execute(f"select * from usuarios where id ='{id_usuario}'")

            if resultado_busca_cliente:

                nome = input(str("Digite o novo nome: "))
                cpf = input(str("Digite o novo cpf: "))
                rg = input(str("Digite o novo rg: "))
                email = input(str("Digite o novo email: "))
                telefone = input(str("Digite o novo telefone: "))
                endereco = input(str("Digite o novo endereco: "))
                data_nascimento = input(str("Digite a nova data de nascimento: "))
                session.execute(f"update usuarios set nome='{nome}', cpf='{cpf}', rg='{rg}', email='{email}', telefone='{telefone}', endereco='{endereco}', data_nascimento='{data_nascimento}' where id='{id_usuario}'")
                print("\nAlterações realizadas com sucesso...\n")
                return

            else:
                print("\nUsuario não encontrado...\n")
                return

        case 2:

            buscar_usuarios(session)
            id_usuario = input(str("Digite o id do usuario que deseja atualizar: "))
            resultado_busca_cliente = session.execute(f"select * from usuarios where id ='{id_usuario}'")

            if resultado_busca_cliente:
                execucao = True

                while execucao:

                    print('''
    [1] Nome
    [2] CPF
    [3] RG
    [4] Email
    [5] Telefone
    [6] Endereço
    [7] Data de nascimento
    [0] Finalizar alterações
                    ''')

                    opcao = input(str("Digite o numero do que deseja atualizar: "))

                    match int(opcao):
                        case 1:
                            nome = input(str("Digite o novo nome: "))
                            session.execute(f"update usuarios set nome='{nome}' where id='{id_usuario}'")
                        case 2:
                            cpf = input(str("Digite o novo cpf: "))
                            session.execute(f"update usuarios set cpf='{cpf}' where id='{id_usuario}'")
                        case 3:
                            rg = input(str("Digite o novo rg: "))
                            session.execute(f"update usuarios set rg='{rg}' where id='{id_usuario}'")
                        case 4:
                            email = input(str("Digite o novo email: "))
                            session.execute(f"update usuarios set email='{email}' where id='{id_usuario}'")
                        case 5:
                            telefone = input(str("Digite o novo telefone: "))
                            session.execute(f"update usuarios set telefone='{telefone}' where id='{id_usuario}'")
                        case 6:
                            endereco = input(str("Digite o novo endereco: "))
                            session.execute(f"update usuarios set endereco='{endereco}' where id='{id_usuario}'")
                        case 7:
                            data_nascimento = input(str("Digite a nova data de nascimento: "))
                            session.execute(f"update usuarios set data_nascimento='{data_nascimento}' where id='{id_usuario}'")
                        case 0:
                            print("\nAlterações realizadas com sucesso...\n")
                            execucao = False
                            return
                        case _:
                            print("Operação não entendida...")

            else:
                print("\nUsuario não encontrado...\n")
                return

        case 0:
            return

        case _:
            print("Operação não entendida...")