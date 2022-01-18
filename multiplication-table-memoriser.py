import random
import time
from time import sleep
while True:

    a = (input("Enter the first Parameter: "))
    b = (input("Enter the second Parameter: "))
    c = (input("Enter the third Parameter: "))
    d = (input("Enter the fourth Parameter: "))
    if a == "q" or a == "quit" or a == "exit":
        break
    if b == "q" or b == "quit" or b == "exit":
        break
    start = True
    while start:

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        sleep(0.150)
        num1 = random.randint(a, b)
        num2 = random.randint(c, d)
        checknum = (input(f"{num1} x {num2} = ??\n"))
        if checknum == 'q' or checknum == 'quit' or checknum == 'exit':
            start = False
        checknum = int(checknum)
        if checknum == num1*num2:
            sleep(0.5)
            print("Well done!! You're answer is correct")
        elif checknum != num1*num2:
            sleep(0.5)
            print(
                f"Oops, you're answer is wrong.\nCorrect answer is {num1*num2}")
