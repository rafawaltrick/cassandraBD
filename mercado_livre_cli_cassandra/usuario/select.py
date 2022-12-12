def buscar_usuarios(session):

    usuarios = session.execute('select * from usuarios')

    if usuarios:

        print('Listagem dos usuarios...\n')
        
        for usuario in usuarios:
            print('|')
            print(f'| id: {usuario.id}')
            print(f'| nome: {usuario.nome}')
            print(f'| email: {usuario.email}')
            print(f'| cpf: {usuario.cpf}')
            print(f'| rg: {usuario.rg}')
            print(f'| data de nascimento: {usuario.data_nascimento}')
            print(f'| telefone: {usuario.telefone}')
            print(f'| endereco: {usuario.endereco}')
            print('|')

    else:

        print("Nenhum usuario encontrado")