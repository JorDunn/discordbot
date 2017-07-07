import discord
from discord.ext import commands, ipc
import asyncio
import random
from config import Config

conf = Config('bot.json')
print("Token: ", conf.token)
print("Default channel: ", conf.default_channel)

bot = commands.Bot(command_prefix='!', description="Random bot")


@bot.event
async def on_ready():
    print("Logged in as", bot.user.name, bot.user.id)

@bot.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await asyncio.sleep(1)
        msg = await bot.send_message(message.channel, "Pong")
        await asyncio.sleep(2)
        await bot.delete_message(msg)
    elif message.content.startswith('!rude'):
        await asyncio.sleep(1)
        msg = await bot.send_message(message.channel, "Your mother was a hamster, and your father smelt of elderberries!")

bot.run(conf.token)
