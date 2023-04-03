import Functions_File as ff
import PySimpleGUI as ps

ps.theme("DarkTeal2")

AddButton = ps.Button("Add")
Lable1= ps.Text("Enter a To-Do")
InputText1= ps.InputText(tooltip="Enter your todo here",size=(45),key="IT1")

ListBox1= ps.Listbox(values=ff.get_todos(),enable_events=True,size=(44,10),key="Lb1")
EditButton=ps.Button("Edit")
ExitButton=ps.Button("Exit")
window=ps.Window("To-Do Application",
                 layout=[[Lable1],[InputText1,AddButton],[ListBox1,EditButton],[ExitButton]],
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
            todos.append(values["IT1"]+'\n')
            ff.write_todos(todos)
            window["Lb1"].update(values=todos)

        case ps.WIN_CLOSED:
            break

        case 'Exit':
            break

        case 'Edit'|'edit':
            todo = values['Lb1'][0]
            new_todo = values["IT1"]
            todos = ff.get_todos()
            index=todos.index(todo)
            todos[index]=new_todo+'\n'
            ff.write_todos(todos)
            window['Lb1'].update(values=todos)

        case 'Lb1':
            window['IT1'].update(value=values["Lb1"][0])


window.close()
