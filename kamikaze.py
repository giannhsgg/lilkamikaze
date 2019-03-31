import discord
from discord.ext import commands
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix=".")

#Bot Ready event
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('this mothafacka is ready boss!')
    print('------')

@bot.event
async def on_message(message):
    if message.content == "cookie":
        await client.delete_message(message)
        await client.send_message(message.author, ":cookie:")

bot.run('NTYxODU3OTgwNTEzOTEwODE0.XKCVIw.OKfecLRHcG-QP0DdQiAeaOsdPy8')

