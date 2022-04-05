import os
import discord
from json import load
from pathlib import Path
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
import random

bot = commands.Bot(command_prefix='$')
status = cycle(['Bored', 'Simp for Twice', 'Waiting for Ripe!', 'Being an Once', 'My Little Pony racing simulator'])
betters = ['better', 'Better']


@bot.event
async def on_ready():
    change_status.start()
    print('Bot is online. Let the fun begin')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing arguments Please check!")
    if isinstance(error, commands.ArgumentParsingError):
        await ctx.send("Couldn't parse the arguments. Please check help or contact the developer.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Not a valid command. Please contact the developer if you wish to add this command.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if str(message.author.id) == os.getenv('id'):
        if any(word in message.content for word in betters):
            gif = await fetch_better_gif()
            await message.channel.send(f'{gif}')
    await bot.process_commands(message)


async def fetch_better_gif():
    gifs = ['https://tenor.com/view/nayeon-twice-better-dance-kpop-gif-19162116',
            'https://tenor.com/view/jeongyeon-twice-better-gif-19169702',
            'https://tenor.com/view/twice-dancing-sana-hot-mina-gif-19171492',
            'https://c.tenor.com/ctck491rgC0AAAAM/jihyo-twice.gif']
    gif = random.choice(gifs)
    return gif


@bot.command()
async def load(ctx, extension):
    id = ctx.message.author.id
    if str(id) == os.getenv('id'):
        bot.load_extension(f'cogs.{extension}')
    else:
        print(
            f'Unauthorised access by: ID:{id} --- Display_Name:{ctx.message.author.display_name} --- Username:{ctx.message.author.mention}  --- Name:{ctx.message.author.name} --- Server: {ctx.message.guild.name} --- Channel:{ctx.message.channel.mention}')


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def unload(ctx, extension):
    id = ctx.message.author.id
    if str(id) == os.getenv('id'):
        bot.unload_extension(f'cogs.{extension}')
    else:
        print(
            f'Unauthorised access by: ID:{id} --- Display_Name:{ctx.message.author.display_name} --- Username:{ctx.message.author.mention}  --- Name:{ctx.message.author.name} --- Server: {ctx.message.guild.name} --- Channel:{ctx.message.channel.mention}')


@bot.command()
async def reload(ctx, extension):
    id = ctx.message.author.id
    if str(id) == os.getenv('id'):
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
    else:
        print(
            f'Unauthorised access by: ID:{id} --- Display_Name:{ctx.message.author.display_name} --- Username:{ctx.message.author.mention}  --- Name:{ctx.message.author.name} --- Server: {ctx.message.guild.name} --- Channel:{ctx.message.channel.mention}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

load_dotenv('.env')

token = os.getenv('token')
bot.run(token)
