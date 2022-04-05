import discord
from discord.ext import commands, tasks
import random


class BDGFIS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('BDGIFS is online!')

    @commands.command(name='kai', brief="Sends a Kai gif",
                      description="Birthday Gift for Taki")
    async def takibday(self, ctx):
        gif = await fetch_kai_gif()
        await ctx.send(f' <@!761707753144057867> {gif}')

    @commands.command(name='taki', brief="Sends a Taki gif",
                      description="Birthday Gift for Taki")
    async def takiday(self, ctx):
        gif = await fetch_taki_gif()
        await ctx.send(f' <@!761707753144057867> {gif}')


def setup(bot):
    bot.add_cog(BDGFIS(bot))


async def fetch_kai_gif():
    gifs = ['https://tenor.com/view/txt-kai-hueningkai-tomorrow-x-together-cathueka-gif-22178991',
            'https://tenor.com/view/ssoobtea-flying-kiss-ssoobean-ssoobhr-gif-20819645',
            'https://tenor.com/view/hueningkai-blocked-gif-22592291',
            'https://tenor.com/view/mollajoon-hueningkai-gif-23541968',
            'https://tenor.com/view/hueningkai-txt-gif-21918094',
            'https://tenor.com/view/1aeil-hueningkai-hyuka-txt-gif-21663383',
            'https://tenor.com/view/hueningkai-wink-gif-23988293',
            'https://tenor.com/view/wink-blonde-huening-kai-police-gif-23908110',
            'https://tenor.com/view/sookai-txt-kai-soobin-choi-gif-20761362',
            'https://tenor.com/view/mollajoon-hueningkai-gif-23708108','https://tenor.com/view/choibubbles-hueningkai-hueningkai-pretty-gif-22625756','https://tenor.com/view/choibubbles-hueningkai-hueninkai-pretty-gif-22625757']
    gif = random.choice(gifs)
    return gif


async def fetch_taki_gif():
    gifs = ['https://tenor.com/view/taki-iland-ilandtaki-takiiland-kpop-gif-18347361',
            'https://tenor.com/view/excited-exciting-%E3%82%BF%E3%82%AD-patiently-waiting-gif-18680162',
            'https://tenor.com/view/taki-%E3%82%BF%E3%82%AD-iland-gif-19799975',
            'https://tenor.com/view/euijoo-ej-ej-iland-taki-taki-iland-gif-23795970',
            'https://tenor.com/view/k-and-taki-i-land-cute-brother-pat-gif-19531003', 'https://tenor.com/view/taki-iland-taki-iland-k-kay-gif-17852810']
    gif = random.choice(gifs)
    return gif
