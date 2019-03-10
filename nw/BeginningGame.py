import os
import time
import Base
import Classes

def start_Game():
    print('Welcome to a text based RPG game,')
    print('This game is still in development.')
    time.sleep(3)
    #clear = lambda: os.system('cls')
    #clear()
    #this item needs work, do to not understanding shit
    create_NAME()
    time.sleep(2)
    pick_Class()
