import json
import requests
import os

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
pokename = (body["name"])  # should be "pikachu"
pokeid = (body["id"])
poketype = (body["types"])
print(pokename)
print(pokeid)
print(poketype)

key = os.environ.get("GIPHY_KEY")
res1 = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=pikachu&rating=g")
body1 = json.loads(res1.content)
url = body1['data'][5]['url']

print(url)


