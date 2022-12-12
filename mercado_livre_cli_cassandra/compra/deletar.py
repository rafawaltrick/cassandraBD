from compra.select import buscar_compras

def excluir_compra(session):

    buscar_compras(session)
    id_compra = input(str('Digite o id da compra que deseja excluir: '))

    session.execute(f"delete from compras where id='{id_compra}'")
    print(f'\ncompra de id {id_compra} excluido com sucesso...\n')
