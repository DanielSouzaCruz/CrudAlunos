def cadastra_aluno(alunos):
    id = int(input("Id:"))
    nome = input("Nome:")
    idade = int(input("Idade: "))
    cpf = input("CPF:")
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
    elif novo_cadastro ==2:
        menu(alunos)
    else:
        menu(alunos)


def remove_aluno(alunos):
    id = int(input("Digite o Id do Aluno que Deseja(s) Remover:"))
    alunos.remove(id)
    print("Aluno Removido com Sucesso") #concertar assim que listar estiver pronto
    menu(alunos)




def menu(alunos):
    print("## Menu ##")
    print("## Operações Disponiveis: ##")
    print("# 1 - Cadastrar #")
    print("# 2 - Remover #")
    print("# 3 - Listar #")
    print("# 4 - Atualizar #")
    print("# 5 - Fechar #")
    print(" ### ------ ###")

    operacao = int(input("Digite a Operação: "))

    if operacao == 1:
        cadastra_aluno(alunos)
    elif operacao == 2:
        remove_aluno(alunos)
    # elif operacao == 3:
    #     lista_aluno(alunos)
    # elif operacao == 4:
    #     atualiza_aluno(alunos)

    else:
        print("Essa Operação Não Existe")
        menu(alunos)




if __name__ == '__main__':
    alunos = []
    menu(alunos)