def x():
    y = int(input("Enter your number"))
    for i in range(1,11):
        print(y,"*",i,"=",y*i)
x()



def x(y):
    print(len(y))
y = input("Enter your string")
x(y)



def x(y):
    if y==y.upper():
       c = y.lower()
       print(c)
    elif y==y.lower():
        d = y.upper()
        print(d)
y = input("Enter your string")
x(y)




def x(n1,n2,n3):
        n = (n1+n2+n3)/3
        print(n)
n1 = int(input("Enter your first number"))
n2 = int(input("Enter your second number"))
n3 = int(input("Enter your third number"))
x(n1,n2,n3)



def x(n1,n2,n3):
    n = max(n1,n2,n3)
    print(f"The biggest number is {n}")
n1 = int(input("Enter your first number"))
n2 = int(input("Enter your second number"))
n3 = int(input("Enter your third number"))
x(n1,n2,n3)
