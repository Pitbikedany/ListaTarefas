# Agosto 2024
# Daniel Lourenço 
# PYTHON
#Ficheiro sql.sql contem as querys necessarias para criar a base de dados para este programa funcionar

#biblioteca para desenhar a tabela
from tabulate import tabulate
import os
#ficheiro da conexao com a bd
from connection import *
from datetime import datetime

#funcao para limpar a informacao da consola
def limpar():
    os.system('cls')

#funcao para pausar a informacao
def pausar():
    pause = input('Clique ENTER para continuar...')

while True:
    print("""
Lista de Tarefas
    A - Adicionar Tarefa
    T - Tarefas Concluidas
    V - Ver Tarefas
    F - Fechar Programa
""")

    opcao = input('Escolha a opção que deseja: ')
    limpar()

    if opcao == 'A' or opcao == 'a':
        # data da tarefa é extraida automaticamente do sistema
        data_atual = datetime.now()
        data = data_atual.strftime("%d-%m-%Y")
        print('Data: ', data)
        tarefa = input('Tarefa: ')

        try:
            #insert da tarefa na bd
            myqueries.execute(f"INSERT INTO tarefas(data,tarefa) VALUES('{data}','{tarefa}')")
            mydatabase.commit()
            limpar()
            print('Tarefa adicionada com sucesso')
            pausar()
            limpar()
        except:
            print('Ocorreu um erro, tente novamente...')
            pausar()
            limpar()

    elif opcao == 'V' or opcao == 'v':
        datas = []
        tarefas = []
        myqueries.execute(f"SELECT * FROM tarefas")
        datas_bd = myqueries.fetchall()

        for values in datas_bd:
            datas.append(values[0])
            tarefas.append(values[1])
        
        i=0
        #criacao da tabela para mostrar as tarefas
        info_table = [
            ["ID","Data","Tarefa"]
        ]
        while i < len(datas):
            info = [i,datas[i],tarefas[i]]
            i+=1
            info_table.append(info)
        # metodo para criar a tabela com a biblioteca importada    
        table = tabulate(info_table,headers="firstrow",tablefmt="pretty") 
        print(table)

        while True:
            print(""" 
C - Tarefa Concluida
E - Eliminar Tarefa
F - Fechar
""")
            concluir = input('Escolha a opção que deseja: ')
            limpar()

            if concluir == 'C' or concluir == 'c':
                print(table)
                tarefa_concluir = int(input('Digite o numero que deseja marcar como concluido: '))
                try:
                    #insert das tarefas concluidas em outra tabela da bd
                    myqueries.execute(f"INSERT INTO tarefas_concluidas(data,tarefa) VALUES('{datas[tarefa_concluir]}','{tarefas[tarefa_concluir]}')")
                    mydatabase.commit()
                    #delete das tarefas concluidas na tabela principal
                    myqueries.execute(f"DELETE FROM tarefas WHERE tarefa = '{tarefas[tarefa_concluir]}'")
                    mydatabase.commit()
                    limpar()
                except:
                    print('Ocorreu um erro, tente novamente...')
            elif concluir == 'E' or concluir == 'e':
                print(table)
                tarefa_concluir = int(input('Digite o numero que deseja eliminar: '))
                try:
                    #delete da tarefa selecionada pelo user
                    myqueries.execute(f"DELETE FROM tarefas WHERE tarefa = '{tarefas[tarefa_concluir]}'")
                    mydatabase.commit()
                    limpar()
                except:
                    print('Ocorreu um erro, tente novamente...')
                        
            elif concluir == 'F' or concluir == 'f':
                break
            else:
                print("Escolha errada, tente novamente...")

    elif opcao == 'T' or opcao == 't':
        datas = []
        tarefas = []
        myqueries.execute(f"SELECT * FROM tarefas_concluidas")
        datas_bd = myqueries.fetchall()

        for values in datas_bd:
            datas.append(values[0])
            tarefas.append(values[1])
        
        i=0
        info_table = [
            ["ID","Data","Tarefa"]
        ]
        while i < len(datas):
            info = [i,datas[i],tarefas[i]]
            i+=1
            info_table.append(info)
        table = tabulate(info_table,headers="firstrow",tablefmt="pretty") 
        print(table)
        pausar()
        limpar()

    elif opcao == 'F' or opcao == 'f':
        break
    else:
        print('Escolha errada, tente novamente...')