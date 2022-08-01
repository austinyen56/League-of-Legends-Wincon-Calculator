from lcu_driver import Connector
from champion2name import champidtoname as c2n

connector = Connector()

@connector.ready
async def ClientConnect(connection):
    print('League client connected...\nWaiting for champion select...\n')

@connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def ChampSelect(connection, event):
    global mainresult

    resultAlly= {}
    resultSortedAlly, resultSortedEnemy = [], []
    #print(event.data)
    print('Live data was updated! Please wait for finalization phase after ban/pick...')
    if event.data['timer']['phase'] == 'FINALIZATION':
        #print(event.data)  # print the realtime champ select data
        print('\nIn finalization phase:\n')

        for player in event.data['myTeam']:
            if c2n(player['championId']) == 'monkeyking':
                resultAlly[player['assignedPosition']] = 'wukong'
            elif c2n(player['championId']) == 'jarvaniv':
                resultAlly[player['assignedPosition']] = 'jarvan'
            else:
                resultAlly[player['assignedPosition']] = c2n(player['championId'])

        for enemy in event.data['theirTeam']:
            if c2n(enemy['championId']) == 'monkeyking':
                resultSortedEnemy.append('wukong')
            elif c2n(enemy['championId']) == 'jarvaniv':
                resultSortedEnemy.append('jarvan')
            else:
                resultSortedEnemy.append(c2n(enemy['championId']))
        # Used try/except to avoid errors when roles are not assigned to allies (e.g. during a custom game/ special gamemode/ aram)
        # Enemies will never show assigned positions, and enemy champids will not even show in special gamemodes
        try:
            resultSortedAlly = [resultAlly['top'], resultAlly['middle'], resultAlly['jungle'], resultAlly['bottom'], resultAlly['utility']]
        except KeyError:
            if resultSortedAlly == []:
                resultSortedAlly = resultAlly
        
        #print("Current data:", resultAlly)
        print("Detected Allies:", resultSortedAlly, "\nDetected Enemies:", resultSortedEnemy)
        
        if input('\nContinue? (y/n) \nTry changing summoner spells or skins to refresh... ') == 'y':
            await connector.stop()  

    mainresult = [resultSortedAlly, resultSortedEnemy]
    # Ask manually who is top mid bot jg adc supp, and then populate the list for enemy
    
def ClientFetch():
    print('Finding League Client to Connect...')
    connector.start()
    return mainresult

