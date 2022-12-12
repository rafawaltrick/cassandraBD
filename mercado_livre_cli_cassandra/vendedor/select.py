def buscar_vendedores(session):

    vendedores = session.execute('select * from vendedores')

    if vendedores:

        print('Listagem dos vendedores...\n')

        for vendedor in session.execute('select * from vendedores'):
            print('|')
            print(f'| id: {vendedor.id}')
            print(f'| nome: {vendedor.nome}')
            print(f'| email: {vendedor.email}')
            print(f'| cnpj: {vendedor.cnpj}')
            print(f'| telefone: {vendedor.telefone}')
            print('|')

    else:

        print("Nenhum vendedor encontrado...")