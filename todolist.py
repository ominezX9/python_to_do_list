from array import array
tasks = []


def main():
    print("YOUR TO DO LIST 📃")
    menu()


def option_1():
    # Add new tasks
    print("\t ADD TASK")
    print("\t----------")
    new_task = input("New task: ")
    tasks.append(str(new_task) + "\n")
    add_to_file()
    menu()


def add_to_file():
    # adding the user's task to a file
    f = open("current_tasks.txt", "r")
    fileread = f.read()

    if len(fileread) > 0 :
        f = open("current_tasks.txt", "a")
        task = tasks[(len(tasks) - 1)]
        f.write(task)
    else :
        f = open("current_tasks.txt", "w")
        f.writelines(tasks)
        

def option_2():
    # Mark task as complete\
    count = 0
    f = open("current_tasks.txt", "r")
    lines = f.readlines()
    for line in lines:
        count += 1
        print("{}. {}". format(count, line.strip()))

    user = int(input("What have you completed:"))
    useno = user - 1
    print(useno)

    valiwant = lines[useno]
    lines.remove(valiwant)
    f = open("current_tasks.txt", "w")
    f.writelines(lines)
    f.close()

    # print("\n" + str(valiwant) + " moved to completed")
    print("\n" + str(valiwant) + " Completed 🌈🌈")

    # push to completed task

    f = open("completed_tasks.txt", "a")
    f.write(valiwant)
    f.close()

    # fupdate = open("current_tasks.txt", "w")
    # ls = lines.pop(user)
    # print(ls)
    # # for l in lines:
    # #     fupdate.write(l)
    # #     print(l)


    menu()


def option_3():
    # Delete task

    print()


def option_4():
    # View tasks
    for i in tasks:
        print(i)
    print()


def option_5():
    # view completed tasks
    print()


def option_6():
    # exit
    print()


def menu():
    print("""
        1. Add tasks
        2. Mark tasks as complete
        3. Delete tasks
        4. View tasks
        5. View completed task
        6. Exit
    """)
    option = int(input("What would you like to do?: "))
    print()

    if option == 1:
        option_1()
    elif option == 2:
        option_2()


main()
