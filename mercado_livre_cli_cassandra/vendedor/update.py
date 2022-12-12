from vendedor.select import buscar_vendedores

import json

def atualizar_vendedor(session):

    buscar_vendedores(session)
    id_vendedor = input(str("Digite o id do vendedor que deseja atualizar: "))
    resposta_busca_vendedor = session.execute(f"select * from vendedores where id = '{id_vendedor}'")

    if resposta_busca_vendedor:

        nome = input(str("Digite o novo nome do vendedor: "))
        email = input(str('Digite o novo endereço de email: '))
        cnpj = input(str("Digite o novo numero do cnpj: "))
        telefone = input(str('Digite o novo numero do telefone: '))

        produtos_cadastrados = session.execute('select * from produtos')

        for produto in produtos_cadastrados:
            
            vendedor = json.loads(produto.vendedor.replace("\'", "\""))
            if vendedor['id'] == id_vendedor:
                vendedor['nome'] = nome
                vendedor['email'] = email
                vendedor['cnpj'] = cnpj
                vendedor['telefone'] = telefone

                session.execute(f"delete from produtos where id='{produto.id}'")
                session.execute("""
                        insert into produtos
                            (id, nome, descricao, preco, quantidade, data_postagem, vendedor )
                        values
                            (%s,%s,%s,%s,%s,%s,%s)
                """,
                (produto.id,produto.nome, produto.descricao, produto.preco, produto.quantidade, produto.data_postagem, str(vendedor)))

        session.execute(f"update vendedores set nome='{nome}', email='{email}', cnpj='{cnpj}', telefone='{telefone}' where id = '{id_vendedor}'")

    else:
        print("\nVendedor não encontrado...\n")
        return
