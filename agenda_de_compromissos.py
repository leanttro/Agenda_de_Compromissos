compromisso = {}

listacompromisso = []

def l():
    print("="*40)




#MENU PRINCIPAL
while True:
    l()
    print(" "*10,"AGENDA INTERATIVA")
    l()
    print("Bem-vindo(a)! Estamos aqui para ajudar na sua organização. Vamos lá!")
    print("[1] Adicionar Tarefa")
    print("[2] Visualizar Tarefas ")
    print("[3] Agenda Completa")
    print("[4] Alterar Tarefa")
    print("[5] Excluir Tarefa")
    print("[6] Encerrar Agenda")
    menu1 = str(input("--> Qual a opção escolhida: "))

    if menu1 == "1":
        while True:
            l()
            print("ADICIONE UMA TAREFA AQUI!")
            compromisso['Nome'] = str(input("TÍTULO: ")).upper()
            compromisso['Dia'] = str(input("DIA: ")).upper()
            compromisso['Mês'] = str(input("MÊS: ")).upper()
            compromisso['Obs'] = str(input("OBSERVAÇÃO: ")).upper()
            

            listacompromisso.append(compromisso.copy())
            print("TAREFA ADICIONADA COM SUCESSO! -->", end =" ")
            print(listacompromisso)
            while True:
                menu2 = str(input("[1] ADICIONAR OUTRA TAREFA [2] VOLTAR AO MENU: "))
                if menu2 == "1" or menu2 == "2":
                    if menu2 == "1": 
                        break
                    if menu2 == "2":
                        break
                    else:
                        print("ERRO! Digite 1 ou 2")
            if menu2 == "2":
                break
    
    if menu1 == "3":
        for i,v in enumerate(listacompromisso):
            print(f"{i} -> {v}")

            

            
            
    