import Classes
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
        print('your new name is ', format(myCharacter.Default_NAME))
    else:
        # create battle function to continue !
        print('Hello ', format(myCharacter.Default_Name))
#need to add more stuff to this to make it more.. appealing to me..
def pick_Class():
    print('Hello ', format(create_NAME.getting_Name))
    print('Now you need to pick a class: ')
    print('*M* - Mage')
    print('*W* - Warrior')
    print('*H* - Hunter')
    getting_CLASS = input('What is your class: ').upper()
    if(getting_CLASS = 'M'):
        print('You have chosen to be a MAGE')
        myCharacter.Default_class = Classes.Mage
    elif(getting_CLASS = 'W'):
        print('you have chosen to be a WARRIOR')
        myCharacter.Default_class = Classes.Warrior
    elif(getting_CLASS = 'H'):
        print('You have chosen to be a Hunter')
        myCharacter.Default_class = Classes.Hunter
    else:
        print('There seems to be a error, now quiting')
