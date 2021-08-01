import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from configparser import ConfigParser
from cogs.admin import AdminCog
from cogs.welcome import WelcomeCog

cfg = ConfigParser()
cfg.read("bot.ini")
bot = commands.Bot(command_prefix=cfg['BOT']['command_prefix'], intents=discord.Intents.all())

GUILD_IDS = [204104761241370624]

slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="ping")
async def server_response(ctx: SlashContext):
    await ctx.send("pong")

@bot.event
async def on_ready():
    print("Ready!!")




bot.add_cog(AdminCog(bot))
bot.add_cog(WelcomeCog(bot))

bot.run(cfg['BOT']['token'])
