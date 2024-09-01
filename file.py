import os.path

while True:
    print("1-add to file,2-open file ,3-delete file,4-create new file")
    userInput = int(input("Enter number "))
    if userInput == 1:
        add = input("Enter string,which you want to add ")
        with open("tasks.txt","a") as file:
            file.write(add)
    elif userInput == 2:
        if os.path.exists("tasks.txt"):
            with open("tasks.txt",'r') as file:
                print(file.read())
        else:
            print("Error,file is not finded")
    elif userInput == 3:
        if os.path.exists("tasks.txt"):
            os.remove("tasks.txt")
        else:
            print("Error,this file is not exist")
    elif userInput == 4:
            new = input("Enter something into new file ")
            with open("tasks.txt",'w') as file:
                file.write(new)

                

