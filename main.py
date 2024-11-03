from bot import client, run_discord_bot
from gif_response import handle_gif_response
from text_response import handle_text_response

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await handle_text_response(message)

    await handle_gif_response(message)

if __name__ == "__main__":
    run_discord_bot()
