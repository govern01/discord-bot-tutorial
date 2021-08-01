import discord
from discord.ext import commands
from configparser import ConfigParser
from cogs.admin import AdminCog
from cogs.welcome import WelcomeCog

cfg = ConfigParser()
cfg.read("bot.ini")
bot = commands.Bot(command_prefix=cfg['BOT']['command_prefix'])

@bot.command(name="ping")
async def server_response(ctx):
    await ctx.reply("pong")

@bot.event
async def on_ready():
    print("Ready!!")


bot.add_cog(AdminCog(bot))
bot.add_cog(WelcomeCog(bot))

bot.run(cfg['BOT']['token'])
