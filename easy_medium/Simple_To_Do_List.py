# Create a basic to-do list program that allows users to add tasks, remove tasks, and display the list.
tasks = []


def main_app():
    print("\033[37m******************* \033[0m  \033[32m Welcome\033[0m \033[31m To\033[0m \033[33m Our \033[0m \033[34m App \033[0m \033[37m ********************\033[0m")
    print("1) add Task \U0001F195 \U0001F4C3")
    print("2) View Tasks \U0001F441")
    print("3) Remove Task \U0001F5D1")
    print("q) Exist Program  \033[31m X\033[0m")
    choice = input("Enter Your Choice Here : ")
    if choice == "1":
        print(add_todo())
    elif choice == "2":
        print(view_task())
    elif choice == "3":
        print(delete_task())
    elif choice.lower() == 'q':
        print("..Thanks for Using Our App..")
        exit()
    else:
        print("\033[31m Enter Valid Choice!!! \033[0m")
        main_app()


def add_todo():
    while True:
        data = input("Enter Task \033[32m Name \033[0m \033[31m ('b' To go Back To Main)\033[0m: ")
        if data.lower() == 'b':
            main_app()
        else:
            tasks.append(data)


def view_task():
    print("\033[32m******************* Task List ********************\033[0m")
    for i, task in enumerate(tasks[::-1]):
        print(f"\033[31m Task {i + 1} \033[0m \033[34m=>\033[0m \033[32m {task}\033[0m")

    print("\033[31m******************* End Of Task List ********************\033[0m")
    main_app()


def delete_task():
    name = input("Enter Task To Delete: ")
    if name in tasks:
        tasks.remove(name)
        print(f"\033[32m Successfully Deleted \033[31m {name} \033[0m From Tasks \033[0m")
        print("\033[31m******************* Deleted Taks ********************\033[0m")
        main_app()
    else:
        print(f"\033[31m Error While Deleting \033[32m {name} \033[0m Try Again Name Not Found \033[0m")
        delete_task()


main_app()