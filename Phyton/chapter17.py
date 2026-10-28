# # File handling 
# # open("Hello.txt","x") usually x is not used to create file we can use a and w to create file as well
# file= open("Supermen.txt","w")
# data= input("What you want to write in your file")
# file.write(data)

file=open("chapter15.py","r")
print(file.read())

with open("Supermen.txt","a") as fs:
    fs.write(" "+"i want to see if its working or not")

