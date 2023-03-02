import discord
import requests
import json
import os

def run_discord_bot():
    TOKEN = 'MTA4MDQxNjY2NTc0Mjg3NjgwMw.G18JAE.ewOtI_aVfMxJS3SenLaeK-0JYqdujoFL8BJ75U'

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('gif ') and message.content.endswith('.'):
            return None

        elif message.content.lower().startswith("ege"):
            await message.channel.send("ege = GAY TROLOLOLOLOOOO!!!!!")

        elif message.content[0] == '?' or message.content[0]== '!' or message.content[0] == '.' or message.content[0] == '$' or message.content[0] == '@' or message.content[0] == '#':
            message.content = message.content[1:]
            await message.channel.send(f'Simdi sen {message.content} diyince kendini zeki mi saniyon gofikt')

        elif message.content[0] == '"' and message.content[-1] == '"' or message.content[0] == "'" and message.content[-1] == "'":
            message.content = message.content[1:-1]
            await message.channel.send(f'Kardesim, bu kasaba 2 kesme isareti icin cok buyuk. Su sekilde yaz:\n{message.content}')

        elif 'ender abi' in message.content.lower():
            await message.channel.send('goca yarrag')

        elif 'kuzey' in message.content.lower():
            await message.channel.send('ehh eh uhm actually the ending to "Avengers: Endgame" is a literary gem since the direc- *punches face* *puts dick in mouth* *ligma cock*')

        elif 'talha' in message.content.lower():
            await message.channel.send("I'm nobody. I'm nowhere. I drive. I. Am. Him.")



    api_key = "fXAagJPL2EA8yvLp2Dpx9SbjiSP0vskl"
    giphy_endpoint = "http://api.giphy.com/v1/gifs/search"


    def get_gif_url(query):

        api_key = "fXAagJPL2EA8yvLp2Dpx9SbjiSP0vskl"

        url = f"http://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}&limit=1"

        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            gif_url = data["data"][0]["images"]["original"]["url"]
            return gif_url
        else:
            return None

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.content.startswith('gif ') and message.content.endswith('.'):
            search_term = message.content[4:-1]
            gif_url = get_gif_url(search_term)
            if gif_url:
                await message.channel.send(gif_url)
            else:
                await message.channel.send('Oyle bir gif yok aptal maymun')

    client.run(TOKEN)




