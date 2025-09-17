import biblioteca as bib

tarefas = []

while(True):
    bib.Mostrar_Menu()
    
    escolha = int(input("Escolha: "))
    match(escolha):
        case 1:
            novas_tarefas = input("Adicione a nova tarefa: ")
            tarefas.append(novas_tarefas)
            print(tarefas)
        case 2:
            editar_tarefa = novas_tarefas
            print(f"Edite: {editar_tarefa}")

        case 3:
            pass
        case 4:
            break

