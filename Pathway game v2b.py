# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:31:00 2020

@author: dougb
"""

import time

start = int(time.time())

import random

print("Welcome to the game, please type your player name.")
playerName = input()

#below are all the scripts for the various encounters
frontDoor = "This is the front door of the manor.  Type 'bell' to ring the bell."
servantDoor = "This is the servant's entrance.  Type 'knock' to to get someone's attention"
stablePath = "This is the path to the stables.  Type 'walk' if you wish to proceed."
butler1 = "Hello I'm Frederick, the head butler.  Please wait here while I summon the master.\n"
housekeeper = "I'm Margaret, the head housekeeper.  It's about time you got here.  Are you ready to get to work.\nType 'yes' to get to work"
butler2 = "I'm Frederick, the head butler.  Hurry up then, will you come this way?\nType 'yes' to follow."
groudskeeper = "The trouble is down here.  Will you follow me?\nType 'yes' to follow."
youngMaster = "The 'issue' is down this way.  Will you follow me.\nType 'yes' to follow Reggie."
parlor = str(playerName) + "!  Well hello old chap!  Come join me for a drink in the parlor.\n"
diningRoom = str(playerName) + "!  So good to see you again.  You're a bit late old boy, but come join the others in the dining room.\n"
library = "Thank goodness you're here detective.  This way, the first body is in the library.\n"
kitchen = "Come along now to the kitchen.\nGet to work on all these dirty dishes.  We've got guests coming tonight.\n"
guestRoom = "Come along to the south wing.\nWe've got guests coming tonight and you need to get all these rooms ready.\n"
garden = "Follow me to the garden.  We're having a devil of a time with the irrigation system.\n"
pumpHouse = "Follow me to the pump house.  The irrigation pump has gone out on us.\n"
pond = "Come down to the pond, detective.  That's where we found the second body.\n"



def piedmont():
    
    def entrance(): 
        print("\nYou've arrived at Piedmont Manor, " + str(playerName) + ".\nWould you like to enter the grounds?\nType 'enter' to begin.")
        if input() == "enter":
            time.sleep(2)
            portal()
        else: ender()
    #this is the first greeting of the game
    
    def portal():
        portalChoice = random.randint(1,3)
        if portalChoice == 1:
            frontDoorGreet()
        if portalChoice == 2:
            servantDoorGreet()
        if portalChoice == 3:
            stablePathGreet()
    # this chooses which entrance the player takes
            
    def frontDoorGreet():
        print(frontDoor)
        if input() == "bell":
            time.sleep(3)
            print(butler1)
            time.sleep(4)
            print("Lord Piedmont, " + str(playerName) + " is here to see you.\n")
            time.sleep(1)
            room1()
        else: ender()
    #greeting by the butler at the front door.  Sleeps while butler fetches master.
            
    def servantDoorGreet():       
        print(servantDoor)
        if input() == "knock":
            time.sleep(3)
            print("Hang on! I'm coming!\n")
            time.sleep(5)
            servant()
        else: ender()
    #greeting by housekeeper or butler at servant's entrance
            
    def stablePathGreet():
            print (stablePath)
            if input() == "walk":
                time.sleep(4)
                room3()
            else: ender()
    #greeting by groundskeeper or young master at the stables.
    
    def room1():
        roomChoice1 = random.randint(1,3)
        if roomChoice1 == 1:
            print(parlor)
            time.sleep(5)
        if roomChoice1 == 2:
            print(diningRoom)
            time.sleep(5)
        if roomChoice1 == 3:
            print(library)
            time.sleep(5)
    #greeting by lord piedmont and chooses the room you go to.
    
    def servant():
        def room2():
            roomChoice2 = random.randint(1,3)
            if roomChoice2 == 1:
                print(kitchen)
                time.sleep(5)
            if roomChoice2 == 2:
                print(guestRoom)
                time.sleep(5)
            if roomChoice2 == 3:
                print(library)
                time.sleep(5)

        greeter2 = random.randint(1,2)
        if greeter2 == 1:
            print(housekeeper)
            if input() == "yes":
                time.sleep(1)
                room2()
            else: ender()
        if greeter2 == 2:
            print(butler2)
            if input() == "yes":
                time.sleep(1)
                room2()
            else: ender()
        
    #greeting by either butler or housekeeper and direction to your task

    def room3():
        greeter3 = random.randint(1,2)
        roomChoice3 = random.randint(1,3)
        if greeter3 == 1:
            print("Hello, I'm Franklin the groundskeeper.")
        if greeter3 == 2:
            print("I'm Reggie Piedmont, Lord Piedmont's son.")
        if roomChoice3 == 1:
            print(garden)
            time.sleep(5)
        if roomChoice3 == 2:
            print(pumpHouse)
            time.sleep(5)
        if roomChoice3 == 3:
            print(pond)
            time.sleep(5)
    #greeting by either groundskeeper or young master Reggie and direction to your task
    
    def ender():
        print("Thanks for playing.")
     
    def finish():
        finish = int(time.time())
        print("You've been playing this game for " + (str(finish - start)) + " seconds.\nWould you like to play again?")
        if input() == "yes":
            time.sleep(2)
            piedmont()
        else:
            print("Thanks for playing.")

    entrance()
    
    finish()

piedmont()


