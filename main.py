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

@bot.command(name="join")
async def join_voice_chat(ctx):
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()

@bot.command(name="leave")
async def leave_voice_chat(ctx):
    voice_clients = bot.voice_clients
    for client in voice_clients:
        if client.guild.id == ctx.guild.id:
            await client.disconnect()
            break

@bot.command(name="play")
async def play_sound_effect(ctx, sound_effect_title: str):
    sound_effect_path = f"./sound_effects/{sound_effect_title}.mp3"
    sound_effect = discord.FFmpegPCMAudio(sound_effect_path)
    voice_clients = bot.voice_clients
    for client in voice_clients:
        if client.guild.id == ctx.guild.id:
            client.play(sound_effect)
            break

bot.add_cog(AdminCog(bot))
bot.add_cog(WelcomeCog(bot))

bot.run(cfg['BOT']['token'])
