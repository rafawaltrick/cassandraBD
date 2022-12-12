from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from usuario.insert import inserir_usuario
from usuario.select import buscar_usuarios
from usuario.update import atualizar_usuario
from usuario.deletar import excluir_usuario

from produto.insert import inserir_produto
from produto.select import buscar_produtos
from produto.update import atualiazr_produto
from produto.deletar import excluir_produto

from vendedor.select import buscar_vendedores
from vendedor.insert import insert_vendedor
from vendedor.update import atualizar_vendedor
from vendedor.deletar import excluir_vendedor

from compra.select import buscar_compras
from compra.insert import inserir_compra
from compra.deletar import excluir_compra

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('GGaScuFXSyifcZqRwQRXinMl', 'tt57BXRjhR5gGUIA8WTN934B-od00-I0+SneqrvwqhWzuknKzyt.YD9xD3h-gFwM9gABbBsHhfYkSfAxaJZmBhbg+N6qFyw7cmQLt.kijy0Lmb0PqZ.JYcPvRz8f8N.4')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()

if row:
    print("Conexão bem sucedida...")
    execucao = True
    
    while execucao:
        
        print('''
            [1] inserir usuario
            [2] buscar usuarios
            [3] excluir usuario
            [4] inserir produto
            [5] buscar produtos
            [6] excluir produto
            [7] buscar vendedores
            [8] inserir vendedor
            [9] excluir vendedor
            [10] buscar compras
            [11] inserir compra
            [12] excluir compra
            [13] atualizar usuario
            [14] atualizar produto
            [15] atualizar vendedor
            [0] sair
            
            ''')
        
        opcao = input(str('Escolha uma das opções a cima: '))
        match (int(opcao)):
            case 1:
                inserir_usuario(session)
            case 2:
                buscar_usuarios(session)
            case 3:
                excluir_usuario(session)
            case 4:
                inserir_produto(session)
            case 5:
                buscar_produtos(session)
            case 6:
                excluir_produto(session)
            case 7:
                buscar_vendedores(session)
            case 8:
                insert_vendedor(session)
            case 9:
                excluir_vendedor(session)
            case 10:
                buscar_compras(session)
            case 11:
                inserir_compra(session)
            case 12:
                excluir_compra(session)
            case 13:
                atualizar_usuario(session)
            case 14:
                atualiazr_produto(session)
            case 15:
                atualizar_vendedor(session)
            case 0:
                print('Até mais...')
                execucao = False
            case _:
                print("Operação não entendida...")

else:
    print("Ocorreu um erro.")