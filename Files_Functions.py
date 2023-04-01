'''Write a program that opens up a text file and write content to it. Also it should append content if
content already there'''
'''open in write mode adds a new file but open in read mode reads existing file , which means the file should 
be there before open opens the file in read mode'''
'''Write(Takes string as an input and write string to the file) vs writelines(Takes list as an input and write content of 
list in the file)'''
New_content = input("Enter what do you want to add to the file")+"\n"
File_content = []

file1=open("Files/Test.txt",'r')
File_content = file1.readlines()
file1.close()
File_content.append(New_content)
file1 = open("Files/Test.txt",'w')

file1.writelines(File_content)
file1.close()
file1=open("Files/Test.txt",'r')
print(list(file1))

#Create 3 new files and put content in respective file like this
# I love apple, I love cherry, I love Chocolates

list3= ['I love apple','I love cherry','I love chocolates']

for i,item in enumerate(list3):
    file1=open(f"Files/{i+1}.txt",'w')
    file1.write(item)

Temp_List = ['10','12','14']
Temp_List = [str(item)+'\n' for item in Temp_List]
file1= open("Files/temperatures.txt",'w')
file1.writelines(Temp_List)
file1.close()