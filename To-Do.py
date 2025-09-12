import biblioteca as bib

tarefas = []

while(True):
    bib.Mostrar_Menu()

    escolha = int(input(" Escolha: "))
    if(escolha == 1):
        tarefas = input("Adicione a nova tarefa: ")
        tarefas.append(tarefas)
        print(tarefas)
    elif(escolha == 2):
        pass
    elif(escolha == 3):
        pass
    elif(escolha == 4):
        break