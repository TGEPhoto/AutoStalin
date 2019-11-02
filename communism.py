import discord
from discord.ext import commands

class Communism(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.command
    async def communism(self, ctx):
        await ctx.send('Yes, comrade?')

def setup(client):
    client.add_cog(Communism(client))
