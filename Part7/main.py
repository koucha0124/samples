import discord
from discord.ext import commands
#pip install datetime
import datetime

bot = commands.Bot(command_prefix = "m!", intents=discord.Intents.all())
bot.remove_command("help")


def jst():
    now = datetime.datetime.utcnow()
    now = now + datetime.timedelta(hours=9)
    return now

@bot.event
async def on_ready():
	print("準備完了")
    
@bot.event
async def on_message_delete(message):
    now = jst()
    embed = discord.Embed(title="メッセージ削除", color=discord.Color.red())
    embed.add_field(name="メッセージ", value=message.content, inline=False)
    embed.add_field(name="時刻", value=now.strftime('%Y /%m / %d　 %H : %M : %S'), inline=False)
    embed.add_field(name="チャンネル", value=message.channel.mention, inline=False)
    embed.set_footer(icon_url=message.author.avatar_url, text=message.author.display_name)
    channel = message.guild.get_channel(your_channel_id)
    await channel.send(embed=embed)

bot.run(Token)
