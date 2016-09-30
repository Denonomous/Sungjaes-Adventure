import string

def capitalize(word):
    if " of " in word:
        word = string.capwords(word)
        word[word.find("of")].lower()
        return word
    else:
        string.capwords(word)
        return word

def getHealth(mob):
    health = 90 + mob['strength'] * 10
    for item in mob['equipped']:
        if mob['inventory']:
            if mob['equipped'][item]  != '':
                health += items['equippable'][mob['equipped'][item]][1]
    return health

def getArmor(mob):
    armor = 0
    for item in mob['equipped']:
        if mob['equipped']:
            if mob['equipped'][item]  != '':
                armor += items['equippable'][mob['equipped'][item]][2]
    return armor

def getAttack(mob):
    attack = 0
    for item in mob['equipped']:
        if mob['equipped']:
            if mob['equipped'][item]  != '':
                attack += int(round((items['equippable'][mob['equipped'][item]][3] * (0.9 + 0.1 * mob['strength']))))
    return attack

def getMagic(mob):
    magic = 0
    for item in mob['equipped']:
        if mob['equipped']:
            if mob['equipped'][item]  != '':
                magic += int(round((items['equippable'][mob['equipped'][item]][4] * (0.9 + 0.1 * mob['intellect']))))
    return magic

def getSpeed(mob):
    speed = 0
    for item in mob['equipped']:
        if mob['equipped']:
            if mob['equipped'][item]  != '':
                speed += int(round((items['equippable'][mob['equipped'][item]][5] * (0.9 + 0.1 * mob['agility']))))
    return speed

def openInventory(mob):
    print()
    mob['inventory'].sort()
    equipNum = 0
    invNum = 0
    for item in mob['equipped']:
        if mob['equipped'][item]  != '':
            equipNum += 1
            print(str(equipNum) + '. ' + mob['equipped'][item] + '(e)')
    print()
    for item in mob['inventory']:
        invNum += 1
        print(str(invNum) + '. ' + item)
    print()
    action('inventory')

def equip(mob, invNum):
    equipItem = mob['inventory'][int(invNum)]
    equipSlot = items['equippable'][equipItem][0]#Slot of item
    if mob['equipped'][equipSlot] == '': #If slot empty
        print(equipItem, "has been equipped.")
        print()
        mob['equipped'][equipSlot] = equipItem #Equip item
        del (equipItem) #Remove item from inventory
        
    else:
        prevEquipped = mob['equipped'][equipSlot]
        print(prevEquipped, "has been unequipped.")
        print(equipItem, "has been equipped.")
        print()
        mob['inventory'].append(prevEquipped) #Move equipped item back to inventory
        mob['equipped'][equipSlot] = equipItem #Equip item
        del (mob['inventory'][int(invNum)]) #Remove equipped item from inventory
        
def action(event = False):
    if event == False:
        action = input('What do you do? \n\
Open inventory (i)')
        while action != 'i':
            print('That is not a valid option.')
            print()
            action = input('What do you do? \n\
Open inventory (i)')
            print()
        if action == 'i':
            openInventory(sungjae)
        #elif: ...
    if event == 'inventory':
        action = input('Close inventory (i) \n\
Equip (e)')
        while action != 'i' and action != 'e':
            print('That is not a valid option.')
            print()
            action = input('Close inventory (i) \n\
Equip (e)')
        if action == 'i':
            print()
        elif action == 'e':
            invNum = input('Equip what?')
            while invNum.isdigit() == False or len(invNum) > 1 or int(invNum) > len(sungjae['inventory']) or int(invNum) < 0:
                print('That is not a valid option.')
                print()
                invNum = input('Equip what?')
            print()
            invNum = int(invNum)
            invNum -= 1
            equip(sungjae, invNum)

        
    
sungjae = {
    'health' : 0,
    'armor' : 0,
    'attack' : 0,
    'magic' : 0,
    'speed' : 0,
    'strength' : 1,
    'intellect' : 1,
    'agility' : 1,
    'luck' : 1,
    'inventory' : ['wooden battlestaff', 'iron spear'],
    'equipped' : {'onhand' : 'rusty sword',
                  'offhand' : 'wooden shield',
                  'head' : '',
                  'body' : 'bronze armor',
                  'hands' : '',
                  'boots' : '',
                  'rings' :  ''
                  }
}

items = {
                    #[slot[0], health[1], armor[2], attack[3], magic[4], speed[5], strength[6], intellect[7], agility[8], luck[9]]
    'equippable' : {'rusty sword' : ['onhand', 0, 0, 7, 0, 0, 0, 0, 0, 0],
                    'iron spear' : ['onhand', 0, 0, 15, 0, 0, 0, 0, 0, 0],
                    'wooden staff' : ['onhand', 0, 0, 4, 8, 0, 0, 0, 0, 0],
                    'wooden battlestaff' : ['onhand', 0, 0, 8, 7, 0, 0, 0, 0, 0],
                    'wooden shield' : ['offhand', 0, 5, 0, 0, 0, 0, 0, 0, 0],
                    'bronze helm' : ['head', 0, 8, 0, 0, 0, 0, 0, 0, 0],
                    'iron helm' : ['head', 0, 15, 0, 0, 0, 0, 0, 0, 0],
                    'platinum helm' : ['head', 0, 30, 0, 0, 0, 0, 0, 0, 0],
                    'mythril helm' : ['head', 0, 50, 0, 0, 0, 0, 0, 0, 0],
                    'peach\'s hair' : ['head', 0, 80, 0, 0, 0, 0, 0, 0, 2],
                    'bronze armor' : ['body', 0, 20, 0, 0, 0, 0, 0, 0, 0],
                    'iron armor' : ['body', 0, 40, 0, 0, 0, 0, 0, 0, 0],
                    'platinum armor' : ['body', 0, 60, 0, 0, 0, 0, 0, 0, 0],
                    'mythril armor' : ['body', 0, 80, 0, 0, 0, 0, 0, 0, 0],
                    'jacket of jacobus' : ['body', 0, 120, 0, 0, 0, 0, 3, 0, 0],
                    'leather gloves' : ['hands', 0, 3, 0, 0, 1, 0, 0, 0, 0],
                    'thief gloves' : ['hands', 0, 5, 2, 0, 5, 0, 0, 0, 0]
                    }
}
def updateStats(mob):
    mob['health'] = getHealth(mob) #Set current stats
    mob['armor'] = getArmor(mob)
    mob['attack'] = getAttack(mob)
    mob['magic'] = getMagic(mob)
    mob['speed'] = getSpeed(mob)


while True:
    updateStats(sungjae)
    print('Health:' , sungjae['health']) #Test for stats
    print('Armor:', sungjae['armor'])
    print('Attack:', sungjae['attack'])
    print('Magic:', sungjae['magic'])
    print('Speed:', sungjae['speed'])
    print('______________________')
    action()
