list = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

for index in range(len(list)):
    if list[index] < 0:
        print(f"negative number: {list[index]}")
        print(f" its index: {index}")
        break
else:
    print("Error")
