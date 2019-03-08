import os
import time
from Base import myCharacter
form Base import create_NAME
import Classes

def start_Game():
    print('Welcome to a text based RPG game,')
    print('This game is still in development.')
    time.sleep(3)
    clear = lambda: os.system('cls')
    clear()
    create_NAME()
    time.sleep(2)

    print('Hello ', format(myCharacter.Default_NAME))
    print('please select your class: ')
    print('*M* Mage')
    print('*W* Warrior')
    print('*H* Hunter')
    select_Class = input()
    if(select_Class == 'M'):
        myCharacter.Default_class == Classes.Mage
    elif(select_Class == 'W'):
        myCharacter.Default_class == Classes.Warrior
    elif(select_Class == 'H'):
        myCharacter.Default_class == Classes.Hunter
    else:
        print('There was a error, please type M,W,H to select a class')
        select_Class()

        print('You have selected: {}', format(myCharacter.Default_class))
        time.sleep(2.5)
        clear()
