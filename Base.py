from lvlUP.py import LVLUP
gg
class myCharacter():
    isAlive = True
    Current_LvL = 1
    Default_NAME = ''
    Defaut_health = 100.0
    Default_strength = 10.0
    Default_exp = 0.0
    Default_mana = 0.0
    Default_class = None

def create_NAME():
    if(myCharacter.Default_NAME == '' or None):
        print('you need a name for your character.')
        getting_Name = input('Your new name: ')
        myCharacter.Default_NAME = getting_Name
        print('your new name is {}', format(myCharacter.Default_NAME))
    else:
        # create battle function to continue !
        print('Hello ', format(myCharacter.Default_Name))
