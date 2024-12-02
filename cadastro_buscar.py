def cadastrador(lista):
    nome = input('Nome completo: ')
    email = input('Email: ')
    cpf = int(input('CPF: '))
    nascimento = int(input('Qual é a sua data de nascimento? (somente numeros) '))
    lista.append((nome, email, cpf, nascimento))


sistema = []

while True:
    print(' 1 - Cadastrar \n 2 - listar cadastros \n 3 - buscar cadastro')
    resposta = int(input('Qual opção deseja? '))
    if resposta == 1:

        cadastrador(sistema)

    elif resposta == 2:

        for nome, cpf, email, nascimento in sistema:
            print(f'{nome} | {cpf} | {email} | {nascimento}')

    elif resposta == 3:
        busca = input('Qual é o nome? ')
        for nome, cpf, email, nascimento in sistema:
            if nome == busca:
                print(f'{nome} | {email} | {cpf} | {nascimento}')