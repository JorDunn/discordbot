import discord
import asyncio
from discord.ext import commands, ipc
from discordbot.config import Config
from discordbot.quotes import Quotes
from discordbot.weather import Weather

bot = commands.Bot(command_prefix='!', description="A perfectly pleasant discord bot.")

conf = Config('bot.json')

bot_commands = ['!help', '!ping']

@bot.event
async def on_ready():
    print("Logged in as", bot.user.name, "(ID:", bot.user.id, ")")
    await bot.change_presence(game=discord.Game(name='Diablo 4'))
    quotes = Quotes()

@bot.event
async def on_message(message):
    if message.content.startswith('!help') and message.author != bot.user.id:
        msg = await bot.send_message(message.channel, "Here are my current commands")
        list_of_commands = ""
        for command in bot_commands:
            list_of_commands += command + ", "
        msg = await bot.send_message(message.channel, list_of_commands)
    elif message.content.startswith('!ping'):
        await asyncio.sleep(1)
        msg = await bot.send_message(message.channel, "Pong")
        await asyncio.sleep(2)
        await bot.delete_message(msg)
        await bot.delete_message(message)

if __name__ == '__main__':
    bot.run(conf.token)
