import discord
from decouple import config
from keep_alive import keep_alive
from utils import get_random_joke

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        joke = get_random_joke()
        await message.channel.send(joke)

keep_alive()
client.run(config('TOKEN'))
