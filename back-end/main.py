import biblioteca as bib

tarefas = []

while(True):
    bib.Mostrar_Menu()
    
    escolha = int(input("Escolha: "))
    match(escolha):
        case 1:
            novas_tarefas = input("Adicione a nova tarefa: ")
            tarefas.append(novas_tarefas)
            print("Tarefa adicionada")
        case 2:
            if not (tarefas):
                print("Nenhuma tarefa para editar.")
            else:
                for i in range(0, len(tarefas)):
                    print(tarefas)
                    indice = int(input("Digite o número da tarefa que deseja editar: ")) 
                    if((0 <= indice) <= len(tarefas)):
                        nova_descricao = input("Digite a nova descrição da tarefa: ")
                        tarefas[indice] = nova_descricao
                        print("Tarefa editada com sucesso")
                    else:
                        print("Indice Invalido")
                        
        case 3:
            print(tarefas)
            remover_indice = int(input("Digite o indice para qual voce deseja remover: "))
            if(remover_indice < len(tarefas)):
                confirmar = input("Digite (S/N) para confirmar ")
                if confirmar.upper() == "S":
                    removida = tarefas.pop(remover_indice)
                    print(f"Tarefa '{removida}' removida com sucesso")
            else:
                print("Operação cancelada.")
        case 4:
            print("Saindo")
            break
        case _:
            print("Opção invalida")