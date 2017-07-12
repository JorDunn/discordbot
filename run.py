import discord
import asyncio
from discord.ext import commands, ipc
from discordbot.config import Config
from discordbot.quotes import Quotes
from discordbot.weather import Weather

bot = commands.Bot(command_prefix='!', description="A perfectly pleasant discord bot.")

conf = Config('bot.json')

bot_commands = ['!help', '!ping']


async def typing(channel):
    await bot.send_typing(channel)
    await asyncio.sleep(1)


async def send_temp_message(channel, message, sleep):
    await typing(channel)
    msg = await bot.send_message(channel, message)
    await asyncio.sleep(sleep)
    await bot.delete_message(msg)


@bot.event
async def on_ready():
    print("Logged in as", bot.user.name, "(ID:", bot.user.id, ")")
    await bot.change_presence(game=discord.Game(name='Diablo 4'))


@bot.event
async def on_message(message):
    if message.content.startswith('!help') and message.author != bot.user:
        await typing(message.channel)
        await bot.send_message(message.channel, "Here are my current commands:")
        command_list = ""
        for command in bot_commands:
            command_list += command + " "
        await bot.send_message(message.channel, command_list)
    elif message.content.startswith('!ping'):
        if '!ping' in bot_commands:
            await typing(message.channel)
            await bot.send_message(message.channel, "Pong")
        else:
            await send_temp_message(message.channel, "This command has been disabled.", 5)
    elif message.content.startswith('!quote'):
        if '!quote' in bot_commands:
            await typing(message.channel)
            await bot.send_message(message.channel, "This command is not implemented yet.")
        else:
            await send_temp_message(message.channel, "This command has been disabled.", 5)


if __name__ == '__main__':
    bot.run(conf.token)
