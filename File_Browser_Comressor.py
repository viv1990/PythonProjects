import PySimpleGUI as ps
import zipfile_function

ps.theme("Blue Momo")
Browse = ps.FilesBrowse("Browse")
DestFolder = ps.FolderBrowse("Choose")
Compress = ps.Button("Compress")
lable1 = ps.Text("Enter files to compress")
lable2 = ps.Text("Enter Destination")
InputBox1 = ps.InputText(tooltip="File Log",key='FL',do_not_clear=False)
InputBox2 = ps.InputText(tooltip="Destination File Log",key='DF', do_not_clear=False)
OutputLabel = ps.Text(key='Output')

layout = [[lable1],[InputBox1,Browse],[lable2],[InputBox2,DestFolder],[Compress]]


window = ps.Window("File Compressor",layout=layout)
list1=[]
while True:
    event, values = window.read()
    print(values)
    if event =='Compress':
        filepaths = values["Browse"].split(';')
        print(filepaths)
        folder=values['DF']
        zipfile_function.make_zip(filepaths,folder)
        window['Output'].update("Compression Completed")

    if event==ps.WIN_CLOSED:
        break


window.close()