list = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]
p = 0
n = 0

for numbers in list:
    if numbers > 0:
        p += 1
    elif numbers < 0:
        n += 1

print("Positive numbers:", p , "Negative numbers:", n)