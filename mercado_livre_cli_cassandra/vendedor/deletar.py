from vendedor.select import buscar_vendedores

def excluir_vendedor(session):
    buscar_vendedores(session)

    vendedor_id = input(str("Digite o id do vendedor que deseja excluir: "))

    session.execute(f"delete from vendedores where id='{vendedor_id}'")
    print(f'\n vendedor de id {vendedor_id} excluido com sucesso...\n')