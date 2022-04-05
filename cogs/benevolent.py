import discord
from discord.ext import commands, tasks
import random


class GGFIS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('GGIFS is online!')

    @commands.command(name='fistbump', aliases=['fb','Fistbump'], brief="Sends a fistbump gif with the tagged member",
                      description="Sends a fistbump gif to the chat with the tagged member. Use the command along "
                                  "with a member (@member). Best Use-case: With your bros")
    async def fbing(self, ctx, member):
        gif = await fetch_bfist_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='run', aliases=['rn','Run'], brief="Sends a run gif",
                      description="Need to run away because you said something that would piss off someone or something that's funny or something that's wrong")
    async def running(self, ctx):
        gif = await fetch_run_gif()
        await ctx.send(f'{gif}')

    @commands.command(name='hi5', aliases=['highfive', 'h5','Highfive'], brief="Sends a high-five gif with the tagged member",
                      description="Sends a high-five gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: ")
    async def hifiving(self, ctx, member):
        gif = await fetch_hi5_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='hug', aliases=['hg','Hug'], brief="Sends a hugging gif with the tagged member",
                      description="Sends a hugging gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To show support or love and a general stress reliever")
    async def hugging(self, ctx, member):
        gif = await fetch_hug_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='cheer', aliases=['ch','Cheer'], brief="Sends a cheerful gif with the tagged member",
                      description="Sends a cheerful gif to the chat with the tagged member to cheer them up. Use the command along with a member (@member), Best Use-case: To boost their mood or sometimes jus to get through the day")
    async def cheering(self, ctx, member):
        gif = await fetch_cheer_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='kiss', aliases=['ks','Kiss'], brief="Sends a Sana Kiss gif with the tagged member",
                      description="Sends a Sana Kiss gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: Who doesnt want a Sana Kiss smh)")
    async def kissing(self, ctx, member):
        gif = await fetch_kiss_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='pat', aliases=['pt','Pat'], brief="Sends a patting gif with the tagged member",
                      description="Sends a patting gif to the chat with the tagged member. Use the command along with a member (@member), Best Use-case: To console someone")
    async def patting(self, ctx, member):
        gif = await fetch_pat_gif()
        await ctx.send(f'{member} {gif}')

    @commands.command(name='sip', aliases=['sp','Sip'], brief="Sends a gif of someone sipping tea/coffee/beverage",
                      description="Sends a sipping gif to the chat. Best Use-case: To sip some beverage and act cool or indifferent.")
    async def sipping(self, ctx):
        gif = await fetch_sip_gif()
        await ctx.send(f'{gif}')


def setup(bot):
    bot.add_cog(GGFIS(bot))


async def fetch_hug_gif():
    gifs = ['https://tenor.com/view/yoo-jeongyeon-jeongyeon-myoi-mina-mina-twice-gif-19273877',
            'https://tenor.com/view/twice-momo-tzuyu-motzu-twice-hug-gif-23795162',
            'https://tenor.com/view/twice-nayeon-jihyo-gif-5108387',
            'https://tenor.com/view/mochi-peachcat-mochi-peachcat-hug-pat-gif-19092449',
            'https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134',
            'https://tenor.com/view/hug-virtual-hug-hug-sent-gif-5026057',
            'https://tenor.com/view/milk-and-mocha-bear-couple-line-hug-cant-breathe-gif-12687187',
            'https://tenor.com/view/cat-hug-back-hug-notice-me-attention-to-me-gif-14227401',
            'https://tenor.com/view/hug-excited-to-see-you-lilo-and-stitch-lilo-stitch-gif-3578596',
            'https://tenor.com/view/twice-hug-gif-13782502',
            'https://tenor.com/view/twice-cuddlechvv-hug-dahyun-sana-gif-22517282',
            'https://tenor.com/view/sana-twice-dahyun-hug-cute-gif-16057713',
            'https://tenor.com/view/chaeyoung-dahyun-twice-hug-smile-gif-19934895']
    gif = random.choice(gifs)
    return gif


async def fetch_sip_gif():
    gifs = ['https://tenor.com/view/sana-minaszns-sana-drinking-sana-boba-sana-drink-gif-21114646',
            'https://tenor.com/view/%ED%8A%B8%EC%99%80%EC%9D%B4%EC%8A%A4-%EB%AF%B8%EB%82%98-twice-mina-drink-coffee-gif-12006175',
            'https://tenor.com/view/dahyun-chaeyoung-love-shot-drink-bottoms-up-gif-13708774',
            'https://tenor.com/view/love-shot-shot-drink-cheers-bottoms-up-gif-13095164',
            'https://tenor.com/view/twice-momo-kpop-cute-pretty-gif-16703677',
            'https://tenor.com/view/nayeon-drinking-twice-bleuiz-gif-19715780',
            'https://tenor.com/view/hellinheavns-gowon-drink-gif-22520134',
            'https://tenor.com/view/jeongyeon-twice-jeongyeon-jeongyeon-drinking-gif-21275030']
    gif = random.choice(gifs)
    return gif


async def fetch_run_gif():
    gifs = ['https://c.tenor.com/G4lk7OV69DMAAAAM/twice-mina.gif',
            'https://tenor.com/view/jihyo-twice-jeoim-running-gif-22070434',
            'https://tenor.com/view/twice-chaeyoung-running-kpop-%EC%B1%84%EC%98%81-gif-15329239',
            'https://tenor.com/view/twice-dahyun-kim-da-hyun-lead-rapper-vocalist-gif-17236068',
            'https://tenor.com/view/yeonsexual-jeongyeon-jeongyeon-meme-jeongyeon-running-jeongyeon-twice-gif-22171707',
            'https://tenor.com/view/sana-twice-cute-excited-running-gif-22112906',
            'https://tenor.com/view/vitamincream-nayeon-nayeon-running-twice-gif-21675796',
            'https://tenor.com/view/run-gif-14410622',
            'https://tenor.com/view/loona-yves-ha-sooyoung-sooyoung-chuu-gif-22269621',
            'https://tenor.com/view/chuu-jiwoo-loona-jeonsyuri-money-gif-20815298',
            'https://tenor.com/view/funny-animals-dogs-cute-teddy-bear-adorable-gif-10457932']
    gif = random.choice(gifs)
    return gif


async def fetch_cheer_gif():
    gifs = ['https://media.giphy.com/media/ZeXArwk9WimZo0iByt/giphy.gif',
            'https://media.giphy.com/media/f6J2QVFjTegnN6AZar/giphy.gif',
            'https://media.giphy.com/media/3ofSBtlGeOK3gDpvO0/giphy.gif',
            'https://media.giphy.com/media/SPMQbGOW6K0MM/giphy.gif',
            'https://media.giphy.com/media/SsHZjFZTqLLqTedLw9/giphy.gif']
    gif = random.choice(gifs)
    return gif


async def fetch_kiss_gif():
    gifs = ['https://gfycat.com/blandconventionalafricanclawedfrog', 'https://gfycat.com/wellinformedwellgroomedcero',
            'https://gfycat.com/spectacularalarmedamethystinepython',
            'https://gfycat.com/wateryhugeeuropeanfiresalamander', 'https://gfycat.com/majorfirsthandannelid',
            'https://gfycat.com/lightheartedremorsefulgemsbok']
    gif = random.choice(gifs)
    return gif


async def fetch_pat_gif():
    gifs = ['https://tenor.com/view/black-and-white-pokemon-pikachu-gif-17319374',
            'https://c.tenor.com/1I1pGUd3xWkAAAAM/mala-mishra-jha-pat-head.gif',
            'https://tenor.com/view/roseen-bunny-cute-nose-twitch-petting-gif-16870139',
            'https://cdn.discordapp.com/emojis/726930648396201985.gif?v=1',
            'https://tenor.com/view/pat-good-boy-gif-7220650',
            'https://tenor.com/view/big-hero6-baymax-there-there-patting-head-pat-head-gif-4086973',
            'https://tenor.com/view/kitten-pat-caress-love-care-gif-13912621',
            'https://c.tenor.com/WsCvSexlo_UAAAAM/twice-korean.gif']
    gif = random.choice(gifs)
    return gif


async def fetch_hi5_gif():
    gifs = ['https://media.giphy.com/media/4QFAH0qZ0LQnIwVYKT/giphy.gif',
            'https://media.giphy.com/media/ErZq6qTDdHigheeXGt/giphy.gif',
            'https://media.giphy.com/media/6HiKgEiDdTUuA/giphy.gif',
            'https://media.giphy.com/media/fLs7qZ6rU7B6X0uxv3/giphy.gif']
    gif = random.choice(gifs)
    return gif


async def fetch_bfist_gif():
    gifs = ['https://media.giphy.com/media/l0ExgzXpqkcL8zuVO/giphy.gif',
            'https://media.giphy.com/media/SwITwtwPZIwmpplWYE/giphy.gif',
            'https://media.giphy.com/media/98Nrl3nj3FaJG/giphy.gif',
            'https://tenor.com/view/tzuyu-twice-fist-bump-momo-cute-gif-14204093',
            'https://gfycat.com/abandonedshabbyflyinglemur']
    gif = random.choice(gifs)
    return gif
