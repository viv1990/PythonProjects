import PySimpleGUI as ps
AddButton = ps.Button("Add")
Lable1= ps.Text("Enter a To-Do")
InputText1= ps.InputText(tooltip="Enter your todo here",expand_x=True)
window=ps.Window("To-Do Application",layout=[[Lable1],[InputText1,AddButton]],size=(720,200))
window.read()