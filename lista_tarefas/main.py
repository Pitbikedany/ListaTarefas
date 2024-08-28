from tabulate import tabulate
import os
from connection import *
from datetime import datetime

def limpar():
    os.system('cls')

def pausar():
    pause = input('Clique ENTER para continuar...')

while True:
    print("""
Lista de Tarefas
    A - Adicionar Tarefas
    V - Ver Tarefas
    F - Fechar Programa
""")

    opcao = input('Escolha a opção que deseja: ')

    if opcao == 'A' or opcao == 'a':
        data_atual = datetime.now()
        data = data_atual.strftime("%d-%m-%Y")
        print('Data: ', data)
        tarefa = input('Tarefa: ')

        try:
            myqueries.execute(f"INSERT INTO tarefas(mes,data,despesa,custo) VALUES('{data}','{tarefa}')")
            mydatabase.commit()
            break
        except:
            print('Ocorreu um erro, tente novamente...')
            pausar()
            limpar()
    elif opcao == 'V' or opcao == 'v':
        pass
    elif opcao == 'F' or opcao == 'f':
        break
    else:
        print('Escolha errada, tente novamente...')