import discord
import random
from discord.ext import commands

class Ask(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ask(self, ctx, *, question):
        responses = ['Yes, comrade!',
                    'Absolutely not, you filthy capitalist!',
                    'How dare you ask such a question! I have free places in gulag for you!',
                    'Why would you ask such a thing in our motherland?',
                    'That is a very bold statement... capitalist.',
                    'How about a glass of vodka, comrade?',
                    'Они претворяются что платят нам, а мы претворяемся, что работаем за те деньги, которые они нам платят.',
                    'Важнейшим из искусств для нас является кино, по крайней мере до тех пор, пока основные массы населения остаются безграмотными.',
                    'It depends, comrade...',
                    'Stalin is not pleased that you asked this.',
                    'Definitely! Viva viva communista!']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(Ask(client))
