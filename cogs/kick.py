import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'{member.name}#{member.discriminator} has been kicked!')
        await member.create_dm()
        await member.dm_channel.send('You have been kicked from The Communists')
        await member.kick(reason=reason)

def setup(client):
    client.add_cog(Kick(client))
