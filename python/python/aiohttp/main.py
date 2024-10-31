import aiohttp
import asyncio

#biblioteca: usada para fazer requests em API's de forma assicrona
async def main():
    
    async with aiohttp.ClientSession() as session:

        all_pokemon = []

        for pokemon_number in range(1, 151):
            pokemon_url = f'http://pokeapi.co/api/v2/pokemon/{pokemon_number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                all_pokemon.append(pokemon['name'])

        return all_pokemon

a = asyncio.run(main())

print(a)