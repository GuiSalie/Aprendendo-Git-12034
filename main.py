to_do_list = []

while True:
    command = input("Command: ").strip().lower()

    if command == "add":
        el = input("to do: ")
        to_do_list.append(el)
        print("Item added to list! \n")
        print(to_do_list)
    elif command == "remove":
        index = input("remove from list (by index): ")
        to_do_list.remove(index)
        print("Item remmoved from list! \n")
        print(to_do_list)
    elif command == "view":
        print(to_do_list)
    elif command == "check":
        index = input("check item from list (by index): ")
        to_do_list[index] = to_do_list[index] + "✅"
    elif command == "exit":
        print("Exiting program...")
        break 
    elif command == "help":
        print("add, remove, view, check, exit, help")
