class Math:
    @staticmethod
    def plus(a,b):
        return a + b

    @staticmethod
    def minus(a,b):
        return a - b

    @staticmethod
    def mnozhennya(a,b):
        return a * b

    @staticmethod
    def dilennya(a,b):
        if b!=0:
            return a / b
        else:
            return ZeroDivisionError

try:            
    num1 = float(input("Enter 1 number "))
    num2 = float(input("Enter 2 number "))

    print(f"a + b = {Math.plus(num1,num2)}")
    print(f"a + b = {Math.minus(num1,num2)}")
    print(f"a + b = {Math.mnozhennya(num1,num2)}")
    print(f"a + b = {Math.dilennya(num1,num2)}")

except ValueError:
    print("ERROR,incorrect input")