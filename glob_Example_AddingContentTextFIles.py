'''
In this example we used glob module to perform merging of all the text files data into a single file.
.glob is a function in glob module which takes input the folder where all files are there
*.txt filters all the text files , FileList variable is of type list as .glob returns a list
Next we use our file functions to open each file in the FileList and append the content to List1
Finally we wrote the content of List1 to an output text file
'''



import glob
FileList = glob.glob(r"Files\*.txt")
print(FileList)
List1 = []

for filepath in FileList:
    with open(filepath,'r') as FileObj:
        List1.append(FileObj.read())
print(List1)

with open("ContentFromFiles.txt",'w') as OutputFile:
    OutputFile.writelines(List1)



