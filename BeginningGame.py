import os
import time
from Base.py import myCharacter, create_NAME
from lvlUP import LevelUP
from Classes import Mage, Warrior, Hunter

print('Welcome to a text based RPG game,')
print('This game is still in development.')
time.sleep(3)
clear = lambda: os.system('cls')
clear()
create_NAME()
time.sleep(2)
