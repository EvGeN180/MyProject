
numbers = [0, 0, 1, 4, 4, -6, -2, -6, 7]

for index in range(len(numbers)):
    if numbers[index] < 0:
        x = numbers[index]
        y = index


if y != -1:
    print(f"last negative element: {x}")
    print(f"its index: {y}")
else:
    print("Error")
