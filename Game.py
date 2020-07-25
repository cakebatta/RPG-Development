from Monster import *

cactopi = Monster(6, 50, 1, 10, 'Cactopi', ['Quicksilver Sash, Bow of 1000 Needles, Potion, Swiftness Boots, Nothing'], 100, 'Is that a LIVING cactus?!')

dragon = Monster(10, 200, 7, 3, 'Great Dragon', ['Drake Talon Claw, Dragonscale Cloak, Dragonflame Shield, Emrald, Ruby'], 250, 'You think you can see me and live?')


peasant = Monster(2, 60, 3, 3, 'Lowly Peasant', ["Wedding Ring, Grocery Receipt, Daughter's Father's day letter"], 5, 'Please, I have a family!')


print(peasant.combat_message())

##Issue: print message is returning "None"
