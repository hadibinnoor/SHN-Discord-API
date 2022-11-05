import discord
from decouple import config
from keep_alive import keep_alive
from utils import generate_random_url

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
        await message.channel.send(generate_random_url())

keep_alive()
client.run(config('TOKEN'))
