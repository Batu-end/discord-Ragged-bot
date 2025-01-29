# discord-Ragged-bot
A bot for discord, originally made to work with gifs.

# V1 - Responds with specified messages, to messages that:
-  start with a certain character(s)
-  contain a certain word anywhere within the message
-  start and end with the same characters

# V2 - Responds to messages that request gif responses:
-  the message format must be in "gif x." , where 'x' is the desired search term for the gif
-  uses the GIPHY API instead of the regular Tenor gifs , so results may differ from the search results within the Discord gifs section
-  Ragged will always send the first gif result
-  if Ragged can't send the first result after a search , it will instead send an error message
-  Ragged will always send the original version of the gif search result

# V3 - Uses AWS cloud services to run smoothly, 24/7, on demand and without utilizing local computing power.
- Uses the free t2.micro EC2 tier, attached with default EBS volume.
- Based in the US region, within the us-west-1 Availability zone.

# V4 - Ragged had trouble with private keys, as being new to developing with private keys myself.
- Now private keys are actually stored privately within the cloud, which meant that the repo can now be public.
