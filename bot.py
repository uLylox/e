import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logged in.')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hellow! I'm a bot designed by Lylox and still improving. My main functions are being a chatbot and command bot!")

@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh < 1000:
        await ctx.send("he" * count_heh)
    else:
        await ctx.send("Discord doesn't let me send over 2000 letters! Therefore the maximum input is 999 :(")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined in {discord.utils.format_dt(member.joined_at)}, Nice stats buddy! :)')

bot.run("MTIwOTkzNDQ2OTA3MTYzODU3OA.GKdh6c.P4tKFbPRj9N9CHs8597JPiCpgKB6vPQBJ25xtk")
