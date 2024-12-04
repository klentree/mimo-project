todo_list = []

while True:
    index = 1
    for task in todo_list:
        print(f"{index}. {task}")
        index += 1

    print("\nOptions:")
    print("1.) Add Task")
    print("2.) Remove Task")
    print("3.) Quit\n")

    choice = input("Enter a number (1, 2, 3) ")

    if choice == "1":
        new_task = input("Enter the task: ")
        todo_list.append(new_task)
        print(f"Task \"{new_task}\" added\n")

    elif choice == "2":
        if len(todo_list) == 0:
            print("Your ToDo list is empty")
        else:
            todo_list.pop()

    elif choice == "3":
        print("Quitting")
        break

    else:
        print("Wrong number")