'''__name__ is a variable with default value as __main__. If main.py file imports this function file, then
when the main.py file is executed. the __name__ variable changes to Function File name. and hence the code inside
the if conditional block does not get executed.
ANything outside the functions ;like print("hello") here in this program will get executed if the function
file is imported in main.py
'''

def get_todos():
    with open("Files/Todos.txt", 'r') as file:
        todos_local = file.readlines()
        return todos_local

def write_todos(todos_wlocal):
    with open("Files/Todos.txt", 'w') as file:
        file.writelines(todos_wlocal)

def show_list(todos):
    for i, item in enumerate(todos):
        todos[i] = f"{i + 1}. {item}"
        print(todos[i].strip())


if __name__=="__main__":
    print("Hello")
    print(__name__)