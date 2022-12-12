from usuario.select import buscar_usuarios

def excluir_usuario(session):

    buscar_usuarios(session)
    id_usuario = input(str('Digite o id do usuario que deseja excluir: '))
    
    session.execute(f"delete from usuarios where id='{id_usuario}'")
    print(f'\nusuario de id {id_usuario} excluido com sucesso...\n')