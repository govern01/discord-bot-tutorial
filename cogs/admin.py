import discord
from discord.ext import commands

async def admin_check(ctx):
    return ctx.author.id == 138935698177654784

class AdminCog(commands.Cog, command_attrs=dict(checks=[admin_check])):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        await member.edit(mute=True)
        await ctx.send(f"{member.display_name} has been muted.")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        await member.edit(mute=False)
        await ctx.send(f"{member.display_name} has been unmuted.")
