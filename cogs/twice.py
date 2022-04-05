import json
import random
import requests
from discord.ext import commands


class Twice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Twice is online!')

    @commands.command(name='sana', brief="Sends a Sana gifs",
                      description="Sana gifs for all occasions: $sana cute or $sana laugh")
    async def SanaGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$sana ', 'twice Sana ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='mina', brief="Sends a Mina gifs",
                      description="Mina gifs for all occasions: $mina cute or $mina laugh")
    async def MinaGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$mina ', 'twice Mina ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='dubu', brief="Sends a Dahyun gifs",
                      description="Dahyun gifs for all occasions: $dubu cute or $dubu laugh")
    async def DubuGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$dubu ', 'twice dahyun ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')


def setup(bot):
    bot.add_cog(Twice(bot))
