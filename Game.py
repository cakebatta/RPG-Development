from Monster import *

cactopi = Monster()
    level = 6
    health = 50
    armor = 1
    speed = 10
    name = 'Cactopi'
    loot = ['Quicksilver Sash, Bow of 1000 Needles, Potion, Swiftness Boots, Nothing']
    xp = 100
    cm = 'Is that a LIVING cactus?!'

dragon = Monster(10, 200, 7, 3, 'Great Dragon', ['Drake Talon Claw, Dragonscale Cloak, Dragonflame Shield, Emrald, Ruby'], 250, 'You think you can see me and live?')


peasant = Monster(2, 60, 3, 3, 'Lowly Peasant', ["Wedding Ring, Grocery Receipt, Daughter's Father's day letter"], 5, 'Please, I have a family!')


print(peasant.combat_message())

##Current error: 

##Traceback (most recent call last):
  ##File "C:/Users/BB BOBBY/PycharmProjects/puzzlegame/venv/Game.py", line 19, in <module>
    ##print(peasant.combat_message())
  ##File "C:\Users\BB BOBBY\PycharmProjects\puzzlegame\venv\Monster.py", line 13, in combat_message
    ##print(Monster.cm)
##AttributeError: type object 'Monster' has no attribute 'cm'
