import os
import random
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands





client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await client.process_commands(message)



@client.command(name='8ball', 
                aliases=["y/n"],
                description="Answers a yes/no question.")
async def _8ball(ctx, *, question):
    responses = ["Yes",
     "No",
     "Maybe",
     "I don't know",
     "Yes... no... maybe... I don't know... CAN YOU REPEAAAT THEE QUEESTION",
     "Time for an existential crisis...",
     "I don't think so",
     "Yeah for sure",
     "Tbh I don't care",
     "Why don't you use your braincells and come up with a logical answer on your own, geez..."]
    await ctx.channel.send(f'Question: {question} \n Answer: {random.choice(responses)}')
    

@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['quote'])
async def nfexlo_quote(ctx):
    responses = [
        "`Carrots are a fruit, convention isn't the law. \n ~Nova~`",
        "`Oranges are human.\n ~Nova~`",
        "`If you're not smart enough, bullshit it. ~Nova~`",
        "`Life is nothing but disappointment after disappointment and then you die.\n ~Tana~`",
        "`A man is a breastless chicken. \n ~Katia~`",
        "`The subconscious is the graveyard to an old you, a trashcan to current you, and the compost from which the future you will grow. \n ~Ryma~`"
    ]
    await ctx.channel.send(random.choice(responses))




client.run(os.getenv('BOT_TOKEN'))

