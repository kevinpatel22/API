from django.http import JsonResponse
import requests
import json
import os
import pdb

def pokemon_go(request, id):
    api_url = (f"http://pokeapi.co/api/v2/pokemon/{id}/")
    res = requests.get(api_url)
    pokeball = json.loads(res.content)
    pokename = pokeball['name']
    pokeid = pokeball['id']
    types = pokeball['types']
    poketype = []
    for type in types:
        poketype.append(type['type']['name'])
    key = os.environ.get("GIPHY_KEY")
    gif_res = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={key}&tag={pokename}&rating=g")
    gif_pokeball = json.loads(gif_res.content)
    gif_url = gif_pokeball['data']['url']
    return JsonResponse({'name': pokename, 'id': pokeid, 'types': poketype, 'gif': gif_url})
   