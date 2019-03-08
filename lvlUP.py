from Base.py import myCharacter


MAX_EXP = 1000
def LVLUP():
    if(myCharacter.Default_exp == MAX_EXP):
    myCharacter.Current_LvL = myCharacter.Current_LvL ++
else:
    print()

    if(myCharacter.isAlive == False):
        myCharacter.Current_LvL = 1
        myCharacter.Default_exp = 0.0
    else:
