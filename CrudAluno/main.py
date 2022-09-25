def cadastra_aluno(alunos):
    print('\n### Operação Cadastrar ###')
    id = input("Id: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    ra = input("Ra: ")
    alunos.append({
        "id": id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "ra": ra
    })

    print("O Aluno foi Cadastrado com Sucesso!")

    novo_cadastro = int(input("\nGostaria de Cadastrar um Novo Aluno(a)?? 1 - Sim / 2 - Não: "))
    if novo_cadastro == 1:
        cadastra_aluno(alunos)
    else:
        menu(alunos)


def remove_aluno(alunos):
    id = input("Digite o Id do Aluno que Deseja Remover: ")
    i = 0

    while i < len(alunos):
        if alunos[i]['id'] == id:
            alunos.pop(i)
            print("Aluno Removido com Sucesso")
        i += 1
    menu(alunos)

def menu(alunos):
    print("\n## Menu ##")
    print("--- Operações Disponiveis ---")
    print(" 1 - Cadastrar ")
    print(" 2 - Remover ")
    print(" 3 - Listar ")
    print(" 4 - Atualizar ")
    print(" 5 - Fechar ")
    print((("|" + "=-" * 10 + "|")))

    operacao = int(input("\nDigite a Operação: "))

    if operacao == 1:
        cadastra_aluno(alunos)
    elif operacao == 2:
        remove_aluno(alunos)
    elif operacao == 3:
        lista_aluno(alunos)
    elif operacao == 4:
        atualiza_aluno(alunos)
    elif operacao == 5:
        fechar(alunos)
    else:
        print("Essa Operação Não Existe")
        menu(alunos)

def fechar(alunos):
    fechar_lista = int(input("\nTem certeza que deseja fechar o programa? 1 - S / 2 - N: "))

    if fechar_lista == 1:
        print('Programa finalizado!')
        print('Created By:Daniel Souza da Cruz, Eduardo Gabriel')
    else:
        menu(alunos)

def lista_aluno(alunos):
    print('\n ### Listagem ### ')
    for aluno in alunos:
        print("Id: " + aluno['id'] + ' | ' + "Nome: " + aluno['nome'] + ' | ' + "Idade: " + str(aluno['idade']) + ' | ' + "Cpf: " + str(aluno['cpf'] + ' | ' + "RA: " + aluno['ra']))
        print(("|" + "=-" * 35 + "|"))

    print('\n### ------------- ###')
    print('# 1 - cadastrar # ')
    print('# 2 - remover # ')
    print('# 3 - atualizar # ')
    print('# 4 - retornar # ')
    print('### ------------ ### ')
    opcao_lista = int(input("\nDigite uma função para prosseguir: "))

    if opcao_lista == 1:
        cadastra_aluno(alunos)
    elif opcao_lista == 2:
        remove_aluno(alunos)
    elif opcao_lista == 3:
        atualiza_aluno(alunos)
    elif opcao_lista == 4:
        menu(alunos)
    else:
        print('Programa Finalizado')

def atualiza_aluno(alunos):
    id = input('Digite o id do aluno: ')

    for aluno in alunos:
        if aluno['id'] == id:
            aluno['nome'] = input('Nome: ')
            aluno['idade'] = int(input('Idade: '))
            aluno['cpf'] = input('Cpf: ')
            aluno['ra'] = input('Ra: ')
            print('Aluno Atualizado com Sucesso!')
            print('Retornando ao Menu!')
            menu(alunos)


if __name__ == '__main__':
    alunos = []
    menu(alunos)
