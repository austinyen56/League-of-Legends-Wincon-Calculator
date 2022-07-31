'''
League of Legends Wincon Calculator v2.4 @austinyen56
All stats are from the RiotWatcher API, LCU API, (leagueofgraphs.com/champions/), and (na.op.gg/champion/statistics)

Displays checks for matchup, healing, cc, and damage type
'''
from typing import List
import championdb as champion
import os
import pyperclip
import sys
import ritoapi

# Initialzing variables blue1 - blue5, red1 - red5
b1, b2, b3, b4, b5 = ["" for _ in range(5)]
r1, r2, r3, r4, r5 = ["" for _ in range(5)]

print("=============== LoL Wincon Calculator v2.4 @austinyen56 ===============")
print("------Please type everything in lowercase in one word---------\n")

# -----------------Sorting team comp-------------
# Checking if the player is first pick (Will know which side and therefore pick order)
whatpick = True
pick = ""
pickString = ""
while whatpick:
    p = input("Are you first pick? (yes/no): ")
    if p == "yes" or p == "no":
        pick = p
        whatpick = False
        if p == 'yes':
            pickString = 'blue side'
        if p == 'no':
            pickString = 'red side'
    else:
        print("Type 'yes' or 'no', try again")
        continue
# Blue left red right
playerPrint = ["Enter ally 1: ", "Enter enemy 1: ", "Enter enemy 2: ", "Enter ally 2: ", "Enter ally 3: ",
               "Enter enemy 3: ", "Enter enemy 4: ", "Enter ally 4: ", "Enter ally 5: ", "Enter enemy 5: "]
champPrintB = []
champPrintR = []

# First Pick Order
def fp():
    global playerPrint
    print("You are on blue side")
    b1 = champion.checkChamp(playerPrint[0])
    r1 = champion.checkChamp(playerPrint[1])
    r2 = champion.checkChamp(playerPrint[2])
    b2 = champion.checkChamp(playerPrint[3])
    b3 = champion.checkChamp(playerPrint[4])
    r3 = champion.checkChamp(playerPrint[5])
    r4 = champion.checkChamp(playerPrint[6])
    b4 = champion.checkChamp(playerPrint[7])
    b5 = champion.checkChamp(playerPrint[8])
    r5 = champion.checkChamp(playerPrint[9])
    # print(b1, "..............", r1)
    # print(b2, "..............", r2)
    # print(b3, "..............", r3)
    # print(b4, "..............", r4)
    # print(b5, "..............", r5)
    champPrintB.extend([b1, b2, b3, b4, b5])
    champPrintR.extend([r1, r2, r3, r4, r5])

# Second Pick Order
def sp():
    global playerPrint
    print("You are on red side")
    r1 = champion.checkChamp(playerPrint[1])
    b1 = champion.checkChamp(playerPrint[0])
    b2 = champion.checkChamp(playerPrint[3])
    r2 = champion.checkChamp(playerPrint[2])
    r3 = champion.checkChamp(playerPrint[5])
    b3 = champion.checkChamp(playerPrint[4])
    b4 = champion.checkChamp(playerPrint[7])
    r4 = champion.checkChamp(playerPrint[6])
    r5 = champion.checkChamp(playerPrint[9])
    b5 = champion.checkChamp(playerPrint[8])
    # print(b1, "..............", r1)
    # print(b2, "..............", r2)
    # print(b3, "..............", r3)
    # print(b4, "..............", r4)
    # print(b5, "..............", r5)
    champPrintB.extend([b1, b2, b3, b4, b5])
    champPrintR.extend([r1, r2, r3, r4, r5])

# Role correction if mistyped
def roleCorrection(x):
    if x == "middle":
        print("Type 'mid' instead\n")
    if x == "bot" or x == "bottom":
        print("Type 'adc' instead\n")
    if x == "support":
        print("Type 'supp' instead\n")
    if x == "jungle":
        print("Type 'jg' instead\n")

# Clears everything in outfile just in case
open('outfile.txt', 'w').close()
# Function that ONLY prints to outfile
def ONLYprintingtoFile(*content):       
        originalOut = sys.stdout
        with open('outfile.txt', 'a+') as h:
                sys.stdout = h
                print("".join([i for i in content]))
                sys.stdout = originalOut

# Function that prints to both outfile and console
def printConsoleandOutfile(*content):
    with open('outfile.txt', 'a+') as o:
        for out in [sys.stdout, o]:
            print("".join([i for i in content]), file=out)

# Check roles for each player (Manual mode)
def roleCheck():
    global champPrintB
    champRoleB = {}
    global champPrintR
    champRoleR = {}

    # -----------------------Roles for blue---------------
    print("\n")
    print("Enter roles for Blue side")
    i = 0
    while i < len(champPrintB):
        r = input(f"What role is {champPrintB[i]}: ")
        if r == "top" or r == "mid" or r == "adc" or r == "supp" or r == "jg":
            for j in champRoleB.values():
                if r in j:
                    print("There is already a", r)
                    i -= 1
                    continue
            champRoleB[champPrintB[i]] = r
            i += 1
        else:
            print("Not a valid role")
            roleCorrection(r)
            continue

    # -----------------------Roles for red---------------
    print("\n")
    print("Enter roles for Red side")
    i = 0
    while i < len(champPrintR):
        r = input(f"What role is {champPrintR[i]}: ")
        if r == "top" or r == "mid" or r == "adc" or r == "supp" or r == "jg":
            for j in champRoleR.values():
                if r in j:
                    print("There is already a", r)
                    # Need logical fix here       currentcount = i
                    i -= 1
                    continue
            champRoleR[champPrintR[i]] = r
            i += 1
        else:
            print("Not a valid role")
            roleCorrection(r)
            continue

    # print("Blue team: ", champRoleB) #Blue team:  {'heimerdinger': 'supp', 'gwen': 'top', 'masteryi': 'jg', 'zed': 'mid', 'ezreal': 'adc'}
    # print("Red team: ", champRoleR) #Red team:  {'sona': 'supp', 'twitch': 'adc', 'morgana': 'mid', 'gragas': 'jg', 'renekton': 'top'}
    
    # ======================================= Analyitics, Calculating, and Printing =============================
    
    def formatPrintMatchup():
        pass

    print("\n")
    ONLYprintingtoFile("===============Generated from LoL Wincon Calculator v2.4 @austinyen56===============")
    printConsoleandOutfile("          =================Matchup=================")

    def get_champion_from_pos(val, x):
        for key, value in x.items():
            if val == value:
                return key

    printConsoleandOutfile("Top lane:     ", get_champion_from_pos('top', champRoleB).ljust(20, "."), "vs".center(0),
          get_champion_from_pos('top', champRoleR).rjust(20, "."))
    printConsoleandOutfile("Mid lane:     ", get_champion_from_pos('mid', champRoleB).ljust(20, "."), "vs".center(0),
          get_champion_from_pos('mid', champRoleR).rjust(20, "."))
    printConsoleandOutfile("Jungle:       ", get_champion_from_pos('jg', champRoleB).ljust(20, "."), "vs".center(0),
          get_champion_from_pos('jg', champRoleR).rjust(20, "."))
    printConsoleandOutfile("Adc:          ", get_champion_from_pos('adc', champRoleB).ljust(20, "."), "vs".center(0),
          get_champion_from_pos('adc', champRoleR).rjust(20, "."))
    printConsoleandOutfile("Supp:         ", get_champion_from_pos('supp', champRoleB).ljust(20, "."), "vs".center(0),
          get_champion_from_pos('supp', champRoleR).rjust(20, "."))

    # Clearing the list and append champions in order [top, mid, jg, adc, supp]
    champPrintB.clear()
    champPrintR.clear()
    sortroles = ['top', 'mid', 'jg', 'adc', 'supp']
    for r in sortroles:
        champPrintB.append(get_champion_from_pos(r, champRoleB))
        champPrintR.append(get_champion_from_pos(r, champRoleR))
    
    # Enable for debugging -> [top, mid, jg, adc, supp]
    print(champPrintB)
    print(champPrintR)

def autoRoleSort(side):
    #['garen', 'rammus', 'khazix', 'sivir', 'thresh'] top mid jg adc supp
    #['vladimir', 'twistedfate', 'volibear', 'ashe', 'senna']
    allyAPI, enemyAPI = ritoapi.ClientFetch()
    enemySort = {}
    enemyAPISorted = []

    i = 0
    while i < len(enemyAPI):
        print("\nPlease input the following roles for each enemy since Riot's API does not support such data:")
        eRole = input(f"What role is {enemyAPI[i]}: ")
        if eRole == "top" or eRole == "mid" or eRole == "adc" or eRole == "supp" or eRole == "jg":
            for j in enemySort.keys():
                if eRole in j:
                    print("There is already a", eRole)
                    i -= 1
                    continue
            enemySort[eRole] = enemyAPI[i]
            i += 1
        else:
            print("Not a valid role")
            roleCorrection(eRole)
            continue
    try:
        enemyAPISorted = [enemySort['top'], enemySort['mid'], enemySort['jg'], enemySort['adc'], enemySort['supp']]
    except KeyError:
        enemyAPISorted = enemySort


    if side == 'yes':
        champPrintB = allyAPI
        champPrintR = enemyAPISorted
    elif side == 'no':
        champPrintB = enemyAPISorted
        champPrintR = allyAPI
    
    return champPrintB, champPrintR

    

def manualorauto():
    global champPrintB
    global champPrintR
    modeBool = True
    while modeBool:
        mode = input("Do you want to enter champs and roles manually or automatically? (manual/auto): ")
        if mode == "manual":
            modeBool = False
            if pick == "yes":
                fp()
                roleCheck()
                printConsoleandOutfile("You are on Blue Team")

            if pick == "no":
                sp()
                roleCheck()
                printConsoleandOutfile("You are on Red Team")

        elif mode == "auto":
            modeBool = False
            champPrintB, champPrintR = autoRoleSort(pick)
            # Same as line 178, to add in the matchup stats, can consolidate/optimize in the future
            ONLYprintingtoFile("===============Generated from LoL Wincon Calculator v2.4 @austinyen56===============")
            print("")
            printConsoleandOutfile("          =================Matchup=================")
            count = 0
            for lane in ["Top    ", "Mid    ", "Jungle ", "ADC    ", "Supp    "]:
                printConsoleandOutfile(lane,":", champPrintB[count].ljust(20, "."), "vs".center(0),
                          champPrintR[count].rjust(20, "."))
                count += 1
            
        else:
            print("Not a valid input")
            continue
    return champPrintB, champPrintR


champPrintB, champPrintR = manualorauto()

#print(champPrintB)
#print(champPrintR)


# ------------------------------Calculate winrate-----------------------------
# start off with 50% wr on each side
# Check if each lane champ is getting countered or crushing others +-5% wr
# Check the amount of champions with 5+ healing, +3% wr; No champ with healing (healing <=5) -3% wr
# Check if whole team cc >= 15 (may change) +8 wr, 0 cc -8
# Check if no tanks or at least 2 fighters, -10% wr (may change)
# Check if the team has all ad or all ap -5% wr
# Consider edge cases: ex: "are u sure u want this stan-like cancerous figure to be on your team?"
# Or consider meta champs (meta champ list will be according from op.gg but its not necessarily accurate tho...)
# Add a dodge mechanism "exit the client from task manager"
BlueWR = 50
RedWR = 50

print("\n")
printConsoleandOutfile("          =================Stats=================")
#print(champPrintB)
#print(champPrintR)
# print(champion.CHAMPION.get("aatrox"))

for i in range(5):
    # Check if ally is being countered
    ctr = 5
    if (champPrintB[i] in champion.CHAMPION.get(champPrintR[i]).get("crushes") or (
            champPrintR[i] in champion.CHAMPION.get(champPrintB[i]).get("counters"))):
        printConsoleandOutfile(champPrintB[i], " might be countered by ", champPrintR[i])
        BlueWR -= 5
        RedWR += 5
        ctr -= 1
    # Check if enemy is being countered
    elif (champPrintB[i] in champion.CHAMPION.get(champPrintR[i]).get("counters") or (
            champPrintR[i] in champion.CHAMPION.get(champPrintB[i]).get("crushes"))):
        printConsoleandOutfile(champPrintB[i], " can probably beat ", champPrintR[i])
        BlueWR += 5
        RedWR -= 5
        ctr -= 1
    else:
        printConsoleandOutfile(champPrintB[i], " is an even matchup to ", champPrintR[i])

    if ctr == 0:
        print("\n")
        printConsoleandOutfile("All lanes have even matchups")

print("\n")
printConsoleandOutfile("          =================Healing Check=================")
printConsoleandOutfile("          ----------------You are on ", pickString, "----------")
BlueHealTotal = 0
RedHealTotal = 0

for i in range(5):
    BlueHealTotal += int(champion.CHAMPION.get(champPrintB[i]).get("healing"))
    RedHealTotal += int(champion.CHAMPION.get(champPrintR[i]).get("healing"))

if abs(BlueHealTotal - RedHealTotal) >= 5:
    if BlueHealTotal > RedHealTotal:
        printConsoleandOutfile("Red team might get healing reduction items")
        BlueWR += 3
        RedWR -= 3
    if BlueHealTotal < RedHealTotal:
        printConsoleandOutfile("Blue team might have to get healing reduction items")
        BlueWR -= 3
        RedWR += 3
else:
    printConsoleandOutfile("No healing reduction items are needed for either side")
printConsoleandOutfile("Blue team heal score: ", str(BlueHealTotal))
printConsoleandOutfile("Red team heal score: ", str(RedHealTotal))

print("\n")
printConsoleandOutfile("          =================CC Check=================")
printConsoleandOutfile("          ----------------You are on ", pickString, "----------")
BlueCCTotal = 0
BlueKnockupTotal = 0
RedCCTotal = 0
RedKnockupTotal = 0

for i in range(5):
    BlueCCTotal += int(champion.CHAMPION.get(champPrintB[i]).get("cc"))
    BlueKnockupTotal += int(champion.CHAMPION.get(champPrintB[i]).get("knockup"))
    RedCCTotal += int(champion.CHAMPION.get(champPrintR[i]).get("cc"))
    RedKnockupTotal += int(champion.CHAMPION.get(champPrintR[i]).get("knockup"))
err = False
if err == False:
    if BlueCCTotal >= 15:
        printConsoleandOutfile("Blue team has alot of cc, play for teamfights")
        BlueWR += 8
        err = True
    if BlueCCTotal <= 3:
        printConsoleandOutfile("Blue team has barely any cc, be careful")
        BlueWR -= 8
        err = True
    if BlueKnockupTotal >= 2:
        printConsoleandOutfile("Blue team can potentially make a wombo combo")
        BlueWR += 5
        err = True

    if RedCCTotal >= 15:
        printConsoleandOutfile("Red team has alot of cc, watch out and get picks")
        RedWR += 8
        err = True
    if RedCCTotal <= 3:
        printConsoleandOutfile("Red team has barely any cc, punish them")
        RedWR -= 8
        err = True
    if RedKnockupTotal >= 2:
        printConsoleandOutfile("Red team can potentially make a wombo combo")
        RedWR += 5
        err = True

if err == False:
    printConsoleandOutfile("Both teams have equal amount of cc")

printConsoleandOutfile("Blue team CC score: ", str(BlueCCTotal))
printConsoleandOutfile("Red team CC score: ", str(RedCCTotal))
printConsoleandOutfile("Blue team knockup score: ", str(BlueKnockupTotal))
printConsoleandOutfile("Red team knockup score: ", str(RedKnockupTotal))

print("\n")
printConsoleandOutfile("          =================Team Comp Check=================")
printConsoleandOutfile("          ----------------You are on ", pickString, "----------")
AllBlueRoles = [champion.CHAMPION.get(champPrintB[b]).get("role") for b in range(len(champPrintB))]
AllRedRoles = [champion.CHAMPION.get(champPrintR[r]).get("role") for r in range(len(champPrintR))]
BRFreq = {}
RRFreq = {}


def role_frequency(l):
    dict = {}
    for n in l:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    # print(dict)
    return dict


BRFreq = role_frequency(AllBlueRoles)
RRFreq = role_frequency(AllRedRoles)
# no tanks or 2 fighters
freq = False
if freq == False:
    if 'tank' not in BRFreq:
        if 'fighter' not in BRFreq:
            printConsoleandOutfile("Blue team has no tanks or fighters, they are very squishy")
            freq = True
            BlueWR -= 10
        elif int(BRFreq.get('fighter')) < 2:
            printConsoleandOutfile("Blue team has no tanks or not enough fighters, they are very squishy")
            freq = True
            BlueWR -= 10

    if 'tank' not in RRFreq:
        if 'fighter' not in RRFreq:
            printConsoleandOutfile("Red team has no tanks or fighters, they are very squishy")
            freq = True
            RedWR -= 10
        elif int(RRFreq.get('fighter')) < 2:
            printConsoleandOutfile("Red team has no tanks or enough fighters, they are very squishy")
            freq = True
            RedWR -= 10

if freq == False:
    printConsoleandOutfile("Both teams have equal amount of tanks or fighters")

# In future, u can check for meta or not, make list for each role consisting of each champ
# and then check if the certain role is in the list created
# if not meta then -3% wr?

print("\n")
printConsoleandOutfile("          =================Dmg Type Check=================")
printConsoleandOutfile("          ----------------You are on ", pickString, "----------")
AllBlueDmg = [champion.CHAMPION.get(champPrintB[b]).get("dmgtype") for b in range(len(champPrintB))]
AllRedDmg = [champion.CHAMPION.get(champPrintR[r]).get("dmgtype") for r in range(len(champPrintR))]
BDTotal = {}
RDTotal = {}
BDTotal = role_frequency(AllBlueDmg)
RDTotal = role_frequency(AllRedDmg)

dmgerr = False
if dmgerr == False:
    if 'ad' in BDTotal:
        if BDTotal.get('ad') >= 4:
            printConsoleandOutfile("Blue side has too much ad")
            BlueWR -= 5
            dmgerr = True
    else:
        printConsoleandOutfile("Blue side has no ap (excluding hybrids)")

    if 'ap' in BDTotal:
        if BDTotal.get('ap') >= 4:
            printConsoleandOutfile("Blue side has too much ap")
            BlueWR -= 5
            dmgerr = True
    else:
        printConsoleandOutfile("Blue side has no ap (excluding hybrids)")

    if 'ad' in RDTotal:
        if RDTotal.get('ad') >= 4:
            printConsoleandOutfile("Red side has too much ad")
            RedWR -= 5
            dmgerr = True
    else:
        printConsoleandOutfile("Red side has no ap (excluding hybrids)")

    if 'ap' in RDTotal:
        if RDTotal.get('ap') >= 4:
            printConsoleandOutfile("Red side has too much ap")
            RedWR -= 5
            dmgerr = True
    else:
        printConsoleandOutfile("Red side has no ap (excluding hybrids)")

if dmgerr == False:
    printConsoleandOutfile("Both sides have equal amount of ap and ad")

print("\n")
printConsoleandOutfile("Blue WR: ", str(BlueWR), "%")
printConsoleandOutfile("Red WR: ", str(RedWR), "%")


# Are you more likely to win or lose?
def dodgeORnah(wr):
    if wr >= 70:
        if abs(BlueWR - RedWR) >= 18:
            printConsoleandOutfile("You have a huge advantage, win like a boss!")

    if wr <= 43:
        if abs(BlueWR - RedWR) >= 18:
            printConsoleandOutfile("You have a HUGE disadvantage, dodge like the plague")
            byeee = input("Do you want to dodge to save LP? ")
            if byeee == 'yes':
                print("Executing Order 66 on league client to save LP...")
                if sys.platform == 'win32':
                    os.system("taskkill /f /im  LeagueClient.exe")
                if sys.platform == 'darwin':
                    os.system("killall LeagueClient")
                print("Congrats, you saved yourself some LP\nBetter luck next time...")
            if byeee == 'no':
                print("Ok, that's your call")


if BlueWR > RedWR:
    if pickString == 'blue side':
        printConsoleandOutfile("You are more likely to win")
        dodgeORnah(BlueWR)
    if pickString == 'red side':
        printConsoleandOutfile("You are more likely to lose")
        dodgeORnah(RedWR)
elif BlueWR < RedWR:
    if pickString == 'blue side':
        printConsoleandOutfile("You are more likely to lose")
        dodgeORnah(BlueWR)
    if pickString == 'red side':
        printConsoleandOutfile("You are more likely to win")
        dodgeORnah(RedWR)
else:
    printConsoleandOutfile("Both sides are equal in win rates, better player wins!")

print("\n")

def copytoClipboard():
    result = ""
    with open('outfile.txt', 'r') as r:

        result = r.read()
    #print(result)
    
    pyperclip.copy(result)

if input("Do you want to copy results to clipboard? (y/n): ") == "y":
    copytoClipboard()
    print("Copied to clipboard!\n")

input("Click the ENTER key to exit...")

