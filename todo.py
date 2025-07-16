import os


tarefas = []


def adicionar_tarefa():
    tarefa = input('Digite o nome da tarefa: ').strip()
    if tarefa == '':
        print('Tarefa não pode ser vazia.')
        return
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso !')

def remover_tarefa():
    if not tarefas:
        print('Nenhuma tarefa para remover.')
        return
    print('Tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')
    try:
        indice = int(input('Digite o número da tarefa que deseja remover: ')) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')

def listar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    print('Tarefas: ')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')

def gerenciar_tarefas():
    while True:
        print('------ Menu Tarefas ------')
        print('1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Remover tarefa')
        print('0. Voltar')
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            adicionar_tarefa()
            os.system('pause')a
        elif opcao == '2':
            listar_tarefas()
            os.system('pause')
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '0':
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    while True:
        os.system('cls')
        print('------ Menu Principal ------')
        print('1. Gerenciar Tarefas')
        print('0. Sair')
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            gerenciar_tarefas()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')
