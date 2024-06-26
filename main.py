print("Hello")

import random
import string

# RandInt=random.randint(0,50)
# print(RandInt)
#
#
# RandFloat=random.uniform(0,50)
# print(RandFloat)

# stringMyString="bdgfugfeugfyyeygwu"
# StringRand=random.choice(stringMyString)


# x = int(input("Enter a string"))
# randomNum=random.randint(0,x)
# print(randomNum)

# x=str(input("Enter a string"))
# for i in range(5):
#     y = random.choice(x)
# for g in range(5):
#     print(y)


# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)


import string
x = int(input("Введіть довжину пароля"))

for i in range(x):
   a=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
   x=random.choice(a)
   print(x)