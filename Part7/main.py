import discord
from discord.ext import commands
#pip install requests
import datetime


def jst():
    now = datetime.datetime.utcnow()
    now = now + datetime.timedelta(hours=9)
    return now

@bot.event
async def on_ready():
	print("準備完了")
    

bot.run(Token)
