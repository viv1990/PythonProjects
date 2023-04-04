import Functions_File as ff
import PySimpleGUI as ps

ps.theme("DarkTeal2")

AddButton = ps.Button("Add")
Lable1= ps.Text("Enter a To-Do")
InputText1= ps.InputText(tooltip="Enter your todo here",size=(45),key="IT1",do_not_clear=False)

ListBox1= ps.Listbox(values=ff.get_todos(),enable_events=True,size=(44,10),key="Lb1")
EditButton=ps.Button("Edit")
ExitButton=ps.Button("Exit")
DeleteButton=ps.Button("Delete")
window=ps.Window("To-Do Application",
                 layout=[[Lable1],[InputText1,AddButton],[ListBox1,EditButton],[DeleteButton],[ExitButton]],
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
            if(len(values['IT1'])!=0):
                todos=ff.get_todos()
                todos.append(values["IT1"].strip()+'\n')
                ff.write_todos(todos)
                window["Lb1"].update(values=todos)

            else:
                ps.popup("Todo cannot be Blank")

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
            window['IT1'].update(value=values["Lb1"][0].strip())

        case 'Delete':
            todos=ff.get_todos()
            index =todos.index(values['Lb1'][0])
            print(values['Lb1'][0])
            todos.pop(index)
            ff.write_todos(todos)
            window['Lb1'].update(values=todos)

window.close()
