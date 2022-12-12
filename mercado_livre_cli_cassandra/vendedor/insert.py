from datetime import date
import uuid

def insert_vendedor(session):
    dataAtual = date.today()
    execucao = True
    while execucao:

        nome = input(str("Digite o nome do vendedor: "))
        email = input(str('Digite o endereço de email: '))
        cnpj = input(str("Digite o cnpj: "))
        telefone = input(str('Digite o numero do telefone: '))
        data_cadastro = dataAtual.strftime('%d/%m/%Y')

        session.execute("""
                        insert into vendedores
                            (id,nome,email,cnpj,telefone,data_cadastro)
                        values
                            (%s,%s,%s,%s,%s,%s)
        """, 
        (str(uuid.uuid1()),nome, email, cnpj, telefone, data_cadastro))

        opcao = input(str("Deseja cadastrar outro vendedor ? [SIM/NAO] "))

        if opcao.upper() != "SIM":
            execucao = False