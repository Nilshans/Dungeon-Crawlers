import random

def monster(mon):
    if (mon == 'sp'):
        mon_stat = {'monster': 'Giant spider', 'stats':(7, 1, 1, 3)}
    elif (mon == 'tr'):
        mon_stat = {'monster': 'Troll', 'stats':(4, 2, 3, 3)}
    elif (mon == 'sk'):
        mon_stat = {'monster': 'Skeleton', 'stats':(6, 3, 4, 4)}
    elif (mon == 'or'):
        mon_stat = {'monster': 'Orc', 'stats':(2, 4, 7, 2)}
    return mon_stat

def character(char):

    if (char == 'pl'):
        char_stat = {'character': 'Paladin', 'stats': (5, 9, 6, 4), 'special': 'shield'}
    elif (char == 'wi'):
        char_stat = {'character': 'Wizard', 'stats': (6, 4, 9, 5), 'special': 'flashlight'}
    elif (char == 'ro'):
        char_stat = {'character': 'Rogue', 'stats': (7, 5, 5, 7), 'special': 'doubleDamage'}
    return char_stat

def rngjesus(att, agi):
    damage = 0
    luck = 0
    while(att > 0):
        damage += random.randint(1,7)
        att -= 1
    while(agi > 0):
        luck += random.randint(1,7)
        agi -= 1
    if (damage >= luck):
        print(f"damage: {damage} luck: {luck}")
        return True
    else:
        print(f"damage: {damage} luck: {luck}")
        return False

def charAttack(mon, char, mon_hp):
    dialog2 = f"{character(char)['character']} attacks the {monster(mon)['monster']} and deals 1 damage\n"
    dialog5 = f"{character(char)['character']} deals double damage\n"
    dialog9 = f"{monster(mon)['monster']} meet its end by the hand of the {character(char)['character']}\n"
    dialog10 = f"{monster(mon)['monster']} dodges {character(char)['character']}s attack\n"

    rogueSpecial = 1#random.randint(1,2)
    if (rogueSpecial == 1):
        rng = True
    else:
        rng = False

    if (character(char)['special'] == 'doubleDamage' and rng == True):
        if (rngjesus(character(char)['stats'][2],monster(mon)['stats'][3]) == True): # mon_hp -= character(char)['stats'][2] * 2
            mon_hp -= 2
            if (mon_hp <= 0):
                print (dialog5) # Character deals double damage
                print (dialog9) # Monster dies
                #break
            else:
                print (dialog5) # Character deals double damage
                print (f"Hp left: {mon_hp}\n")
        else:
            print (dialog10) # Monster dodges attack
    else:
        if (rngjesus(character(char)['stats'][2],monster(mon)['stats'][3]) == True):
            mon_hp -= 1
            if (mon_hp == 0):
                print(dialog2) # Character attacks normally
                print (dialog9) # Monster dies
                #break
            else:
                print(dialog2) # Character attacks normally
                print (f"Hp left: {mon_hp}\n")
        else:
            print (dialog10) # Monster dodges attack
    return mon_hp

def monAttack(initiative, mon, char, special, char_hp):
    dialog3 = f"{monster(mon)['monster']} takes the initiative and attack first\n"
    dialog4 = f"{character(char)['character']} blocks attack with his shield\n"
    dialog7 = f"{character(char)['character']} takes 1 damage but still stands\n"
    dialog8 = f"{character(char)['character']} takes 1 damage and meet his end\n"
    dialog11 = f"{character(char)['character']} dodges {monster(mon)['monster']}s attack\n"
    dialog12 = f"{monster(mon)['monster']} attacks {character(char)['character']} 1 damage\n"

    if (initiative == 'first'):
        print (dialog3) # Monster attacks first
        if (character(char)['special'] == 'shield' and special == True):
            print (dialog4) # Character blocks attack
            special = False
        else:
            if (rngjesus(monster(mon)['stats'][2],character(char)['stats'][3]) == True): # Throw dice, mon attack / char agil
                char_hp -= 1
                if (char_hp == 0):
                    print (dialog8) # Character dies
                    #break
                print (dialog7) # Character takes damage
                print (f"Hp left: {char_hp}\n")
            else:
                print (dialog11)
    else:
        if (character(char)['special'] == 'shield' and special == True):
            print (dialog4) # Character blocks attack
            special = False
            if (rngjesus(monster(mon)['stats'][2],character(char)['stats'][3]) == True):
                char_hp -= 1
                if (char_hp == 0):
                    print (dialog8) # Character dies
                    #break
                else:
                    print(dialog12)
                    print (f"Hp left: {char_hp}\n")
            else:
                print (dialog11)
        else:
            if (rngjesus(monster(mon)['stats'][2],character(char)['stats'][3]) == True):
                char_hp -= 1
                if (char_hp == 0):
                    print (dialog8) # Character dies
                    #break
                else:
                    print(dialog12)
                    print (f"Hp left: {char_hp}\n")
            else:
                print (dialog11)
    return {'hp':char_hp, 'special':special}


def fightOrFlight(mon, char):
    #rngjesus(mon, char)
    special = True
    mon_initiative = False
    if (rngjesus(monster(mon)['stats'][0],character(char)['stats'][0]) == True):
        mon_initiative = True

    mon_hp = monster(mon)['stats'][1]
    char_hp = character(char)['stats'][1]

    dialog1 = f"You encounter a {monster(mon)['monster']}\n"
    dialog6 = f"{character(char)['character']} brights up the room with a spell and escapes\n"
    print (dialog1) # Character encounters a monster

    while (mon_hp > 0 and char_hp > 0):
        print(f"Monster HP: {mon_hp}  Character HP: {char_hp}")
        while True:
            choise = input(f"Will you attack (a) or run (r)? \n")
            if (choise != 'a' and choise != 'r'):
                print("answer should be 'a' or 'r' ")
                continue
            else:
                break

        if (choise == 'a'): # Character attacks

            if (mon_initiative == True):
                char_hp = monAttack('first', mon, char,special, char_hp)['hp']
                special = monAttack('second', mon, char,special, char_hp)['special']
                if (char_hp > 0):
                    mon_hp = charAttack(mon, char, mon_hp)
                else:
                    break
            else:
                mon_hp = charAttack(mon, char, mon_hp)
                if (mon_hp > 0):
                    char_hp = monAttack('second', mon, char,special, char_hp)['hp']
                    special = monAttack('second', mon, char,special, char_hp)['special']
                else:
                    break

        elif (choise == 'r'): # Character tries to run
            if (monster(mon)['stats'][0] < character(char)['stats'][0]):
                print("your escape was successful")
            if (character(char)['special'] == 'flashlight' and special == True):
                print (dialog6) # Character use flashlight to escape
                special = False
                break
            else:
                print("You cant run from this battle, fight!")

#tr = Troll | sk = Skeleton | sp = Giant spider | or = Orc
#pl = Paladin | wi = Wizard | ro = Rogue
def main():
    fightOrFlight('or', 'pl')

if __name__ == "__main__":
    main()
