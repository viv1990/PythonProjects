'''Break will exit the while code/loop and reach to the bye print statement'''
'''For loop in case 'show' will make sure that rather than printing todos which will display the list with quotes and commas in between, the for loop separates each item of the list'''
'''Case _, where _ is a variable which takes on any other value other than add, show or exit,
You can place any other variable so whatever you type other than add/show/exit as input will bind to that variable and 
print you have an invalid input, _ can pe replaced by any variable. _ is a good way to show to aware other developers'''
'''Use of bitwise OR operator'''
todos = []

while True:
    user_choice = input("Enter 'add' to add new todo, 'show' to show the todo list or 'exit' to exit the loop or 'del' to delete some item from todo list")
    user_choice = user_choice.lower()
    user_choice = user_choice.strip()
    match user_choice:
        case "add" | "sum":
            todo = input("Enter a todo")
            todos.append(todo)
        case "show" | "display":
            i=1
            for item in todos:
                print(i  , "  :" ,item)
                i=i+1
        case "exit":
            break
        case "delete" | "del" |"remove":
            user_action = int(input("Please enter which todo task to edit"))
            if (user_action<=len(todos)):
                todos.pop(user_action-1)
                print("updated list pof todos: \n", todos )
            else:
                print("Task does not exist")

        case "edit":
            user_edit_choice = int(input("Please enter which todo task to edit"))
            if (user_edit_choice <= len(todos)):
                print("Do you want to edit the below task: \n", todos[user_edit_choice-1])
                user_edit_confirm = input("press 'y' for Yes or else press 'n' for No")
                if(user_edit_confirm=='y'):
                    todos[user_edit_choice-1]=input("Enter the new task")
                else:
                    print("Task incorrectly selected")
            else:
                print("Task does not exist")
        case _:
           print("You have entered an invalid input")
print('Bye')