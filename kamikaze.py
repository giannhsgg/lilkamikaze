import discord
from discord.ext import commands
import asyncio
import re

bot = commands.Bot(command_prefix='!!')

#Bot Ready
@bot.event
async def on_ready():
    print("♥ Bot",bot.user.name, "is starting up.")
    print("♥ Id :",bot.user.id)
    print("♥ Ready boss!(っ◔◡◔)っ")

#"commands"
@bot.event
async def on_message(message):
    if message.content.lower() == "oggs":
        await bot.process_commands(message)
        await bot.send_message(message.channel, " @OGG Bot#3905 is here for you homie")
    if message.content.lower() == "cookie":
        await bot.process_commands(message)
        await bot.send_message(message.channel, ":cookie:")
    if message.content.lower() == "poutsa":
        await bot.process_commands(message)
        await bot.send_message(message.channel, ":eggplant:")
    if message.content.lower() == "rebas":
        await bot.process_commands(message)
        await bot.send_message(message.channel, ":middle_finger:")

@bot.command
async def testembed(ctx):
    embed = discord.Embed(title="xes", description="Gamaei", colour=discord.Color.red(), url="www.google.com")
    await ctx.send(embed=embed)

bot.run('NTYxODU3OTgwNTEzOTEwODE0.XKtb1A.NAy7j5nnAloFVoj6qkiq1yQWLTI')
