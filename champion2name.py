import urllib.request, json

def getClientVersion():
    url = 'https://ddragon.leagueoflegends.com/api/versions.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data[0]
#print("http://ddragon.leagueoflegends.com/cdn/"+ getClientVersion() +"/data/en_US/champion.json")

def champidtoname(id):
    with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/"+ getClientVersion() +"/data/en_US/champion.json") as url:
        data = json.loads(url.read().decode())
    for allchamps in data['data']:
        if data['data'][allchamps]['key'] == str(id):
            return allchamps.lower()


#print(champidtoname(360))