import random
import math

class Item:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Weapon(Item):
    def __init__(self, name, range, damage, one_handed, effect):
        super().__init__(name)
        self.range = range
        self.damage = damage
        self.one_handed = one_handed
        self.effect = effect
    def getRange(self):
        return self.range
    def getDamage(self):
        return self.damage
    def setDamage(self,newDamage):
        self.damage = newDamage
    def getOneHanded(self):
        return self.one_handed
    def getHealing(self):
        return self.healing
    def getEffect(self):
        return self.effect

class Armor(Item):
    def __init__(self, name, weight, rating, base_rating):
        super().__init__(name)
        self.weight = weight
        self.rating = rating
        self.rating = rating
        self.base_rating = base_rating

    def getWeight(self):
        return self.weight
    def setWeight(self,newWeigth):
        self.weight = newWeigth
    def getRating(self):
        return self.rating
    def setRating(self, newRating):
        self.rating = newRating
    def getBaseRating(self):
        return self.base_rating
class Hero:

    def __init__(self, race, skill, name, main_weapon, off_weapon, armor: Armor, inventory, max_health, health, strength, intellect, charisma, effect, power):
        self.race = race
        self.skill = skill
        self.name = name
        self.main_weapon = main_weapon
        self.off_weapon = off_weapon
        self.armor = armor
        self.inventory = inventory
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.intellect = intellect
        self.charisma = charisma
        self.effect = effect
        self.power = power

    def getName(self):
        return self.name
    def getRace(self):
        return self.race
    def getSkill(self):
        return self.skill

    def getMaxHealth(self):
        return self.max_health
    def setMaxHealth(self,newMaxHealth):
        self.max_health = newMaxHealth


    def getHealth(self):
        return self.health
    def setHealth(self,newHealth):
        self.health = newHealth

    def getStrength(self):
        return self.strength
    def setStrength(self, newStrength):
        self.strength = newStrength

    def getIntellect(self):
        return self.intellect
    def setIntellect(self, newIntellect):
        self.intellect = newIntellect

    def getCharisma(self):
        return self.charisma
    def setCharisma(self, newCharisma):
        self.charisma = newCharisma


    def getMainWeapon(self):
        return self.main_weapon
    def setMainWeapon(self,newMainWeapon):
        self.main_weapon = newMainWeapon

    def getOffWeapon(self):
        return self.off_weapon
    def setOffWeapon(self,newOffWeapon):
        self.off_weapon = newOffWeapon

    def getArmor(self):
        return self.armor
    def setArmor(self,newArmor):
        self.armor = newArmor

    def listInventory(self):

       for x in range(len(self.inventory)):
            print()
            if type(self.inventory[x]) == Armor:
                print(f"Armor: {self.inventory[x].getName()} \n"
                      f"    Weight: {self.inventory[x].getWeight()} \n"
                      f"    Armor Rating: {self.inventory[x].getRating()}\n")
            elif type(self.inventory[x]) == Weapon:
                print(f'Weapon: {self.inventory[x].getName()} \n'
                      f'    Range: {self.inventory[x].getRange()} \n    Damage: {self.inventory[x].getDamage()} \n'
                      f'    One Handed: {self.inventory[x].getOneHanded()}\n'
                      f'    Effect: {self.inventory[x].getEffect()}\n')
    def getInventory(self):
        String = ""
        for x in range(len(self.inventory)):
            if type(self.inventory[x]) == Armor:
                String += f"{self.inventory[x].getName()} \n {self.inventory[x].getWeight()} \n {self.inventory[x].getRating()}"
            elif type(self.inventory[x]) == Weapon:
                String += f" {self.inventory[x].getName()} \n {self.inventory[x].getRange()} \n {self.inventory[x].getDamage()} \n {self.inventory[x].getOneHanded()}"
        return String
    def appendInventory(self):
        return self.inventory

    def getEffect(self):
        return self.effect
    def setEffect(self, newEffect):
        self.effect = newEffect
    def getPower(self):
        return self.power

def Effect(target, effect):
    if effect == "Armor":
        target.setEffect("Armor")
        target.getArmor().setRating((target.getArmor().getBaseRating() + 3))
        print("You conjure a thick layer of ice around your armor.")
    if effect == "Burning":
        if type(target) == Hero:
            target.setEffect("Burning")
        elif type(target) == Enemy:
            target.setEnemyEffect("Burning")
    if effect == "Heal":
        if type(target) == Hero:
            Character.setHealth((Character.getHealth() + random.randint(2,6)))
            if Character.getHealth() > Character.getMaxHealth():
                Character.setHealth(Character.getMaxHealth())
            print(f"You have healed yourself! CURRENT HEALTH - {Character.getHealth()}")
    if effect == "Lesser Heal":
        target.setEnemyHealth(target.getEnemyHealth() + random.randint(1,4))
        print(f"{target.getEnemyName()} Has been healed! ENEMYS CURRENT HEALTH {target.getEnemyHealth()}")
def effectTick(target):
    if type(target) == Hero:
        if target.getEffect() != [] and random.randint(1,5) == 5:
            target.getArmor().setRating(target.getArmor().getBaseRating())
            target.setEffect([])
            print("All active effects have faded")
        elif target.getEffect() != []:
            if target.getEffect() == "Burning":
                if target.getRace() == "solsil":
                    target.setHealth(target.getHealth() - 1)
                    print(f"{target.getName()} BURNED for 1 HP")
                else:
                    target.setHealth(target.getHealth() - 2)
                    print(f"{target.getName()} BURNED for 2 HP")
    elif type(target) == Enemy:
        if target == Sirus and Sirus.getEnemyEffect() == "Bind":
            if random.randint(1,4) == 4:
                print("The effects of the dagger have worn off.")
                Sirus.setEnemyArmor(Abyssal_Armor)
                Sirus.setEnemyEffect([])
        else:
            if target.getEnemyEffect() != [] and random.randint(1,5) == 5:
                target.getEnemyArmor().setRating(target.getEnemyArmor().getBaseRating())
                target.setEnemyEffect([])
                print(f"{target.getEnemyName()} has shrugged off all effects.")
            elif target.getEnemyEffect() != []:
                if target.getEnemyEffect() == "Burning":
                    if target.getEnemyRace() == "solsil":
                        target.setEnemyHealth(target.getHealth() - 1)
                        print(f"{target.getEnemyName()} BURNED for 1 HP")
                    else:
                        target.setEnemyHealth(target.getEnemyHealth() - 2)
                        print(f"{target.getEnemyName()} BURNED for 2 HP")

class Enemy:

    def __init__(self, race, skill, name, health, main_weapon, armor: Armor, effect):
        self.race = race
        self.skill = skill
        self.name = name
        self.health = health
        self.main_weapon = main_weapon
        self.armor = armor
        self.effect = effect

    def getEnemyArmor(self):
        return self.armor
    def setEnemyArmor(self,newArmor):
        self.armor = newArmor

    def getEnemyMainWeapon(self):
        return self.main_weapon
    def setEnemyMainWeapon(self,newMainWeapon):
        self.main_weapon = newMainWeapon

    def getEnemyHealth(self):
        return self.health
    def setEnemyHealth(self,newHealth):
        self.health = newHealth

    def getEnemyName(self):
        return self.name
    def getEnemyRace(self):
        return self.race
    def getEnemySkill(self):
        return self.skill

    def getEnemyEffect(self):
        return self.effect
    def setEnemyEffect(self, newEffect):
        self.effect = newEffect

def checkAllCommands(x):
    x = x.lower()
    if x == "help":
        commandHelp()
    elif x  == "inventory":
        commandInventory()
    elif x == "drop":
        commandDrop()
    elif x == "equip weapon":
        commandEquipWeapon()
    elif x == "equip armor":
        commandEquipArmor()
    elif x == "equipment":
        commandEquipment()
    elif x == "power":
        commandPower()
    elif x == "stats":
        commandStats()
def commandHelp():
    print("Inventory\nEquip Weapon\nEquip Armor\nEquipment\nDrop\nStats\nPower")
def commandInventory():
    Character.listInventory()
def commandDrop():
    print('Dropping something deletes it forever, what would you like to drop?')
    drop = input("Drop > ")
    if drop in Character.getInventory():
        for x in range(len(Character.inventory)):
            if Character.inventory[x].getName() == drop:
                print(f'You drop the {Character.inventory[x].getName()}.')
                del Character.inventory[x]
    else: print("Cannot find that item in your inventory")
def consoleDrop(drop):
    if drop in Character.inventory:
        for x in Character.inventory:
            if x == drop:
                print(f'You drop the {drop.getName()}')
                del Character.inventory[Character.inventory.index(drop)]
def commandEquipment():
    if Character.getArmor() != "":
        print(f'Equipped Armor - {Character.getArmor().getName()}\n'
              f'Armor Weight - {Character.getArmor().getWeight()}\n'
              f'Armor Rating - {Character.getArmor().getRating()}\n')
    if Character.getMainWeapon() != "":
        print(f'Equipped Main-Hand Weapon - {Character.getMainWeapon().getName()}\n'
              f'Weapon Type - {Character.getMainWeapon().getRange()}\n'
              f'Weapon Damage - {Character.getMainWeapon().getDamage()}\n'
              f'Weapon Effect - {Character.getMainWeapon().getEffect()}\n')

    if Character.getOffWeapon() != "":
        print(f'Equipped Off-Hand Weapon - {Character.getOffWeapon().getName()}\n'
              f'Weapon Type - {Character.getOffWeapon().getRange()}\n'
              f'Weapon Damage - {Character.getOffWeapon().getDamage()}\n')
def commandEquipWeapon():
    weapon = input("Equip > ")
    if weapon in Character.getInventory():
        for x in range(len(Character.inventory)):
            if type(Character.inventory[x]) == Weapon and Character.inventory[x].getName() == weapon:
                if Character.inventory[x].getOneHanded():
                    print("Equip this weapon in the off hand or the main hand?")
                    hand = input("> ").lower()
                    if hand == "off hand":
                        if Character.getOffWeapon() != Character.inventory[x]:
                            Character.setOffWeapon(Character.inventory[x])
                            print(f"{Character.inventory[x].getName()} has been equipped in the off hand.")
                            if Character.getOffWeapon() == Character.getMainWeapon():
                                Character.setMainWeapon("")
                        else:
                            print("That weapon is already equipped there.")
                    elif hand == "main hand":
                        print(Character.getMainWeapon())
                        if Character.getMainWeapon() != Character.inventory[x]:
                            Character.setMainWeapon(Character.inventory[x])
                            print(f"{Character.inventory[x].getName()} has been equipped in the main hand.")
                            if Character.getOffWeapon() == Character.getMainWeapon():
                                Character.setOffWeapon("")
                        else:
                            print("That weapon is already equipped there.")
                else:
                    Character.setOffWeapon("")
                    Character.setMainWeapon(Character.inventory[x])
                    print(f"{Character.inventory[x].getName()} has been equipped using both hands.")
    else:
        print("You do not have this item, make sure to type its name exactly as its seen in your inventory.")
def commandEquipArmor():
    armor = input("Equip > ")
    if armor in Character.getInventory():
        for x in range(len(Character.inventory)):
           if type(Character.inventory[x]) == Armor and Character.inventory[x].getName() == armor:
               Character.setArmor(Character.inventory[x])
               print(f'{Character.inventory[x].getName()} has been equipped.')
    else:
        print("You do not have this item, make sure to type its name exactly as its seen in your inventory.")
def commandStats():
    print(f"Max Health - {Character.getMaxHealth()}\n"
          f"Current Health - {Character.getHealth()}\n"
          f"Strength - {Character.getStrength()}\n"
          f"Intellect - {Character.getIntellect()}\n"
          f"Charisma - {Character.getCharisma()}\n")
    if Character.getEffect() != []:
        print(f"Current Effects - {Character.getEffect()}")
def commandPower():
    print(Character.getPower())
    print("What power do you wish to use?")
    usePower = input("Power > ")
    temp = Character.getPower()
    for x in Character.getPower():
       if x == usePower:
           Powers(x)
def Powers(x):
    if x == "Archeons Resolve":
        Character.getEffect().clear()
        print("Using Archeons Resolve you shrug off all effects.")
    elif x == "Blessing of The Suns":
        b
    elif x  == "Blessing of The Sanctum":
        b
    elif x == "Aminic Magic":
        Character.setStrength((Character.getStrength() + random.randint(4,6)))
        print("Aminic energy empowers Rays next attack")
    elif x == "Heal":
        Character.setHealth((Character.getHealth() + random.randint(6, 12)))
        if Character.getHealth() > Character.getMaxHealth():
            Character.setHealth(Character.getMaxHealth())
        print(f"Lordaeron calls upon the light healing himself to {Character.getHealth()}")
    elif x == "Insanity":
        b
    elif x == "THE RULES":
        b


def startGame():
    print("You awaken in the land known as Northern Archea which resides in the center of this world Terradestril. \n"
          "Here it is the ending of the Third Era, more commonly known as the turning Age of The Magi. "
          "\nThis is a dark time where the Gods have gone silent and evil beings born through necromancy crawl the land freely.\n"
          "Now Hero, chose your path wisely and honor the fate you have been given.")
    heroRace = ""
    heroSkill = ""
    heroPower = []
    choice = True
    while choice:
        print("Chose your origin, Solsil, Norsil, or Man")
        originChoice = input("> ").lower()
        if originChoice == "solsil":
            print(
                "The Solsil, referred to as Sun Elves, are magnificent beings that draw their energy from the Sun Well.\n"
                "Solsil possess a decent quantity of mana and strength along with an attunement to fire.\n"
                "Their racial, Blessing of The Suns, allows them to explode with a fiery magic once a year.")
            print("If you wish to continue from this origin type continue. If not type back.")
            originChoice = input("> ").lower()
            if originChoice == "continue":
                heroRace = "solsil"
                heroPower = ["Blessing of The Suns"]
                choice = False
        elif originChoice == "norsil":
            print(
                "The Norsil, referred to as High Elves, are slender beings that draw their energy from the World Well.\n"
                "Norsil possess a vast quantity of mana yet lack in strength, along with an attunement to nature.\n"
                "If Norsil do practice melee combat they are often seen as shifty and agile fighters.\n"
                "Their racial, Blessing of The Sanctum, can tangle everyone around the Norsil in roots once a year.")
            print("If you wish to continue from this origin type continue. If not type back.")
            originChoice = input("> ").lower()
            if originChoice == "continue":
                heroRace = "norsil"
                heroPower = ["Blessing of The Sanctum"]
                choice = False
        elif originChoice == "man":
            print(
                "Man is native to Archea, these are versatile beings with no specific ties to artifacts or Gods as a race.\n"
                "Men possess greater strength however it is rare to find a man with supple mana, men can be equally attuned in all things.\n"
                "Their racial, Archeons Resolve, can remove a debuff at random once a year.")
            print("If you wish to continue from this origin type continue. If not type back.")
            originChoice = input("> ").lower()
            if originChoice == "continue":
                heroRace = "man"
                heroPower = ["Archeons Resolve"]
                choice = False
        else:
            print("Do not attempt to deviate from your path.")

    choice = True
    while choice:
        print("Chose your characters path, Mage or Warrior.")
        characterChoice = input("> ")
        characterChoice = characterChoice.lower()
        if characterChoice == "mage":
            choice = False
            heroSkill = "mage"
        elif characterChoice == "warrior":
            choice = False
            heroSkill = "warrior"

        else:
            print(f"Do not stray from your given path.")

    print("What will you go by?")
    heroName = input("> ")

    # Hero Inventory
    heroInventory = []
    if heroSkill == "warrior":
        # Easter Eggs
        if heroName == "Ray Shiota" and heroRace == "man":
            Arcanite_Reaper = Weapon("Arcanite Reaper", "melee", 6, False, [])
            heroInventory.append(Arcanite_Reaper)
            heroPower.append("Aminic Magic")
        if heroName == "Mograin" and heroRace == "man":
            Fragment_Of_Mograins_Sword = Item("Fragment Of Mograins Sword")
            heroInventory.append(Fragment_Of_Mograins_Sword)
        if heroName == "Lordaeron" and heroRace == "man":
            Lordaeric_Hammer = Weapon("Lordaeric Hammer", "melee", 6, False, [])
            heroInventory.append(Lordaeric_Hammer)
            heroPower.append("Heal")
        if heroRace != "norsil":
            Iron_Armor = Armor("Iron Armor", "Heavy", 6, 6)
            Iron_Sword = Weapon("Iron Sword", "melee", 3, True, [])
            heroInventory.append(Iron_Sword)
            heroInventory.append(Iron_Armor)

        else:
            global Frost_Bolt
            global College_Robes
            global Grand_Order_Robes
            global Fireball
            global Nature_Bolt
            if heroName == "Endol Nolvit":
                Iron_Sword = Weapon("Iron Sword", "melee", 3, True, [])
                Shadow_Bolt = Weapon("Shadow Bolt", "ranged", 3, True, [])
                heroPower.append("Insanity")
                heroInventory.append(Iron_Sword)
                heroInventory.append(Shadow_Bolt)
            Hide_Armor = Armor("Hide Armor", "light", 5, 5)
            Rusty_Dagger = Weapon("Rusty Dagger", "melee", 2, True, [])
            Iron_Dagger = Weapon("Iron Dagger", "melee", 2, True, [])
            heroInventory.append(Rusty_Dagger)
            heroInventory.append(Iron_Dagger)
            heroInventory.append(Hide_Armor)

    elif heroRace == "norsil":
        College_Robes = Armor("College Robes", "light", 3, 3)
        Nature_Bolt = Weapon("Nature Bolt", "ranged", 4, False, [])
        heroInventory.append(College_Robes)
        heroInventory.append(Nature_Bolt)

    elif heroRace == "solsil":
        Grand_Order_Robes = Armor("Grand Order Robes", "light", 4, 4)
        Fireball = Weapon("Fireball", "ranged", 4, False, [])
        heroInventory.append(Grand_Order_Robes)
        heroInventory.append(Fireball)

    else:
        if heroName == "Khadgar":
            Useless_Orb_Of_LordaeronII = Item("Useless_Orb_Of_LordaeronII")
            heroInventory.append(Useless_Orb_Of_LordaeronII)
            heroPower.append("THE RULES")
        College_Robes = Armor("College Robes", "light", 3, 3)
        Frost_Bolt = Weapon("Frost Bolt", "ranged", 4, False, [])
        heroInventory.append(College_Robes)
        heroInventory.append(Frost_Bolt)

    heroHealth = 0
    heroStrength = 0
    heroIntellect = 0
    heroCharisma = 0

    # All Randomized Stats
    if heroRace == "man":
        if heroSkill == "warrior":
            heroStrength = random.randint(16, 18)
            heroIntellect = random.randint(0, 4)
            heroCharisma = random.randint(9, 11)
            heroHealth = random.randint(50, 55)
        else:
            heroStrength = random.randint(9, 12)
            heroIntellect = random.randint(7, 14)
            heroCharisma = random.randint(12, 16)
            heroHealth = random.randint(35, 37)
    if heroRace == "solsil":
        if heroSkill == "warrior":
            heroStrength = random.randint(12, 14)
            heroIntellect = random.randint(7, 10)
            heroCharisma = random.randint(9, 13)
            heroHealth = random.randint(50, 52)
        else:
            heroStrength = random.randint(7, 10)
            heroIntellect = random.randint(13, 15)
            heroCharisma = random.randint(9, 13)
            heroHealth = random.randint(34, 36)
    if heroRace == "norsil":
        if heroSkill == "warrior":
            heroStrength = random.randint(8, 11)
            heroIntellect = random.randint(8, 12)
            heroCharisma = random.randint(8, 10)
            heroHealth = random.randint(45, 50)
        else:
            heroStrength = random.randint(2, 7)
            heroIntellect = random.randint(16, 18)
            heroCharisma = random.randint(10, 12)
            heroHealth = random.randint(33, 35)

    heroEffect = []
    global Character
    Character = Hero(heroRace, heroSkill, heroName, "", "", "", heroInventory, heroHealth, heroHealth, heroStrength,
                     heroIntellect, heroCharisma, heroEffect, heroPower)

    # Character Statpoint Choice
    statpoints = 4
    if Character.getName() == "Khadgar":
        statpoints == 6
    print(f"Finally spend your {statpoints} points wisely, as these can greatly impact your destiny")
    print("Each point into health can grant 3-5 hitpoints, where all the other stats progress linearly")
    print(f'Health - {Character.getHealth()}\n'
          f'Strength - {Character.getStrength()}\n'
          f'Intellect - {Character.getIntellect()}\n'
          f'Charisma - {Character.getCharisma()}\n')
    choice = True
    while choice == True:
        temp = int(input("Health > "))
        tempHP = 0
        if temp <= statpoints and temp >= 0:
            choice = False
            statpoints -= temp
            while temp > 0:
                tempHP += random.randint(3, 5)
                temp -= 1
            Character.setHealth((Character.getHealth() + tempHP))
            Character.setMaxHealth((Character.getMaxHealth() + tempHP))
        else:
            print("Invalid Number. Remeber you only have 4 points spend them wisely")

    if statpoints > 0:
        choice = True
    while choice == True:
        temp = int(input("Strength > "))
        if temp <= statpoints and temp >= 0:
            choice = False
            statpoints -= temp
            Character.setStrength((Character.getStrength() + temp))
        else:
            print(f"Invalid Number. Remember you only have {statpoints} left, spend them wisely")

    if statpoints > 0:
        choice = True
    while choice == True:
        temp = int(input("Intellect > "))
        if temp <= statpoints and temp >= 0:
            choice = False
            statpoints -= temp
            Character.setIntellect((Character.getIntellect() + temp))
        else:
            print(f"Invalid Number. Remember you only have {statpoints} left, spend them wisely")

    if statpoints > 0:
        choice = True
    while choice == True:
        temp = int(input("Charisma > "))
        if temp <= statpoints and temp >= 0:
            choice = False
            statpoints -= temp
            Character.setCharisma((Character.getCharisma() + temp))
            print(f"Final Charisma - {Character.getCharisma()}")
        else:
            print(f"Invalid Number. Remember you only have {statpoints} left, spend them wisely")
    print(f'\nHealth - {Character.getHealth()}\n'
          f'Strength - {Character.getStrength()}\n'
          f'Intellect - {Character.getIntellect()}\n'
          f'Charisma - {Character.getCharisma()}\n')
    print(f"Now awaken {Character.getName()}, your destiny awaits you.")
    global strengthMod
    global intellectMod
    global charismaMod
    strengthMod = 0
    intellectMod = 0
    charismaMod = 0
    rollModifyers()
    if Character.getSkill() == "warrior":
        WarriorJourney()
    if Character.getSkill() == "mage":
        MageJourney()
def rollModifyers():
    strengthMod = math.trunc((Character.getStrength() - 10) / 2)
    intellectMod = math.trunc((Character.getIntellect() - 10) / 2)
    charismaMod = math.trunc((Character.getCharisma() -10) / 2)
def Roll():
    return random.randint(1,20)
def characterRoll(x):
    return (random.randint(1,20) + x)

def Action(mod,target):
    roll = characterRoll(mod)
    if Character.getMainWeapon().getEffect() == "Heal" or Character.getMainWeapon().getEffect() == "Armor":
        if roll > 6:
            Effect(Character, Character.getMainWeapon().getEffect())
        else: print(f"You failed to cast {Character.getMainWeapon().getName()}")
    else:
        if roll >= 20:
            target.setEnemyHealth((target.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2)))
            if Character.getMainWeapon().getEffect() != [] and Character.getMainWeapon().getEffect() != "Armor":
                Effect(target, Character.getMainWeapon().getEffect())
            if target.getEnemyHealth() <= 0:
                print(f"YOU HAVE SLAIN {target.getEnemyName()}!")
            else:
                print(f'You have CRITICALLY hit {target.getEnemyName()} for {(Character.getMainWeapon().getDamage() * 2)}')
                print(f'CURRENT HEALTH OF {target.getEnemyName()} - {target.getEnemyHealth()}')
        elif roll > target.getEnemyArmor().getRating():
            target.setEnemyHealth((target.getEnemyHealth() - Character.getMainWeapon().getDamage()))
        #Effects / DoT
            if Character.getMainWeapon().getEffect() != []:
                Effect(target, Character.getMainWeapon().getEffect())
            if target.getEnemyHealth() <= 0:
                print(f"YOU HAVE SLAIN {target.getEnemyName()}!")
            else:
                print(f'You have hit {target.getEnemyName()} for {Character.getMainWeapon().getDamage()}')
                print(f'CURRENT HEALTH OF {target.getEnemyName()} - {target.getEnemyHealth()}')
        else:
            if target.getEnemyArmor().getWeight() == "light":
                print(f"{target.getEnemyName()} swiftly dodges your attack")
            else: print(f'Your attack glances off of The {target.getEnemyArmor().getName()}')
        effectTick(Character)
def AttacksCharacter(enemy):
    roll = Roll()
    if roll >= 20:
        Character.setHealth((Character.getHealth() - (enemy.getEnemyMainWeapon().getDamage() * 2)))
        if enemy.getEnemyMainWeapon().getEffect() != []:
            Effect(Character, enemy.getEnemyMainWeapon().getEffect())
        if Character.getHealth() <= 0:
            print("gg")
        print(f'You have been CRITICALLY hit for {(enemy.getEnemyMainWeapon().getDamage() * 2)} by {enemy.getEnemyMainWeapon().getName()}')
        print(f'CURRENT HEALTH - {Character.getHealth()}')
    elif roll > Character.getArmor().getRating():
        Character.setHealth((Character.getHealth() - enemy.getEnemyMainWeapon().getDamage()))
        if enemy.getEnemyMainWeapon().getEffect() != []:
            Effect(Character, enemy.getEnemyMainWeapon().getEffect())
        if Character.getHealth() <= 0:
            print("gg")
        print(f'You have been hit for {enemy.getEnemyMainWeapon().getDamage()} by {enemy.getEnemyMainWeapon().getName()}')
        print(f'CURRENT HEALTH - {Character.getHealth()}')
    else:
        if Character.getArmor().getWeight() == "light":
            print(f"You swiftly dodge the {enemy.getEnemyMainWeapon().getName()}")
        else: print(f'The {enemy.getEnemyMainWeapon().getName()} glances off your armor harmlessly')
    if Character.getHealth() <= 0:
        restartGame()
    effectTick(enemy)
def HealsEnemy(caster, target):
    roll = Roll()
    if roll > 4:
        Effect(target, caster.getEnemyMainWeapon().getEffect())
        print(f"{caster.getEnemyName()} healed {target.getEnemyName()}!")
    else:
        print(f"{caster.getEnemyName()} failed to heal {target.getEnemyName()}!")


def WarriorJourney():
    print("\n\n\n\n\n\nAwakening in an empty feild ")
def MageJourney():
    if Character.getRace() == "man":
        print("\n\n\n\n\n\nAwakening from what seemed like a day dream, you find yourself drenched in sweat. Trying to regain your bearings you realize you were training your frost magic "
              "\nin the courtyard of the college."
              "\n As a Human mage much more focus is required to perform the arcane arts than it would be for elves to perform, as they achieve arcane out of instinct.")
    else: print("Awakening from a plesant nap under the suns in green grasses, you take in the beauty of the world and feel the mana connect you to your surroundings.")
    print("Before heading back into the College of Arcanum you must equip the proper attire. To do this type Inventory to see your robes. \n"
          "Then type Equip Armor and select the armor within your inventory. This is called a command and a list of commands can be found whenever you type help into the system.")
    choice = True
    while choice == True:
        equipArmor = input("> ")
        checkAllCommands(equipArmor)
        if Character.getArmor() != "":
            choice = False

    print("While were at it might as well equip your weapon too, use the same process to figure out how to equip your weapon.\n"
          "Remember use help for a list of commands whenever you get stuck.")
    choice = True
    while choice == True:
        equipWeapon = input("> ")
        checkAllCommands(equipWeapon)
        if Character.getMainWeapon() != "":
            choice = False
        if Character.getMainWeapon() != "":
            choice = False
    mageType = None
    if Character.getRace() == "man":
        mageType = "Cryomancy"
    elif Character.getRace() == "solsil":
        mageType = "Pyromancy"
    else: mageType = "Druidic"
    print(f"\nFeeling confident and equipped, you head inside the college where a class is gathering and a pale fellow mage introduces himself."
          f"\n\nHello {Character.getName()}, Im Necramil and have taken notice to your {mageType} skills and was wondering if you could help me out with a project.\n"
          f"It would be quick, I bet we could even make it back to class before it starts."
          f"\n\nFollow Necramil or Attend Class")
    global Lesser_Heal
    global Health_Potion
    global Dummy
    global Improved_Grand_Order_Robes
    global Shadow_Bolt
    global Iron_Dagger
    global Bones
    global Necramil
    global SkeletonHord
    global Necromancer
    global Bone_Shiv
    Lesser_Heal = Weapon("Lesser_Heal", "ranged", 0, False, "Lesser Heal")
    Health_Potion = Item("Health_Potion")
    Improved_Grand_Order_Robes = Armor("Improved Grand Order Robes", "light", 5, 5)
    Shadow_Bolt = Weapon("Shadow Bolt", "ranged", 3, True, [])
    Iron_Dagger = Weapon("Iron Dagger", "melee", 2, True,  [])
    Bone_Shiv = Weapon("Bones", "melee", 1, True, "Mob")
    Bones = Armor("Bones", "light", 0, 0)
    Necramil = Enemy("norsil", "mage", "Necramil", 33, Iron_Dagger, Improved_Grand_Order_Robes, [])
    Dummy = Enemy("Dummy", "", "Training Dummy", 1, Iron_Dagger, Improved_Grand_Order_Robes, [])
    SkeletonHord = Enemy("Skeleton", "warrior", "Skeleton Hord",25 , Bone_Shiv, Bones, [])
    Necromancer = Enemy("man", "mage", "Summoner", 20, Shadow_Bolt, Improved_Grand_Order_Robes, [])
    global Darkness
    global Abyssal_Armor
    global Archmages_Robes
    global Sirus
    global Maeven
    global Iron_Sword
    global Enchanted_Robes
    global soulBindingDagger
    global Iron_Armor
    Iron_Armor = Armor("Iron Armor", "Heavy", 6, 6)
    Enchanted_Robes = Armor("Enchanted Robes", "light", 5, 5)
    soulBindingDagger = Weapon("Soul Binding Dagger", "melee", 3, True, [])
    Iron_Sword = Weapon("Iron Sword", "melee", 3, True, [])
    Darkness = Weapon("Darkness", "Ranged", 8, False, "Darkness")
    Abyssal_Armor = Armor("Abyssal Armor", "heavy", 10, 10)
    Archmages_Robes = Armor("Archmages Robes", "light", 7, 7)
    Sirus = Enemy("Inar", "mage", "Sirus", 58, Darkness, Abyssal_Armor, [])
    Maeven = Enemy("man", "mage", "Maeven", 50, Iron_Dagger, Archmages_Robes, [])
    choice = True
    while choice == True:
        choice1 = input("> ").lower()
        checkAllCommands(choice1)
        if choice1 == "follow necramil":
            choice = False

            questNecramil()

        elif choice1 == "attend class":
            choice = False

            questAttendClass()

    print("You return to the Grand Hall and begin to search for the Quarter Master when you run into Necramil.")
    if Necramil.getEnemyHealth() > 0:
        print("\n\"Hey again, still havent found anyone to help me yet and I really need this done so the professor doesnt chew me out.\n"
            "Would you mind helping me, this time ill throw in a reward too.\"\n")
    choice = True
    while choice == True:
        if Necramil.getEnemyHealth() > 0:
            print("Find The Quarter Master | Follow Necramil | Ask Necramil What The Reward Is")
        else: print("| Find The Quarter Master |")
        answer = input("> ").lower()
        if answer == "follow necramil" and Necramil.getEnemyHealth() > 0:
            choice = False

            questNecramil()

        elif answer == "ask necramil what the reward is" and Necramil.getEnemyHealth() > 0:
            choice = False
            print("\"Ahhh, I do believe suprises are more fun, but if you really must know ill teach you a new spell I have just aquired!\"")
            if Roll() > 11:
                print("The reward entices you and you agree to follow him.")

                questNecramil()

            else:
                choice = True
                while choice == True:
                    print("Follow Necramil | Find The Quarter Master")
                    answer = input("> ").lower()
                    if answer == "follow necramil":
                        choice = False

                        questNecramil()

                    elif answer == "find the quarter master":
                        choice = False

                        questQuarterMaster()

        elif answer == "find the quarter master":
            choice = False
            if Necramil.getEnemyHealth() > 0:
                print("\"DAMNED LOWLIFE!\"")
                print("Necramil flings a curse your way.")
                if characterRoll(strengthMod) > 10:
                    print("You dodge it in time, and as Necramil scurries away you head to find the Quarter Master.")

                    questQuarterMaster()
                else:
                    Character.setEffect("Necramils Curse")
                    Character.setIntellect(Character.getIntellect() - 1)
                    print("You feel the curse set in, your intelligence seems to have been supressed")
                    print("Ready to fight, you turn to where Necramil was but he is nowhere to be seen.")
                    print("Annoyed, you walk over to the Quarter Master.")

                    questQuarterMaster()

            questQuarterMaster()

def questAttendClass():
    def questSecondTry(prof_mood):
        print("You wait a while until returning to the class")
        choice = True
        while choice == True:
            print("| Confront the Professor |")
            answer = input("> ").lower()
            if answer == "confront the professor":
                checkAllCommands(answer)
                choice = False
                if prof_mood == "chill" or "angry":
                    print("\"Alright do you know what you did wrong last time?\"")
                    if prof_mood == "angry":
                        print("\"Do you understand what you did a few hours ago, do you understand what could have happended had I not avoided your spell\"")
                    choice = True
                    while choice == True:
                        print("1 | \"Yes Professor, I understand.\"")
                        print("2 | \"Yes, Im sorry I just got nervous.\"")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "1":
                            print("\"Yes Professor, I understand.\"\n")
                            choice = False
                            roll = characterRoll(charismaMod)
                            if (roll > 7 and prof_mood == "chill") or (roll > 11 and prof_mood == "angry"):
                                print("\"Alright, take as many times as you need. As long as I see you perform the spell correctly ill give you the tome.\"\n")
                                if Character.getRace() == "man":
                                    Character.inventory.append(Layered_Ice)
                                    print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                if Character.getRace() == "norsil":
                                    print("Regrowth has been added to your inventory, dont forget to equip it.")
                                    Character.inventory.append(Regrowth)
                                if Character.getRace() == "solsil":
                                    Character.inventory.append(Incinerate)
                                    print("Incinerate has been added to your inventory, dont forget to equip it.")
                                choice = True
                                while choice == True:
                                    print("| Cast |")
                                    answer = input("> ").lower()
                                    checkAllCommands(answer)
                                    if answer == "cast":
                                        if Character.getRace() == "norsil" or Character.getRace() == "man":
                                            Action(intellectMod, Character)
                                            if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                choice = False
                                                print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                            elif Character.getEffect != [] and Character.getRace() == "man":
                                                choice = False
                                                print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                            else: print("\"Try again.\"")
                                        else:
                                            Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                            Action(intellectMod, Dummy)
                                            if Dummy.getEnemyEffect() != []:
                                                choice = False
                                                print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                            else:
                                                print("\"Try again\"")
                            else:
                                print("\"Alright so then explain to me why you think you deserve another chance.\"\n")
                                choice = True
                                while choice == True:
                                    print("1 | \"I cant wait another week, I want to need to join the battlefeild.\"\n")
                                    print("2 | \"Trust me, I wont dissapoint you this time.\"\n")
                                    answer = input("> ").lower()
                                    checkAllCommands(answer)
                                    if answer == "1":
                                        choice = False
                                        print("\"I cant wait another week, I need to join the battlefeild.\"\n")
                                        print("\"An honorable cause. Fine, but im not letting you leave until you have passed the test. You will need it out there.\"\n")
                                        if Character.getRace() == "man":
                                            Character.inventory.append(Layered_Ice)
                                            print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                        if Character.getRace() == "norsil":
                                            print("Regrowth has been added to your inventory, dont forget to equip it.")
                                            Character.inventory.append(Regrowth)
                                        if Character.getRace() == "solsil":
                                            Character.inventory.append(Incinerate)
                                            print("Incinerate has been added to your inventory, dont forget to equip it.")
                                        choice = True
                                        while choice == True:
                                            print("| Cast |")
                                            answer = input("> ").lower()
                                            checkAllCommands(answer)
                                            if answer == "cast":
                                                if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                    Action(intellectMod, Character)
                                                    if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    elif Character.getEffect != [] and Character.getRace() == "man":
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:
                                                        print("\"Try again.\"")
                                                else:
                                                    Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                    Action(intellectMod, Dummy)
                                                    if Dummy.getEnemyEffect() != []:
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:
                                                        print("\"Try again\"")
                                    if answer == "2":
                                        choice = False
                                        print("\"Trust me, I wont dissapoint you this time.\"\n")
                                        roll = characterRoll(charismaMod)
                                        if (roll > 9 and prof_mood == "chill") or (roll > 16 and prof_mood == "angry"):
                                            print("\"Dont know why, but for some reason I trust you. Alright then, as long as I see you pass the test ill give you the tome.\"\n")
                                            if Character.getRace() == "man":
                                                Character.inventory.append(Layered_Ice)
                                                print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                            if Character.getRace() == "norsil":
                                                print("Regrowth has been added to your inventory, dont forget to equip it.")
                                                Character.inventory.append(Regrowth)
                                            if Character.getRace() == "solsil":
                                                Character.inventory.append(Incinerate)
                                                print("Incinerate has been added to your inventory, dont forget to equip it.")
                                            choice = True
                                            while choice == True:
                                                print("| Cast |")
                                                answer = input("> ").lower()
                                                checkAllCommands(answer)
                                                if answer == "cast":
                                                    if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                        Action(intellectMod, Character)
                                                        if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        elif Character.getEffect != [] and Character.getRace() == "man":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            print("\"Try again.\"")
                                                    else:
                                                        Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                        Action(intellectMod, Dummy)
                                                        if Dummy.getEnemyEffect() != []:
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            print("\"Try again\"")
                                            if Character.getRace() == "man":
                                                Character.inventory.append(Layered_Ice)
                                                print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                            if Character.getRace() == "norsil":
                                                print("Regrowth has been added to your inventory, dont forget to equip it.")
                                                Character.inventory.append(Regrowth)
                                            if Character.getRace() == "solsil":
                                                Character.inventory.append(Incinerate)
                                                print("Incinerate has been added to your inventory, dont forget to equip it.")
                                            choice = True
                                            while choice == True:
                                                print("| Cast |")
                                                answer = input("> ").lower()
                                                checkAllCommands(answer)
                                                if answer == "cast":
                                                    if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                        Action(intellectMod, Character)
                                                        if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        elif Character.getEffect != [] and Character.getRace() == "man":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            print("\"Try again.\"")
                                                    else:
                                                        Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                        Action(intellectMod, Dummy)
                                                        if Dummy.getEnemyEffect() != []:
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            print("\"Try again\"")
                                        else:
                                            if prof_mood == "angry":
                                                print(f"\"Are you delusional? You just threw a {Character.getMainWeapon().getName()} at me!\"\n")
                                                print("\"Ill give you ONE more chance, and if you mess it up you WILL get out of my sight!\"\n")
                                            else:
                                                print("\"Fine, Ill give you one more chance\"\n")
                                            if Character.getRace() == "man":
                                                Character.inventory.append(Layered_Ice)
                                                print(
                                                    "Layered_Ice has been added to your inventory, dont forget to equip it.")
                                            if Character.getRace() == "norsil":
                                                print(
                                                    "Regrowth has been added to your inventory, dont forget to equip it.")
                                                Character.inventory.append(Regrowth)
                                            if Character.getRace() == "solsil":
                                                Character.inventory.append(Incinerate)
                                                print(
                                                    "Incinerate has been added to your inventory, dont forget to equip it.")
                                            choice = True
                                            while choice == True:
                                                print("| Cast |")
                                                answer = input("> ").lower()
                                                checkAllCommands(answer)
                                                if answer == "cast":
                                                    if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                        Action(intellectMod, Character)
                                                        if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        elif Character.getEffect != [] and Character.getRace() == "man":
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            choice = False
                                                            print( "\"You leave feeling defeated, you will just have to survive without that spell.\"")
                                                            if Character.getRace() == "man":
                                                                consoleDrop(Layered_Ice)
                                                                Character.setMainWeapon(Frost_Bolt)
                                                            elif Character.getRace() == "norsil":
                                                                consoleDrop(Regrowth)
                                                                Character.setMainWeapon(Nature_Bolt)
                                                    else:
                                                        Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                        Action(intellectMod, Dummy)
                                                        if Dummy.getEnemyEffect() != []:
                                                            choice = False
                                                            print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                        else:
                                                            choice = False
                                                            print("\"You leave feeling defeated, you will just have to survive without that spell.\"")
                                                            consoleDrop(Incinerate)
                                                            Character.setMainWeapon(Fireball)
                        elif answer == "2":
                            choice = False
                            print("\"Yes, Im sorry I just got nervous.\"\n")
                            print("Get nervous while your in combat and its all over for you. Now explain to me why I should give you another chance.\n")
                            choice = True
                            while choice == True:
                                print("1 | \"I cant wait another week, I want to need to join the battlefeild.\"\n")
                                print("2 | \"Trust me, I wont dissapoint you this time.\"\n")
                                answer = input("> ").lower()
                                checkAllCommands(answer)
                                if answer == "1":
                                    choice = False
                                    print("\"I cant wait another week, I need to join the battlefeild.\"\n")
                                    print("\"An honorable cause. Fine, but im not letting you leave until you have passed the test. You will need it out there.\"\n")
                                    if Character.getRace() == "man":
                                        Character.inventory.append(Layered_Ice)
                                        print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                    if Character.getRace() == "norsil":
                                        print("Regrowth has been added to your inventory, dont forget to equip it.")
                                        Character.inventory.append(Regrowth)
                                    if Character.getRace() == "solsil":
                                        Character.inventory.append(Incinerate)
                                        print("Incinerate has been added to your inventory, dont forget to equip it.")
                                    choice = True
                                    while choice == True:
                                        print("| Cast |")
                                        answer = input("> ").lower()
                                        checkAllCommands(answer)
                                        if answer == "cast":
                                            if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                Action(intellectMod, Character)
                                                if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                    choice = False
                                                    print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                elif Character.getEffect != [] and Character.getRace() == "man":
                                                    choice = False
                                                    print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                else:
                                                    print("\"Try again.\"")
                                            else:
                                                Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                Action(intellectMod, Dummy)
                                                if Dummy.getEnemyEffect() != []:
                                                    choice = False
                                                    print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                else:
                                                    print("\"Try again\"")
                                if answer == "2":
                                    choice = False
                                    print("\"Trust me, I wont dissapoint you this time.\"\n")
                                    roll = characterRoll(charismaMod)
                                    if (roll > 9 and prof_mood == "chill") or (roll > 16 and prof_mood == "angry"):
                                        print("\"Dont know why, but for some reason I trust you. Alright then, as long as I see you pass the test ill give you the tome.\"\n")
                                        if Character.getRace() == "man":
                                            Character.inventory.append(Layered_Ice)
                                            print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                        if Character.getRace() == "norsil":
                                            print("Regrowth has been added to your inventory, dont forget to equip it.")
                                            Character.inventory.append(Regrowth)
                                        if Character.getRace() == "solsil":
                                            Character.inventory.append(Incinerate)
                                            print("Incinerate has been added to your inventory, dont forget to equip it.")
                                        choice = True
                                        while choice == True:
                                            print("| Cast |")
                                            answer = input("> ").lower()
                                            checkAllCommands(answer)
                                            if answer == "cast":
                                                if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                    Action(intellectMod, Character)
                                                    if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    elif Character.getEffect != [] and Character.getRace() == "man":
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:print("\"Try again.\"")
                                                else:
                                                    Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                    Action(intellectMod, Dummy)
                                                    if Dummy.getEnemyEffect() != []:
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:
                                                        print("\"Try again\"")
                                    else:
                                        if prof_mood == "angry":
                                            print(f"\"Are you delusional? You just threw a {Character.getMainWeapon().getName()} at me!\"\n")
                                            print("\"Ill give you ONE more chance, and if you mess it up you WILL get out of my sight!\"\n")
                                        else: print("\"Fine, Ill give you one more chance\"\n")
                                        if Character.getRace() == "man":
                                            Character.inventory.append(Layered_Ice)
                                            print("Layered_Ice has been added to your inventory, dont forget to equip it.")
                                        if Character.getRace() == "norsil":
                                            print("Regrowth has been added to your inventory, dont forget to equip it.")
                                            Character.inventory.append(Regrowth)
                                        if Character.getRace() == "solsil":
                                            Character.inventory.append(Incinerate)
                                            print("Incinerate has been added to your inventory, dont forget to equip it.")
                                        choice = True
                                        while choice == True:
                                            print("| Cast |")
                                            answer = input("> ").lower()
                                            checkAllCommands(answer)
                                            if answer == "cast":
                                                if Character.getRace() == "norsil" or Character.getRace() == "man":
                                                    Action(intellectMod, Character)
                                                    if Character.getMaxHealth() == Character.getHealth() and Character.getRace() == "norsil":
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    elif Character.getEffect != [] and Character.getRace() == "man":
                                                        choice = False
                                                        print( "\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:
                                                        choice = False
                                                        print("\"You leave feeling defeated, you will just have to survive without that spell.\"")
                                                        if Character.getRace() == "man":
                                                            consoleDrop(Layered_Ice)
                                                            Character.setMainWeapon(Frost_Bolt)
                                                        elif Character.getRace() == "norsil":
                                                            consoleDrop(Regrowth)
                                                            Character.setMainWeapon(Nature_Bolt)
                                                else:
                                                    Dummy = Enemy("Dummy", "", "Dumb", 0, Iron_Dagger, Improved_Grand_Order_Robes, [])
                                                    Action(intellectMod, Dummy)
                                                    if Dummy.getEnemyEffect() != []:
                                                        choice = False
                                                        print("\"Congradulations, now if you will return to the Quarter Master I believe he has work for you.\"")
                                                    else:
                                                        choice = False
                                                        print("\"You leave feeling defeated, you will just have to survive without that spell.\"")
                                                        consoleDrop(Incinerate)
                                                        Character.setMainWeapon(Fireball)

    if Necramil.getEnemyHealth() <= 0:
        print("\n\n\n\n\n\n\n\n\n\nYou walk into an empty class room and approach the professor as he glares at you over the tome he is studying.")
        print("\n\"I can hardly believe that a student would show up this late to one of my classes, so whats your excuse\"\n")
        choice = True
        while choice == True:
            print("| 1 | \"Sorry had to take care of a necromancer who tried to kill me.\"\n")
            print("| 2 | \"Got caught up in my studies, im sorry im late professor.\"\n")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "1":
                choice = False
                print("\" Sorry had to take care of a necromancer who tried to kill me.\"")
                print("\nSeems to be everyones excuse these days, no matter ill still allow you to take the test.")
            elif answer == "2":
                choice = False
                print('\" Got caught up in my studies, im sorry im late professor.\"')
                print("\n Ha! If you have been studying for so long I expect you to pass this test without breaking a sweat.")
    else:
        print("\n\n\n\n\n\n\n\n\n\nRealizing that today is a test of the new spell you have been learning, you fall into line with the rest of the students.")
        print("An hour goes by and your finally up and the professor approches you.")
    print("\n\"Now if you would, take this tome, read its instructions, and cast the spell.\"")
    if Character.getRace() == "man":
        global Layered_Ice
        Layered_Ice = Weapon("Layered_Ice", "ranged", 0, False,  "Armor")
        print("\nLayered Ice was added to your inventory.\n")
        Character.inventory.append(Layered_Ice)
        print("\"This spell casts upon the user, so you will be the target.\"")
        choice = True
        while choice == True:
            print("| Cast |")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "cast":
                if Character.getMainWeapon().getName() == "Frost Bolt":
                    choice = False
                    print(f"\"YOU FOOL!\" The professor screams as he narrowly dodges the {Character.getMainWeapon().getName()} you have just hurled at him")
                    print(f"\"Ill speak to you after class, {Character.getName()}\"")
                    questSecondTry("angry")
                elif Character.getMainWeapon().getName() == "Layered Ice":
                    choice = False
                    Action(intellectMod,Character)
                    if Character.getEffect() != []:
                        print("\"Well done! you pass the test, and get to keep that tome.\"")
                        print("\"Make sure to see the Quarter Master after so he can assign you a task.\"")
                        print("\nYou walk out into back into the colleges grand hall.")
                    else:
                        print("\"Good try, maybe next week...\"")
                        print("\"Ill be taking that back too.\"")
                        consoleDrop(Layered_Ice)
                        Character.setMainWeapon(Frost_Bolt)
                        questSecondTry("chill")
    elif Character.getRace() == "solsil":
        global Incinerate
        Incinerate = Weapon("Incinerate", "ranged", 1, False, "Burning")
        print("\nIncinerate was added to your inventory.\n")
        Character.inventory.append(Incinerate)
        print("\"Aim at that target over there.\"")
        choice = True
        while choice == True:
            print("| Cast |")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "cast":
                if Character.getMainWeapon().getName() == "Fireball":
                    choice = False
                    print(f"\"YOU FOOL!\" The professor screams as he narrowly dodges the {Character.getMainWeapon().getName()} you have just hurled at him")
                    print(f"\"Ill speak to you after class, {Character.getName()}\"")
                    questSecondTry("angry")
                elif Character.getMainWeapon().getName() == "Incinerate":
                    choice = False
                    Action(intellectMod, Dummy)
                    if Dummy.getEnemyEffect() != []:
                        print("\"Well done! you pass the test, and get to keep that tome.\"")
                        print("\"Make sure to see the Quarter Master after so he can assign you a task.\"")
                        print("\nYou walk out into back into the colleges grand hall.")
                    else:
                        print("\"Good try, maybe next week...\"")
                        print("\"Ill be taking that back too.\"")
                        consoleDrop(Incinerate)
                        Character.setMainWeapon(Fireball)
                        questSecondTry("chill")
    elif Character.getRace() == "norsil":
        global Regrowth
        Regrowth = Weapon("Regrowth", "ranged", 0, False,  "Heal")
        print("\nRegrowth was added to your inventory.\n")
        print("\"This spell casts upon the user, so you will be the target.\"")
        Character.inventory.append(Regrowth)
        choice = True
        while choice == True:
            print("| Cast |")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "cast":
                if Character.getMainWeapon().getName() == "Nature Bolt":
                    choice = False
                    print(f"\"YOU FOOL!\" The professor screams as he narrowly dodges the {Character.getMainWeapon().getName()} you have just hurled at him")
                    print(f"\"Ill speak to you after class, {Character.getName()}\"")
                    questSecondTry("angry")
                elif Character.getMainWeapon().getName() == "Regrowth":
                    choice = False
                    Character.setHealth((Character.getHealth() - 1))
                    Action(intellectMod, Character)
                    if Character.getHealth() == Character.getMaxHealth():
                        print("\"Well done! you pass the test, and get to keep that tome.\"")
                        print("\"Make sure to see the Quarter Master after so he can assign you a task.\"")
                        print("\nYou walk out into back into the colleges grand hall.")
                    else:
                        print("Good try, maybe next week...")
                        print("Ill be taking that back too.")
                        consoleDrop(Regrowth)
                        Character.setMainWeapon(Nature_Bolt)
                        questSecondTry("chill")
    Dummy.setEnemyHealth(-1)
def questNecramil():
    print("\n\n\n\n\n\n\n\n\n\nNecramil leads you to a deserted class where he pulls a book off a wall and a secret entrance opens up.\n\n "
          "\"My professor does fancy passages like this to his lab, ive always thought they were extra.\""
          "\n\n The door closes behind you, and you continue down a declining path. You arrive at a room with a stone block in the middle of it.\n\n"
          "\"Here we are, ive been working on this spell for a while. Its supposed to increase the health of its target temporarily and im hoping to use it in combat"
          " if you would just lay down on the table we can begin, dont worry ive practiced on a multitude of creatures here and its worked just fine.\n")
    print("| Decline | Lay Down |")
    choice = True
    while choice == True:
        choice2 = input("> ").lower()
        checkAllCommands(choice2)
        if choice2 == "lay down":
            choice = False
            print("As you lay down on the tablet you see a malicious grin dawn upon Necramils face as he attempts to bring a dagger down on your chest.")
            if characterRoll(strengthMod) > 15:
                print("In the knick of time you grab his hand and toss it to the side")
                Skeleton = Enemy("undead", "warrior", "Skeleton", 0, Iron_Dagger, Bones, [])

            else:
                AttacksCharacter(Necramil)
                print("From the your blood he summons a skeleton from his slumber as you realize you are in the catacombs with a necromancer.")
                Skeleton = Enemy("undead", "warrior", "Skeleton", 2, Iron_Dagger, Bones, [])
            Necramil.setEnemyMainWeapon(Shadow_Bolt)
            choice = True
            while choice == True:
                if Skeleton.getEnemyHealth() > 0:
                    print("| Attack Skeleton | Attack Necramil |")
                else:
                    print("| Attack Necramil |")
                choice3 = input("> ").lower()
                checkAllCommands(choice3)
                if choice3 == "attack skeleton":
                    Action(intellectMod, Skeleton)
                    AttacksCharacter(Necramil)
                elif choice3 == "attack necramil":
                    if Skeleton.getEnemyHealth() > 0:
                        AttacksCharacter(Skeleton)
                    Action(intellectMod, Necramil)
                    AttacksCharacter(Necramil)
                if Necramil.getEnemyHealth() <= 0 and Skeleton.getEnemyHealth() <= 0:
                    choice3 = False
                    if Character.getHealth() <= 15:
                        print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                    else:
                        print("You emerge victorious from your first encounter with a necromancer.")
                    choice = True
                    while choice == True:
                        print("| Loot the Body | Return to the College |")
                        choice2 = input("> ").lower()
                        checkAllCommands(choice2)
                        if choice2 == "loot the body":
                            print(
                                f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the body then head back to the college.")
                            Character.appendInventory().append(Iron_Dagger)
                            Character.appendInventory().append(Necramil.getEnemyArmor())
                            choice = False
                        if choice2 == "return to the college":
                            print(
                                "disgusted by the smell of the dead you return to the college in search of a healer.")
                            choice = False
        elif choice2 == "decline":
            choice2 = False
            print("Seems like a waste to walk all the way down here just to turn around dont you think?")
            print("You know im offering you extra health, cant see why anyone would decline such a thing")
            choice = True
            while choice == True:
                print("| Attack Necramil | Continue Conversation | Lay Down |")
                choice2 = input("> ").lower()
                checkAllCommands(choice2)
                if choice2 == "continue conversation":
                    choice = False
                    choice1 = True
                    while choice1 == True:
                        print("\n| 1 | \"Im leaving, and if you follow me it will be your last mistake\"")
                        print("\n| 2 | \"Ha! Ive been a necromancer for longer then you have you really think im going to become one of your \'expiriments\' \"")
                        print("\n| 3 | \"Look man I gotta get back to my class, promise ill come back after. Ill even shake on it.\"\n")
                        choice2 = input("> ")
                        checkAllCommands(choice2)
                        if choice2 == "2":
                            choice1 = False
                            print("\"Ha! Ive been a necromancer for longer then you have you really think im going to become one of your \'expiriments\'. \"")
                            if characterRoll(charismaMod) > 10:
                                print("Necramil sneers and heads deeper into the catacombs. You turn around and head back to the college.")
                                Necramil.setEnemyHealth(0)
                            else:
                                print("\"LIAR!\" Necramil begins to cast a spell.")
                                Necramil.setEnemyMainWeapon(Shadow_Bolt)
                                while Necramil.getEnemyHealth() > 0:
                                    print("| 1 | Attack Necramil")
                                    choice4 = input("> ").lower()
                                    checkAllCommands(choice4)
                                    if choice4 == "1":
                                        Action(intellectMod,Necramil)
                                        AttacksCharacter(Necramil)
                                if Character.getHealth() <= 15:
                                    print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                                else:
                                    print("You emerge victorious from your first encounter with a necromancer.")
                                choice = True
                                while choice == True:
                                    print("| Loot the Bodies | Return to the College |")
                                    choice2 = input("> ").lower()
                                    checkAllCommands(choice2)
                                    if choice2 == "loot the bodies":
                                        print(f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the bodies then head back to the college.")
                                        Character.appendInventory().append(Iron_Dagger)
                                        Character.appendInventory().append(Necramil.getEnemyArmor())
                                        choice = False
                                    if choice2 == "return to the college":
                                        print("disgusted by the smell of the dead you return to the college in search of a healer.")
                                        choice = False
                        elif choice2 == "1":
                            choice1 = False
                            print("\"Im leaving, and if you follow me it will be your last mistake.\"")
                            if characterRoll(charismaMod) > 14:
                                print("You turn to leave and head back to the college, Necramil doesnt follow.")
                                Necramil.setEnemyHealth(0)
                            else:
                                print("You hear Necramil approaching quickly, turing to face him you see he is prepairing to cast a spell.")
                                Necramil.setEnemyMainWeapon(Shadow_Bolt)
                                while Necramil.getEnemyHealth() > 0:
                                    print("| 1 | Attack Necramil")
                                    choice4 = input("> ").lower()
                                    checkAllCommands(choice4)
                                    if choice4 == "1":
                                        Action(intellectMod,Necramil)
                                        AttacksCharacter(Necramil)
                                if Character.getHealth() <= 15:
                                    print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                                else:
                                    print("You emerge victorious from your first encounter with a necromancer.")
                                choice = True
                                while choice == True:
                                    print("| Loot the Bodies | Return to the College |")
                                    choice2 = input("> ").lower()
                                    checkAllCommands(choice2)
                                    if choice2 == "loot the bodies":
                                        print(f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the bodies then head back to the college.")
                                        Character.appendInventory().append(Iron_Dagger)
                                        Character.appendInventory().append(Necramil.getEnemyArmor())
                                        choice = False
                                    if choice2 == "return to the college":
                                        print("disgusted by the smell of the dead you return to the college in search of a healer.")
                                        choice = False
                        elif choice2 == "3":
                            choice1 = False
                            print("\"Look man I gotta get back to my class, promise ill come back after. Ill even shake on it.\"\n")
                            print("Necramil approaches and shakes your hand, a small glint can be seen flashing as he stabs you with a dagger.")
                            AttacksCharacter(Necramil)
                            print("From the your blood he summons a skeleton from his slumber as you realize you are in the catacombs with a necromancer.")
                            Skeleton = Enemy("undead", "warrior", "Skeleton", 2, Iron_Dagger, Bones, [])
                            Necramil.setEnemyMainWeapon(Shadow_Bolt)
                            choice = True
                            while choice == True:
                                if Skeleton.getEnemyHealth() > 0:
                                    print("| Attack Skeleton | Attack Necramil |")
                                else:
                                    print("| Attack Necramil |")
                                choice3 = input("> ").lower()
                                checkAllCommands(choice3)
                                if choice3 == "attack skeleton":
                                    Action(intellectMod, Skeleton)
                                    AttacksCharacter(Necramil)
                                elif choice3 == "attack necramil":
                                    if Skeleton.getEnemyHealth() > 0:
                                        AttacksCharacter(Skeleton)
                                    Action(intellectMod, Necramil)
                                    AttacksCharacter(Necramil)
                                if Necramil.getEnemyHealth() <= 0 and Skeleton.getEnemyHealth() <= 0:
                                    choice3 = False
                                    if Character.getHealth() <= 15:
                                        print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                                    else:
                                        print("You emerge victorious from your first encounter with a necromancer.")
                                    choice = True
                                    while choice == True:
                                        print("| Loot the Body | Return to the College |")
                                        choice2 = input("> ").lower()
                                        checkAllCommands(choice2)
                                        if choice2 == "loot the body":
                                            print(f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the body then head back to the college.")
                                            Character.appendInventory().append(Iron_Dagger)
                                            Character.appendInventory().append(Necramil.getEnemyArmor())
                                            choice = False
                                        if choice2 == "return to the college":
                                            print(
                                                "disgusted by the smell of the dead you return to the college in search of a healer.")
                                            choice = False
                elif choice2 == "attack necramil":
                    print("Without another word you viciously attack Necramil")
                    Necramil.setEnemyMainWeapon(Shadow_Bolt)
                    while Necramil.getEnemyHealth() > 0:
                        print("| 1 | Attack Necramil")
                        choice4 = input("> ").lower()
                        checkAllCommands(choice4)
                        if choice4 == "1":
                            Action(intellectMod, Necramil)
                            AttacksCharacter(Necramil)
                    if Character.getHealth() <= 15:
                        print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                    else:
                        print("You emerge victorious from your first encounter with a necromancer.")
                    choice = True
                    while choice == True:
                        print("| Loot the Bodies | Return to the College |")
                        choice2 = input("> ").lower()
                        checkAllCommands(choice2)
                        if choice2 == "loot the bodies":
                            print(f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the bodies then head back to the college.")
                            Character.appendInventory().append(Iron_Dagger)
                            Character.appendInventory().append(Necramil.getEnemyArmor())
                            choice = False
                        if choice2 == "return to the college":
                            print("disgusted by the smell of the dead you return to the college in search of a healer.")
                            choice = False
                elif choice2 == "lay down":
                    print("As you lay down on the tablet you see a malicious grin dawn upon Necramils face as he attempts to bring a dagger down on your chest.")
                    if characterRoll(strengthMod) > 15:
                        print("In the knick of time you grab his hand and toss it to the side")
                        Skeleton = Enemy("undead", "warrior", "Skeleton", 0, Iron_Dagger, Bones, [])
                    else:
                        AttacksCharacter(Necramil)
                        print("From the your blood he summons a skeleton from his slumber as you realize you are in the catacombs with a necromancer.")
                        Skeleton = Enemy("undead", "warrior", "Skeleton", 2, Iron_Dagger, Bones, [])
                    Necramil.setEnemyMainWeapon(Shadow_Bolt)
                    choice = True
                    while choice == True:
                        if Skeleton.getEnemyHealth() > 0:
                            print("| Attack Skeleton | Attack Necramil |")
                        else:
                            print("| Attack Necramil |")
                        choice3 = input("> ").lower()
                        checkAllCommands(choice3)
                        if choice3 == "attack skeleton":
                            Action(intellectMod, Skeleton)
                            AttacksCharacter(Necramil)
                        elif choice3 == "attack necramil":
                            if Skeleton.getEnemyHealth() > 0:
                                AttacksCharacter(Skeleton)
                            Action(intellectMod, Necramil)
                            AttacksCharacter(Necramil)
                        if Necramil.getEnemyHealth() <= 0 and Skeleton.getEnemyHealth() <= 0:
                            choice3 = False
                            if Character.getHealth() <= 15:
                                print("All bloodied, you release a sigh of relief and bandage your wounds until you can see a healer.")
                            else:
                                print("You emerge victorious from your first encounter with a necromancer.")
                            choice = True
                            while choice == True:
                                print("| Loot the Body | Return to the College |")
                                choice2 = input("> ").lower()
                                checkAllCommands(choice2)
                                if choice2 == "loot the body":
                                    print(f"You loot {Iron_Dagger.getName()} and {Necramil.getEnemyArmor().getName()} from the body then head back to the college.")
                                    Character.appendInventory().append(Iron_Dagger)
                                    Character.appendInventory().append(Necramil.getEnemyArmor())
                                    choice = False
                                if choice2 == "return to the college":
                                    print("disgusted by the smell of the dead you return to the college in search of a healer.")
                                    choice = False
    if Character.getHealth() < Character.getMaxHealth():
        choice = True
        visitHealer = False
        while choice == True:
            if visitHealer == False and Dummy.getEnemyHealth() >= 0:
                print("| Find the Healer | Attend Class |")
            elif visitHealer == True and Dummy.getEnemyHealth() >=0:
                print("| Attend Class |")
            elif visitHealer == False and Dummy.getEnemyHealth() < 0:
                print("| Find the Quarter Master | Find the Healer |")
            elif visitHealer == True and Dummy.getEnemyHealth() < 0:
                print("| Find the Quarter Master |")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "find the healer":
                if Character.getArmor() == Grand_Order_Robes or Character.getArmor() == Improved_Grand_Order_Robes:
                    visitHealer = True
                    print("As you approach the healer they immediatly see your wounds and begin to heal you.")
                    Character.setHealth(Character.getMaxHealth())
                    print(f"CURRENT HEALTH - {Character.getHealth()}")
                    print("Before you leave the healer tells you \"If you see that scoundril necramil tell me to give my dagger back!\"")
                    choice1 = True
                    while choice1 == True:
                        print("Offer the Dagger | Leave")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "offer the dagger":
                            choice1 = False
                            print("Oh thank you so much, here take this as a token of my gratitude.")
                            consoleDrop(Iron_Dagger)
                            print("Health Potion was added to your inventory.")
                            Character.inventory.append(Health_Potion)
                        elif answer == "leave":
                            choice1 = False
                else:
                    print("Sorry I am only able to serve members of the Grand Order, you will have to find you healing elsewhere.")
            elif answer == "attend class" and Dummy.getEnemyHealth() >= 0:
                choice = False

                questAttendClass()

            elif answer == "find the quarter master" and Dummy.getEnemyHealth() <= 0:
                print("Returning to your quest you go find the Quarter Master.")

                questQuarterMaster()

    elif Dummy.getEnemyHealth() >= 0:

        questAttendClass()

    else:
        print("Seeing as you dont have any wounds to be healed you go find the Quarter Master.")
def questQuarterMaster():
    print("\n\n\n\n\n\n\n\n\nJust as you reach the Quarter Master a man runs frantically into the building, and screams.")
    print("\n\"THE BARRIER HAS FALLEN, AND THE SKELETONS! THE SKELETONS!\"\n")
    print("As he crumples into a ball on the floor out of fear, and the Quarter Master rushes past you toward the door")
    choice = True
    while choice == True:
        print("| Rush After Him |")
        answer = input("> ").lower()
        checkAllCommands(answer)
        if answer == "rush after him":
            choice = False
            print("You burst through the main doors and take in the horrific scene that plays around you.")
            print("As the arcane barrier slowly fades a rattling of a million bones can be heard banging against its walls and many dark hoods peak out from the bubbling sea of beige.")
            print("But most terrible and twisted of all is the churning void of darkness and flesh that floats ominously above the hoard and begins to form into a humanoid shape.")
            print("You sat there frozen, but to your suprise a tug on your robes pulls you out of it. You turn to find an old, blind lady sitting down by the door taking in the scene.")
            print("Her milky eyes gaze into deep your soul, and she asks if you have a healing potion to spare.")
            choice = True
            while choice == True:
                if Health_Potion in Character.inventory:
                    print("| Offer The Potion | Decline |")
                else: print("| Tell Her You Dont Have One |")
                answer = input("> ").lower()
                checkAllCommands(answer)
                if answer == "offer the potion":
                    choice = False
                    print("\n\"Thats much better, thank you sweetie.\"")
                    print("\"Oh! I was supposed to tell you something important. Hmmm what was it.\"")
                    print("\n\"Through Ax'Altour I bansish thee, Sirus of the Inar, never return to Terradestril. \"\n")
                    print("If you werent already confused enough she falls asleep and a booming, thunderous voice snaps you back into it")
                    print("\n\"HOLD THEM OFF A BIT LONGER\"\n")
                    print("You look up and see a mass of mana surround what seems to be the Archmage of the college, Maeven")
                    choice = True
                    while choice == True:
                        print("| Rush Into The Battlefeild |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "rush into the battlefeild":
                            choice = False
                            questSkeleHoard()
                elif answer == "Decline":
                    choice = False
                    print("\"Oh that is too bad, Hmm I was supposed to tell you something but my memory is getting hazy.\"")
                    print("\n\"Through Ax'Altour I banish thee, .... of the Inar, never return to ....\"\n")
                    print("As she mumbles through the sentence she dozes off at the final words. Suddenly a thunderous voice snaps you out of it.")
                    print("\n\"HOLD THEM OFF A BIT LONGER\"\n")
                    print("You look up and see a mass of mana surround what seems to be the Archmage of the college, Maeven")
                    choice = True
                    while choice == True:
                        print("| Rush Into The Battlefeild |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "rush into the battlefeild":
                            choice = False
                            questSkeleHoard()
                elif answer == "tell her you dont have one" and Necramil.getEnemyHealth() <= 0:
                    choice = False
                    print("\"Oh thats fine sweetie, but I have something to tell you.\"")
                    print("\n\"Through Ax'Altour I bansish thee, Sirus of the Inar, never return to ....\"\n")
                    print("She dozes off before she can finish the final word. Suddenly a thunderous voice snaps you out of it.")
                    print("\n\"HOLD THEM OFF A BIT LONGER\"\n")
                    print("You look up and see a mass of mana surround what seems to be the Archmage of the college, Maeven")
                    choice = True
                    while choice == True:
                        print("| Rush Into The Battlefeild |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "rush into the battlefeild":
                            choice = False
                            questSkeleHoard()
                elif answer == "tell her you dont have one":
                    choice = False
                    print("\"Oh that is too bad, Hmm I was supposed to tell you something but my memory is getting hazy.\"")
                    print("\n\"Through Ax'Altour I banish thee, .... of the Inar, never return to ....\"\n")
                    print("As she mumbles through the sentence she dozes off at the final words. Suddenly a thunderous voice snaps you out of it.")
                    print("\n\"HOLD THEM OFF A BIT LONGER\"\n")
                    print("You look up and see a mass of mana surround what seems to be the Archmage of the college, Maeven")
                    choice = True
                    while choice == True:
                        print("| Rush Into The Battlefeild |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "rush into the battlefeild":
                            choice = False
                            questSkeleHoard()
def questSkeleHoard():
    print("\n\n\n\n\n\n\n\nAs you rush into combat along side your fellow mages your adrenaline courses agressively through your body."
          "\nYou are met with a sketeton hord of around 25 that begin to swarm you with a necromancer controlling them from behind.")
    choice = True
    while choice == True:
        if Necromancer.getEnemyHealth() <= 0 and SkeletonHord.getEnemyHealth() <= 0:
            choice = False
            questToTheTower()
        else:
            print("| 1 | Attack The Hord")
            print("| 2 | Attack The Summoner")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "1":
                if random.randint(1, 7) == 7:
                    print("You have been healed by a nearby restoration mage!")
                    Character.setHealth(Character.getHealth() + random.randint(6,9))
                    print(f"CURRENT HEALTH - {Character.getHealth()}")
                Action(intellectMod, SkeletonHord)
                if SkeletonHord.getEnemyHealth() > 0:
                    SkeletonHord.getEnemyMainWeapon().setDamage(math.trunc(SkeletonHord.getEnemyHealth() / 2))
                    AttacksCharacter(SkeletonHord)
                if SkeletonHord.getEnemyHealth() <= 7:
                    Necromancer.setEnemyMainWeapon(Lesser_Heal)
                if Necromancer.getEnemyMainWeapon() == Lesser_Heal:
                    HealsEnemy(Necromancer, SkeletonHord)
                else: AttacksCharacter(Necromancer)
            elif answer == "2":
                if random.randint(1, 7) == 7:
                    print("You have been healed by a nearby restoration mage!")
                    Character.setHealth(Character.getHealth() + random.randint(6, 9))
                    print(f"CURRENT HEALTH - {Character.getHealth()}")
                Action(intellectMod, Necromancer)
                if Necromancer.getEnemyHealth() <= 0:
                    SkeletonHord.setEnemyHealth(0)
                elif random.randint(1, 5) == 5 and SkeletonHord.getEnemyHealth() > 0:
                    Necromancer.setEnemyMainWeapon(Shadow_Bolt)
                    Character.getArmor().setRating(0)
                    print("The hord crushes you in a mass of bones and pins you to the floor.")
                    choice1 = True
                    while choice1 == True:
                        print("| Break Out |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "break out":
                            if characterRoll(strengthMod) > 9:
                                Character.getArmor().setRating(Character.getArmor().getBaseRating())
                                print("You break out of the skeletons grasp and regain your footing")
                                choice1 = False
                                if SkeletonHord.getEnemyHealth() <= 7:
                                    Necromancer.setEnemyMainWeapon(Lesser_Heal)
                            else:
                                print("You struggle to no avail")
                                AttacksCharacter(Necromancer)
                else:
                    if SkeletonHord.getEnemyHealth() > 0:
                        SkeletonHord.getEnemyMainWeapon().setDamage(math.trunc(SkeletonHord.getEnemyHealth() / 2))
                        AttacksCharacter(SkeletonHord)
                        if SkeletonHord.getEnemyHealth() > 0:
                            print(f"{SkeletonHord.getEnemyHealth()} Skeletons Remain!")
                    if SkeletonHord.getEnemyHealth() <= 7:
                        Necromancer.setEnemyMainWeapon(Lesser_Heal)
                    if Necromancer.getEnemyMainWeapon() == Lesser_Heal and SkeletonHord.getEnemyHealth() > -1:
                        HealsEnemy(Necromancer, SkeletonHord)
                    elif Necromancer.getEnemyMainWeapon() == Lesser_Heal and SkeletonHord.getEnemyHealth() <= -1:
                        Necromancer.setEnemyMainWeapon(Shadow_Bolt)
                        AttacksCharacter(Necromancer)
                    else:
                        AttacksCharacter(Necromancer)
def questToTheTower():
    print("\n\n\n\n\n\n\n\n\nAs you finish off the necromancer you feel deep tremors of the earth shaking below you.")
    print("Just before another group of skeletons reach you the ground splits, and the college becomes sundered from the mainland land as a result of Maevens spell.")
    print("Realizing the sea of skeletons cannot reach you you cheer in victory!")
    print("Yet a chill is sent down your spine as the abyssal darkness that hovers above the army begins to move, passing over the new ravine as this figure seemed to transend the mortal plane.")
    choice = True
    while choice == True:
        print("| Succumb | Resist |")
        answer = input("> ").lower()
        checkAllCommands(answer)
        if answer == "succumb":
            choice = False
            print("Your mind collapses in on itself, succumbing to the twisted dark abyss of Sirus's perversions")
            unlockSirus = True
        if answer == "resist":
            choice = False
            if characterRoll(charismaMod) <= 1:
                print("Your mind collapses in on itself, succumbing to the twisted dark abyss of Sirus's perversions")
                print("You have failed")
                unlockSirus = True
            else:
                looted = False
                print("Through great effort you force the dark being out of your mind and it passes over you seeminly making an attempt at the college.")
                choice = True
                while choice == True:
                    if looted == False:
                        print("| Follow After The Darkness | Loot The Bodies |")
                    elif looted == True:
                        print("| Follow After The Darkness |")
                    answer = input("> ").lower()
                    checkAllCommands(answer)
                    if answer == "loot the bodies":
                        looted = True
                        Skeleton = Enemy("Skeleton", "warrior", "Skeleton", 1, Iron_Sword, Bones, [])
                        if random.randint(0,1) == 1 or random.randint(0,1) == 1:
                            Character.appendInventory().append(Enchanted_Robes)
                            print("You find enchanted robes that seem to enhance intelligence. Along with a large health potion.")
                            print("Just before you are about to guzzle the much needed potion, you hear the rattle of bones behind you.")
                            if characterRoll(strengthMod) > 9:
                                print("You deftly dodge out of the way of the skeletons sneak attack.")
                            else:
                                AttacksCharacter(Skeleton)
                                AttacksCharacter(Skeleton)
                            choice1 = True
                            while choice1 == True:
                                print("| Attack |")
                                answer = input("> ").lower()
                                checkAllCommands(answer)
                                if answer == "attack":
                                    if Character.getMainWeapon() != soulBindingDagger:
                                        Action(strengthMod, Skeleton)
                                        print("This soul has already been bound.")
                                    else:
                                        Action(intellectMod, Skeleton)
                                    if Skeleton.getEnemyHealth() > 0:
                                        AttacksCharacter(Skeleton)
                                    else:
                                        choice1 = False
                                        print("You finish your health potion without interruption.")
                                        Character.setHealth(Character.getMaxHealth())
                        else:
                            Character.appendInventory().append(soulBindingDagger)
                            print("You find a soul binding dagger with mysterious enchants you cant quite figure out. Along with a large health potion.")
                            print("Just before you are about to guzzle the much needed potion, you hear the rattle of bones behind you.")
                            if characterRoll(strengthMod) > 9:
                                print("You deftly dodge out of the way of the skeletons sneak attack.")
                            else:
                                AttacksCharacter(Skeleton)
                                AttacksCharacter(Skeleton)
                            choice1 = True
                            while choice1 == True:
                                print("| Attack |")
                                answer = input("> ")
                                checkAllCommands(answer)
                                if Character.getMainWeapon() == soulBindingDagger:
                                    Action(strengthMod, Skeleton)
                                    print("This soul has already been bound.")
                                else:
                                    Action(intellectMod, Skeleton)
                                if Skeleton.getEnemyHealth() > 0:
                                    AttacksCharacter(Skeleton)
                                else:
                                    choice1 = False
                                    print("You finish your health potion without interruption.")
                                    Character.setHealth(Character.getMaxHealth())
                    elif answer == "follow after the darkness" and  looted == False:
                        print("As you valiantly chase after the darkness without hesitation a restoration healer heals you for half of your max health.")
                        Character.setHealth(Character.getMaxHealth() / 2)
                        if Character.getHealth() > Character.getMaxHealth():
                            Character.setHealth(Character.getMaxHealth())

                        questFinalBattle("early")

                    elif answer == "follow after the darkness" and looted == True:
                        print("You begin to chase after the darkness in hopes destory it.")

                        questFinalBattle("late")
def questFinalBattle(x):
    Roll = characterRoll(strengthMod)
    if x == "early":
        Roll + 5
    if Roll >= 10:
        timing = "early"
    else: timing = "late"
    Amulet = False
    if timing == "early":
        print("\n\n\n\n\n\n\nYou make it to the top of the college where a spent Maeven lays nearly unconsious. ")
        print("Your fellow mages have slowed the dark figure significantly, but now he nears the top of the tower.")
        print("Looking back out at the sea of skeletons you realize that they have been attacked from behind by a warrior group unknown to you.")
        choice = True
        while choice == True:
            print("| Talk To Maeven | Prepair For The Darkness |")
            answer = input("> ").lower()
            if answer == "talk to maeven":
                choice = False
                Amulet = True
                print("\n\"Mage ... .... take this.... you must stop Sirus...\"\n")
                print("Just before Maeven passes out he hands you an intricate amulet that you equip.")
                if Character.getRace() == "norsil":
                    Nature_Bolt.setDamage(Nature_Bolt.getDamage() + 1)
                    print(f"The Amulet violently increases you mana control and boosts the damage capabilities of Nature Bolt.")
                elif Character.getRace() == "man":
                    Frost_Bolt.setDamage(Frost_Bolt.getDamage() + 1)
                    print(f"The Amulet violently increases you mana control and boosts the damage capabilities of Frost Bolt.")
                elif Character.getRace() == "solsil":
                    Fireball.setDamage(Fireball.getDamage() + 1)
                    print(f"The Amulet violently increases you mana control and boosts the damage capabilities of Fireball.")
                print("\n\n\"Cower mortal in the presence of your new lord Sirus.\"")
                if characterRoll(charismaMod) > 8:
                    choice = True
                    print("You fight through your fear and resist Sirus's words.")
                    while choice == True:
                        print("| Kneel To Sirus | Attack Sirus |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "kneel to sirus":
                            choice = False
                            print("\"Such feeble minds.\"")
                            print("Sirus with attention now turned on Maevens unconsious body attempts to rip his soul straight from his physical body.")
                            choice = True
                            while choice == True:
                                print("| Sneak Attack |")
                                answer = input("> ").lower()
                                checkAllCommands(answer)
                                if answer == "sneak attack":
                                    choice = False
                                    if Character.getMainWeapon() == soulBindingDagger:
                                        Sirus.setEnemyHealth(Sirus.getEnemyHealth() - 6)
                                        print("You CRITICALLY STRUCK SIRUS for 6!")
                                        print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                        questMageSirusCombat("SoulBound")
                                    else:
                                        Sirus.setEnemyHealth(Sirus.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2))
                                        print(f"You CRITICALLY STRUCK SIRUS for {Character.getMainWeapon().getDamage() * 2}!")
                                        print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                        questMageSirusCombat("")

                        elif answer == "attack sirus":
                            choice = False
                            questMageSirusCombat("")
                else:
                    print("Your soul cant help but cower, once you collect enough courage you turn and see Sirus hunched over Maeven and taking his soul.")
                    Maeven.setEnemyHealth(41)
                    print("MAEVEN CURRENT HEALTH - 41")
                    choice = True
                    while choice == True:
                        print("| Sneak Attack |")
                        answer = input("> ").lower()
                        checkAllCommands(answer)
                        if answer == "sneak attack":
                            choice = False
                            if Character.getMainWeapon() == soulBindingDagger:
                                Sirus.setEnemyHealth(Sirus.getEnemyHealth() - 6)
                                print("You CRITICALLY STRUCK SIRUS for 6!")
                                print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                questMageSirusCombat("SoulBound")
                            else:
                                Sirus.setEnemyHealth(Sirus.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2))
                                print(f"You CRITICALLY STRUCK SIRUS for {Character.getMainWeapon().getDamage() * 2}!")
                                print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                questMageSirusCombat("")
            elif answer == "prepair for the darkness":
                choice = False
                print("Thinking quickly you decide to hide Maevens body inside of a nearby crate and you yourself feign death where his body was in hopes to catch the darkness off guard")
                print("Trying your hardest to act dead, your heart rate quickens as an overwhelming sense of fear grows within you from the presense of this darkness.")
                choice = True
                while choice == True:
                    print("| Attack | Wait For Him To Come Closer |")
                    answer = input("> ").lower()
                    checkAllCommands(answer)
                    if answer == "wait for him to come closer":
                        choice = False
                        if characterRoll(charismaMod) > 5:
                            print("You sucsessfully calm yourself down and the darkness nears.")
                            print("As you begin to feel its crooked breathing upon your face you realize this is your moment.")
                            choice = True
                            while choice == True:
                                print("| 1 | Sneak Attack")
                                answer = input("> ").lower()
                                checkAllCommands(answer)
                                if answer == "1":
                                    if Character.getMainWeapon() == soulBindingDagger:
                                        Sirus.setEnemyHealth(Sirus.getEnemyHealth() - 6)
                                        print("You CRITICALLY STRUCK SIRUS for 6!")
                                        print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                        questMageSirusCombat("SoulBound")
                                    else:
                                        Sirus.setEnemyHealth(Sirus.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2))
                                        print(f"You CRITICALLY STRUCK SIRUS for {Character.getMainWeapon().getDamage() * 2}!")
                                        print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                                        questMageSirusCombat("")
                        else:
                            print("You are unable to compose yourself and Sirus notices your presense.")
                            questMageSirusCombat("")
                    elif answer == "attack":
                        questMageSirusCombat("")
    elif timing == "late":
        print("\n\n\n\n\n\n\nYou finally make to the highest tower in the College to see Sirus hunched over Maevens unconsious body.\nSirus is seemingly siphoning his soul from maevens body")
        choice = True
        while choice == True:
            print("| Sneak Attack |")
            answer = input("> ").lower()
            checkAllCommands(answer)
            if answer == "sneak attack":
                if Character.getMainWeapon() == soulBindingDagger:
                    Sirus.setEnemyHealth(Sirus.getEnemyHealth() - 6)
                    print("You CRITICALLY STRUCK SIRUS for 6!")
                    print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                    questMageSirusCombat("SoulBound")
                else:
                    Sirus.setEnemyHealth(Sirus.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2))
                    print(f"You CRITICALLY STRUCK SIRUS for {Character.getMainWeapon().getDamage() * 2}!")
                    print(f"SIRUS CURRENT HEALTH {Sirus.getEnemyHealth()}")
                    questMageSirusCombat("")
def questMageSirusCombat(x):
    if Character.getArmor() == Enchanted_Robes:
        Character.setIntellect(Character.getIntellect() + 2)
    if x == "SoulBound":
        Sirus.setEnemyEffect("Bind")
        Sirus.setEnemyArmor(Bones)
        print("\n\n\n\n\n\n\nSirus lets out a painful howl as the daggers enchantment takes effect.")
        print("He plucks the dagger from his back and sends it flying into the ocean.")
        print("He belts curses and turns toward you, eyes alight with vengance and fury.")
        print("You feel no fear, for it is as if the dagger has stripped him of his godlike powers temporarily.")
    if x == "":
        print("\n\n\n\n\n\n\nSirus turns toward you, his beady crimson eyes stare into your soul alight with vengance and fury.")
        if characterRoll(charismaMod) < 9:
            print("You have been frozen in fear, when you regain your thoughts Sirus is back to work on Maeven")
            Maeven.setEnemyHealth(Maeven.getEnemyHealth() - 5)
        else:
            print("Fighting against your primal urge to run you face Sirus and prepair to attack")
    if True:
        Distance = 0
        choice = True
        advantage = 0
        while choice == True:
            if advantage == 1:
                choice2 = True
                while choice2 == True:
                    print("| Sneak Attack |")
                    answer = input("> ")
                    checkAllCommands(answer)
                    if answer == "sneak attack":
                        choice2 = False
                        advantage = 0
                        Sirus.setEnemyHealth(Sirus.getEnemyHealth() - (Character.getMainWeapon().getDamage() * 2))
                        print("\nYou have landed a sneak attack on sirus!")
                        print(f"SIRUS CURRENT HEALTH - {Sirus.getEnemyHealth()}\n")
            print("| 1 | Attack Sirus")
            if Distance != 0:
                print("| 2 | Move Away From The Edge")
            answer = input("> ")
            checkAllCommands(answer)
            if answer == "2" and Distance != 0:
                Distance = 0
                print("You move away from the edge of the tower.")
                Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                print("Sirus rips Mavens soul further from his body.")
                print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                if Maeven.getEnemyHealth() <= 0:
                    print("You have failed to save Maeven")
                    restartGame()
            if answer == "1":
                temp = Sirus.getEnemyHealth()
                Action(intellectMod,Sirus)
                if Sirus.getEnemyHealth() <= 0:
                    questFinalMoments()
                if temp == Sirus.getEnemyHealth():
                    tempNum = random.randint(1,4)
                    if tempNum == 4:
                        turns = 0
                        print("Sirus summons two skeletons to deal with you.")
                        SirusSkeleton1 = Enemy("Skeleton", "warrior", "Skeleton", 1 ,Iron_Sword, Iron_Armor, [])
                        SirusSkeleton2 = Enemy("Skeleton", "warrior", "Skeleton", 1 ,Iron_Sword, Iron_Armor, [])
                        choice1 = True
                        while choice1 == True:
                            turns += 1
                            print("| 1 | Attack The Skeletons | 2 | Attack Sirus ")
                            answer = input("> ")
                            checkAllCommands(answer)
                            if answer == "1":
                                if SirusSkeleton2.getEnemyHealth() <= 0:
                                    Action(intellectMod, SirusSkeleton1)
                                    if SirusSkeleton1.getEnemyHealth() > 0:
                                        AttacksCharacter(SirusSkeleton1)
                                    else:
                                        if turns == 2:
                                            print("You cleared the skeletons faster then Sirus expected.")
                                            advantage = 1
                                        choice1 = False
                                else:
                                    Action(intellectMod, SirusSkeleton2)
                                    AttacksCharacter(SirusSkeleton1)
                                    if SirusSkeleton2.getEnemyHealth() > 0:
                                        AttacksCharacter(SirusSkeleton2)
                            elif answer == "2":
                                Action(intellectMod, Sirus)
                                if Sirus.getEnemyHealth() <= 0:
                                    questFinalMoments()
                                turns -= 1
                                if SirusSkeleton1.getEnemyHealth() > 0:
                                    AttacksCharacter(SirusSkeleton1)
                                if SirusSkeleton2.getEnemyHealth() > 0:
                                    AttacksCharacter(SirusSkeleton2)
                            if turns == 3 or turns == 5 or turns == 7 or turns >= 9:
                                Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                                print("Sirus rips Mavens soul further from his body.")
                                print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                                if Maeven.getEnemyHealth() <= 0:
                                    print("You have failed to save Maeven")
                                    restartGame()
                    elif tempNum == 3:
                        print("Sirus faces his clawed hand toward you and emits a forceful blast.")
                        choice1 = True
                        while choice1 == True:
                            print("| Stand Your Ground |")
                            answer = input("> ")
                            checkAllCommands(answer)
                            if answer == "stand your ground":
                                tempRoll = characterRoll(strengthMod)
                                if tempRoll >= 18:
                                    print("You shrug off his blast as if it were a gentle breeze.")
                                    advantage = 1
                                elif tempRoll <= 17 and tempRoll >= 15:
                                    print("You push through the blast only moving back slightly")
                                    Distance += 1
                                elif tempRoll <= 14 and tempRoll >= 10:
                                    print("You brace yourself for the impact and it moves back toward the edge of the tower.")
                                    Distance += 2
                                elif tempRoll <= 9 and tempRoll >= 2:
                                    print("You brace yourself as the blast hits you full force moving you consiterably closer to the edge of the tower.")
                                    Distance += 3
                                else:
                                    print("The blast causes you to lose your footing as you grovel for something to grab onto to stop yourself from flying back to your death.")
                                    Distance += 5
                                if Distance == 3 or Distance == 4:
                                    print("You are nearing the edge of the tower.")
                                elif Distance >= 5:
                                    print("Just before you fall off the tower you manage to grab into the edge of the platform.")
                                    choice2 = True
                                    while choice2 == True:
                                        print("| Attempt To Pull Yourself Up |")
                                        answer = input("> ")
                                        checkAllCommands(answer)
                                        if answer == "attempt to pull yourself up":
                                            if characterRoll(strengthMod) > 14:
                                                print("You just manage to pull yourself back onto the tower.")
                                                Distance = 4
                                                choice2 = False
                                            else:
                                                print("You fall to your death.")
                                                restartGame()
                                choice1 = False
                    elif tempNum == 2:
                        illusionSwitch = random.randint(0,1)
                        print("In your mind you can sense that Sirus has tried to invade.")
                        if characterRoll(intellectMod) >= 18:
                            print("You see right through the illusion.")
                            if illusionSwitch == 0:
                                print("You sense that Sirus has failed to invade your mind.")
                            else:
                                print("You sense that Sirus has switched the positions of himself and Maeven in your mind.")
                        else:
                            print("Weary of an illusion you come to a crossroads")
                        choice1 = True
                        while choice1 == True:
                            print("| Attack Sirus | Attack Maeven | Wait It Out |")
                            answer = input("> ").lower()
                            checkAllCommands(answer)
                            if answer == "attack sirus":
                                if illusionSwitch == 0:
                                    Action(intellectMod, Sirus)
                                    print("Looks like your gut was right. The illusion fades")
                                    print("You inturrupt Sirus's spell")
                                    choice1 = False
                                    if Sirus.getEnemyHealth() <= 0:
                                        questFinalMoments()
                                else:
                                    Action(intellectMod, Maeven)
                                    print("Looks like your gut was wrong. The illusion fades")
                                    Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                                    print("Sirus rips Mavens soul further from his body.")
                                    print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                                    if Maeven.getEnemyHealth() <= 0:
                                        print("You have failed to save Maeven")
                                        restartGame()
                                    choice1 = False
                            elif answer == "attack maeven":
                                if illusionSwitch == 0:
                                    Action(intellectMod, Maeven)
                                    print("Looks like your gut was wrong. The illusion fades")
                                    Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                                    print("Sirus rips Mavens soul further from his body.")
                                    print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                                    if Maeven.getEnemyHealth() <= 0:
                                        print("You have failed to save Maeven")
                                        restartGame()
                                    choice1 = False
                                else:
                                    Action(intellectMod, Sirus)
                                    print("Looks like your gut was right. The illusion fades")
                                    print("You inturrupt Sirus's spell")
                                    choice1 = False
                                    if Sirus.getEnemyHealth() <= 0:
                                        questFinalMoments()
                            elif answer == "wait it out":
                                Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                                print("Sirus rips Mavens soul further from his body.")
                                print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                                if Maeven.getEnemyHealth() <= 0:
                                    print("You have failed to save Maeven")
                                    restartGame()
                                print("You take a second to search your mind.")
                                if illusionSwitch == 0:
                                    print("You sense that Sirus has failed to invade your mind.")
                                else:
                                    print( "You sense that Sirus has switched the positions of himself and Maeven in your mind.")
                    elif tempNum == 1:
                        turns = 0
                        print("Sirus breifly takes his eyes off Maeven to brand you with their seering crimson stare.")
                        choice1 = True
                        while choice1 == True:
                            print("| Resist |")
                            answer = input("> ").lower()
                            checkAllCommands(answer)
                            if answer == "resist":
                                if turns == 0 and characterRoll(charismaMod) >= 17:
                                    print("You stare Sirus down uneffected by his gaze")
                                    advantage = 1
                                    choice1 = False
                                elif characterRoll(charismaMod) > random.randint(3,10):
                                    turns += 1
                                    choice1 = False
                                    print("You shake off your crippling fear and regain your senses.")
                                else:
                                    turns += 1
                                    print("Unable to shake the image from your head you cower in fear.")
                                    Maeven.setEnemyHealth(Maeven.getEnemyHealth() - Sirus.getEnemyMainWeapon().getDamage())
                                    print("Sirus rips Mavens soul further from his body.")
                                    print(f"MAEVEN CURRENT HEALTH - {Maeven.getEnemyHealth()}")
                                    if Maeven.getEnemyHealth() <= 0:
                                        print("You have failed to save Maeven")
                                        restartGame()
                elif Sirus.getEnemyEffect() == "bind":
                    AttacksCharacter(Sirus)
                elif Sirus.getEnemyHealth() <= 0:
                    questFinalMoments()
                else:
                    print("Do not interfere with the inevitable mortal.")
                    print("Your futile efforts will only prolong this splended night.")
def questFinalMoments():
    print("or so you thought.\n\n\n\n")
    print("\nWith horrendous sounds you cant even begin to decipher Sirus's physical body bursts and blots out the night sky with an unnatural energy.")
    print("\nHe begins to speak directly into your consious, thousands, millions of words none of which are comprehensible.")
    print("\nJust before you lose your sanity a angelic being shatters through the darkness and locks into combat with Sirus.")
    print("\nThis being is actually a man, a warrior emminating the effigy even the avatar of the Ainar Mograin, the Titan who who was able to cut the hand off of the god Kirash.")
    print("\nAs they clashed you couldnt help but take in the beauty of the warriors every move.\nHis movements incredibly fluid and deadly.\nHis mind able to keep up with the vicious attacks Sisrus sent forth.\nHis emotions calm and collected waiting for an opening.")
    print("\nThis battle was truly an equal fight, but an effigy of a Ainar can only keep up for so long against the Greatest Inar, Sirus.")
    print("\nYou could see the effigy fading and Sirus beginning to grow in malice as he forsaw his victory.\n\n")
    print("\nAfter long hours the effigy was reduced back into a mere man who still stood his ground firmly against such a vile being.")
    print("\nWith the final blow Sirus sunk his blade deep into the mans chest. The Sun of Heli rose above the skyline earlier than usual crippling Sirus.")
    print("\nThe fatally wounded warrior pulled himself up Sirus's blade to embrace him.")
    print("\"NOW MAGE! BANISH HIM!\"")
    chance = 0
    finalChoice = True
    while finalChoice == True:
        chance += 1
        answer = input("> ").lower()
        if answer == "through ax'altour i bansish thee, sirus of the inar, never return to terradestril." or "through ax'altour i bansish thee sirus of the inar never return to terradestril" or "through ax'altour i bansish thee, sirus of the inar never return to terradestril." or "through ax'altour i bansish thee sirus of the inar, never return to terradestril.":
            print("\n\"THROUGH AX'ALTOUR I BANISH THEE, SIRUS OF THE INAR, NEVER RETURN TO TERRADESTRIL.\"\n")
            print("It was finished, with a terrible shriek heard all across Terradestril Sirus of the Inar was sent back to the abyssal realm.")
            print("The College of Arcanum alog with its Archmage was saved, and the rift between mages and warriors was broken all thanks to your work.")
            print(f"Congradulations {Character.getName()} you have fulfulled your destiny. Thank you for playing my game :)")
        elif chance == 2:
            restartGame()
        else:
            print("\"I CANT HOLD HIM HERE FOR MUCH LONGER!\"")
def restartGame():
    print("YOU HAVE FAILED")
    print("| RESTART GAME |")
    choice = True
    while choice == True:
        answer = input("> ").lower()
        if answer == "restart game":
            Character.appendInventory().clear()
            startGame()




startGame()





