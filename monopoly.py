import random
import time
class Player:
    flag = 0
    bought = 0
    one_n_half = 0
    def __init__(self,name,figure,lvl,balance):
        self.name = name
        self.figure = figure
        self.lvl = lvl
        self.balance = balance
        self.place = 0

    def dice(self,a):       #roll a dice
        self.place = self.place+a
       

    def check_balance(self):   
        print( self.balance)
    
    def bonus_cell(self):
        print("Congratulations! You've just earned 100$")
        self.balance =  self.balance + 100

    def empty_cell(self):
        print("You're on empty one")

    def skip_cell(self):
        print("Ohh no... You're in trouble. Skip next turn")
        self.flag = 1 

    def factory_cell(self):
        a = input("You have a choice. Buy that factory for 10$ or not: ")
        if a.lower() == "yes" :
            print("You've successfuly bought it!")
            self.bought = 1
            time.sleep(0.10)
            self.balance -= 10
            b = input("Do you want to check your balance? ")
            if b.lower() == "yes":
                time.sleep(0.10)
                print(f"Your balance is {self.balance}$")
        else:
            print("Okay!")
            self.bought = 0

    def secret_cell(self):
        a = [1,2,3,4,5]
        chance = random.choice(a)
        print("Wow! A secret cell. You're a lucky man! Let's see what you got to do.")
        time.sleep(1)
        if chance == 1:
            print("Oops, your luck is against you, you must pay 50$ ")
            self.balance -= 50
            b = input("Do you want to check your balance? ")
            if b.lower() == "yes":
                time.sleep(0.10)
                print(f"Your balance is {self.balance}$")
        elif chance == 2:
            print("Wow! You just won a 50$")
            self.balance += 50
            b = input("Do you want to check your balance? ")
            if b.lower() == "yes":
                time.sleep(0.10)
                print(f"Your balance is {self.balance}$")
        elif chance == 3:    #should ask about it 
            print("Give a 1/5 of your money to a person with less of them ")
            self.one_n_half = 1
        elif chance == 4:
            print("Skip next turn")
            self.flag =1
        else:
            print("There is nothing")


    def house_cell(self):
        a = input("You have a choice. Buy that house for 10$ or not: ")
        if a.lower() == "yes" :
            print("You've successfuly bought it!")
            self.bought = 1
            time.sleep(0.10)
            self.balance -= 10
            b = input("Do you want to check your balance? ")
            if b.lower() == "yes":
                time.sleep(0.10)
                print(f"Your balance is {self.balance}$")
        else:
            print("Okay!")
            self.bought = 0
        
    
