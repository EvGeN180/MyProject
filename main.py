import random

# ex1


def func():
    myList=[]
    for i in range(10):
        myList.append(random.randint(-100,100))
    print(f"List:{myList}")
    return myList

def funct():
    rand = func()
    rand.sort()
    max_n=rand[9]
    print(f"Max number {max_n}")
    min_n=rand[0]
    print(f"Min number {min_n}")
funct()


# ex2

def computer():
    gamelist=['камінь','ножиці','папір']
    computer_input = random.choice(gamelist)
    return computer_input

def user():
    user_input=input("Виберіть камінь\ножиці\папір ")
    return user_input.lower()

def game():
    gamelist=['камінь','ножиці','папір']
    computer_input = computer()
    user_input = user()
    if user_input == gamelist[0] and computer_input == gamelist[1] or user_input == gamelist[1] and computer_input == gamelist[2] or user_input == gamelist[2] and computer_input == gamelist[0]:
        print("Ви перемогли!")
    if user_input == gamelist[1] and computer_input == gamelist[0] or user_input == gamelist[2] and computer_input == gamelist[1] or user_input == gamelist[0] and computer_input == gamelist[2]:
        print("Переміг комп'ютер!")
    if user_input == gamelist[0] and computer_input == gamelist[0] or user_input == gamelist[1] and computer_input == gamelist[1] or user_input == gamelist[2] and computer_input == gamelist[2]:
        print("Нічия!")
    print("Ваш вибір -",user_input)
    print("Вибір комп'ютера -",computer_input)

game()