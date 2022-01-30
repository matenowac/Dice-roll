#Rzut kośćmi
from random import randint
import time

x = 1
y = 6

again = True
dice1 = randint(x, y)
dice2 = randint(x, y)

while again:
    print("Rzucam...")
    time.sleep(1)
    print("Twój wynik: ", dice1, "i", dice2)
    repeat = input("Powtórzyć rzut? (t/n)")
    if repeat.lower() == "t":
        continue
    else:
        break