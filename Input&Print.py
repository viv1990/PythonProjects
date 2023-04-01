i = int(input('Enter how many tasks you need to enter in the TODO list: '))
todo_list = []
Len_Todo_list = []
while i>0:
    todo = input("Enter task:")
    todo_list.append(todo)
    Len_Todo_list.append(len(todo))
    i-=1

print(todo_list)
print("Length of each todo item is:",Len_Todo_list)
