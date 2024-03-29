'''
Database of all league champions v1.5 @austinyen56
Obtained from riot API
'''
import difflib
championNames = ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelionsol',
                 'azir', 'bard', 'belveth', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath', 'corki',
                 'darius', 'diana', 'draven', 'drmundo', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora',
                 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger',
                 'illaoi', 'irelia', 'ivern', 'janna', 'jarvan', 'jax', 'jayce', 'jhin', 'jinx', 'ksante', 'kaisa', 'kalista',
                 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'khazix', 'kindred', 'kled',
                 'kogmaw', 'leblanc', 'leesin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite',
                 'malzahar', 'maokai', 'masteryi', 'missfortune', 'wukong', 'mordekaiser', 'morgana', 'nami', 'nasus',
                 'nautilus', 'neeko', 'nidalee', 'nilah', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy',
                 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', 'reksai', 'rell', 'renata', 'renekton', 'rengar', 'riven',
                 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana',
                 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahmkench',
                 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate',
                 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vex', 'vi', 'viego', 'viktor', 'vladimir',
                 'volibear', 'warwick', 'xayah', 'xerath', 'xinzhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'zeri',
                 'ziggs', 'zilean', 'zoe', 'zyra']


# def championStats(champion):
#    if champion not in championNames:
#        print("not a champion")
#    else:
#        print("ur champ name is ", champion)

def champSpellCheck(c):
    c = c.lower()
    CM = difflib.get_close_matches(c, championNames)
    if CM == [] or c == 'asol' or c == 'monkey' or c == 'monkas' or c == 'trash' or c == 'trashcan' or c == 'satan':
        if c == 'ww':
            print("Did you mean: 'warwick'?")
        if c == 'asol':
            print("Did you mean: 'aurelionsol'?")
        if c == 'ez':
            print("Did you mean: 'ezreal'?")
        if c == 'gp':
            print("Did you mean: 'gangplank'?")
        if c == 'hiemer':
            print("Did you mean: 'heimerdinger'?")
        if c == '4':
            print("Did you mean: 'jhin'?")
        if c == 'lb':
            print("Did you mean: 'leblanc'?")
        if c == 'rock':
            print("Did you mean: 'malphite'?")
        if c == 'monkey' or c == 'monkas' or c == 'monkeyking':
            print("Did you mean: 'wukong'?")
        if c == 'vb':
            print("Did you mean: 'volibear'?")
        if c == 'trashcan' or c == 'trash' or c == 'trashbag' or c == 'cancer':
            print("Did you mean: 'yasuo'?")
        if c == 'satan' or c == 'devil':
            print("Did you mean: 'teemo'?")
        if c == 'tf':
            print("Did you mean: 'twistedfate'?")
    else:
        print(f"Did you mean: '{CM}'?")

def checkChamp(inputMsg):
    global validChamp
    while True:
        userinputchampion = input(inputMsg).lower()
        if userinputchampion not in championNames:
            print("Not a valid champion, type again")
            champSpellCheck(userinputchampion)
            continue
        validChamp = userinputchampion
        break
    return validChamp


# ---------Dict of all champions
# Format: mainrole, alternative role, cc[including slows] (0 = none, 10 = a shit ton)
# Knockup (0 = none, 4 = all abilities), Healing (0 = none, 10 = massive healing)
# Damage type (ap, ad, hybrid), role, top 5 counters, top 5 crushes

CHAMPION = {
    "aatrox": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '6',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'kayle', 'fiora', 'renekton', 'illaoi'],
        "crushes": ['shen', 'nasus', 'gangplank', 'vladimir', 'sion'],
    },
    "ahri": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'zed', 'twistedfate', 'yasuo', 'ekko'],
        "crushes": ['galio', 'akali', 'malzahar', 'ziggs', 'yone'],
    },
    "akali": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '0',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['kled', 'renekton', 'lissandra', 'annie', 'lucian'],
        "crushes": ['syndra', 'kayle', 'malphite', 'gwen', 'xerath'],
    },
    "akshan": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '0',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['anivia', 'veigar', 'cassiopeia'],
        "crushes": ['zeri', 'corki'],
    },
    "alistar": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '7',
        "knockup": '2',
        "healing": '3',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'pyke', 'janna', 'soraka', 'brand'],
        "crushes": ['blitzcrank', 'rell', 'nami', 'samira'],
    },
    "amumu": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '6',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['diana', 'morgana', 'masteryi', 'shaco'],
        "crushes": ['rumble'],
    },
    "anivia": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '7',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['diana', 'lucian', 'kassadin', 'fizz', 'yasuo'],
        "crushes": ['vladimir', 'irelia', 'zoe', 'yone'],
    },
    "annie": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '8',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'qiyana', 'sylas', 'leblanc'],
        "crushes": ['akali', 'lux', 'viktor', 'yasuo'],
    },
    "aphelios": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'caitlyn', 'kogmaw', 'jhin', 'kalista'],
        "crushes": ['vayne', 'ashe', 'kaisa', 'xayah', 'lucian'],
    },
    "ashe": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'caitlyn', 'ezreal', 'jinx', 'sivir'],
        "crushes": ['missfortune', 'kalista', 'lucian'],
    },
    "aurelionsol": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['yasuo', 'yone', 'sylas'],  # change this to all mid laners
        "crushes": [''],
    },
    "azir": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['yasuo', 'yone', 'katarina', 'zed'],
        "crushes": [''],
    },
    "bard": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['brand', 'zilean', 'zyra', 'pyke'],
        "crushes": ['alistar', 'blitzcrank', 'senna', 'braum', 'rakan'],
    },
    "belveth": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '5',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['jax'],
        "crushes": [''],
    },
    "blitzcrank": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'pyke', 'zilean', 'sona', 'swain'],
        "crushes": ['xerath', 'karma', 'velkoz'],
    },
    "brand": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zilean', 'yuumi', 'soraka', 'janna'],
        "crushes": ['alistar', 'rakan', 'seraphine', 'braum', 'thresh'],
    },
    "braum": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'xerath', 'nami', 'pyke', 'zyra', 'brand'],
        "crushes": ['bard', 'nautilus', 'karma', 'rakan']
    },
    "caitlyn": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'kalista', 'ziggs', 'ezreal'],
        "crushes": ['kogmaw', 'vayne', 'ashe', 'aphelios', 'xayah']
    },
    "camille": {
        "mainRole": 'top',
        "altRole": 'mid',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['warwick', 'renekton', 'quinn', 'gangplank', 'fiora'],
        "crushes": ['kayle', 'shen', 'garen', 'tryndamere']
    },
    "cassiopeia": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'yasuo', 'katarina'],
        "crushes": ['sylas', 'vladimir', 'yone']
    },
    "chogath": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '5',
        "knockup": '1',
        "healing": '1',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['irelia', 'darius', 'gnar', 'drmundo'],
        "crushes": ['malphite', 'shen', 'renekton', 'aatrox']
    },
    "corki": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '1',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'hybrid',
        "role": 'marksman',
        "counters": ['lucian', 'vladimir', 'zed', 'ekko', 'yasuo'],
        "crushes": ['malzahar', 'orianna', 'lux', 'vicktor', 'akali']
    },
    "darius": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '1',
        "knockup": '1',
        "healing": '7',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'drmundo', 'wukong', 'ornn', 'gangplank'],
        "crushes": ['shen', 'sion', 'nasus', 'sylas', 'kayle']
    },
    "diana": {
        "mainRole": 'mid',
        "altRole": 'jg',
        "cc": '5',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['annie', 'fizz', 'galio', 'lulu', 'malzahar', 'mordekaiser', 'rumble', 'viktor', 'vladimir', 'yone',
                     'zed'],
        "crushes": ['ziggs', 'lux', 'ahri', 'viego', 'zoe']
    },
    "drmundo": {
        "mainRole": 'mid',
        "altRole": 'jg',
        "cc": '3',
        "knockup": '0',
        "healing": '10',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'kled', 'camile', 'tryndamere'],
        "crushes": ['malphite', 'jayce', 'tahmkench', 'singed', 'kennen']
    },
    "draven": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '1',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['kogmaw', 'ezreal', 'ziggs', 'caitlyn'],
        "crushes": ['ashe', 'kalista', 'vayne', 'aphelios', 'xayah']
    },
    "ekko": {
        "mainRole": 'mid',
        "altRole": 'jg',
        "cc": '2',
        "knockup": '0',
        "healing": '5',
        "dmgtype": 'ap',
        "role": 'assassin',
        "counters": ['lucian', 'shaco', 'galio', 'yasuo', 'zed'],
        "crushes": ['rammus', 'zoe', 'orianna', 'malzahar']
    },
    "elise": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'assassin',
        "counters": ['rengar', 'shaco', 'zac', 'nocturne'],
        "crushes": ['rammus', 'poppy']
    },
    "evelynn": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'assassin',
        "counters": ['diana', 'masteryi', 'warwick', 'shaco'],
        "crushes": ['rammus', 'gragas', 'udyr']
    },
    "ezreal": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'hybrid',
        "role": 'marksman',
        "counters": ['draven', 'ziggs', 'kalista', 'vayne'],
        "crushes": ['swain', 'xayah', 'lucian']
    },
    "fiddlesticks": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '8',
        "knockup": '0',
        "healing": '6',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['diana', 'olaf', 'nocturne', 'vi', 'warwick'],
        "crushes": ['rammus', 'gragas', 'zac']
    },
    "fiora": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['gangplank', 'sion', 'renekton', 'malphite'],
        "crushes": ['sylas', 'irelia', 'shen', 'mordekaiser']
    },
    "fizz": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['viego', 'galio', 'zed', 'vladimir'],
        "crushes": ['veigar', 'lucian', 'xerath', 'katarina']
    },
    "galio": {
        "mainRole": 'mid',
        "altRole": 'supp',
        "cc": '6',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'lucian', 'talon', 'ahri', 'viego'],
        "crushes": ['akali', 'lucian']
    },
    "gangplank": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'ornn', 'sion'],
        "crushes": ['shen', 'malphite', 'gnar', 'renekton']
    },
    "garen": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['tryndamere', 'camille', 'gnar'],
        "crushes": ['shen', 'malphite', 'gwen', 'jayce']
    },
    "gnar": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'riven', 'fiora', 'gangplank'],
        "crushes": ['shen', 'garen', 'kayle']
    },
    "gragas": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '6',
        "knockup": '2',
        "healing": '2',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['masteryi', 'diana', 'fiddlesticks', 'viego'],
        "crushes": ['zac', 'rumble']
    },
    "graves": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['masteryi', 'fiddlesticks', 'ekko'],
        "crushes": ['rammus', 'zac', 'udyr', 'rengar']
    },
    "gwen": {
        "mainRole": 'top',
        "altRole": 'mid',
        "cc": '0',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['tryndamere', 'quinn', 'singed', 'warwick'],
        "crushes": ['shen', 'malphite', 'yorick', 'illaoi']
    },
    "hecarim": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '5',
        "knockup": '1',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['xinzhao', 'trundle', 'fiddlesticks'],
        "crushes": ['rammus', 'udyr', 'ivern', 'rengar']
    },
    "heimerdinger": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": [],
        "crushes": ['sylas']
    },
    "illaoi": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['gwen', 'mordekaiser'],
        "crushes": ['shen', 'nasus', 'darius']
    },
    "irelia": {
        "mainRole": 'top',
        "altRole": 'mid',
        "cc": '4',
        "knockup": '0',
        "healing": '7',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['riven', 'tryndamere'],
        "crushes": ['kayle', 'xerath', 'gangplank']
    },
    "ivern": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'mage',
        "counters": ['masteryi', 'diana', 'xinzhao'],
        "crushes": ['hecarim']
    },
    "janna": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '2',
        "healing": '6',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['velkoz', 'zyra'],
        "crushes": ['rell', 'morgana', 'alistar']
    },
    "jarvan": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['masteryi', 'viego', 'kayn'],
        "crushes": ['zac', 'nidalee']
    },
    "jax": {
        "mainRole": 'top',
        "altRole": 'jg',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['drmundo', 'gangplank'],
        "crushes": ['kayle', 'renekton', 'shen']
    },
    "jayce": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'drmundo', 'malphite'],
        "crushes": ['shen', 'akali', 'sylas']
    },
    "jhin": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'swain'],
        "crushes": ['aphelios', 'kogmaw']
    },
    "jinx": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'ziggs'],
        "crushes": ['kalista', 'aphelios']
    },
    "ksante": {
        "mainRole": 'top',
        "altRole": 'supp',
        "cc": '3',
        "knockup": '1',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'tank',
        "counters": ['zac', 'chogath'],
        "crushes": ['aatrox', 'pantheon']
    },    
    "kaisa": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'tahmkench', 'swain'],
        "crushes": ['lucian', 'xayah']
    },
    "kalista": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'tahmkench', 'swain'],
        "crushes": ['lucian', 'xayah']
    },
    "karma": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zyra', 'pyke', 'maokai', 'sona'],
        "crushes": ['taric', 'rell', 'pantheon', 'alistar']
    },
    "karthus": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['masteryi', 'fiddlesticks'],
        "crushes": ['zac', 'xinzhao']
    },
    "kassadin": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['lucian', 'pantheon', 'irelia'],
        "crushes": ['katarina', 'veigar', 'annie', 'xerath', 'akali']
    },
    "katarina": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'assassin',
        "counters": ['lucian', 'vladimir', 'zed'],
        "crushes": ['veigar', 'irelia', 'ryze']
    },
    "kayle": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'hybrid',
        "role": 'fighter',
        "counters": ['irelia', 'sion', 'tryndamere', 'wukong'],
        "crushes": ['shen', 'volibear', 'renekton']
    },
    "kayn": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['masteryi', 'warwick', 'reksai'],
        "crushes": ['ivern', 'rammus', 'jarvan', 'sejuani']
    },
    "kennen": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '6',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['drmundo'],
        "crushes": ['aatrox']
    },
    "khazix": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['warwick', 'fiddlesticks', 'morgana', 'volibear', 'udyr'],
        "crushes": ['nidalee', 'ivern', 'karthus', 'evelynn', 'taliyah', 'lilia']
    },
    "kindred": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['masteryi', 'taliyah', 'poppy'],
        "crushes": ['rammus', 'ivern', 'rengar', 'trundle']
    },
    "kled": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['fiora', 'jax', 'camille'],
        "crushes": ['sylas', 'nasus', 'akali']
    },
    "kogmaw": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'ezreal', 'xayah', 'caitlyn'],
        "crushes": ['aphelios', 'lucian']
    },
    "leblanc": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['lucian', 'malzahar', 'zed'],
        "crushes": ['annie', 'irelia', 'zoe']
    },
    "leesin": {
        "mainRole": 'jg',
        "altRole": 'top',
        "cc": '3',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['masteryi', 'zac'],
        "crushes": ['ivern', 'lilia', 'rammus']
    },
    "leona": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '8',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['pyke', 'sona'],
        "crushes": ['pantheon']
    },
    "lillia": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['diana', 'khazix', 'xinzhao'],
        "crushes": ['hecarim']
    },
    "lissandra": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '7',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'katarina', 'viego', 'sylas'],
        "crushes": ['akali', 'qiyanna']
    },
    "lucian": {
        "mainRole": 'adc',
        "altRole": 'mid',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'veigar'],
        "crushes": ['galio', 'kassadin', 'akali', 'yone']
    },
    "lulu": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zyra', 'senna', 'sona', 'xerath'],
        "crushes": ['rell', 'alistar', 'taric']
    },
    "lux": {
        "mainRole": 'supp',
        "altRole": 'mid',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'annie', 'lucian', 'xerath'],
        "crushes": ['rell', 'alistar', 'syndra']
    },
    "malphite": {
        "mainRole": 'top',
        "altRole": 'mid',
        "cc": '5',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'hybrid',
        "role": 'tank',
        "counters": ['drmundo', 'sylas', 'mordekaiser', 'sion'],
        "crushes": ['irelia', 'renekton', 'jayce']
    },
    "malzahar": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '7',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'ekko', 'viktor'],
        "crushes": ['leblanc', 'qiyana']
    },
    "maokai": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'zilean', 'zyra'],
        "crushes": ['pyke', 'karma']
    },
    "masteryi": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['rammus', 'zac', 'amumu', 'fiddlesticks'],
        "crushes": ['karthus', 'nidalee', 'evelynn', 'taliyah', 'lilia', 'gragas']
    },
    "missfortune": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'ashe'],
        "crushes": ['vayne', 'aphelios', 'lucian']
    },
    "mordekaiser": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '5',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['tryndamere', 'irelia', 'fiora', 'gangplank'],
        "crushes": ['malphite', 'shen', 'illaoi', 'renekton']
    },
    "morgana": {
        "mainRole": 'supp',
        "altRole": 'jg',
        "cc": '10',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['pyke', 'senna', 'sona', 'zyra'],
        "crushes": ['rell', 'alistar', 'braum', 'leona']
    },
    "nami": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '10',
        "knockup": '2',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['pyke', 'sona', 'zyra'],
        "crushes": ['rell', 'braum']
    },
    "nasus": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '6',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'sylas', 'kled'],
        "crushes": ['malphite', 'teemo', 'renekton']
    },
    "nautilus": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '7',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['pyke', 'senna', 'taric'],
        "crushes": ['karma', 'xerath']
    },
    "neeko": {
        "mainRole": 'mid',
        "altRole": 'supp',
        "cc": '6',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'yasuo', 'yone'],
        "crushes": ['akali', 'katarina', 'thresh']
    },
    "nidalee": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['masteryi', 'rengar', 'vi'],
        "crushes": ['rammus', 'zac', 'rumble', 'graves']
    },
    "nilah": {
        "mainRole": 'adc',
        "altRole": 'mid',
        "cc": '5',
        "knockup": '1',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": [''],
        "crushes": ['']
    },
    "nocturne": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['fiddlesticks', 'ekko', 'nunu'],
        "crushes": ['rammus', 'amumu', 'udyr']
    },
    "nunu": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '7',
        "knockup": '1',
        "healing": '5',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['masteryi', 'reksai', 'xinzhao'],
        "crushes": ['zac', 'udyr']
    },
    "olaf": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '7',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['khazix'],
        "crushes": ['fiddlesticks', 'elise', 'xinzhao']
    },
    "orianna": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '5',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'corki'],
        "crushes": ['galio', 'lucian', 'lux']
    },
    "ornn": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '7',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'tank',
        "counters": ['irelia', 'volibear', 'camille'],
        "crushes": ['malphite', 'renekton']
    },
    "pantheon": {
        "mainRole": 'mid',
        "altRole": 'supp',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['pyke', 'soraka', 'leona'],
        "crushes": ['kassadin', 'lucian', 'alistar', 'yone']
    },
    "poppy": {
        "mainRole": 'top',
        "altRole": 'supp',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'tank',
        "counters": ['drmundo', 'sett', 'irelia', 'masteryi'],
        "crushes": ['sylas', 'shen', 'irelia', 'aatrox']
    },
    "pyke": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['maokai', 'nami'],
        "crushes": ['braum', 'alistar', 'pantheon']
    },
    "qiyana": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['irelia', 'malzahar'],
        "crushes": ['akali', 'syndra', 'galio']
    },
    "quinn": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['drmundo', 'malphite'],
        "crushes": ['gwen']
    },
    "rakan": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '6',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'braum', 'brand', 'zyra'],
        "crushes": ['pyke', 'xerath']
    },
    "rammus": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '8',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['nidalee', 'nocturne', 'hecarim'],
        "crushes": ['viego', 'kindred', 'masteryi']
    },
    "reksai": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '4',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['fiddlesticks', 'ekko'],
        "crushes": ['zac', 'nunu', 'rumble']
    },
    "rell": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '8',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'tank',
        "counters": ['senna', 'nami', 'morgana', 'lux'],
        "crushes": ['blitzcrank', 'pyke']
    },
    "renata": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '8',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['senna', 'nami', 'morgana', 'lux'],
        "crushes": ['blitzcrank', 'pyke']
    },
    "renekton": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '6',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['gangplank', 'ornn', 'kayle'],
        "crushes": ['nasus', 'shen', 'tryndamere', 'irelia']
    },
    "rengar": {
        "mainRole": 'jg',
        "altRole": 'top',
        "cc": '2',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['masteryi', 'set', 'kayn'],
        "crushes": ['nunu', 'zac', 'nidalee']
    },
    "riven": {
        "mainRole": 'top',
        "altRole": 'mid',
        "cc": '4',
        "knockup": '1',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['renekton', 'tryndamere', 'quinn'],
        "crushes": ['shen', 'irelia', 'sion', 'kayle']
    },
    "rumble": {
        "mainRole": 'top',
        "altRole": 'jg',
        "cc": '1',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['masteryi', 'gragas'],
        "crushes": ['ivern', 'rammus', 'rengar', 'amumu']
    },
    "ryze": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'lux', 'lucian'],
        "crushes": ['sylas', 'vladimir', 'qiyanna', 'sylas']
    },
    "samira": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'swain'],
        "crushes": ['sivir', 'lucian']
    },
    "sejuani": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '8',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['diana', 'masteryi', 'volibear'],
        "crushes": ['zac', 'khazix']
    },
    "senna": {
        "mainRole": 'supp',
        "altRole": 'adc',
        "cc": '2',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['zilean', 'brand', 'zyra'],
        "crushes": ['taric', 'pantheon', 'alistar', 'rakan']
    },
    "seraphine": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['pyke', 'xerath', 'sona', 'zilean'],
        "crushes": ['alistar', 'rell', 'leona']
    },
    "sett": {
        "mainRole": 'top',
        "altRole": 'supp',
        "cc": '5',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['illaoi', 'ornn', 'gangplank'],
        "crushes": ['shen', 'nasus', 'sylas']
    },
    "shaco": {
        "mainRole": 'jg',
        "altRole": 'supp',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'hybrid',
        "role": 'assassin',
        "counters": ['jarvan', 'sejuani'],
        "crushes": ['ivern', 'nidalee', 'lilia', 'rammus']
    },
    "shen": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['illaoi', 'urgot', 'gangplank', 'riven'],
        "crushes": ['malphite', 'akali']
    },
    "shyvana": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'hybrid',
        "role": 'fighter',
        "counters": ['diana', 'hecarim'],
        "crushes": ['leesin']
    },
    "singed": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'fighter',
        "counters": ['drmundo', 'camille', 'darius'],
        "crushes": ['nasus', 'shen', 'gwen', 'aatrox']
    },
    "sion": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '5',
        "knockup": '2',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'tank',
        "counters": ['aatrox', 'renekton', 'riven'],
        "crushes": ['malphite', 'kayle', 'jayce']
    },
    "sivir": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'twitch'],
        "crushes": ['ashe', 'missfortune']
    },
    "skarner": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['leesin', 'xinzhao'],
        "crushes": ['']
    },
    "sona": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '5',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['senna', 'zyra', 'pyke'],
        "crushes": ['alistar', 'nami']
    },
    "soraka": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '9',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['senna', 'sona', 'xerath', 'pyke'],
        "crushes": ['braum', 'velkoz', 'braum']
    },
    "swain": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '1',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['tristana', 'xerath', 'zilean'],
        "crushes": ['alistar', 'samira', 'leona']
    },
    "sylas": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '2',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['tryndamere', 'kled', 'heimerdinger'],
        "crushes": ['malphite', 'irelia', 'nasus']
    },
    "syndra": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['yasuo', 'qiyanna'],
        "crushes": ['viktor', 'zed']
    },
    "tahmkench": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['ezreal', 'thresh'],
        "crushes": ['kaisa']
    },
    "taliyah": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['xinzhao'],
        "crushes": ['kindred']
    },
    "talon": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'assassin',
        "counters": ['irelia', 'viego', 'fizz'],
        "crushes": ['galio', 'kassadin', 'lucian', 'lux']
    },
    "taric": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '4',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['senna', 'lulu', 'karma'],
        "crushes": ['yuumi', 'nautilus']
    },
    "teemo": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'gangplank', 'malphite'],
        "crushes": ['shen', 'kayle', 'camille', 'irelia']
    },
    "thresh": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '6',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['brand', 'braum', 'senna'],
        "crushes": ['rell', 'tahmkench']
    },
    "tristana": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'swain'],
        "crushes": ['ashe', 'aphelios']
    },
    "trundle": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['diana', 'shaco'],
        "crushes": ['zac', 'sett']
    },
    "tryndamere": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['ornn', 'camille'],
        "crushes": ['kayle', 'gwen', 'shen']
    },
    "twistedfate": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'yasuo', 'ekko'],
        "crushes": ['malzahar', 'galio', 'akali']
    },
    "twitch": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'hybrid',
        "role": 'marksman',
        "counters": ['draven', 'tristana'],
        "crushes": ['ashe', 'aphelios']
    },
    "udyr": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['nunu'],
        "crushes": ['zac', 'nidalee']
    },
    "urgot": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['drmundo', 'wukong', 'kayle'],
        "crushes": ['shen', 'sylas']
    },
    "varus": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'twitch'],
        "crushes": ['ashe', 'aphelios', 'kogmaw', 'jinx']
    },
    "vayne": {
        "mainRole": 'adc',
        "altRole": 'top',
        "cc": '2',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'kogmaw'],
        "crushes": ['ziggs']
    },
    "veigar": {
        "mainRole": 'mid',
        "altRole": 'supp',
        "cc": '4',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'lucian', 'katarina', 'ekko'],
        "crushes": ['twistedfate', 'yasuo']
    },
    "velkoz": {
        "mainRole": 'mid',
        "altRole": 'supp',
        "cc": '2',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['zed', 'yasuo', 'soraka', 'yuumi'],
        "crushes": ['alistar', 'nautilus']
    },
    "vex": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['velkoz','veigar', 'anivia'],
        "crushes": ['lissandra', 'leblanc']
    },
    "vi": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '5',
        "knockup": '2',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['hecarim', 'graves', 'kindred'],
        "crushes": ['zac', 'nidalee']
    },
    "viego": {
        "mainRole": 'jg',
        "altRole": 'mid',
        "cc": '3',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'corki', 'reksai'],
        "crushes": ['galio', 'lucian']
    },
    "viktor": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '2',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'kassadin'],
        "crushes": ['galio', 'syndra']
    },
    "vladimir": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '0',
        "knockup": '0',
        "healing": '3',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['drmundo', 'malzahar', 'anivia'],
        "crushes": ['veigar', 'annie', 'gwen', 'irelia']
    },
    "volibear": {
        "mainRole": 'top',
        "altRole": 'jg',
        "cc": '3',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['illaoi', 'gangplank', 'kayle'],
        "crushes": ['nasus', 'sejuani', 'shen', 'malphite']
    },
    "warwick": {
        "mainRole": 'jg',
        "altRole": 'top',
        "cc": '6',
        "knockup": '0',
        "healing": '4',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['nocturne', 'graves'],
        "crushes": ['camille', 'mordekaiser', 'zac']
    },
    "wukong": {
        "mainRole": 'top',
        "altRole": 'jg',
        "cc": '5',
        "knockup": '1',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['illaoi', 'renekton', 'chogath'],
        "crushes": ['kayle', 'teemo']
    },
    "xayah": {
        "mainRole": 'adc',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '1',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['draven', 'ezreal', 'caitlyn'],
        "crushes": ['kogmaw', 'missfortune']
    },
    "xerath": {
        "mainRole": 'supp',
        "altRole": 'mid',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'yasuo', 'diana'],
        "crushes": ['braum', 'alistar', 'lux']
    },
    "xinzhao": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '5',
        "knockup": '2',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['masteryi', 'rengar', 'warwick', 'nocturne'],
        "crushes": ['ivern', 'lilia', 'rammus']
    },
    "yasuo": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '4',
        "knockup": '1',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['viego', 'irelia', 'aurelionsol'],
        "crushes": ['galio', 'veigar']
    },
    "yone": {
        "mainRole": 'mid',
        "altRole": 'top',
        "cc": '4',
        "knockup": '1',
        "healing": '3',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['irelia', 'pantheon', 'anivia'],
        "crushes": ['galio', 'orianna', 'viktor', 'neeko']
    },
    "yorick": {
        "mainRole": 'top',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '2',
        "dmgtype": 'ad',
        "role": 'fighter',
        "counters": ['sett', 'gwen'],
        "crushes": ['shen', 'darius']
    },
    "yuumi": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '9',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['pyke', 'senna', 'taric'],
        "crushes": ['braum', 'velkoz', 'xerath']
    },
    "zac": {
        "mainRole": 'jg',
        "altRole": 'none',
        "cc": '7',
        "knockup": '2',
        "healing": '7',
        "dmgtype": 'ap',
        "role": 'tank',
        "counters": ['diana', 'nidalee'],
        "crushes": ['sejuani', 'amumu']
    },
    "zed": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'asssassin',
        "counters": ['irelia', 'heimerdinger', 'kayle'],
        "crushes": ['veigar', 'lucian', 'ryze', 'annie']
    },
    "zeri": {
        "mainRole": 'adc',
        "altRole": 'top',
        "cc": '0',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ad',
        "role": 'marksman',
        "counters": ['ziggs', 'ezreal'],
        "crushes": ['']
    },
    "ziggs": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '2',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['yasuo', 'zed', 'vayne', 'diana'],
        "crushes": ['malzahar', 'orianna', 'caitlyn', 'lucian']
    },
    "zilean": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['xerath', 'pyke', 'zyra'],
        "crushes": ['braum', 'alistar', 'swain']
    },
    "zoe": {
        "mainRole": 'mid',
        "altRole": 'none',
        "cc": '3',
        "knockup": '0',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['irelia', 'malzahar'],
        "crushes": ['sylas', 'viktor', 'orianna', 'lucian']
    },
    "zyra": {
        "mainRole": 'supp',
        "altRole": 'none',
        "cc": '7',
        "knockup": '1',
        "healing": '0',
        "dmgtype": 'ap',
        "role": 'mage',
        "counters": ['pyke', 'braum', 'xerath'],
        "crushes": ['alistar', 'janna', 'rakan']
    }
}

# 11 min per row (6 champs)
# x = input()
# if x not in (CHAMPION.get('aatrox').get("roles")):
#    print("not an official role")
# print(type(CHAMPION))
# print(CHAMPION.get('aatrox').get("altRole"))
