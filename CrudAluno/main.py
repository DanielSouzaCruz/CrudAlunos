def register_students(students):
    print('\n### Operação Cadastrar ###')
    name = input("Nome: ")
    age = int(input("Idade: "))
    cpf = input("CPF: ")
    ra = input("Ra: ")

    if len(students) == 0:
        student_id = 1
    else:
        student_id = int(students[-1]["id"]) + 1

    students.append({
        "id": str(student_id),
        "nome": name,
        "idade": age,
        "cpf": cpf,
        "ra": ra
    })

    print("O Aluno foi Cadastrado com Sucesso!")

    new_register = int(input("\nGostaria de Cadastrar um Novo Aluno(a)?? 1 - Sim / 2 - Não: "))
    if new_register == 1:
        register_students(students)
    else:
        menu(students)

def remove_student(students):
    id = input("Digite o Id do Aluno que Deseja Remover: ")
    i = 0

    while i < len(students):
        if students[i]['id'] == id:
            students.pop(i)
            print("Aluno Removido com Sucesso")
        i += 1
    menu(students)

def menu(students):
    print("\n## Menu ##")
    print("--- Operações Disponiveis ---")
    print(" 1 - Cadastrar ")
    print(" 2 - Remover ")
    print(" 3 - Listar ")
    print(" 4 - Atualizar ")
    print(" 5 - Fechar ")
    print((("|" + "=-" * 10 + "|")))

    operation = int(input("\nDigite a Operação: "))

    if operation == 1:
        register_students(students)
    elif operation == 2:
        remove_student(students)
    elif operation == 3:
        list_student(students)
    elif operation == 4:
        update_student(students)
    elif operation == 5:
        close(students)
    else:
        print("Essa Operação Não Existe")
        menu(students)

def close(students):
    print('Programa finalizado!')
    print('Created By: Daniel Souza da Cruz, Eduardo Gabriel')

def list_student(students):
    print('\n ### Listagem ### ')
    for student in students:
        print("Id: " + student['id'] + ' | ' + "Nome: " + student['nome'] + ' | ' + "Idade: " + str(student['idade']) + ' | ' + "Cpf: " + str(student['cpf'] + ' | ' + "RA: " + student['ra']))
        print(("|" + "=-" * 35 + "|"))
    menu(students)

def update_student(students):
    for student in students:
        print("Id: " + student['id'] + ' | ' + "Nome: " + student['nome'] + ' | ' + "Idade: " + str(student['idade']) + ' | ' + "Cpf: " + str(student['cpf'] + ' | ' + "RA: " + student['ra']))
        print(("|" + "=-" * 35 + "|"))
    id = input('Digite o id do aluno: ')

    for student in students:
        if student['id'] == id:
            student['nome'] = input('Nome: ')
            student['idade'] = int(input('Idade: '))
            student['cpf'] = input('Cpf: ')
            student['ra'] = input('Ra: ')
            print('Aluno Atualizado com Sucesso!')
            print('Retornando ao Menu!')
            menu(students)

if __name__ == '__main__':
    students = []
    menu(students)
