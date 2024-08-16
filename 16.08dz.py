with open("C:\\Users\\Malin\\OneDrive\\Робочий стіл\\info.txt", "w" ) as file1:
    file1.write(" Evgen Malyna,14 years old,lyceum21 ")
file1.close()
with open("C:\\Users\\Malin\\OneDrive\\Робочий стіл\\info.txt","r") as file1:
    print(file1.read())
file1.close()
