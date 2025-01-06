import random

number = random.randint(1,10)

for i in range(1,10):
 mynum = int(input())
 if number > mynum:
    print ("Введенный число больше ")
 elif number < mynum:
    print ("Введенный число меньше")
 elif number == mynum:
  print ("Вы нашли число Поздравляю")
  break