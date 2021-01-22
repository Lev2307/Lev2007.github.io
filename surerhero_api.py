import json
import requests
import pprint

#Pretty printer
pp = pprint.PrettyPrinter(indent=4)

#API data
API_KEY = 10218686935504422

#DATA
with open('heroes_data.json', 'r+') as f:
    heroes_data = json.loads(f.read())


class SuperHeroAPI:
    def __init__(self, API=API_KEY, data = heroes_data):
        self._token = API
        self._data = data
        self._url = f'https://superheroapi.com/api/{self._token}'

    def get_hero(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')

    def _get_id(self, name):
        data = self._data.get(name, False)
        if data:
            return data
        else:
            raise NotFoundError('Name not found')

    def _parse_name(self, name):
        return name.lower().title()

    def download_image(self, name):
        image_url = self.get_hero_image_url(name)
        with open(f'{name}.jpg', 'wb') as f:
            response = requests.get(image_url).content
            f.write(response)
    

    def get_hero_image_url(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}/image')['url']
    
    def get_hero_idintification_card(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        stats = self._parse_api(self._url + f'/{hero_id}/powerstats/')
        hero_int = stats['intelligence']
        hero_str = stats['strength']
        hero_speed = stats['speed']
        hero_power = stats['power']
        hero_combat = stats['combat']
        print(f'Name: {name}; \nInt: {hero_int}; \nStr: {hero_str}; \nSpd: {hero_speed}; \nRwr: {hero_power}; \nCmbt: {hero_combat}')
        #     

    def _parse_api(self, url):
        response = requests.get(url, timeout=5)
        response.close()
        return response.json()




s = SuperHeroAPI()
result = s.get_hero('superman')
s.get_hero_idintification_card('superman')
pp.pprint(result)


class NotFoundError(Exception):
    pass
