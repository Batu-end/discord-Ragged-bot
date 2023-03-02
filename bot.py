import discord
import requests
import json

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

        if message.content.lower().startswith("ege"):
            await message.channel.send("ege harbi gay mq")

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

    client.run(TOKEN)

    giphy_api_key = "fXAagJPL2EA8yvLp2Dpx9SbjiSP0vskl"
    giphy_endpoint = "http://api.giphy.com/v1/gifs/search"

    def gif_response(message):
        if message.content.startswith('gif ') and message.content.endswith('.'):
            search_term = message.content[4:-1]










