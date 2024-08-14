def func():
    my_list = ['dwfd','1','2','yrh','7.8','ttt']
    element = input("Enter element  ")
    if element.lower().strip() in my_list:
        return element
    if element.lower().strip() not in my_list:
        raise ValueError("There is no this element is this list")
try:
    func()
except ValueError as message:
    print("Error!",message)




def function():
     my_list = ['dwfd','1','2','yrh','7.8','ttt']
     print(my_list)
     element = input("Enter element, which you want delete ")
     el = element.lower().strip()

     if el in my_list:
        my_list.remove(el)
        return my_list
     if el not in my_list:
        raise ValueError("There is no this element is this list,you cant delete it")
try:
    function()
except ValueError as m:
    print("ERROR",m)


def f():
    n = int(input("Enter pair number "))
    if n %2 == 0:
        return n
    if n%2 != 0:
        return ValueError("This number is not pair")
try:
    print(f())

except ValueError as message:
    print("ERROR",message)

