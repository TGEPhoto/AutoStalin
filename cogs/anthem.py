import discord
from discord.ext import commands

class Anthem(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def anthem(self, ctx):
        await ctx.send('Our glorious anthem: https://www.youtube.com/watch?v=U06jlgpMtQs')

def setup(client):
    client.add_cog(Anthem(client))
