import uuid

def inserir_usuario(session):

    print('Iniciando cadastro do usuario...\n')

    nome = input(str('Digite o nome do usuario: '))
    email = input(str('Digite o endereço de email: '))
    cpf = input(str('Digite o numero do cpf: '))
    rg = input(str('Digite o numero do rg: '))
    data_nascimento = input(str('Digite a data de nascimento: '))
    telefone = input(str('Digite o numero do telefone: '))
    endereco = input(str('Digite o endereço: '))
    
    session.execute("""
                    insert into usuarios 
                        (id,nome,email,cpf,rg,data_nascimento,telefone,endereco)
                    values
                        (%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (str(uuid.uuid1()),nome, email, cpf, rg, data_nascimento, telefone, endereco)
                    )

    print('\nUsuario cadastrado com sucesso.')