import Functions_File as ff
import PySimpleGUI as ps

AddButton = ps.Button("Add")
Lable1= ps.Text("Enter a To-Do")
InputText1= ps.InputText(tooltip="Enter your todo here",expand_x=True)

InputText2= ps.InputText(tooltip="Your To-Do List",expand_x=True,expand_y=True)
ShowButton=ps.Button("Show")
ExitButton=ps.Button("Exit")
window=ps.Window("To-Do Application",
                 layout=[[Lable1],[InputText1,AddButton],[InputText2,ShowButton],[ExitButton]],
                 size=(800,500),
                 font=("Helvetica",20))


# window.read gives us two values, one is what event happened and what were the associated values
# so if we press add button , add is an event which happened, the data written in the text box
# becomes the values. Values are returned in Dictionary format (Key:value) pair
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add'|'add':
            todos=ff.get_todos()
            todos.append(values[0]+'\n')
            print(todos)
            ff.write_todos(todos)

        case ps.WIN_CLOSED:
            break

        case 'Exit':
            break

        case 'Show'|'display':
            todos = ff.get_todos()



window.close()
