import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "m!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
	print("準備完了")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description=f"実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -BotMissingPermissions", description=f"Botの必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title=":x: 失敗 -CommandNotFound", description=f"不明なコマンドもしくは現在使用不可能なコマンドです。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
        embed = discord.Embed(title=":x: 失敗 -MemberNotFound", description=f"指定されたメンバーが見つかりません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed) 
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数が足りないため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者（こーちゃ！#6958）をメンションしてください。")
        await ctx.send(embed=embed) 
    else:
        raise error

bot.run(Token)
