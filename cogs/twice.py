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

    @commands.command(name='nayeon', aliases=['nayu','Nayeon','nAyeon','NAyeon','naYeon','NaYeon','nAYeon','NAYeon','nayEon','NayEon','nAyEon','NAyEon','naYEon','NaYEon','nAYEon','NAYEon','nayeOn','NayeOn','nAyeOn','NAyeOn','naYeOn','NaYeOn','nAYeOn','NAYeOn','nayEOn','NayEOn','nAyEOn','NAyEOn','naYEOn','NaYEOn','nAYEOn','NAYEOn','nayeoN','NayeoN','nAyeoN','NAyeoN','naYeoN','NaYeoN','nAYeoN','NAYeoN','nayEoN','NayEoN','nAyEoN','NAyEoN','naYEoN','NaYEoN','nAYEoN','NAYEoN','nayeON','NayeON','nAyeON','NAyeON','naYeON','NaYeON','nAYeON','NAYeON','nayEON','NayEON','nAyEON','NAyEON','naYEON','NaYEON','nAYEON','NAYEON
,'nayeon'],brief="Sends a Nayeon gifs",
                      description="Nayeon gifs for all occasions: $nayeon cute or $nayeon laugh")
    async def NayuGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$nayeon ', 'twice nayeon ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='jeongyeon', aliases=['jeong'],brief="Sends a Jeongyeon gifs",
                      description="Jeongyeon gifs for all occasions: $jeongyeon cute or $jeongyeon laugh")
    async def JeongyeonGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$jeongyeon ', 'twice jeongyeon ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='momo', aliases=['momo,''Momo','mOmo','MOmo','moMo','MoMo','mOMo','MOMo','momO','MomO','mOmO','MOmO','moMO','MoMO','mOMO','MOMO'],brief="Sends a Momo gifs",
                      description="Momo gifs for all occasions: $momo cute or $momo laugh")
    async def MomoGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$momo ', 'twice momo ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='sana', aliases=['sana','Sana','sAna','SAna','saNa','SaNa','sANa','SANa','sanA','SanA','sAnA','SAnA','saNA','SaNA','sANA','SANA'],brief="Sends a Sana gifs",
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

    @commands.command(name='jihyo', aliases=['jihyo','Jihyo','jIhyo','JIhyo','jiHyo','JiHyo','jIHyo','JIHyo','jihYo','JihYo','jIhYo','JIhYo','jiHYo','JiHYo','jIHYo','JIHYo','jihyO','JihyO','jIhyO','JIhyO','jiHyO','JiHyO','jIHyO','JIHyO','jihYO','JihYO','jIhYO','JIhYO','jiHYO','JiHYO','jIHYO','JIHYO'],brief="Sends a Jihyo gifs",
                      description="Jihyo gifs for all occasions: $jihyo cute or $jihyo laugh")
    async def JihyoGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$jihyo ', 'twice jihyo ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='mina', aliases=['mina','Mina','mIna','MIna','miNa','MiNa','mINa','MINa','minA','MinA','mInA','MInA','miNA','MiNA','mINA','MINA'],brief="Sends a Mina gifs",
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

    @commands.command(name='dubu',aliases=['dahyun','Dahyun','dAhyun','DAhyun','daHyun','DaHyun','dAHyun','DAHyun','dahYun','DahYun','dAhYun','DAhYun','daHYun','DaHYun','dAHYun','DAHYun','dahyUn','DahyUn','dAhyUn','DAhyUn','daHyUn','DaHyUn','dAHyUn','DAHyUn','dahYUn','DahYUn','dAhYUn','DAhYUn','daHYUn','DaHYUn','dAHYUn','DAHYUn','dahyuN','DahyuN','dAhyuN','DAhyuN','daHyuN','DaHyuN','dAHyuN','DAHyuN','dahYuN','DahYuN','dAhYuN','DAhYuN','daHYuN','DaHYuN','dAHYuN','DAHYuN','dahyUN','DahyUN','dAhyUN','DAhyUN','daHyUN','DaHyUN','dAHyUN','DAHyUN','dahYUN','DahYUN','dAhYUN','DAhYUN','daHYUN','DaHYUN','dAHYUN','DAHYUN'] brief="Sends a Dahyun gifs",
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

    @commands.command(name='chae', aliases=['chaeyoung','Chaeyoung'],brief="Sends a Chaeyoung gifs",
                      description="Chaeyoung gifs for all occasions: $chae cute or $chae laugh")
    async def ChaeyoungGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$chaeyoung ', 'twice chaeyoung ')
        url = "https://g.tenor.com/v1/search?q={}&key=ARKAC62PRROD&limit=100".format(searchterm)
        gifs = []
        response = requests.get(url)
        if response.status_code == 200:
            topgifs = json.loads(response.content)
            for i in range(0, 2):
                gifs.append(topgifs['results'][i]['media'][0]['gif']['url'])
            gif = random.choice(gifs)
        await ctx.send(f'{gif}')

    @commands.command(name='tzuyu', aliases=['tzuyu','Tzuyu','tZuyu','TZuyu','tzUyu','TzUyu','tZUyu','TZUyu','tzuYu','TzuYu','tZuYu','TZuYu','tzUYu','TzUYu','tZUYu','TZUYu','tzuyU','TzuyU','tZuyU','TZuyU','tzUyU','TzUyU','tZUyU','TZUyU','tzuYU','TzuYU','tZuYU','TZuYU','tzUYU','TzUYU','tZUYU','TZUYU'
],brief="Sends a Tzuyu gifs",
                      description="Tzuyu gifs for all occasions: $tzuyu cute or $tzuyu laugh")
    async def TzuyuGif(self, ctx, searchterm):
        searchterm = ctx.message.content.replace('$tzuyu ', 'twice tzuyu ')
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
