import discord
from discord.ext import commands
#pip install discord-buttons-plugin
from discord_buttons_plugin import *
#pip install requests
import requests

bot = commands.Bot(command_prefix = "m!", intents=discord.Intents.all())
buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
	print("準備完了")
  
@buttons.click
async def button_hello(ctx):
	await ctx.reply("こんにちは！")

@buttons.click
async def button_ephemeral(ctx):
	await ctx.reply("このメッセージはあなたにしか見えていません！", flags = MessageFlags().EPHEMERAL)

@bot.command()
async def create(ctx):
	await buttons.send(
		content = "テストボタン", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="Hello", 
					style=ButtonType().Primary, 
					custom_id="button_hello"
				)
			]),ActionRow([
				Button(
					label="Ephemeral",
					style=ButtonType().Danger,
					custom_id="button_ephemeral"
				)
			])
		]
	)

bot.run(Token)
