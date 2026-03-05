from time import sleep
from os import system

def press_enter_to_continue():
    input("Pressione ENTER para continuar...")

def clear():
    system("clear") #Limpa o terminal

def execute(todo):

    main_opt = -1
    
    while (main_opt != 0):
        clear()
        #Opções do menu principal
        print("O que deseja fazer?")
        print("1. Ver lista")
        print("2. Adicionar item à lista")
        print("3. Remover item da lista")
        print("4. Marcar item como feito")
        print("0. Sair")
        
        main_opt = input("Ação: ")
        
        #Ações
        if (main_opt == "0"):
            print("Saindo...")
            exit(0)

        if (main_opt == "1"):
            clear()
            print("Todos itens da lista: \n")
            for idx, item in enumerate(todo):
                print(f"{idx}. {item}")
            print("")

            press_enter_to_continue()
            continue

        if (main_opt == "2"):
            new_item = input("\nDigite o novo item: ")

            #Aqui vai a lógica de adicionar à lista

            press_enter_to_continue()
            continue
         
        if (main_opt == "3"):
            rm_item = int(input("Digite o indice do item a ser removido: "))

            #Aqui vai a lógica de remover com base no indice

            press_enter_to_continue()
            continue

        if (main_opt == "4"):
            check_item = int(input("Digite o indice a ser marcado: "))
            
            #Aqui vai a lógica de check

            press_enter_to_continue()
            continue

        print("Opção inválida...")
        sleep(3)


if __name__ == "__main__":
    todolist = ['Criar a todolist', 'fazer menus']
    execute(todolist)
