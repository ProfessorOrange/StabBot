import discord
from discord.ext import commands, tasks
import random


class EGIFS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('EGIFS is online!')

    @commands.command(name='laugh', aliases=['lg','Laugh'], brief="Sends a laughing gif",
                      description="Sends a aughing  gif to the chat . Best Use-case: To laugh")
    async def laugh(self, ctx):
        gif = await fetch_laugh_gif()
        await ctx.send(f'{gif}')

    @commands.command(name='bonk', aliases=['bnk'], brief="Sends a laughing gif",
                      description="Sends a aughing  gif to the chat . Best Use-case: To laugh")
    async def laugh(self, ctx):
        gif = await fetch_bonk()
        await ctx.send(f'{gif}')

    @commands.command(name='i-', aliases=['disappoint', 'confused'],
                      brief="Sends a Disappointed/Confused/Surprise Nayeon gif",
                      description="Sends aDisappointed/Confused/Surprise Nayeon gif to the chat. Best Use-case: To express confusion/disappointment/surprise ")
    async def ing(self, ctx):
        gif = await fetch_i()
        await ctx.send(f'{gif}')

    @commands.command(name='cry', aliases=['cr','Cry'], brief="Sends a cry gif ",
                      description="Sends a crying gif to the chat. Best Use-case: To pout or cry")
    async def cry(self, ctx):
        gif = await fetch_cry_gif()
        await ctx.send(f'{gif}')

    @commands.command(name='jealous', aliases=['jl','Jealous'], brief="Sends a gif of twice being jealous",
                      description="Shows your jealous side. Best Use-case: To show jealousy")
    async def jealous(self, ctx, member):
        gif = await fetch_jeal_gif()
        await ctx.send(f'{member} {gif}')


def setup(bot):
    bot.add_cog(EGIFS(bot))


async def fetch_i():
    gifs = ['https://tenor.com/view/nayeon-im-nayeon-confused-confusion-nayeon-confused-gif-21322244',
            'https://tenor.com/view/twice-nayeon-im-nayeon-lead-vocalist-lead-dancer-gif-16762998',
            'https://tenor.com/view/basictingz-wjsnpopper-nayeon-sad-nayeon-dissapointed-im-nayeon-gif-21231648']
    gif = random.choice(gifs)
    return gif


async def fetch_jeal_gif():
    gifs = ['https://thumbs.gfycat.com/SecondhandHiddenHydatidtapeworm-max-1mb.gif',
            'https://gfycat.com/ampleeuphoricfly-twice-momo-jealous-when-dahyun-call-sana-darling',
            'https://media.giphy.com/media/wiLVI4rqxNGNOXWtF3/giphy.gif']
    gif = random.choice(gifs)
    return gif


async def fetch_cry_gif():
    gifs = [
        'https://c.tenor.com/I-jFmOOAGh4AAAAM/nayeon-crying.gif',
        'https://c.tenor.com/iOnqJXh8hU8AAAAM/kpop-twice.gif',
        'https://c.tenor.com/i-rQoNLTf4IAAAAM/nayeon-cry.gif',
        'https://c.tenor.com/K3-2Wc6KgTMAAAAM/dahyun-crying.gif',
        'https://c.tenor.com/TOtfX0VlVGAAAAAM/twice-chaeyoung.gif',
        'https://gfycat.com/impolitemammothconch']
    gif = random.choice(gifs)
    return gif


async def fetch_laugh_gif():
    gifs = [
        'https://c.tenor.com/g9uRBg053CcAAAAM/twice-kpop.gif'
        'https://c.tenor.com/hcUlo7cUMb8AAAAM/twice-nayeon.gif',
        'https://c.tenor.com/12QpWCvwyOoAAAAM/jeongyeon-twice.gif',
        'https://c.tenor.com/THYryH1pLdkAAAAM/jeongyeon-twice.gif',
        'https://c.tenor.com/jAa8LtgNZ0AAAAAM/twice-kpop.gif',
        'https://c.tenor.com/axsm6UBuMPMAAAAM/mina-smile.gif',
        'https://tenor.com/view/kekwtf-gif-18599263',
        'https://gfycat.com/welltodograygalapagospenguin-dahyun-pocari-sweat-fan-signing-twice',
        'https://gfycat.com/unacceptablerespectfulequine-twice-mina-kpop',
        'https://gfycat.com/pepperydeficientallosaurus-dahyun-twice-kpop',
        'https://gfycat.com/classicartisticanura-dahyun-twice-dtna-kpop']
    gif = random.choice(gifs)
    return gif

async def fetch_bonk():
    gifs = ['https://cdn.discordapp.com/attachments/913104971350806599/923976689875300383/despicable-me-minions.gif']
    gif = random.choice(gifs)
    return gif
