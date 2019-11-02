import discord
from discord.ext import commands

class Capitalism(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def capitalism(self, ctx):
        await ctx.send('No.')

def setup(client):
    client.add_cog(Capitalism(client))
