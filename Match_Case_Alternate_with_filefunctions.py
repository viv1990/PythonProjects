# Todos are stored in a text file and keeps on getting appended in the file. Here we are using 'with' context manager
# The benefit is you do not need to close the file, it is automatically done
from Functions_File import get_todos,write_todos,show_list
# Importing the functions created from Functions_file to this program and use it here
todos = []
while True:
    user_choice = input("Type add,show,edit,del")
    user_choice = user_choice.strip()

    # if 'add' in user_choice: which was previously written will fail if user inputs: edit add the member, as
    # interpreter will see add is there in user's choice which will let it enter the first if condition
    # However user actually wants to edit, and so startswith is a better string method to see if actually add starts at
    # at the first position
    if user_choice.startswith('add') or user_choice.startswith('new'):
        todo = user_choice[4:]
        if(len(todo)>0):
            todos = get_todos() #Function called, todos is a global variable
            todos.append(todo+'\n')
            write_todos(todos)
        else:
            continue

    elif user_choice.startswith('show') or user_choice.startswith('display'):
        todos = get_todos()
        show_list(todos)

    elif user_choice.startswith('edit') or user_choice.startswith('modify'):
        todos = get_todos()
        print("Here is your existing todo list")
        show_list(todos)
        try:
            user_editChoice = int(input("Enter a todo number to edit"))
            if (user_editChoice <= len(todos)):
                todos = get_todos()
                todos[int(user_editChoice) - 1] = input("Enter a new todo") + '\n'
                print(todos)
                write_todos(todos)
        except(ValueError):
            print("You entered an invalid Input, please enter a number to edit")
            continue
        except(IndexError):
            print("There is no todo with the number you entered, Please try again")
            continue

    elif ('del' or 'delete') in user_choice:
        todos = get_todos()
        print("Here is your existing todo list")
        show_list(todos)

        try:
            todo = int(input("Enter a todo to delete"))
            x = todos[todo-1]
            todos = get_todos()
            todos.pop(int(todo) - 1)
            with open("Files/Todos.txt", 'w') as file:
                file.writelines(todos)
        except(ValueError):
            print("You entered an invalid Input, please enter a number to edit")
            continue
        except(IndexError):
            print("There is no todo with the number you entered, Please try again")
            continue

    elif 'exit' in user_choice:
        break

    else:
        print("Command invalid")
