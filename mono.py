from monopoly import  Player
import random
import time
def sell():
    if James_prop:
        businesses = input("You have a choice, sell something and make some money or not. Do you want to sell something? ")
        print(f'There are your available propperties {James_prop}')
        if businesses.lower() == 'yes':
            whom = input("""Now you need to choose whom you want to sell it: 
                                        Robert
                                        Mary
                                        Jhon
                                        Jennifer
                                        William \n""") 
            what = input("What do you want to sell? ")
            if whom.lower() == 'robert':
                what = what.lower()
                James_prop.remove(what.capitalize())
                Robert_prop.append(what.capitalize())
                print(f"It's successfuly gone from you to {whom}")
                check = input("Do you want to check all your properties? ")
                if check.lower() == 'yes':
                    print(f'Here {James_prop}')
                else:
                    print('As you wish')
            else:
                print("See you next time")
    else:
        pass
def sell1():
    if Robert_prop:
        businesses = input("You have a choice, sell something and make some money or not. Do you want to sell something? ")
        print(f'There are your available propperties {Robert_prop}')
        if businesses.lower() == 'yes':
            whom = input("""Now you need to choose whom you want to sell it: 
                                        James
                                        Mary
                                        Jhon
                                        Jennifer
                                        William\n""") 
            what = input("What do you want to sell? ")
            if whom.lower() == 'james':
                what=what.lower()
                Robert_prop.remove(what.capitalize())
                James_prop.append(what.capitalize())
                print(f"It's successfuly gone from you to {whom}")
                check = input("Do you want to check all your properties? ")
                if check.lower() == 'yes':
                    print(f'Here {Robert_prop}')
                else:
                    print('As you wish')
            else:
                print("See you next time")
    else:
        pass
def half():
    if James.one_n_half ==1:

        Robert.balance += James.balance //5
        James.balance //=5
        James.one_n_half =0
        check = input("Do you want to see your balance? ")
        if check.lower() == 'yes':
            print(f'{James.balance}$')
        else:
            print('As you wish') 
def half1():
    if Robert.one_n_half ==1:

        James.balance += Robert.balance //5
        Robert.balance //=5
        Robert.one_n_half =0
        check = input("Do you want to see your balance? ")
        if check.lower() == 'yes':
            print(f'{Robert.balance}$')
        else:
            print('As you wish')

    
figures = list(['Hat','Car','Dog','Iron','Shoe','Ship'])
s = input("Hey, mate! Do you want to play the game?: ")
while s.lower() != 'no':
    lap = 0
    time.sleep(1)
    print("So, how I can see, you've decided to play. Okay! Let's start")
    time.sleep(1)
    James = Player("James",random.choice(figures),1,100)
    Robert = Player("Robert",random.choice(figures),5,100)
    Mary = Player("Mary",random.choice(figures),3,100)
    Jhon = Player("Jhon",random.choice(figures),9,100)
    Jennifer = Player("Jennifer",random.choice(figures),7,100)
    William = Player("William",random.choice(figures),2,100)
    print("You're all on cell #1")
    print(f"""Your balances are:
            James {James.balance}$
            Robert {Robert.balance}$
            Mary {Mary.balance}$
            Jhon {Jhon.balance}$
            Jennifer {Jennifer.balance}$
            William {William.balance}$
Spend your money wisely!
            """)
    time.sleep(4)
    print("Let's roll the dice and decide who will be the first")
    time.sleep(1.5)
    dice =random.randint(1,2)   #whos turn
    James_prop =[]
    Robert_prop = []
    while True:

        a = random.randint(1,6)        #what cell
        if dice == 1:
            print("So, James it's your turn! Roll the dice")
            time.sleep(1)
            James.dice(a)
            if James.place == 1:

                James.secret_cell()
                time.sleep(1)
                half()
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                
            elif James.place == 2:
                prop = 'Adidas'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)

                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
               
            elif James.place == 3:

                James.bonus_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                
            elif James.place == 4:
                prop = 'Nike'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                    
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 5:
                print('You must go back!')
                James.place =2
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                
                
            elif James.place == 6:
                prop = 'BMW'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 7:
                
                James.secret_cell()
                time.sleep(1)
                half()
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 8:
                James.empty_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 9:
                prop = 'Audi'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
            
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 10:
                James.bonus_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 11:
                prop = 'Puma'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")

                sell()
                

                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
            
            elif James.place == 12:
                James.skip_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                
            
            elif James.place == 13:
                James.empty_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 14:
                James.bonus_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 15:
                James.secret_cell()
                time.sleep(1)
                half()
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 16:
                prop = 'Google'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                sell()

                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 17:
                James.skip_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                


            elif James.place == 18:
                James.bonus_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
            
            elif James.place == 19:
                prop = 'Apple'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                
                sell()

                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 20:
                James.secret_cell()
                time.sleep(1)
                half()
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 21:
                James.skip_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2
                

            elif James.place == 22:
                James.empty_cell()
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 23:
                prop = 'Samsung'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 24:
                print('You must go back!')
                James.place =21
                time.sleep(1)
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 25:
                James.secret_cell()
                time.sleep(1)
                half()
                sell()
                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place == 26:
                prop = 'Nokia'
                if prop  not in James_prop and prop not in Robert_prop: 
                    James.factory_cell()
                
                elif prop in Robert_prop:
                    print("That's not yours! You must pay!")
                    James.balance -=5
                    Robert.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {James.balance}")
                    else:
                        print("Maybe later...")
                elif prop in James_prop:
                    print("It's already here")
                
                if James.bought ==1:
                    
                    James_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(James_prop)
                else:
                    print("As you wish")
                sell()

                if Robert.flag ==1:
                    dice = 1
                    Robert.flag =0
                elif Robert.flag ==0:
                    dice = 2

            elif James.place >= 27:
                lap +=1 
                print(f"This was {lap} James' lap")
                James.place = 0



        elif dice == 2:
            print("So, Robert it's your turn! Roll the dice")
            time.sleep(1)
            Robert.dice(a)
            if Robert.place == 1:
                Robert.secret_cell()
                time.sleep(1)
                half1()
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                
            elif Robert.place == 2:
                prop = 'Adidas'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)

                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
               
            elif Robert.place == 3:
                Robert.bonus_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                
            elif Robert.place == 4:
                prop = 'Nike'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                
            elif Robert.place == 5:
                print('You must go back!')
                Robert.place =2
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                
                
            elif Robert.place == 6:
                prop = 'BMW'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)

                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()

                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 7:
                Robert.secret_cell()
                time.sleep(1)
                half1()
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 8:
                Robert.empty_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 9:
                prop = 'Audi'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()

                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 10:
                Robert.bonus_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 11:
                prop = 'Puma'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")

                sell1()

                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
            
            elif Robert.place == 12:
                Robert.skip_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                
            
            elif Robert.place == 13:
                Robert.empty_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 14:
                Robert.bonus_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 15:
                Robert.secret_cell()
                time.sleep(1)
                half1()
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 16:
                prop = 'Google'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)

                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()

                time.sleep(1)
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 17:
                Robert.skip_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                

            elif Robert.place == 18:
                Robert.bonus_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 19:
                prop = 'Apple'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()

                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 20:
                Robert.secret_cell()
                time.sleep(1)
                half1()
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 21:
                Robert.skip_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1
                

            elif Robert.place == 22:
                Robert.empty_cell()
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 23:
                prop = 'Samsung'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 24:
                print('You must go back!')
                Robert.place =21
                time.sleep(1)
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 25:
                Robert.secret_cell()
                time.sleep(1)
                half1()
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place == 26:
                prop = 'Nokia'
                if prop  not in Robert_prop and prop not in James_prop: 
                    Robert.factory_cell()
                
                elif prop in James_prop:
                    print("That's not yours! You must pay!")
                    Robert.balance -=5
                    James.balance +=5
                    pay = input("Do you want to check your balance after that? ")
                    if pay.lower() == 'yes':
                        print(f"Here it is {Robert.balance}")
                    else:
                        print("Maybe later...")
                elif prop in Robert_prop:
                    print("It's already here")
                
                if Robert.bought ==1:
                    Robert_prop.append(prop)
                check = input("Do you want to check all yours properties? ")
                if check.lower() == "yes":
                    print(Robert_prop)
                else:
                    print("As you wish")
                sell1()
                if James.flag ==1:
                    dice = 2
                    James.flag =0
                elif James.flag ==0:
                    dice = 1

            elif Robert.place >= 27:
                lap +=1 
                print(f"This was {lap} Robert's lap")
                Robert.place =0

        if James.balance >=10000 or Robert.balance >=10000:
            break

        
  
    time.sleep(1)
    s = input("Do you want to paly it again? ")
