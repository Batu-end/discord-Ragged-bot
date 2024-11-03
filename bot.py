import discord
import bot
import json
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def run_discord_bot():
    """
    Runs the Discord bot using the token from the environment variable.

    This function initializes a Discord client with the specified intents
    and runs the bot using the token retrieved from the environment variable
    'DISCORD_TOKEN'.

    Environment Variables:
    - DISCORD_TOKEN: The token used to authenticate the Discord bot.

    Raises:
    - RuntimeError: If the 'DISCORD_TOKEN' environment variable is not set.
    """

    discord_token = os.getenv("DISCORD_TOKEN")

    client.run(discord_token)
