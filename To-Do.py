import biblioteca as bib

tarefas = []

bib.Mostrar_Menu()

while(True):
    bib.Mostrar_Menu()
    
    escolha = int(input(" Escolha: "))
    if(escolha == 1):
        tarefas [0+1] = input("Adicione a Tarefa: ")
    elif(escolha == 2):
        pass
    elif(escolha == 3):
        pass
    elif(escolha == 4):
        break