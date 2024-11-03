import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def get_gif_url(query):
        """
        Fetches the URL of the first GIF matching the search query from the Giphy API.

        Args:
            query (str): The search term to query the Giphy API.

        Returns:
            str: The URL of the first GIF matching the search query if the request is successful.
            None: If the request fails or no GIFs are found.

        Raises:
            requests.exceptions.RequestException: If there is an issue with the HTTP request.
        """

        api_key = os.getenv("GIF_API_KEY")
        url = f"http://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}&limit=1"

        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            gif_url = data["data"][0]["images"]["original"]["url"]
            return gif_url
        else:
            return None

async def handle_gif_response(message):
    """
    Handles a GIF response based on the content of a Discord message.

    This function checks if the message content starts with 'gif ' and ends with a period.
    If so, it extracts the search term from the message, retrieves a GIF URL using the search term,
    and sends the GIF URL to the message channel. If no GIF URL is found, it sends a message indicating
    that no such GIF exists.

    Args:
        message (discord.Message): The Discord message object containing the content to be processed.

    Returns:
        None
    """

    if message.content.startswith('gif ') and message.content.endswith('.'):
        search_term = message.content[4:-1]
        gif_url = get_gif_url(search_term)
        if gif_url:
            await message.channel.send(gif_url)
        else:
            await message.channel.send('Unfortunately, there is no such gif.')
