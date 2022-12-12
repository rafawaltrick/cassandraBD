from produto.select import buscar_produtos

def excluir_produto(session):
    buscar_produtos(session)

    id_produto = input(str('Digite o id do produto que deseja excluir: '))

    session.execute(f"delete from produtos where id='{id_produto}'")
    print(f'\nproduto de id {id_produto} excluido com sucesso...\n')