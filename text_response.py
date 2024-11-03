# This file contains the text response function that is called when a message is sent to the bot.

async def handle_text_response(message):
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
        await message.channel.send('K.E.Ç.İ: Kulvarının en çarpıcı ismi.')

    elif 'alp' in message.content.lower():
        await message.channel.send('# Alp, shcrift "A." Stands for:\n"Almighty."')

    elif 'kuzey' in message.content.lower():
        await message.channel.send('ehh eh uhm actually the ending to "*insert niche movie that noone cares about*" is a literary gem since the direc- *punches face*')

    elif 'talha' in message.content.lower():
        await message.channel.send("I'm nobody. I'm nowhere. I drive. I. Am. Gay.")
