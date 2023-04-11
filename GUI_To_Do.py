import Functions_File as ff
import PySimpleGUI as ps
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as f:
        pass

ps.theme("DarkTeal2")
clockLable = ps.Text("",key="Time")
AddButton = ps.Button(image_source="D:\PythonProjects\Files\Add_Buttons.png",key='Add',image_size=(50,20),tooltip="Press to add To-Do",mouseover_colors="Blue")
Lable1= ps.Text("Enter a To-Do")
InputText1= ps.InputText(tooltip="Enter your todo here",size=(45),key="IT1")

ListBox1= ps.Listbox(values=ff.get_todos('todos.txt'),enable_events=True,size=(44,10),key="Lb1")
EditButton=ps.Button("Edit",key='Edit')
ExitButton=ps.Button(image_source="D:\PythonProjects\Files\Exit_Button.png",image_size=(100,30), tooltip="Press to exit",key='Exit')
DeleteButton=ps.Button(image_source="D:\PythonProjects\Files\Delete_Button.png",image_size=(100,30),tooltip="Press to delete To-Do",key='Delete')

Buttons_List=[[DeleteButton]]
Buttons_List1=[[ExitButton]]


window=ps.Window("To-Do Application",
                 layout=[[clockLable],[Lable1],[InputText1,AddButton],[ListBox1,EditButton],[ps.Column([[DeleteButton]]),ps.Column([[ExitButton]])]],
                 size=(800,600),
                 font=("Helvetica",20))


# window.read gives us two values, one is what event happened and what were the associated values
# so if we press add button , add is an event which happened, the data written in the text box
# becomes the values. Values are returned in Dictionary format (Key:value) pair
while True:
    event, values = window.read(timeout=200)
    # timeout waits for 200 ms for the user's event. After the end of timeout, event will contain '__TIMEOUT__' and the following code of lines
    # will be executed till the match statement, as there is no case in the match related to timeout so the screen continue to show till user
    # does another event like Add, Delete or edir or exit
    window["Time"].update(value=time.strftime(format("%d %m %y %H:%M:%S")))
    print(event)
    print(values)
    match event:    
        case 'Add'|'add':
            if(len(values['IT1'])!=0):
                todos=ff.get_todos('todos.txt')
                todos.append(values["IT1"].strip()+'\n')
                ff.write_todos(todos)
                window["Lb1"].update(values=todos)
                window["IT1"].update(value="")

            else:
                ps.popup("Todo cannot be Blank",font=("Helvetica",20))

        case ps.WIN_CLOSED:
            break

        case 'Exit':
            break

        case 'Edit'|'edit':
            try:
                todo = values['Lb1'][0]
                new_todo = values["IT1"]
                todos = ff.get_todos('todos.txt')
                index=todos.index(todo)
                todos[index]=new_todo+'\n'
                ff.write_todos(todos)
                window['Lb1'].update(values=todos)
                window["IT1"].update(value="")
            except(IndexError):
                ps.popup("Please select what you want to edit first", font=("Helvetica",20))

        case 'Lb1':
            try:
                window['IT1'].update(value=values["Lb1"][0].strip())
            except(IndexError):
                ps.popup("There is no item in the list", font=("Helvetica",20))

        case 'Delete':
            try:
                todos=ff.get_todos('todos.txt')
                index =todos.index(values['Lb1'][0])
                print(values['Lb1'][0])
                todos.pop(index)
                ff.write_todos(todos)
                window['Lb1'].update(values=todos)
                window["IT1"].update(value="")
            except(IndexError):
                ps.popup("Please select what you want to delete first", font=("Helvetica",20))

window.close()
