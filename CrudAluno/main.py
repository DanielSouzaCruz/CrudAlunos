def cadastra_aluno(alunos):
    print('\n### Operação Cadastrar ###')
    id = input("Id: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    ca = input("Ca: ")
    alunos.append({
        "id": id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "ca": ca
    })

    print("O Aluno foi Cadastrado com Sucesso!")

    novo_cadastro = int(input("Gostaria de Cadastrar um Novo Aluno(a)?? [1-Sim/2-Não]: "))
    if novo_cadastro == 1:
        cadastra_aluno(alunos)
    else:
        menu(alunos)


def remove_aluno(alunos):
    id = int(input("Digite o Id do Aluno que Deseja(s) Remover:"))
    aluno.remove(id)
    print("Aluno Removido com Sucesso") #concertar assim que listar estiver pronto
    menu(alunos)


def menu(alunos):
    print("\n## Menu ##")
    print("--- Operações Disponiveis ---")
    print("# 1 - Cadastrar #")
    print("# 2 - Remover #")
    print("# 3 - Listar #")
    print("# 4 - Atualizar #")
    print("# 5 - Fechar #")
    print("### -------- ###")

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
    fechar_lista = int(input("Tem certeza que deseja fechar o programa? 1 - S / 2 - N "))

    if fechar_lista == 1:
        print('Programa finalizado!')
    else:
        menu(alunos)

def lista_aluno(alunos):
    print('\n ### Listagem ### ')
    for aluno in alunos:
        print(aluno['id'] + ', ' + aluno['nome'] + ', ' + str(aluno['idade']) + ', ' + str(aluno['cpf'] + ', ' + aluno['ca']))

    print('\n### ------------- ###')
    print('# 1 - cadastrar # ')
    print('# 2 - remover # ')
    print('# 3 - atualizar # ')
    print('# 4 - fechar # ')
    print('### ------------ ### ')
    opcao_lista = int(input("\nDigite uma função para prosseguir: "))

    if opcao_lista == 1:
        cadastra_aluno(alunos)
    elif opcao_lista == 2:
        remove_aluno(alunos)
    elif opcao_lista == 3:
        atualiza_aluno(alunos)
    elif opcao_lista == 4:
        fechar(alunos)
    else:
        print('Programa Finalizado')

def atualiza_aluno(alunos):
    id = input('Digite o id do aluno: ')

    for aluno in alunos:
        if aluno['id'] == id:
            aluno['nome'] = input('Nome: ')
            aluno['idade'] = int(input('Idade: '))
            aluno['cpf'] = input('Cpf: ')
            aluno['ca'] = input('Ca: ')
            print('Dados do aluno atualizados!')
            menu(alunos)

if __name__ == '__main__':
    alunos = []
    menu(alunos)