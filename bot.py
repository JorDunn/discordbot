import discord
from discord.ext import commands, ipc
import asyncio
import random
from config import Config

conf = Config('bot.json')

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

bot.run(conf.token)
