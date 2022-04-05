import discord
from discord.ext import commands, tasks
import random


class HGIFS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('HGIFS is online!')

    @commands.command(name='stab', aliases=['st'], brief="Sends a stabbing gif with the tagged member",
                      description="Sends a stabbing gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To vent frustration of someone or something or for pleasure")
    async def stabbing(self, ctx, member):
        gif = await fetch_stab_gif()
        id=member
        if member == "<@!855093695786778684>":
            gif1 = await dodge_gif()
            await ctx.send(f'{gif1}')
            id = ctx.message.author.mention
        await ctx.send(f'{id} {gif}')

    @commands.command(name='slap', aliases=['sl'], brief="Sends a slap gif with the tagged member",
                      description="Sends a slap gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To slap someone silly")
    async def slapping(self, ctx, member):
        gif = await fetch_slap_gif()
        id=member
        if member == "<@!855093695786778684>":
            gif1 = await dodge_gif()
            await ctx.send(f'{gif1}')
            id = ctx.message.author.mention
        await ctx.send(f'{id} {gif}')

    @commands.command(name='kick', aliases=['kc'], brief="Sends a kick gif with the tagged member",
                      description="Sends a kick gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To kick someone")
    async def kicking(self, ctx, member):
        gif = await fetch_kick_gif()
        id=member
        if member == "<@!855093695786778684>":
            gif1 = await dodge_gif()
            await ctx.send(f'{gif1}')
            id = ctx.message.author.mention
        await ctx.send(f'{id} {gif}')

    @commands.command(name='surgery', aliases=['sg'], brief="Sends a chasing gif with the tagged member",
                      description="Sends a kick gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To kick someone")
    async def chase(self, ctx, member):
        gif = await chase_gif()
        id=member
        if member == "<@!855093695786778684>":
            gif1 = await dodge_gif()
            await ctx.send(f'{gif1}')
            id = ctx.message.author.mention
        await ctx.send(f'{id} {gif}')


def setup(bot):
    bot.add_cog(HGIFS(bot))


async def dodge_gif():
    gifs = [
        'https://giphy.com/gifs/peacocktv-matrix-keanu-reeves-dodging-bullets-eIm624c8nnNbiG0V3g',
        'https://giphy.com/gifs/skeleton-dodge-reaper-3o7aDcYHcBee34V6uc',
        'https://media.giphy.com/media/FTt7SaAjcXYjaj83rk/giphy.gif']
    gif = random.choice(gifs)
    return gif


async def fetch_kick_gif():
    gifs = [
        'https://tenor.com/view/%EB%B0%80%EB%8B%A4-%EB%B0%9C%EC%B0%A8%EA%B8%B0-%EB%8C%84%EC%8A%A4-%EA%B5%B0%EB%AC%B4-%ED%9D%94%EB%93%A4%EB%8B%A4-gif-18261645',
        'https://tenor.com/view/milk-and-mocha-milk-mocha-kicked-fell-down-gif-14700601',
        'https://tenor.com/view/stop-playing-couple-handphone-kick-mobile-gif-16897236',
        'https://tenor.com/view/ninja-kick-die-pow-gif-13730734',
        'https://tenor.com/view/missed-kick-missed-kick-minions-fail-gif-12718518']
    gif = random.choice(gifs)
    return gif


async def chase_gif():
    gifs = ['https://gfycat.com/corruptdrearyaffenpinscher',
            'https://tenor.com/view/chasing-running-funny-gif-17013760',
            'https://tenor.com/view/homer-simpson-chasing-dog-fluffytail-gif-13518540',
            'https://tenor.com/view/sponge-bob-running-chasing-squidward-gif-14263887']
    gif = random.choice(gifs)
    return gif


async def fetch_stab_gif():
    gifs = ['https://tenor.com/view/killed-em-hold-this-stabbed-gif-14017151',
            'https://tenor.com/view/kill-stab-thinking-arya-got-gif-14033550',
            'https://tenor.com/view/knife-backstab-gif-gif-9184018',
            'https://tenor.com/view/excel-saga-stabby-stab-stab-fustrated-anime-gif-14178229',
            'https://tenor.com/view/saturdays-best-saturdays-best-you-tube-back-stab-gif-14026299',
            'https://tenor.com/view/penguin-stab-cutting-throat-violent-pissed-gif-9643496',
            'https://tenor.com/view/kamen-rider-kuuga-rising-titan-stab-stabbing-stabbing-anger-kill-gif-18889075']
    gif = random.choice(gifs)
    return gif


async def fetch_slap_gif():
    gifs = ['https://tenor.com/view/nope-stupid-slap-in-the-face-phone-gif-15151334',
            'https://tenor.com/view/batman-slap-robin-slap-gif-10206784',
            'https://tenor.com/view/peach-cat-slap-angry-mad-gif-15310661',
            'https://tenor.com/view/back-slap-backhand-funny-animals-penguin-slap-gif-11724800',
            'https://tenor.com/view/spank-tom-and-jerry-tom-puppy-gif-5196956',
            'https://tenor.com/view/family-guy-brian-griffin-stewie-griffin-slap-push-gif-4590339',
            'https://tenor.com/view/spongebob-squarepants-patrick-star-gloves-slap-gif-17514643']
    gif = random.choice(gifs)
    return gif
