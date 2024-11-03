import random

# List of gif links to be used in for sigma gifs.
gif_list = [
    'https://tenor.com/view/thomas-shelby-gif-23960893',
    'https://tenor.com/view/standing-thomas-shelby-peaky-blinders-gif-27268060',
    'https://tenor.com/view/john-wick-keanu-reeves-serious-walking-im-coming-for-you-gif-17750404',
    'https://tenor.com/view/looking-back-john-wick-keanu-reeves-john-wick-chapter4-staring-back-gif-26625896',
    'https://tenor.com/view/michael-scofield-gif-24495899',
    'https://tenor.com/view/american-psycho-smoke-sigma-gif-26186111',
    'https://tenor.com/view/cillianmurphygun-cillianmurphy-jazmincoded-gif-3811002643797340103',
    'https://tenor.com/view/fight-club-quotes-gif-27239086'
]

async def handle_text_response(message):
    """
    Handles text responses based on the content of the message.
    Parameters:
        message (discord.Message): The message object that triggered the event.
    Returns:
        None
    Behavior:
        - If the message starts with 'gif ' and ends with '.', it returns None.
        - If the message contains 'ege' (case insensitive), it responds with "skibi".
        - If the message starts with any of the characters '?', '!', '.', '$', '@', '#', it removes the first character and responds with a sarcastic message.
        - If the message is enclosed in double or single quotes, it removes the quotes and responds with a message suggesting to write without quotes.
        - If the message contains 'batu' (case insensitive), it responds with a specific message (currently incomplete).
        - If the message contains 'alp' (case insensitive), it responds with a message about "Almighty".
        - If the message contains 'kuzey' (case insensitive), it responds with a humorous message about a niche movie.
        - If the message contains 'talha' (case insensitive), it responds with a quote about being nobody and driving.
        - If the message contains 'berke' (case insensitive), it responds with a quote from "Breaking Bad".
    """

    if message.content.startswith('gif ') and message.content.endswith('.'):
        return None

    elif 'ege' in message.content.lower():
        await message.channel.send("skibi")

    elif message.content[0] == '?' or message.content[0]== '!' or message.content[0] == '.' or message.content[0] == '$' or message.content[0] == '@' or message.content[0] == '#':
        message.content = message.content[1:]
        await message.channel.send(f'Simdi sen {message.content} diyince kendini zeki mi saniyon gofikt')

    elif message.content[0] == '"' and message.content[-1] == '"' or message.content[0] == "'" and message.content[-1] == "'":
        message.content = message.content[1:-1]
        await message.channel.send(f'Kardesim, bu kasaba 2 kesme isareti icin cok buyuk. Su sekilde yaz:\n{message.content}')

    elif 'batu' in message.content.lower():
        await message.channel.send(random.choice(gif_list))

    elif 'alp' in message.content.lower():
        await message.channel.send('# Alp, shcrift "A." Stands for:\n# "***Almighty.***"')

    elif 'kuzey' in message.content.lower():
        await message.channel.send('ehh eh uhm actually the ending to "*insert niche movie that noone cares about*" is a literary gem since the direc- *punches face*')

    elif 'talha' in message.content.lower():
        await message.channel.send("I'm nobody. I'm driving.*(ehliyetim yok)*")
    
    elif 'berke' in message.content.lower():
        await message.channel.send('https://tenor.com/view/dog-nose-butterfly-dog-puppy-peaceful-gif-14700589898488542320')

    elif 'efe' in message.content.lower():
        await message.channel.send("is that.. ***dante?***")
