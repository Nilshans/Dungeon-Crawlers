def monster(mon):
    if (mon == 'sp'):
        mon_stat = {'monster': 'Giant spider', 'stats':(7, 1, 2, 4)}
    elif (mon == 'tr'):
        mon_stat = {'monster': 'Troll', 'stats':(7, 1, 2, 4)}
    elif (mon == 'sk'):
        mon_stat = {'monster': 'Skeleton', 'stats':(7, 1, 2, 4)}
    elif (mon == 'or'):
        mon_stat = {'monster': 'Orc', 'stats':(7, 1, 2, 4)}
    return mon_stat

def character(char):

    if (char == 'pl'):
        char_stat = {'character': 'Paladin', 'stats': (5, 9, 6, 4), 'special': 'shield'}
    elif (char == 'wi'):
        char_stat = {'character': 'Wizard', 'stats': (5, 9, 6, 4), 'special': 'flashlight'}
    elif (char == 'ro'):
        char_stat = {'character': 'Rogue', 'stats': (5, 9, 6, 4), 'special': 'doubleDamage'}
    return char_stat

def fightOrFlight(mon, char):
    special = True
    mon_hp = monster(mon)['stats'][1]
    char_hp = character(char)['stats'][1]

    dialog1 = f"You encounter a {monster(mon)['monster']}\n"
    dialog2 = f"You attack the {monster(mon)['monster']} for {character(char)['stats'][2]} damage\n"
    dialog3 = f"{monster(mon)['monster']} takes the initiative and attack\n"
#specials
    dialog4 = f"{character(char)['character']} blocks attack with his shield\n"
    dialog5 = f"{character(char)['character']} deals double damage with his first blow\n"
    dialog6 = f"{character(char)['character']} brights up the room with a spell and escapes\n"

    print (dialog1) #Character encounters a monster
    while True:
        choise = input(f"Will you attack (a) or run (r)? \n")
        if (choise != 'a' and choise != 'r'):
            print("answer should be 'a' or 'r' ")
            continue
        else:
            break
    if (choise == 'a'): #character attacks
        if (monster(mon)['stats'][0] > character(char)['stats'][0]):
            print (dialog3) #Monster attacks first
        if (character(char)['special'] == 'shield' and special == True):
            print (dialog4) # Character blocks attack
            special = False
        if (character(char)['special'] == 'doubleDamage' and special == True):
            print (dialog5) # Character deals double damage
            special = False
        else:
            print(dialog2) #character attacks normally

    elif (choise == 'r'): #character tries to run
        if (monster(mon)['stats'][0] < character(char)['stats'][0]):
            print("your escape was successful")
        if (character(char)['special'] == 'flashlight' and special == True):
            print (dialog6) # Character use flashlight to escape
            special = False
        else:
            print("You cant run from this battle, fight!")

#tr = Troll | sk = Skeleton | sp = Giant spider | or = Orc
#pl = Paladin | wi = Wizard | ro = Rogue
def main():
    fightOrFlight('sp', 'wi')

if __name__ == "__main__":
    main()
