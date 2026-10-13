import random as r
import time as t

while True:
    print("Welcome to RPS")

    t.sleep(3) # intermission

    desire = int(input("1 - rock, 2 - paper, 3 - blades "))
    ergaliodesiring = r.randint(1, 3)


    if desire==1:
      print("You desired Rock")
    elif desire==2:
     print("You desired Paper")
    else:
        print("You desired Blades")
    if ergaliodesiring==1:
       print("Computer desired Rock")
    elif ergaliodesiring==2:
        print("Computer desired Paper")
    else:
      print("Computer desired Blades")

    if desire==ergaliodesiring:
     print("Draw ½")
    elif (desire==1 and ergaliodesiring==2):
     print("Computer won")
    elif (desire==2 and ergaliodesiring==3):
     print("Computer won")
    elif (desire==3 and ergaliodesiring==1):
     print("Computer won")
    elif (desire==3 and ergaliodesiring==2):
     print("You won")
    elif (desire==2 and ergaliodesiring==1):
     print("You won")
    elif (desire==1 and ergaliodesiring==3):
     print("You won")