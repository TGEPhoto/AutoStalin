import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "%")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching Bombing of Berlin'))
    print('Bot is online.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjM2NTM4MTQ2ODE3MDQ4NTg3.XbBb1A.5mv8HMXC2j42VIjKOOInyZ4MNl8')
