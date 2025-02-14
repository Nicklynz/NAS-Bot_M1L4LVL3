import aiohttp  # A library for asynchronous HTTP requests
import random

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.type = None
        self.hp = None
        self.attack = None
        self.defence = None
        self.speed = None
        number_to_get = random.randint(1, 2048)
        if number_to_get == random.randint(1, 2048):
            self.shiny = True
        else:
            self.shiny = False
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return str.capitalize(data['forms'][0]['name'])  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails
    
    async def get_hp(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['stats'][0]['base_stat']  # Returning a Pokémon's name
                else:
                    return 50  # Return the default stat if the request fails
    
    async def get_attack(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['stats'][1]['base_stat']  # Returning a Pokémon's name
                else:
                    return 50  # Return the default stat if the request fails
    
    async def get_defense(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['stats'][2]['base_stat']  # Returning a Pokémon's name
                else:
                    return 50  # Return the default stat if the request fails
    
    async def get_speed(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['stats'][5]['base_stat']  # Returning a Pokémon's name
                else:
                    return 50  # Return the default stat if the request fails
    
    async def get_type(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return str.capitalize(data['types'][0]['type']['name'])  # Returning a Pokémon's name
                else:
                    return 50  # Return the default stat if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        for i in range(6):
            match i:
                case 0:
                    if not self.name:
                        self.name = await self.get_name()  # Retrieving attributes if it has not yet been uploaded
                case 1:
                    if not self.type:
                        self.type = await self.get_type()
                case 2:
                    if not self.hp:
                        self.hp = await self.get_hp()
                case 3:
                    if not self.attack:
                        self.attack = await self.get_attack()
                case 4:
                    if not self.defence:
                        self.defence = await self.get_defense()
                case 5:
                    if not self.speed:
                        self.speed = await self.get_speed()
        return f"""The name of your Pokémon : {self.name}
    Stats :
        Type : {self.type}
        HP : {self.hp}
        Attack : {self.attack}
        Defence : {self.defence}
        Speed : {self.speed}"""  # Returning the string with the Pokémon's name

    async def show_img(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    match self.shiny:
                        case True:
                            return data['sprites']['front_shiny']  # Returning a shiny Pokémon's img
                        case _:
                            return data['sprites']['front_default']  # Returning a Pokémon's img
                else:
                    pass