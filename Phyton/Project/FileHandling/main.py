from pathlib import Path
def createFile():
    try:
        name=input("Please tell your file name:- ")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data=input("What you want to write:- ")
                fs.write(data)
            print("File created successfully")
        else:
            print("Error file name already exist")
    except Exception as err:
        print(f"An error occured as{err}")
            
def readFile():
    try:
        name=input("Please tell your file name: ")
        path=Path(name)
        if path.exists():
            with open(path,"r") as fs:
                print(fs.read())
        else:
            print("sorry file does not exists")
    except Exception as err:
        print("An error occured as ",err)



def updateFile():
    try:
        name= input("Enter the name of the file: ")
        path=Path(name)
        if path.exists():
            print("Operation")
            print("1.Renaming the file: ")
            print("2.Appending the content: ")
            print("3.OverWriting the file : ")
            a=int(input("Enter your response: "))
            if a==1:
                newName=input("Tell your new file name: ")
                new_path=Path(newName)
                
                if not new_path.exists():
                    path.rename(new_path)
                    print("Rename successfull")
                else:
                    print("File name already exists")
            elif a==2:
                with open(path,"a")as fs:
                    data=input("Enter the data to append: ")
                    fs.write(data)
            elif a==3:
                with open(path,"w")as fs:
                    data=input("Enter the data to append: ")
                    fs.write(data)
            else:
                print("Invalid respose")
        else:
            print("File does not exists")
    except Exception as err:
        print("An error occured as ",err)




def deleteFile():
    name=input("Enter file name: ")
    path=Path(name)
    if path.exists():
        path.unlink()
        print("File deleted successfully")
    else:
        print("File does not exists")






print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

a=int(input("\nTell your response:- "))

if a==1:
    createFile()

elif a==2:
    readFile()

elif a==3:
    updateFile()

elif a==4:
    deleteFile()
else:
    print("Invalid response")



